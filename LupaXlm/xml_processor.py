# -*- coding: utf-8 -*-
# xml_processor.py

import os
from pathlib import Path
import xml.etree.ElementTree as ET
import pandas as pd
from datetime import datetime
import logging
from typing import Dict, Any, List, Optional, Tuple
from field_definitions import (
    INVOICE_LINES,
    InvoiceData, 
    XML_MAPPINGS,
    UBLEXTENSIONS_FIELDS,
    INVOICE_GENERAL_FIELDS,
    ACCOUNTING_SUPPLIER_FIELDS,
    ACCOUNTING_CUSTOMER_FIELDS
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class XMLProcessor:
    def __init__(self):
        self.namespaces = {
            'ext': 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2',
            'sts': 'dian:gov:co:facturaelectronica:Structures-2-1',
            'cbc': 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2',
            'cac': 'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2',
            'ds': 'http://www.w3.org/2000/09/xmldsig#'
        }

    def extract_field_value(self, root: ET.Element, field_name: str, line_context: ET.Element = None) -> Optional[str]:
        """Extract field value from XML using xpath"""
        try:
            xpath = XML_MAPPINGS.get(field_name)
            if not xpath:
                return None

            # If we have a line context and this is a line field, adjust the xpath
            if line_context is not None and field_name in INVOICE_LINES:
                xpath = xpath.replace('.//cac:InvoiceLine/', './')
                context = line_context
            else:
                context = root

            if '@' in xpath:  # This is an attribute
                parent_xpath, attr_name = xpath.rsplit('/@', 1)
                parent = context.find(parent_xpath, self.namespaces)
                return parent.get(attr_name) if parent is not None else None
            else:
                element = context.find(xpath, self.namespaces)
                return element.text.strip() if element is not None and element.text else None
        except Exception as e:
            logger.warning(f"Error extracting field {field_name}: {e}")
            return None

    def process_header_data(self, xml_file: Path, root: ET.Element) -> InvoiceData:
        """Process header level data from XML"""
        data = InvoiceData(FileName=xml_file.name)
        
        # Extract header level fields
        all_fields = (INVOICE_GENERAL_FIELDS + UBLEXTENSIONS_FIELDS + 
                     ACCOUNTING_SUPPLIER_FIELDS + ACCOUNTING_CUSTOMER_FIELDS)
        
        for field_name in all_fields:
            value = self.extract_field_value(root, field_name)
            if hasattr(data, field_name):
                setattr(data, field_name, value)
                
        return data

    def process_line_items(self, xml_file: Path, root: ET.Element) -> List[Dict[str, Any]]:
        """Process line items from XML"""
        line_items = []
        
        # Find all invoice lines
        invoice_lines = root.findall('.//cac:InvoiceLine', self.namespaces)
        
        for line in invoice_lines:
            line_data = {'FileName': xml_file.name}
            
            # Extract line-specific fields
            for field_name in INVOICE_LINES:
                value = self.extract_field_value(root, field_name, line)
                line_data[field_name] = value
                
            line_items.append(line_data)
            
        return line_items

    def process_xml_file(self, xml_file: Path) -> Tuple[InvoiceData, List[Dict[str, Any]]]:
        """Process a single XML file and return header data and line items separately"""
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            
            # Process header data
            header_data = self.process_header_data(xml_file, root)
            
            # Process line items
            line_items = self.process_line_items(xml_file, root)
            
            return header_data, line_items
                
        except Exception as e:
            logger.error(f"Error processing {xml_file}: {e}")
            return InvoiceData(FileName=xml_file.name), []

    def process_folder(self, folder_path: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """Process all XML files in a folder"""
        folder = Path(folder_path)
        xml_files = list(folder.glob('*.xml'))
        
        if not xml_files:
            logger.warning(f"No XML files found in {folder}")
            return pd.DataFrame(), pd.DataFrame()
        
        header_results = []
        line_results = []
        
        for xml_file in xml_files:
            header_data, line_items = self.process_xml_file(xml_file)
            header_results.append(vars(header_data))
            line_results.extend(line_items)
        
        header_df = pd.DataFrame(header_results)
        lines_df = pd.DataFrame(line_results)
        
        return header_df, lines_df

def process_invoices(input_folder: str, output_file: str):
    """Process invoice files and save results to Excel with multiple sheets"""
    processor = XMLProcessor()
    
    # Generate timestamp and create output filename
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    file_name, file_ext = os.path.splitext(output_file)
    output_file_with_timestamp = f"{file_name}_{timestamp}{file_ext}"
    
    logger.info(f"Processing XML files from: {input_folder}")
    
    # Get header and line item data separately
    header_df, lines_df = processor.process_folder(input_folder)
    
    if not header_df.empty or not lines_df.empty:
        try:
            with pd.ExcelWriter(output_file_with_timestamp, engine='xlsxwriter') as writer:
                # UBLExtensions sheet
                columns_ubl = ['FileName'] + UBLEXTENSIONS_FIELDS
                header_df[columns_ubl].to_excel(writer, sheet_name='UBLExtensions', index=False)
                
                # Invoice General sheet
                columns_invoice = ['FileName'] + INVOICE_GENERAL_FIELDS
                header_df[columns_invoice].to_excel(writer, sheet_name='InvoiceGeneral', index=False)
                      
                # AccountingSupplier sheet
                columns_supplier = ['FileName'] + ACCOUNTING_SUPPLIER_FIELDS
                header_df[columns_supplier].to_excel(writer, sheet_name='AccountingSupplier', index=False)

                # AccountingCustomer sheet
                columns_customer = ['FileName'] + ACCOUNTING_CUSTOMER_FIELDS
                header_df[columns_customer].to_excel(writer, sheet_name='AccountingCustomer', index=False)

                # InvoiceLine sheet
                columns_lines = ['FileName'] + INVOICE_LINES
                lines_df[columns_lines].to_excel(writer, sheet_name='InvoiceLines', index=False)
            
            logger.info(f"Results saved to: {output_file_with_timestamp}")
            
        except Exception as e:
            logger.error(f"Error saving Excel file: {e}")
            raise
    else:
        logger.warning("No data to save")

if __name__ == "__main__":
    # Define paths relative to script location
    script_dir = Path(__file__).parent
    input_folder = script_dir / "XML"
    output_file = script_dir / "Facturacion_Electronica.xlsx"
    
    process_invoices(str(input_folder), str(output_file))