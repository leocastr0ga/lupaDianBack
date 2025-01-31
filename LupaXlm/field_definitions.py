# -*- coding: utf-8 -*-
# field_definitions.py

from dataclasses import dataclass
from typing import Optional

@dataclass
class InvoiceData:
    """Data class to store invoice information"""
    FileName: str = ''
    
    # General Invoice Fields (FAD Section)
    UBLVersionID: Optional[str] = None
    CustomizationID: Optional[str] = None
    ProfileID: Optional[str] = None
    ProfileExecutionID: Optional[str] = None
    InvoiceID: Optional[str] = None
    UUID: Optional[str] = None
    UUIDSchemeID: Optional[str] = None
    UUIDSchemeName: Optional[str] = None
    IssueDate: Optional[str] = None
    IssueTime: Optional[str] = None
    DueDate: Optional[str] = None
    InvoiceTypeCode: Optional[str] = None
    Note: Optional[str] = None
    DocumentCurrencyCode: Optional[str] = None
    LineCountNumeric: Optional[int] = None
    InvoicePeriodStartDate: Optional[str] = None
    InvoicePeriodStartTime: Optional[str] = None
    InvoicePeriodEndDate: Optional[str] = None
    InvoicePeriodEndTime: Optional[str] = None
    OrderReferenceID: Optional[str] = None
    OrderReferenceIssueDate: Optional[str] = None
    BillingReferenceID: Optional[str] = None
    BillingReferenceUUID: Optional[str] = None
    BillingReferenceSchemeName: Optional[str] = None
    BillingReferenceIssueDate: Optional[str] = None
    DespatchDocumentReferenceID: Optional[str] = None
    DespatchDocumentReferenceIssueDate: Optional[str] = None
    ReceiptDocumentReferenceID: Optional[str] = None
    ReceiptDocumentReferenceIssueDate: Optional[str] = None
    AdditionalDocumentReferenceID: Optional[str] = None
    AdditionalDocumentReferenceIssueDate: Optional[str] = None
    AdditionalDocumentTypeCode: Optional[str] = None

    # Delivery Section
    InvoiceActualDeliveryDate: Optional[str] = None
    InvoiceActualDeliveryTime: Optional[str] = None
    InvoiceDeliveryAddressID: Optional[str] = None
    InvoiceDeliveryAddressCityName: Optional[str] = None
    InvoiceDeliveryAddressCountrySubentity: Optional[str] = None
    InvoiceDeliveryAddressPostalZone: Optional[str] = None
    InvoiceDeliveryAddressLine: Optional[str] = None
    InvoiceDeliveryAddressCountryCode: Optional[str] = None
    InvoiceDeliveryContactName: Optional[str] = None
    InvoiceDeliveryContactTelephone: Optional[str] = None
    InvoiceDeliveryContactTelefax: Optional[str] = None
    InvoiceDeliveryContactElectronicMail: Optional[str] = None

    # DeliveryTerms Section
    InvoiceDeliveryTermsID: Optional[str] = None
    InvoiceDeliveryTermsSpecialTerms: Optional[str] = None
    InvoiceDeliveryTermsLossRiskResponsibilityCode: Optional[str] = None
    InvoiceDeliveryTermsLossRisk: Optional[str] = None

    # PrepaidPayment Section
    InvoicePrepaidPaymentID: Optional[str] = None
    InvoicePrepaidPaymentPaidAmount: Optional[str] = None
    InvoicePrepaidPaymentCurrencyID: Optional[str] = None
    InvoicePrepaidPaymentReceivedDate: Optional[str] = None
    InvoicePrepaidPaymentPaidDate: Optional[str] = None
    InvoicePrepaidPaymentPaidTime: Optional[str] = None
    InvoicePrepaidPaymentInstructionID: Optional[str] = None

    # AllowanceCharge Section
    InvoiceAllowanceChargeID: Optional[str] = None
    InvoiceAllowanceChargeChargeIndicator: Optional[str] = None
    InvoiceAllowanceChargeReasonCode: Optional[str] = None
    InvoiceAllowanceChargeReason: Optional[str] = None
    InvoiceAllowanceChargeMultiplierFactorNumeric: Optional[str] = None
    InvoiceAllowanceChargeAmount: Optional[str] = None
    InvoiceAllowanceChargeAmountCurrencyID: Optional[str] = None
    InvoiceAllowanceChargeBaseAmount: Optional[str] = None
    InvoiceAllowanceChargeBaseAmountCurrencyID: Optional[str] = None

    # PaymentExchangeRate Section
    InvoicePaymentExchangeRateSourceCurrencyCode: Optional[str] = None
    InvoicePaymentExchangeRateSourceCurrencyBaseRate: Optional[str] = None
    InvoicePaymentExchangeRateTargetCurrencyCode: Optional[str] = None
    InvoicePaymentExchangeRateTargetCurrencyBaseRate: Optional[str] = None
    InvoicePaymentExchangeRateCalculationRate: Optional[str] = None
    InvoicePaymentExchangeRateDate: Optional[str] = None

    # PaymentAlternativeExchangeRate Section
    InvoicePaymentAlternativeExchangeRateSourceCurrencyCode: Optional[str] = None
    InvoicePaymentAlternativeExchangeRateSourceCurrencyBaseRate: Optional[str] = None
    InvoicePaymentAlternativeExchangeRateTargetCurrencyCode: Optional[str] = None
    InvoicePaymentAlternativeExchangeRateTargetCurrencyBaseRate: Optional[str] = None
    InvoicePaymentAlternativeExchangeRateCalculationRate: Optional[str] = None

    # TaxTotal Section
    InvoiceTaxTotalTaxAmount: Optional[str] = None
    InvoiceTaxTotalTaxAmountCurrencyID: Optional[str] = None

    # WithholdingTaxTotal Section
    InvoiceWithholdingTaxTotalTaxAmount: Optional[str] = None
    InvoiceWithholdingTaxTotalTaxAmountCurrencyID: Optional[str] = None

    # LegalMonetaryTotal Section
    InvoiceLineExtensionAmount: Optional[str] = None
    InvoiceTaxExclusiveAmount: Optional[str] = None
    InvoiceTaxInclusiveAmount: Optional[str] = None
    InvoiceAllowanceTotalAmount: Optional[str] = None
    InvoiceChargeTotalAmount: Optional[str] = None
    InvoicePayableRoundingAmount: Optional[str] = None
    InvoicePayableAmount: Optional[str] = None
    InvoicePayableAmountCurrencyID: Optional[str] = None



    # UBLExtensions Section
    UBLExtensions: Optional[str] = None
    UBLExtension: Optional[str] = None
    ExtensionContent: Optional[str] = None
    DianExtensions: Optional[str] = None
    InvoiceControl: Optional[str] = None
    InvoiceAuthorization: Optional[str] = None
    AuthorizationPeriodStartDate: Optional[str] = None
    AuthorizationPeriodEndDate: Optional[str] = None
    AuthorizedInvoicesPrefix: Optional[str] = None
    AuthorizedInvoicesFrom: Optional[str] = None
    AuthorizedInvoicesTo: Optional[str] = None
    InvoiceSourceCountryCode: Optional[str] = None
    InvoiceSourceCountryListAgencyID: Optional[str] = None
    InvoiceSourceCountryListAgencyName: Optional[str] = None
    InvoiceSourceCountryListSchemeURI: Optional[str] = None
    SoftwareProviderID: Optional[str] = None
    SoftwareProviderSchemeAgencyID: Optional[str] = None
    SoftwareProviderSchemeAgencyName: Optional[str] = None
    SoftwareID: Optional[str] = None
    SoftwareSchemeAgencyID: Optional[str] = None
    SoftwareSchemeAgencyName: Optional[str] = None
    SoftwareSecurityCode: Optional[str] = None
    SoftwareSecuritySchemeAgencyID: Optional[str] = None
    SoftwareSecuritySchemeAgencyName: Optional[str] = None
    AuthorizationProviderID: Optional[str] = None
    AuthorizationProviderSchemeAgencyID: Optional[str] = None
    AuthorizationProviderSchemeAgencyName: Optional[str] = None
    AuthorizationProviderSchemeID: Optional[str] = None
    AuthorizationProviderSchemeName: Optional[str] = None
    QRCode: Optional[str] = None
    Signature: Optional[str] = None
    UBLVersionID: Optional[str] = None
    CustomizationID: Optional[str] = None

    # AccountingSupplierParty Section (FAJ)
    SupplierAdditionalAccountID: Optional[str] = None
    SupplierPartyID: Optional[str] = None
    SupplierPartyName: Optional[str] = None
    SupplierIndustryClassificationCode: Optional[str] = None
    SupplierPhysicalLocationID: Optional[str] = None
    SupplierCityName: Optional[str] = None
    SupplierPostalZone: Optional[str] = None
    SupplierCountrySubentity: Optional[str] = None
    SupplierCountrySubentityCode: Optional[str] = None
    SupplierLine: Optional[str] = None
    SupplierCountryCode: Optional[str] = None
    SupplierCountryName: Optional[str] = None
    SupplierCountryLanguageID: Optional[str] = None
    SupplierRegistrationName: Optional[str] = None
    SupplierTaxLevelCode: Optional[str] = None
    SupplierTaxLevelCodeListName: Optional[str] = None
    SupplierTaxSchemeID: Optional[str] = None
    SupplierTaxSchemeName: Optional[str] = None
    SupplierCompanyID: Optional[str] = None
    SupplierCompanyIDSchemeID: Optional[str] = None
    SupplierCompanyIDSchemeName: Optional[str] = None
    SupplierCompanyIDSchemeAgencyID: Optional[str] = None
    SupplierCompanyIDSchemeAgencyName: Optional[str] = None
    SupplierCorporateRegistrationScheme: Optional[str] = None
    SupplierContactName: Optional[str] = None
    SupplierContactTelephone: Optional[str] = None
    SupplierContactTelefax: Optional[str] = None
    SupplierContactElectronicMail: Optional[str] = None
    SupplierContactNote: Optional[str] = None
    SupplierRegistrationAddressID: Optional[str] = None
    SupplierRegistrationAddressCityName: Optional[str] = None
    SupplierRegistrationAddressPostalZone: Optional[str] = None
    SupplierRegistrationAddressCountrySubentity: Optional[str] = None
    SupplierRegistrationAddressCountrySubentityCode: Optional[str] = None
    SupplierRegistrationAddressLine: Optional[str] = None
    SupplierRegistrationAddressCountryCode: Optional[str] = None
    SupplierRegistrationAddressCountryName: Optional[str] = None
    SupplierRegistrationAddressCountryLanguageID: Optional[str] = None
    SupplierShareholderParticipationPercent: Optional[str] = None

    # AccountingCustomerParty Section (FAK)
    CustomerAdditionalAccountID: Optional[str] = None
    CustomerPartyID: Optional[str] = None
    CustomerPartyIDSchemeName: Optional[str] = None
    CustomerSchemeID: Optional[str] = None
    CustomerSchemeName: Optional[str] = None
    CustomerPhysicalLocationID: Optional[str] = None
    CustomerCityName: Optional[str] = None
    CustomerPostalZone: Optional[str] = None
    CustomerCountrySubentity: Optional[str] = None
    CustomerCountrySubentityCode: Optional[str] = None
    CustomerLine: Optional[str] = None
    CustomerCountryCode: Optional[str] = None
    CustomerCountryName: Optional[str] = None
    CustomerCountryLanguageID: Optional[str] = None
    CustomerRegistrationName: Optional[str] = None
    CustomerTaxLevelCode: Optional[str] = None
    CustomerTaxLevelCodeListName: Optional[str] = None
    CustomerTaxSchemeID: Optional[str] = None
    CustomerTaxSchemeName: Optional[str] = None
    CustomerCompanyID: Optional[str] = None
    CustomerCompanyIDSchemeID: Optional[str] = None
    CustomerCompanyIDSchemeName: Optional[str] = None
    CustomerCompanyIDSchemeAgencyID: Optional[str] = None
    CustomerCompanyIDSchemeAgencyName: Optional[str] = None
    CustomerSchemeAgencyID: Optional[str] = None
    CustomerSchemeAgencyName: Optional[str] = None
    CustomerCorporateRegistrationScheme: Optional[str] = None
    CustomerContactName: Optional[str] = None
    CustomerContactTelephone: Optional[str] = None
    CustomerContactTelefax: Optional[str] = None
    CustomerContactElectronicMail: Optional[str] = None
    CustomerContactNote: Optional[str] = None
    CustomerRegistrationAddressID: Optional[str] = None
    CustomerRegistrationAddressCityName: Optional[str] = None
    CustomerRegistrationAddressPostalZone: Optional[str] = None
    CustomerRegistrationAddressCountrySubentity: Optional[str] = None
    CustomerRegistrationAddressCountrySubentityCode: Optional[str] = None
    CustomerRegistrationAddressLine: Optional[str] = None
    CustomerRegistrationAddressCountryCode: Optional[str] = None
    CustomerRegistrationAddressCountryName: Optional[str] = None
    CustomerRegistrationAddressCountryLanguageID: Optional[str] = None
    CustomerShareholderParticipationPercent: Optional[str] = None
    CustomerTaxRepresentativeID: Optional[str] = None
    CustomerTaxRepresentativeIDSchemeID: Optional[str] = None
    CustomerTaxRepresentativeIDSchemeAgencyID: Optional[str] = None
    CustomerTaxRepresentativeIDSchemeAgencyName: Optional[str] = None
    CustomerDeliveryActualDate: Optional[str] = None
    CustomerDeliveryActualTime: Optional[str] = None
    CustomerDeliveryAddressID: Optional[str] = None
    CustomerDeliveryAddressCityName: Optional[str] = None
    CustomerDeliveryAddressCountrySubentity: Optional[str] = None
    CustomerDeliveryAddressPostalZone: Optional[str] = None
    CustomerDeliveryAddressLine: Optional[str] = None
    CustomerDeliveryAddressCountryCode: Optional[str] = None

    # InvoiceLine Section
    InvoiceLineID: Optional[str] = None
    InvoiceLineIDSchemeID: Optional[str] = None
    InvoiceLineNote: Optional[str] = None
    InvoiceLineInvoicedQuantity: Optional[str] = None
    InvoiceLineInvoicedQuantityUnitCode: Optional[str] = None
    InvoiceLineLineExtensionAmount: Optional[str] = None
    InvoiceLineLineExtensionAmountCurrencyID: Optional[str] = None
    InvoiceLineFreeOfChargeIndicator: Optional[str] = None

        # PricingReference Section
    InvoiceLinePricingReferencePriceAmount: Optional[str] = None
    InvoiceLinePricingReferencePriceAmountCurrencyID: Optional[str] = None
    InvoiceLinePricingReferencePriceTypeCode: Optional[str] = None

        # AllowanceCharge Section
    InvoiceLineAllowanceChargeID: Optional[str] = None
    InvoiceLineAllowanceChargeChargeIndicator: Optional[str] = None
    InvoiceLineAllowanceChargeReason: Optional[str] = None
    InvoiceLineAllowanceChargeMultiplierFactorNumeric: Optional[str] = None
    InvoiceLineAllowanceChargeAmount: Optional[str] = None
    InvoiceLineAllowanceChargeAmountCurrencyID: Optional[str] = None
    InvoiceLineAllowanceChargeBaseAmount: Optional[str] = None
    InvoiceLineAllowanceChargeBaseAmountCurrencyID: Optional[str] = None
    
        # TaxTotal Section
    InvoiceLineTaxTotalTaxAmount: Optional[str] = None
    InvoiceLineTaxTotalTaxAmountCurrencyID: Optional[str] = None
    InvoiceLineTaxTotalTaxableAmount: Optional[str] = None
    InvoiceLineTaxTotalTaxableAmountCurrencyID: Optional[str] = None
    InvoiceLineTaxTotalPercent: Optional[str] = None
    InvoiceLineTaxTotalTaxSchemeID: Optional[str] = None
    InvoiceLineTaxTotalTaxSchemeName: Optional[str] = None

        # WithholdingTaxTotal Section
    InvoiceLineWithholdingTaxTotalTaxAmount: Optional[str] = None
    InvoiceLineWithholdingTaxTotalTaxAmountCurrencyID: Optional[str] = None
    InvoiceLineWithholdingTaxTotalTaxableAmount: Optional[str] = None
    InvoiceLineWithholdingTaxTotalTaxableAmountCurrencyID: Optional[str] = None
    InvoiceLineWithholdingTaxTotalPercent: Optional[str] = None
    InvoiceLineWithholdingTaxTotalTaxSchemeID: Optional[str] = None
    InvoiceLineWithholdingTaxTotalTaxSchemeName: Optional[str] = None

        # Item Section
    InvoiceLineItemDescription: Optional[str] = None
    InvoiceLineItemBuyersItemID: Optional[str] = None
    InvoiceLineItemSellersItemID: Optional[str] = None
    InvoiceLineItemStandardItemID: Optional[str] = None
    InvoiceLineItemStandardItemIDSchemeID: Optional[str] = None
    InvoiceLineItemStandardItemIDSchemeAgencyID: Optional[str] = None
    InvoiceLineItemStandardItemIDSchemeName: Optional[str] = None

        # Price Section
    InvoiceLinePriceAmount: Optional[str] = None
    InvoiceLinePriceAmountCurrencyID: Optional[str] = None
    InvoiceLinePriceBaseQuantity: Optional[str] = None
    InvoiceLinePriceBaseQuantityUnitCode: Optional[str] = None



#----------------------------------------------------
                     
# Field groupings for different sheets
UBLEXTENSIONS_FIELDS = [
    'UBLExtensions',
    'UBLExtension',
    'ExtensionContent',
    'DianExtensions',
    'InvoiceControl',
    'InvoiceAuthorization',
    'AuthorizationPeriodStartDate',
    'AuthorizationPeriodEndDate',
    'AuthorizedInvoicesPrefix',
    'AuthorizedInvoicesFrom',
    'AuthorizedInvoicesTo',
    'InvoiceSourceCountryCode',
    'InvoiceSourceCountryListAgencyID',
    'InvoiceSourceCountryListAgencyName',
    'InvoiceSourceCountryListSchemeURI',
    'SoftwareProviderID',
    'SoftwareProviderSchemeAgencyID',
    'SoftwareProviderSchemeAgencyName',
    'SoftwareID',
    'SoftwareSchemeAgencyID',
    'SoftwareSchemeAgencyName',
    'SoftwareSecurityCode',
    'SoftwareSecuritySchemeAgencyID',
    'SoftwareSecuritySchemeAgencyName',
    'AuthorizationProviderID',
    'AuthorizationProviderSchemeAgencyID',
    'AuthorizationProviderSchemeAgencyName',
    'AuthorizationProviderSchemeID',
    'AuthorizationProviderSchemeName',
    'QRCode',
    'Signature',
    'UBLVersionID',
    'CustomizationID'
]

INVOICE_GENERAL_FIELDS = [
    'UBLVersionID',
    'CustomizationID',
    'ProfileID',
    'ProfileExecutionID',
    'AuthorizedInvoicesPrefix',
    'InvoiceID',
    'SupplierCompanyID',
    'SupplierPartyName',
    'CustomerCompanyID',
    'CustomerRegistrationName',
    'UUID',
    'UUIDSchemeID',
    'UUIDSchemeName',
    'IssueDate',
    'IssueTime',
    'DueDate',
    'InvoiceTypeCode',
    'Note',
    'DocumentCurrencyCode',
    'LineCountNumeric',
    'InvoiceTaxTotalTaxAmount',
    'InvoiceTaxTotalTaxAmountCurrencyID',

    'InvoiceWithholdingTaxTotalTaxAmount',
    'InvoiceWithholdingTaxTotalTaxAmountCurrencyID',

    'InvoiceLineExtensionAmount',
    'InvoiceTaxExclusiveAmount',
    'InvoiceTaxInclusiveAmount',
    'InvoiceAllowanceTotalAmount',
    'InvoiceChargeTotalAmount',
    'InvoicePayableRoundingAmount',
    'InvoicePayableAmount',
    'InvoicePayableAmountCurrencyID',
    
    'InvoicePeriodStartDate',
    'InvoicePeriodStartTime',
    'InvoicePeriodEndDate',
    'InvoicePeriodEndTime',
    'OrderReferenceID',
    'OrderReferenceIssueDate',
    'BillingReferenceID',
    'BillingReferenceUUID',
    'BillingReferenceSchemeName',
    'BillingReferenceIssueDate',
    'DespatchDocumentReferenceID',
    'DespatchDocumentReferenceIssueDate',
    'ReceiptDocumentReferenceID',
    'ReceiptDocumentReferenceIssueDate',
    'AdditionalDocumentReferenceID',
    'AdditionalDocumentReferenceIssueDate',
    'AdditionalDocumentTypeCode',
    'InvoiceActualDeliveryDate',
    'InvoiceActualDeliveryTime',
    'InvoiceDeliveryAddressID',
    'InvoiceDeliveryAddressCityName',
    'InvoiceDeliveryAddressCountrySubentity',
    'InvoiceDeliveryAddressPostalZone',
    'InvoiceDeliveryAddressLine',
    'InvoiceDeliveryAddressCountryCode',
    'InvoiceDeliveryContactName',
    'InvoiceDeliveryContactTelephone',
    'InvoiceDeliveryContactTelefax',
    'InvoiceDeliveryContactElectronicMail',

    'InvoiceDeliveryTermsID',
    'InvoiceDeliveryTermsSpecialTerms',
    'InvoiceDeliveryTermsLossRiskResponsibilityCode',
    'InvoiceDeliveryTermsLossRisk',

    'InvoicePrepaidPaymentID',
    'InvoicePrepaidPaymentPaidAmount',
    'InvoicePrepaidPaymentCurrencyID',
    'InvoicePrepaidPaymentReceivedDate',
    'InvoicePrepaidPaymentPaidDate',
    'InvoicePrepaidPaymentPaidTime',
    'InvoicePrepaidPaymentInstructionID',

    'InvoiceAllowanceChargeID',
    'InvoiceAllowanceChargeChargeIndicator',
    'InvoiceAllowanceChargeReasonCode',
    'InvoiceAllowanceChargeReason',
    'InvoiceAllowanceChargeMultiplierFactorNumeric',
    'InvoiceAllowanceChargeAmount',
    'InvoiceAllowanceChargeAmountCurrencyID',
    'InvoiceAllowanceChargeBaseAmount',
    'InvoiceAllowanceChargeBaseAmountCurrencyID',

    'InvoicePaymentExchangeRateSourceCurrencyCode',
    'InvoicePaymentExchangeRateSourceCurrencyBaseRate',
    'InvoicePaymentExchangeRateTargetCurrencyCode',
    'InvoicePaymentExchangeRateTargetCurrencyBaseRate',
    'InvoicePaymentExchangeRateCalculationRate',
    'InvoicePaymentExchangeRateDate',

    'InvoicePaymentAlternativeExchangeRateSourceCurrencyCode',
    'InvoicePaymentAlternativeExchangeRateSourceCurrencyBaseRate',
    'InvoicePaymentAlternativeExchangeRateTargetCurrencyCode',
    'InvoicePaymentAlternativeExchangeRateTargetCurrencyBaseRate',
    'InvoicePaymentAlternativeExchangeRateCalculationRate',

    
]


ACCOUNTING_SUPPLIER_FIELDS = [
    'SupplierAdditionalAccountID',
    'SupplierPartyID',
    'SupplierPartyName',
    'SupplierIndustryClassificationCode',
    'SupplierPhysicalLocationID',
    'SupplierCityName',
    'SupplierPostalZone',
    'SupplierCountrySubentity',
    'SupplierCountrySubentityCode',
    'SupplierLine',
    'SupplierCountryCode',
    'SupplierCountryName',
    'SupplierCountryLanguageID',
    'SupplierRegistrationName',
    'SupplierTaxLevelCode',
    'SupplierTaxLevelCodeListName',
    'SupplierTaxSchemeID',
    'SupplierTaxSchemeName',
    'SupplierCompanyID',
    'SupplierCompanyIDSchemeID',
    'SupplierCompanyIDSchemeName',
    'SupplierCompanyIDSchemeAgencyID',
    'SupplierCompanyIDSchemeAgencyName',
    'SupplierCorporateRegistrationScheme',
    'SupplierContactName',
    'SupplierContactTelephone',
    'SupplierContactTelefax',
    'SupplierContactElectronicMail',
    'SupplierContactNote',
    'SupplierRegistrationAddressID',
    'SupplierRegistrationAddressCityName',
    'SupplierRegistrationAddressPostalZone',
    'SupplierRegistrationAddressCountrySubentity',
    'SupplierRegistrationAddressCountrySubentityCode',
    'SupplierRegistrationAddressLine',
    'SupplierRegistrationAddressCountryCode',
    'SupplierRegistrationAddressCountryName',
    'SupplierRegistrationAddressCountryLanguageID',
    'SupplierShareholderParticipationPercent'
]


# Add to field groupings
ACCOUNTING_CUSTOMER_FIELDS = [
    'CustomerAdditionalAccountID',
    'CustomerPartyID',
    'CustomerPartyIDSchemeName',
    'CustomerSchemeID',
    'CustomerSchemeName',
    'CustomerPhysicalLocationID',
    'CustomerCityName',
    'CustomerPostalZone',
    'CustomerCountrySubentity',
    'CustomerCountrySubentityCode',
    'CustomerLine',
    'CustomerCountryCode',
    'CustomerCountryName',
    'CustomerCountryLanguageID',
    'CustomerRegistrationName',
    'CustomerTaxLevelCode',
    'CustomerTaxLevelCodeListName',
    'CustomerTaxSchemeID',
    'CustomerTaxSchemeName',
    'CustomerCompanyID',
    'CustomerCompanyIDSchemeID',
    'CustomerCompanyIDSchemeName',
    'CustomerCompanyIDSchemeAgencyID',
    'CustomerCompanyIDSchemeAgencyName',
    'CustomerSchemeAgencyID',
    'CustomerSchemeAgencyName',
    'CustomerCorporateRegistrationScheme',
    'CustomerContactName',
    'CustomerContactTelephone',
    'CustomerContactTelefax',
    'CustomerContactElectronicMail',
    'CustomerContactNote',
    'CustomerRegistrationAddressID',
    'CustomerRegistrationAddressCityName',
    'CustomerRegistrationAddressPostalZone',
    'CustomerRegistrationAddressCountrySubentity',
    'CustomerRegistrationAddressCountrySubentityCode',
    'CustomerRegistrationAddressLine',
    'CustomerRegistrationAddressCountryCode',
    'CustomerRegistrationAddressCountryName',
    'CustomerRegistrationAddressCountryLanguageID',
    'CustomerShareholderParticipationPercent',
    'CustomerTaxRepresentativeID',
    'CustomerTaxRepresentativeIDSchemeID',
    'CustomerTaxRepresentativeIDSchemeAgencyID',
    'CustomerTaxRepresentativeIDSchemeAgencyName',
    'CustomerDeliveryActualDate',
    'CustomerDeliveryActualTime',
    'CustomerDeliveryAddressID',
    'CustomerDeliveryAddressCityName',
    'CustomerDeliveryAddressCountrySubentity',
    'CustomerDeliveryAddressPostalZone',
    'CustomerDeliveryAddressLine',
    'CustomerDeliveryAddressCountryCode'
]

INVOICE_LINES = [
    # InvoiceLine Section
    'InvoiceLineID',
    'InvoiceLineItemDescription',
    'InvoiceLineInvoicedQuantity',
    'InvoiceLineIDSchemeID',
    'InvoiceLineNote',
    'InvoiceLineInvoicedQuantityUnitCode',
    'InvoiceLineLineExtensionAmount',
    'InvoiceLineLineExtensionAmountCurrencyID',
    'InvoiceLineFreeOfChargeIndicator',

    # Item Section
    
    'InvoiceLineItemBuyersItemID',
    'InvoiceLineItemSellersItemID',
    'InvoiceLineItemStandardItemID',
    'InvoiceLineItemStandardItemIDSchemeID',
    'InvoiceLineItemStandardItemIDSchemeAgencyID',
    'InvoiceLineItemStandardItemIDSchemeName',

    # TaxTotal Section
    'InvoiceLineTaxTotalTaxAmount',
    'InvoiceLineTaxTotalTaxAmountCurrencyID',
    'InvoiceLineTaxTotalTaxableAmount',
    'InvoiceLineTaxTotalTaxableAmountCurrencyID',
    'InvoiceLineTaxTotalPercent',
    'InvoiceLineTaxTotalTaxSchemeID',
    'InvoiceLineTaxTotalTaxSchemeName',

    # Price Section
    'InvoiceLinePriceAmount',
    'InvoiceLinePriceAmountCurrencyID',
    'InvoiceLinePriceBaseQuantity',
    'InvoiceLinePriceBaseQuantityUnitCode'

    # PricingReference Section
    'InvoiceLinePricingReferencePriceAmount',
    'InvoiceLinePricingReferencePriceAmountCurrencyID',
    'InvoiceLinePricingReferencePriceTypeCode',

    # AllowanceCharge Section
    'InvoiceLineAllowanceChargeID',
    'InvoiceLineAllowanceChargeChargeIndicator',
    'InvoiceLineAllowanceChargeReason',
    'InvoiceLineAllowanceChargeMultiplierFactorNumeric',
    'InvoiceLineAllowanceChargeAmount',
    'InvoiceLineAllowanceChargeAmountCurrencyID',
    'InvoiceLineAllowanceChargeBaseAmount',
    'InvoiceLineAllowanceChargeBaseAmountCurrencyID',

    # WithholdingTaxTotal Section
    'InvoiceLineWithholdingTaxTotalTaxAmount',
    'InvoiceLineWithholdingTaxTotalTaxAmountCurrencyID',
    'InvoiceLineWithholdingTaxTotalTaxableAmount',
    'InvoiceLineWithholdingTaxTotalTaxableAmountCurrencyID',
    'InvoiceLineWithholdingTaxTotalPercent',
    'InvoiceLineWithholdingTaxTotalTaxSchemeID',
    'InvoiceLineWithholdingTaxTotalTaxSchemeName',
]

# XML mappings
XML_MAPPINGS = {
    # General Invoice Fields
    'UBLVersionID': './cbc:UBLVersionID',
    'CustomizationID': './cbc:CustomizationID',
    'ProfileID': './cbc:ProfileID',
    'ProfileExecutionID': './cbc:ProfileExecutionID',
    'InvoiceID': './cbc:ID',
    'UUID': './cbc:UUID',
    'UUID_schemeID': './cbc:UUID/@schemeID',
    'UUID_schemeName': './cbc:UUID/@schemeName',
    'IssueDate': './cbc:IssueDate',
    'IssueTime': './cbc:IssueTime',
    'DueDate': './cbc:DueDate',
    'InvoiceTypeCode': './cbc:InvoiceTypeCode',
    'Note': './cbc:Note',
    'DocumentCurrencyCode': './cbc:DocumentCurrencyCode',
    'LineCountNumeric': './cbc:LineCountNumeric',
    # Tax Representative Party Section
    'InvoiceTaxRepresentativeID': './/cac:TaxRepresentativeParty/cac:PartyIdentification/cbc:ID',
    'InvoiceTaxRepresentativeIDSchemeID': './/cac:TaxRepresentativeParty/cac:PartyIdentification/cbc:ID/@schemeID',
    'InvoiceTaxRepresentativeIDSchemeAgencyID': './/cac:TaxRepresentativeParty/cac:PartyIdentification/cbc:ID/@schemeAgencyID',
    'InvoiceTaxRepresentativeIDSchemeAgencyName': './/cac:TaxRepresentativeParty/cac:PartyIdentification/cbc:ID/@schemeAgencyName',

    # Delivery Section
    'InvoiceActualDeliveryDate': './/cac:Delivery/cbc:ActualDeliveryDate',
    'InvoiceActualDeliveryTime': './/cac:Delivery/cbc:ActualDeliveryTime',
    'InvoiceDeliveryAddressID': './/cac:Delivery/cac:DeliveryAddress/cbc:ID',
    'InvoiceDeliveryAddressCityName': './/cac:Delivery/cac:DeliveryAddress/cbc:CityName',
    'InvoiceDeliveryAddressCountrySubentity': './/cac:Delivery/cac:DeliveryAddress/cbc:CountrySubentity',
    'InvoiceDeliveryAddressPostalZone': './/cac:Delivery/cac:DeliveryAddress/cbc:PostalZone',
    'InvoiceDeliveryAddressLine': './/cac:Delivery/cac:DeliveryAddress/cac:AddressLine/cbc:Line',
    'InvoiceDeliveryAddressCountryCode': './/cac:Delivery/cac:DeliveryAddress/cac:Country/cbc:IdentificationCode',
    'InvoiceDeliveryContactName': './/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:Name',
    'InvoiceDeliveryContactTelephone': './/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:Telephone',
    'InvoiceDeliveryContactTelefax': './/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:Telefax',
    'InvoiceDeliveryContactElectronicMail': './/cac:Delivery/cac:DeliveryParty/cac:Contact/cbc:ElectronicMail',

    # DeliveryTerms Section
    'InvoiceDeliveryTermsID': './/cac:DeliveryTerms/cbc:ID',
    'InvoiceDeliveryTermsSpecialTerms': './/cac:DeliveryTerms/cbc:SpecialTerms',
    'InvoiceDeliveryTermsLossRiskResponsibilityCode': './/cac:DeliveryTerms/cbc:LossRiskResponsibilityCode',
    'InvoiceDeliveryTermsLossRisk': './/cac:DeliveryTerms/cbc:LossRisk',

    # PrepaidPayment Section
    'InvoicePrepaidPaymentID': './/cac:PrepaidPayment/cbc:ID',
    'InvoicePrepaidPaymentPaidAmount': './/cac:PrepaidPayment/cbc:PaidAmount',
    'InvoicePrepaidPaymentCurrencyID': './/cac:PrepaidPayment/cbc:PaidAmount/@currencyID',
    'InvoicePrepaidPaymentReceivedDate': './/cac:PrepaidPayment/cbc:ReceivedDate',
    'InvoicePrepaidPaymentPaidDate': './/cac:PrepaidPayment/cbc:PaidDate',
    'InvoicePrepaidPaymentPaidTime': './/cac:PrepaidPayment/cbc:PaidTime',
    'InvoicePrepaidPaymentInstructionID': './/cac:PrepaidPayment/cbc:InstructionID',

    # AllowanceCharge Section
    'InvoiceAllowanceChargeID': './/cac:AllowanceCharge/cbc:ID',
    'InvoiceAllowanceChargeChargeIndicator': './/cac:AllowanceCharge/cbc:ChargeIndicator',
    'InvoiceAllowanceChargeReasonCode': './/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode',
    'InvoiceAllowanceChargeReason': './/cac:AllowanceCharge/cbc:AllowanceChargeReason',
    'InvoiceAllowanceChargeMultiplierFactorNumeric': './/cac:AllowanceCharge/cbc:MultiplierFactorNumeric',
    'InvoiceAllowanceChargeAmount': './/cac:AllowanceCharge/cbc:Amount',
    'InvoiceAllowanceChargeAmountCurrencyID': './/cac:AllowanceCharge/cbc:Amount/@currencyID',
    'InvoiceAllowanceChargeBaseAmount': './/cac:AllowanceCharge/cbc:BaseAmount',
    'InvoiceAllowanceChargeBaseAmountCurrencyID': './/cac:AllowanceCharge/cbc:BaseAmount/@currencyID',

    # PaymentExchangeRate Section
    'InvoicePaymentExchangeRateSourceCurrencyCode': './/cac:PaymentExchangeRate/cbc:SourceCurrencyCode',
    'InvoicePaymentExchangeRateSourceCurrencyBaseRate': './/cac:PaymentExchangeRate/cbc:SourceCurrencyBaseRate',
    'InvoicePaymentExchangeRateTargetCurrencyCode': './/cac:PaymentExchangeRate/cbc:TargetCurrencyCode',
    'InvoicePaymentExchangeRateTargetCurrencyBaseRate': './/cac:PaymentExchangeRate/cbc:TargetCurrencyBaseRate',
    'InvoicePaymentExchangeRateCalculationRate': './/cac:PaymentExchangeRate/cbc:CalculationRate',
    'InvoicePaymentExchangeRateDate': './/cac:PaymentExchangeRate/cbc:Date',

    # PaymentAlternativeExchangeRate Section
    'InvoicePaymentAlternativeExchangeRateSourceCurrencyCode': './/cac:PaymentAlternativeExchangeRate/cbc:SourceCurrencyCode',
    'InvoicePaymentAlternativeExchangeRateSourceCurrencyBaseRate': './/cac:PaymentAlternativeExchangeRate/cbc:SourceCurrencyBaseRate',
    'InvoicePaymentAlternativeExchangeRateTargetCurrencyCode': './/cac:PaymentAlternativeExchangeRate/cbc:TargetCurrencyCode',
    'InvoicePaymentAlternativeExchangeRateTargetCurrencyBaseRate': './/cac:PaymentAlternativeExchangeRate/cbc:TargetCurrencyBaseRate',
    'InvoicePaymentAlternativeExchangeRateCalculationRate': './/cac:PaymentAlternativeExchangeRate/cbc:CalculationRate',

    # TaxTotal Section
    'InvoiceTaxTotalTaxAmount': './/cac:TaxTotal/cbc:TaxAmount',
    'InvoiceTaxTotalTaxAmountCurrencyID': './/cac:TaxTotal/cbc:TaxAmount/@currencyID',

    # WithholdingTaxTotal Section
    'InvoiceWithholdingTaxTotalTaxAmount': './/cac:WithholdingTaxTotal/cbc:TaxAmount',
    'InvoiceWithholdingTaxTotalTaxAmountCurrencyID': './/cac:WithholdingTaxTotal/cbc:TaxAmount/@currencyID',

    # LegalMonetaryTotal Section
    'InvoiceLineExtensionAmount': './/cac:LegalMonetaryTotal/cbc:LineExtensionAmount',
    'InvoiceTaxExclusiveAmount': './/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount',
    'InvoiceTaxInclusiveAmount': './/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount',
    'InvoiceAllowanceTotalAmount': './/cac:LegalMonetaryTotal/cbc:AllowanceTotalAmount',
    'InvoiceChargeTotalAmount': './/cac:LegalMonetaryTotal/cbc:ChargeTotalAmount',
    'InvoicePrepaidAmount': './/cac:LegalMonetaryTotal/cbc:PrepaidAmount',
    'InvoicePrepaidAmountCurrencyID': './/cac:LegalMonetaryTotal/cbc:PrepaidAmount/@currencyID',
    'InvoicePayableRoundingAmount': './/cac:LegalMonetaryTotal/cbc:PayableRoundingAmount',
    'InvoicePayableAmount': './/cac:LegalMonetaryTotal/cbc:PayableAmount',
    'InvoicePayableAmountCurrencyID': './/cac:LegalMonetaryTotal/cbc:PayableAmount/@currencyID',

    #------------------------------------------------------------------------------------------------------
    
    # UBLExtensions Fields
    'UBLExtensions': './/ext:UBLExtensions',
    'UBLExtension': './/ext:UBLExtensions/ext:UBLExtension',
    'ExtensionContent': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent',

    # UBLExtensions Dian Extensions
    'DianExtensions': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions',
    'InvoiceControl': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:InvoiceControl',
    'InvoiceAuthorization': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:InvoiceControl/sts:InvoiceAuthorization',
    'AuthorizationPeriodStartDate': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:InvoiceControl/sts:AuthorizationPeriod/cbc:StartDate',
    'AuthorizationPeriodEndDate': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:InvoiceControl/sts:AuthorizationPeriod/cbc:EndDate',
    'AuthorizedInvoicesPrefix': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:InvoiceControl/sts:AuthorizedInvoices/sts:Prefix',
    'AuthorizedInvoicesFrom': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:InvoiceControl/sts:AuthorizedInvoices/sts:From',
    'AuthorizedInvoicesTo': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:InvoiceControl/sts:AuthorizedInvoices/sts:To',

    # UBLExtensions Invoice Source
    'InvoiceSourceCountryCode': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:InvoiceSource/cbc:IdentificationCode',
    'InvoiceSourceCountryListAgencyID': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:InvoiceSource/cbc:IdentificationCode/@listAgencyID',
    'InvoiceSourceCountryListAgencyName': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:InvoiceSource/cbc:IdentificationCode/@listAgencyName',
    'InvoiceSourceCountryListSchemeURI': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:InvoiceSource/cbc:IdentificationCode/@listSchemeURI',

    # UBLExtensions Software Provider
    'SoftwareProviderID': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:SoftwareProvider/sts:ProviderID',
    'SoftwareProviderSchemeAgencyID': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:SoftwareProvider/sts:ProviderID/@schemeAgencyID',
    'SoftwareProviderSchemeAgencyName': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:SoftwareProvider/sts:ProviderID/@schemeAgencyName',
    'SoftwareID': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:SoftwareProvider/sts:softwareID',
    'SoftwareSchemeAgencyID': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:SoftwareProvider/sts:softwareID/@schemeAgencyID',
    'SoftwareSchemeAgencyName': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:SoftwareProvider/sts:softwareID/@schemeAgencyName',
    'SoftwareSecurityCode': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:SoftwareSecurityCode',
    'SoftwareSecuritySchemeAgencyID': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:SoftwareSecurityCode/@schemeAgencyID',
    'SoftwareSecuritySchemeAgencyName': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:SoftwareSecurityCode/@schemeAgencyName',

    # UBLExtensions Authorization Provider
    'AuthorizationProviderID': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:AuthorizationProvider/sts:AuthorizationProviderID',
    'AuthorizationProviderSchemeAgencyID': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:AuthorizationProvider/sts:AuthorizationProviderID/@schemeAgencyID',
    'AuthorizationProviderSchemeAgencyName': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:AuthorizationProvider/sts:AuthorizationProviderID/@schemeAgencyName',
    'AuthorizationProviderSchemeID': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:AuthorizationProvider/sts:AuthorizationProviderID/@schemeID',
    'AuthorizationProviderSchemeName': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:AuthorizationProvider/sts:AuthorizationProviderID/@schemeName',

    # UBLExtensions QR Code and Signature
    'QRCode': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/sts:DianExtensions/sts:QRCode',
    'Signature': './/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/ds:Signature',

    # UBLExtensions UBL Version and Customization
    'UBLVersionID': './/cbc:UBLVersionID',
    'CustomizationID': './/cbc:CustomizationID',

    #------------------------------------------------------------------------------------------------------

    # AccountingSupplierParty mappings
    'SupplierAdditionalAccountID': './/cac:AccountingSupplierParty/cbc:AdditionalAccountID',
    'SupplierPartyID': './/cac:AccountingSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID',
    'SupplierPartyName': './/cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name',
    'SupplierIndustryClassificationCode': './/cac:AccountingSupplierParty/cac:Party/cbc:IndustryClassificationCode',
    'SupplierPhysicalLocationID': './/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cac:Address/cbc:ID',
    'SupplierCityName': './/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cac:Address/cbc:CityName',
    'SupplierPostalZone': './/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cac:Address/cbc:PostalZone',
    'SupplierCountrySubentity': './/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cac:Address/cbc:CountrySubentity',
    'SupplierCountrySubentityCode': './/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cac:Address/cbc:CountrySubentityCode',
    'SupplierLine': './/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cac:Address/cac:AddressLine/cbc:Line',
    'SupplierCountryCode': './/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cac:Address/cac:Country/cbc:IdentificationCode',
    'SupplierCountryName': './/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cac:Address/cac:Country/cbc:Name',
    'SupplierCountryLanguageID': './/cac:AccountingSupplierParty/cac:Party/cac:PhysicalLocation/cac:Address/cac:Country/cbc:Name/@languageID',
    
        # AccountingSupplierParty Tax Information
    'SupplierRegistrationName': './/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:RegistrationName',
    'SupplierTaxLevelCode': './/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:TaxLevelCode',
    'SupplierTaxLevelCodeListName': './/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:TaxLevelCode/@listName',
    'SupplierTaxSchemeID': './/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID',
    'SupplierTaxSchemeName': './/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:Name',

        # AccountingSupplierParty Legal Entity Information
    'SupplierCompanyID': './/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyID',
    'SupplierCompanyIDSchemeID': './/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyID/@schemeID',
    'SupplierCompanyIDSchemeName': './/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyID/@schemeName',
    'SupplierCompanyIDSchemeAgencyID': './/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyID/@schemeAgencyID',
    'SupplierCompanyIDSchemeAgencyName': './/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyID/@schemeAgencyName',

        # AccountingSupplierParty Contact Information
    'SupplierContactName': './/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Name',
    'SupplierContactTelephone': './/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Telephone',
    'SupplierContactTelefax': './/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:Telefax',
    'SupplierContactElectronicMail': './/cac:AccountingSupplierParty/cac:Party/cac:Contact/cbc:ElectronicMail',

        # AccountingSupplierParty Registration Address
    'SupplierRegistrationAddressID': './/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cac:RegistrationAddress/cbc:ID',
    'SupplierRegistrationAddressCityName': './/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cac:RegistrationAddress/cbc:CityName',
    'SupplierRegistrationAddressPostalZone': './/cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cac:RegistrationAddress/cbc:PostalZone',
    'SupplierShareholderParticipationPercent': './/cac:AccountingSupplierParty/cac:Party/cac:PartyLegalEntity/cac:ShareholderParty/cbc:PartecipationPercent',

    #------------------------------------------------------------------------------------------------------

    # AccountingCustomerParty mappings
    'CustomerAdditionalAccountID': './/cac:AccountingCustomerParty/cbc:AdditionalAccountID',
    'CustomerPartyID': './/cac:AccountingCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID',
    'CustomerPartyIDSchemeName': './/cac:AccountingCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID/@schemeName',
    'CustomerSchemeID': './/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyID/@schemeID',
    'CustomerSchemeName': './/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyID/@schemeName',
    'CustomerPhysicalLocationID': './/cac:AccountingCustomerParty/cac:Party/cac:PhysicalLocation/cac:Address/cbc:ID',
    'CustomerCityName': './/cac:AccountingCustomerParty/cac:Party/cac:PhysicalLocation/cac:Address/cbc:CityName',
    'CustomerPostalZone': './/cac:AccountingCustomerParty/cac:Party/cac:PhysicalLocation/cac:Address/cbc:PostalZone',
    'CustomerCountrySubentity': './/cac:AccountingCustomerParty/cac:Party/cac:PhysicalLocation/cac:Address/cbc:CountrySubentity',
    'CustomerCountrySubentityCode': './/cac:AccountingCustomerParty/cac:Party/cac:PhysicalLocation/cac:Address/cbc:CountrySubentityCode',
    'CustomerLine': './/cac:AccountingCustomerParty/cac:Party/cac:PhysicalLocation/cac:Address/cac:AddressLine/cbc:Line',
    'CustomerCountryCode': './/cac:AccountingCustomerParty/cac:Party/cac:PhysicalLocation/cac:Address/cac:Country/cbc:IdentificationCode',
    'CustomerCountryName': './/cac:AccountingCustomerParty/cac:Party/cac:PhysicalLocation/cac:Address/cac:Country/cbc:Name',
    'CustomerCountryLanguageID': './/cac:AccountingCustomerParty/cac:Party/cac:PhysicalLocation/cac:Address/cac:Country/cbc:Name/@languageID',
    
    # Tax Information
    'CustomerRegistrationName': './/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:RegistrationName',
    'CustomerTaxLevelCode': './/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:TaxLevelCode',
    'CustomerTaxLevelCodeListName': './/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:TaxLevelCode/@listName',
    'CustomerTaxSchemeID': './/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID',
    'CustomerTaxSchemeName': './/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cac:TaxScheme/cbc:Name',

    # Legal Entity Information
    'CustomerCompanyID': './/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyID',
    'CustomerCompanyIDSchemeID': './/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyID/@schemeID',
    'CustomerCompanyIDSchemeName': './/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyID/@schemeName',
    'CustomerCompanyIDSchemeAgencyID': './/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyID/@schemeAgencyID',
    'CustomerCompanyIDSchemeAgencyName': './/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyID/@schemeAgencyName',

    # Contact Information
    'CustomerContactName': './/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name',
    'CustomerContactTelephone': './/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Telephone',
    'CustomerContactTelefax': './/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Telefax',
    'CustomerContactElectronicMail': './/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:ElectronicMail',
    'CustomerContactNote': './/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Note',

    # Registration Address
    'CustomerRegistrationAddressID': './/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cac:RegistrationAddress/cbc:ID',
    'CustomerRegistrationAddressCityName': './/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cac:RegistrationAddress/cbc:CityName',
    'CustomerRegistrationAddressPostalZone': './/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cac:RegistrationAddress/cbc:PostalZone',
    'CustomerRegistrationAddressCountrySubentity': './/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cac:RegistrationAddress/cbc:CountrySubentity',
    'CustomerRegistrationAddressCountrySubentityCode': './/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cac:RegistrationAddress/cbc:CountrySubentityCode',
    'CustomerRegistrationAddressLine': './/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cac:RegistrationAddress/cac:AddressLine/cbc:Line',
    'CustomerRegistrationAddressCountryCode': './/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cac:RegistrationAddress/cac:Country/cbc:IdentificationCode',
    'CustomerRegistrationAddressCountryName': './/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cac:RegistrationAddress/cac:Country/cbc:Name',
    'CustomerRegistrationAddressCountryLanguageID': './/cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cac:RegistrationAddress/cac:Country/cbc:Name/@languageID',

    # Shareholder Participation
    'CustomerShareholderParticipationPercent': './/cac:AccountingCustomerParty/cac:Party/cac:PartyLegalEntity/cac:ShareholderParty/cbc:PartecipationPercent',

    # Tax Representative
    'CustomerTaxRepresentativeID': './/cac:AccountingCustomerParty/cac:Party/cac:TaxRepresentativeParty/cac:PartyIdentification/cbc:ID',
    'CustomerTaxRepresentativeIDSchemeID': './/cac:AccountingCustomerParty/cac:Party/cac:TaxRepresentativeParty/cac:PartyIdentification/cbc:ID/@schemeID',
    'CustomerTaxRepresentativeIDSchemeAgencyID': './/cac:AccountingCustomerParty/cac:Party/cac:TaxRepresentativeParty/cac:PartyIdentification/cbc:ID/@schemeAgencyID',
    'CustomerTaxRepresentativeIDSchemeAgencyName': './/cac:AccountingCustomerParty/cac:Party/cac:TaxRepresentativeParty/cac:PartyIdentification/cbc:ID/@schemeAgencyName',

    # Delivery Address
    'CustomerDeliveryActualDate': './/cac:AccountingCustomerParty/cac:Party/cac:Delivery/cbc:ActualDeliveryDate',
    'CustomerDeliveryActualTime': './/cac:AccountingCustomerParty/cac:Party/cac:Delivery/cbc:ActualDeliveryTime',
    'CustomerDeliveryAddressID': './/cac:AccountingCustomerParty/cac:Party/cac:Delivery/cac:DeliveryAddress/cbc:ID',
    'CustomerDeliveryAddressCityName': './/cac:AccountingCustomerParty/cac:Party/cac:Delivery/cac:DeliveryAddress/cbc:CityName',
    'CustomerDeliveryAddressCountrySubentity': './/cac:AccountingCustomerParty/cac:Party/cac:Delivery/cac:DeliveryAddress/cbc:CountrySubentity',
    'CustomerDeliveryAddressPostalZone': './/cac:AccountingCustomerParty/cac:Party/cac:Delivery/cac:DeliveryAddress/cbc:PostalZone',
    'CustomerDeliveryAddressLine': './/cac:AccountingCustomerParty/cac:Party/cac:Delivery/cac:DeliveryAddress/cac:AddressLine/cbc:Line',
    'CustomerDeliveryAddressCountryCode': './/cac:AccountingCustomerParty/cac:Party/cac:Delivery/cac:DeliveryAddress/cac:Country/cbc:IdentificationCode',

#------------------------------------------------------------------------------------------------------

    # InvoiceLine Section
    'InvoiceLineID': './/cac:InvoiceLine/cbc:ID',
    'InvoiceLineIDSchemeID': './/cac:InvoiceLine/cbc:ID/@schemeID',
    'InvoiceLineNote': './/cac:InvoiceLine/cbc:Note',
    'InvoiceLineInvoicedQuantity': './/cac:InvoiceLine/cbc:InvoicedQuantity',
    'InvoiceLineInvoicedQuantityUnitCode': './/cac:InvoiceLine/cbc:InvoicedQuantity/@unitCode',
    'InvoiceLineLineExtensionAmount': './/cac:InvoiceLine/cbc:LineExtensionAmount',
    'InvoiceLineLineExtensionAmountCurrencyID': './/cac:InvoiceLine/cbc:LineExtensionAmount/@currencyID',
    'InvoiceLineFreeOfChargeIndicator': './/cac:InvoiceLine/cbc:FreeOfChargeIndicator',

    # PricingReference Section
    'InvoiceLinePricingReferencePriceAmount': './/cac:InvoiceLine/cac:PricingReference/cac:AlternativeConditionPrice/cbc:PriceAmount',
    'InvoiceLinePricingReferencePriceAmountCurrencyID': './/cac:InvoiceLine/cac:PricingReference/cac:AlternativeConditionPrice/cbc:PriceAmount/@currencyID',
    'InvoiceLinePricingReferencePriceTypeCode': './/cac:InvoiceLine/cac:PricingReference/cac:AlternativeConditionPrice/cbc:PriceTypeCode',

    # AllowanceCharge Section
    'InvoiceLineAllowanceChargeID': './/cac:InvoiceLine/cac:AllowanceCharge/cbc:ID',
    'InvoiceLineAllowanceChargeChargeIndicator': './/cac:InvoiceLine/cac:AllowanceCharge/cbc:ChargeIndicator',
    'InvoiceLineAllowanceChargeReason': './/cac:InvoiceLine/cac:AllowanceCharge/cbc:AllowanceChargeReason',
    'InvoiceLineAllowanceChargeMultiplierFactorNumeric': './/cac:InvoiceLine/cac:AllowanceCharge/cbc:MultiplierFactorNumeric',
    'InvoiceLineAllowanceChargeAmount': './/cac:InvoiceLine/cac:AllowanceCharge/cbc:Amount',
    'InvoiceLineAllowanceChargeAmountCurrencyID': './/cac:InvoiceLine/cac:AllowanceCharge/cbc:Amount/@currencyID',
    'InvoiceLineAllowanceChargeBaseAmount': './/cac:InvoiceLine/cac:AllowanceCharge/cbc:BaseAmount',
    'InvoiceLineAllowanceChargeBaseAmountCurrencyID': './/cac:InvoiceLine/cac:AllowanceCharge/cbc:BaseAmount/@currencyID',

    # TaxTotal Section
    'InvoiceLineTaxTotalTaxAmount': './/cac:InvoiceLine/cac:TaxTotal/cbc:TaxAmount',
    'InvoiceLineTaxTotalTaxAmountCurrencyID': './/cac:InvoiceLine/cac:TaxTotal/cbc:TaxAmount/@currencyID',
    'InvoiceLineTaxTotalTaxableAmount': './/cac:InvoiceLine/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount',
    'InvoiceLineTaxTotalTaxableAmountCurrencyID': './/cac:InvoiceLine/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount/@currencyID',
    'InvoiceLineTaxTotalPercent': './/cac:InvoiceLine/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent',
    'InvoiceLineTaxTotalTaxSchemeID': './/cac:InvoiceLine/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:ID',
    'InvoiceLineTaxTotalTaxSchemeName': './/cac:InvoiceLine/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:Name',

    # WithholdingTaxTotal Section
    'InvoiceLineWithholdingTaxTotalTaxAmount': './/cac:InvoiceLine/cac:WithholdingTaxTotal/cbc:TaxAmount',
    'InvoiceLineWithholdingTaxTotalTaxAmountCurrencyID': './/cac:InvoiceLine/cac:WithholdingTaxTotal/cbc:TaxAmount/@currencyID',
    'InvoiceLineWithholdingTaxTotalTaxableAmount': './/cac:InvoiceLine/cac:WithholdingTaxTotal/cac:TaxSubtotal/cbc:TaxableAmount',
    'InvoiceLineWithholdingTaxTotalTaxableAmountCurrencyID': './/cac:InvoiceLine/cac:WithholdingTaxTotal/cac:TaxSubtotal/cbc:TaxableAmount/@currencyID',
    'InvoiceLineWithholdingTaxTotalPercent': './/cac:InvoiceLine/cac:WithholdingTaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent',
    'InvoiceLineWithholdingTaxTotalTaxSchemeID': './/cac:InvoiceLine/cac:WithholdingTaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:ID',
    'InvoiceLineWithholdingTaxTotalTaxSchemeName': './/cac:InvoiceLine/cac:WithholdingTaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:Name',

    # Item Section
    'InvoiceLineItemDescription': './/cac:InvoiceLine/cac:Item/cbc:Description',
    'InvoiceLineItemBuyersItemID': './/cac:InvoiceLine/cac:Item/cac:BuyersItemIdentification/cbc:ID',
    'InvoiceLineItemSellersItemID': './/cac:InvoiceLine/cac:Item/cac:SellersItemIdentification/cbc:ID',
    'InvoiceLineItemStandardItemID': './/cac:InvoiceLine/cac:Item/cac:StandardItemIdentification/cbc:ID',
    'InvoiceLineItemStandardItemIDSchemeID': './/cac:InvoiceLine/cac:Item/cac:StandardItemIdentification/cbc:ID/@schemeID',
    'InvoiceLineItemStandardItemIDSchemeAgencyID': './/cac:InvoiceLine/cac:Item/cac:StandardItemIdentification/cbc:ID/@schemeAgencyID',
    'InvoiceLineItemStandardItemIDSchemeName': './/cac:InvoiceLine/cac:Item/cac:StandardItemIdentification/cbc:ID/@schemeName',

    # Price Section
    'InvoiceLinePriceAmount': './/cac:InvoiceLine/cac:Price/cbc:PriceAmount',
    'InvoiceLinePriceAmountCurrencyID': './/cac:InvoiceLine/cac:Price/cbc:PriceAmount/@currencyID',
    'InvoiceLinePriceBaseQuantity': './/cac:InvoiceLine/cac:Price/cbc:BaseQuantity',
    'InvoiceLinePriceBaseQuantityUnitCode': './/cac:InvoiceLine/cac:Price/cbc:BaseQuantity/@unitCode'
}
