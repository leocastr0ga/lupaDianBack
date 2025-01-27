using System;
using System.Collections.Generic;
using System.IO;
using System.Net;
using System.Net.Http;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.IO.Compression; 

namespace diantokensearchback.Services
{
    public class TableDownloadService
    {
        private readonly HttpClient _httpClient;
        private readonly CookieContainer _cookieContainer;

        public TableDownloadService()
        {
            _cookieContainer = new CookieContainer();
            var handler = new HttpClientHandler
            {
                CookieContainer = _cookieContainer,
                UseCookies = true
            };
            _httpClient = new HttpClient(handler);
        }

        public async Task<(List<Dictionary<string, object>> TabulatedData, List<string> DownloadedFiles, double TotalSeconds, double AverageSecondsPerDocument)> AuthenticateTabulateAndDownloadAsync(
            string authUrl,
            string startDate,
            string endDate,
            string downloadPath,
            bool recibidos,
            bool enviados)
        {
            var stopwatch = System.Diagnostics.Stopwatch.StartNew(); // Iniciar cronómetro

            var tabulatedData = new List<Dictionary<string, object>>();
            var downloadedFiles = new List<string>();

            try
            {
                // **Paso 1: Autenticación**
                Console.WriteLine($"Autenticando con: {authUrl}");
                var authResponse = await _httpClient.GetAsync(authUrl);
                if (!authResponse.IsSuccessStatusCode)
                {
                    Console.WriteLine($"Error en autenticación: {authResponse.StatusCode}");
                    stopwatch.Stop();
                    return (tabulatedData, downloadedFiles, stopwatch.Elapsed.TotalSeconds, 0);
                }
                Console.WriteLine("Autenticación exitosa. Cookies capturadas.");

                if (!Directory.Exists(downloadPath))
                {
                    Directory.CreateDirectory(downloadPath);
                }

                if (recibidos)
                {
                    await ProcesarYDescargar("Received");
                }

                if (enviados)
                {
                    await ProcesarYDescargar("Sent");
                }

                stopwatch.Stop(); // Detener el cronómetro
                double totalSeconds = stopwatch.Elapsed.TotalSeconds;
                double avgPerDoc = (downloadedFiles.Count > 0) ? totalSeconds / downloadedFiles.Count : 0;

                return (tabulatedData, downloadedFiles, totalSeconds, avgPerDoc);

                async Task ProcesarYDescargar(string tipo)
                {
                    string tipoConsulta = (tipo == "Received") ? "Recibido" : "Enviado";

                    string endpointUrl = $"https://catalogo-vpfe.dian.gov.co/Document/{tipo}";
                    Console.WriteLine($"Solicitando datos desde: {endpointUrl}");
                    var requestData = $"startDate={startDate}&endDate={endDate}";
                    var requestContent = new StringContent(requestData, Encoding.UTF8, "application/x-www-form-urlencoded");
                    var response = await _httpClient.PostAsync(endpointUrl, requestContent);

                    if (!response.IsSuccessStatusCode)
                    {
                        Console.WriteLine($"Error al obtener datos de la tabla ({tipo}): {response.StatusCode}");
                        return;
                    }

                    var responseContent = await response.Content.ReadAsStringAsync();
                    Console.WriteLine($"Datos obtenidos correctamente para {tipo}.");

                    // Guardar la respuesta HTML
                    string responseFilePath = Path.Combine(downloadPath, $"tabla_datos_{tipo}.html");
                    await File.WriteAllTextAsync(responseFilePath, responseContent);
                    Console.WriteLine($"HTML de la tabla ({tipo}) guardado en: {responseFilePath}");

                    // Tabular datos
                    var datosTabulados = TabulateDataFromHtml(responseContent);

                    // Agregar el campo "Tipo_Consulta" a cada fila
                    foreach (var row in datosTabulados)
                    {
                        row["Tipo_Consulta"] = tipoConsulta;
                    }

                    // Agregar al total
                    tabulatedData.AddRange(datosTabulados);

                    // Crear diccionario trackId -> row
                    var rowsByTrackId = new Dictionary<string, Dictionary<string, object>>();
                    foreach (var row in datosTabulados)
                    {
                        if (row.ContainsKey("id") && row["id"] != null)
                        {
                            var trackIdKey = row["id"]?.ToString();
                            if (!string.IsNullOrEmpty(trackIdKey))
                            {
                                rowsByTrackId[trackIdKey] = row;
                            }
                        }
                    }

                    // Filtrar trackIds que no sean "Application response"
                    var trackIds = new List<string>();
                    var validDocTipos = new HashSet<string> { "96" };
                    foreach (var kvp in rowsByTrackId)
                    {
                        var row = kvp.Value;
                        if (row.ContainsKey("DocTipo"))
                        {
                            var docTipoValue = row["DocTipo"]?.ToString();
                            if (docTipoValue != null && (!validDocTipos.Contains(docTipoValue)))
                            {
                                //{
                                // Es "Application response", no se descarga
                                // continue;
                                //}
                                trackIds.Add(kvp.Key);
                            }
                        }
                    }



                    Console.WriteLine($"Se encontraron {trackIds.Count} TrackIDs únicos en {tipo} para descarga.");

                    if (trackIds.Count == 0)
                    {
                        Console.WriteLine($"No se encontraron TrackIDs únicos para descargar en {tipo} (o todos eran Application response).");
                        return;
                    }

                    // Descargar archivos con el nombre personalizado
                    // Descargar archivos con el nombre personalizado
                    // Descargar archivos con el nombre personalizado
                    foreach (var trackId in trackIds)
                    {
                        var row = rowsByTrackId[trackId];
                        var docTipoActual = row.ContainsKey("DocTipo") ? row["DocTipo"]?.ToString() ?? "" : "";

                        string downloadUrl;
                        if (docTipoActual == "05" )
                        {
                            downloadUrl = $"https://catalogo-vpfe.dian.gov.co/Document/GetFilePdf?cune={trackId}";
                        }
                        else if (docTipoActual == "60")
                        {
                            downloadUrl = $"https://catalogo-vpfe.dian.gov.co/Document/DownloadZipFilesEquivalente?trackId={trackId}";
                        }
                        else if (docTipoActual == "102")
                        {
                            downloadUrl = $"https://catalogo-vpfe.dian.gov.co/Document/GetFilePdf?cune={trackId}";
                        }
                        else
                        {
                            downloadUrl = $"https://catalogo-vpfe.dian.gov.co/Document/DownloadZipFiles?trackId={trackId}";
                        }


                        Console.WriteLine($"Descargando archivo desde: {downloadUrl}");

                        var downloadResponse = await _httpClient.GetAsync(downloadUrl);
                        if (downloadResponse.IsSuccessStatusCode)
                        {
                            // Extraer datos para el nombre del archivo
                            string fecha = row.ContainsKey("Fecha") ? row["Fecha"]?.ToString() ?? "" : "";
                            string prefijo = row.ContainsKey("Prefijo") ? row["Prefijo"]?.ToString() ?? "" : "";
                            string n_documento = row.ContainsKey("N_documento") ? row["N_documento"]?.ToString() ?? "" : "";
                            string thisTipoConsulta = row.ContainsKey("Tipo_Consulta") ? row["Tipo_Consulta"]?.ToString() ?? "" : "";
                            string docTipo = row.ContainsKey("DocTipo") ? row["DocTipo"]?.ToString() ?? "" : "";

                            string nit, nombreCorto;
                            if (tipo == "Received")
                            {
                                string nitEmisor = row.ContainsKey("NIT Emisor") ? row["NIT Emisor"]?.ToString() ?? "" : "";
                                string emisor = row.ContainsKey("Emisor") ? row["Emisor"]?.ToString() ?? "" : "";
                                string emisorCorto = (emisor.Length > 10) ? emisor.Substring(0, 10) : emisor;

                                nit = nitEmisor;
                                nombreCorto = emisorCorto;
                            }
                            else // Sent
                            {
                                string nitReceptor = row.ContainsKey("NIT Receptor") ? row["NIT Receptor"]?.ToString() ?? "" : "";
                                string receptor = row.ContainsKey("Receptor") ? row["Receptor"]?.ToString() ?? "" : "";
                                string receptorCorto = (receptor.Length > 10) ? receptor.Substring(0, 10) : receptor;

                                nit = nitReceptor;
                                nombreCorto = receptorCorto;
                            }

                            string safeFecha = RemoveInvalidFileNameChars(fecha);
                            string safePrefijo = RemoveInvalidFileNameChars(prefijo);
                            string safeN_documento = RemoveInvalidFileNameChars(n_documento);
                            string safeTipoConsulta = RemoveInvalidFileNameChars(thisTipoConsulta);
                            string safeDocTipo = RemoveInvalidFileNameChars(docTipo);
                            string safeNit = RemoveInvalidFileNameChars(nit);
                            string safeNombreCorto = RemoveInvalidFileNameChars(nombreCorto);

                            var contentType = downloadResponse.Content.Headers.ContentType?.MediaType;

                            // Determinar la extensión según el tipo MIME de la respuesta
                            string fileExtension;
                            if (contentType == "application/pdf")
                            {
                                fileExtension = "pdf";
                            }
                            else if (contentType == "application/zip")
                            {
                                fileExtension = "zip";
                            }
                            else
                            {
                                // Si no se reconoce el tipo, puedes usar una extensión genérica o basarte en DocTipo
                                // fileExtension = (docTipoActual == "05") ? "pdf" : "zip"; // Si quieres mantener la lógica anterior
                                // o simplemente:
                                fileExtension = "bin"; // extensión genérica para contenido desconocido
                            }

                            string fileName = $"{safeTipoConsulta}-{safeDocTipo}-{safeFecha}-{safePrefijo}-{safeN_documento}-{safeNit}-{safeNombreCorto}-{trackId}.{fileExtension}";
                            string filePath = Path.Combine(downloadPath, fileName);

                            var fileContent = await downloadResponse.Content.ReadAsByteArrayAsync();
                            await File.WriteAllBytesAsync(filePath, fileContent);

                            Console.WriteLine($"Archivo descargado exitosamente: {filePath}");
                            downloadedFiles.Add(filePath);

                            // Si el archivo es un ZIP, extraerlo y clasificar contenidos
                            if (fileExtension == "zip")
                            {
                                string pdfFolder = Path.Combine(downloadPath, "PDF");
                                string xmlFolder = Path.Combine(downloadPath, "XML");

                                if (!Directory.Exists(pdfFolder))
                                    Directory.CreateDirectory(pdfFolder);

                                if (!Directory.Exists(xmlFolder))
                                    Directory.CreateDirectory(xmlFolder);

                                string baseName = Path.GetFileNameWithoutExtension(fileName); // Quitar .zip

                                using (var zipArchive = System.IO.Compression.ZipFile.OpenRead(filePath))
                                {
                                    foreach (var entry in zipArchive.Entries)
                                    {
                                        if (entry.FullName.EndsWith(".pdf", StringComparison.OrdinalIgnoreCase))
                                        {
                                            string pdfFilePath = Path.Combine(pdfFolder, baseName + ".pdf");
                                            entry.ExtractToFile(pdfFilePath, overwrite: true);
                                        }
                                        else if (entry.FullName.EndsWith(".xml", StringComparison.OrdinalIgnoreCase))
                                        {
                                            string xmlFilePath = Path.Combine(xmlFolder, baseName + ".xml");
                                            entry.ExtractToFile(xmlFilePath, overwrite: true);
                                        }
                                    }
                                }
                            }
                        }
                        else
                        {
                            Console.WriteLine($"Error al descargar archivo con TrackID {trackId}: {downloadResponse.StatusCode}");
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
                double totalSeconds = stopwatch.Elapsed.TotalSeconds;
                double avgPerDoc = (downloadedFiles.Count > 0) ? totalSeconds / downloadedFiles.Count : 0;
                return (tabulatedData, downloadedFiles, totalSeconds, avgPerDoc);
            }
        }


        /// <summary>
        /// Tabula los datos de la tabla HTML en una estructura con propiedades con nombre.
        /// Ahora además, extrae el data-type y lo agrega como "DocTipo" justo después de "Recepcion".
        /// </summary>
        private List<Dictionary<string, object>> TabulateDataFromHtml(string htmlContent)
        {
            var tabulatedData = new List<Dictionary<string, object>>();

            string[] headers = {
                "Recepcion",
                "Fecha",
                "Prefijo",
                "N_documento",
                "Tipo",
                "NIT Emisor",
                "Emisor",
                "NIT Receptor",
                "Receptor",
                "Resultado",
                "Estado RADIAN",
                "Valor Total"
            };

            var rowRegex = new Regex(@"<tr.*?>(.*?)<\/tr>", RegexOptions.Singleline);
            var matches = rowRegex.Matches(htmlContent);

            foreach (Match match in matches)
            {
                var rowContent = match.Groups[1].Value;

                // Extraer trackId (data-id) de la fila
                var trackIdMatch = Regex.Match(rowContent, @"data-id=""(.*?)""");
                var trackId = trackIdMatch.Success ? trackIdMatch.Groups[1].Value : null;

                // Extraer data-type
                var dataTypeMatch = Regex.Match(rowContent, @"data-type=""(.*?)""");
                var docTipo = dataTypeMatch.Success ? dataTypeMatch.Groups[1].Value : "";

                // Extraer celdas (td)
                var cellMatches = Regex.Matches(rowContent, @"<td.*?>(.*?)<\/td>", RegexOptions.Singleline);
                var cells = new List<string>();

                foreach (Match cellMatch in cellMatches)
                {
                    var cellContent = Regex.Replace(cellMatch.Groups[1].Value, @"<.*?>", "").Trim();
                    cells.Add(cellContent);
                }

                if (!string.IsNullOrEmpty(trackId) && cells.Count > 1)
                {
                    var rowData = new Dictionary<string, object>
                    {
                        { "id", trackId }
                    };

                    // Agregar las columnas en orden
                    for (int i = 1; i < cells.Count && i <= headers.Length; i++)
                    {
                        rowData[headers[i - 1]] = cells[i];

                        // Después de agregar "Recepcion" (que es el primer header), agregamos "DocTipo"
                        if (i == 1) // i=1 corresponde a headers[0] = "Recepcion"
                        {
                            rowData["DocTipo"] = docTipo;
                        }
                    }

                    tabulatedData.Add(rowData);
                }
            }
            var validDocTipos = new HashSet<string> { "96"};

            tabulatedData = tabulatedData
                .Where(row => 
                {
                    // Primero verificamos que exista la clave "DocTipo"
                    if (!row.ContainsKey("DocTipo"))
                        return false;

                    var docTipoValue = row["DocTipo"]?.ToString();
                    
                    // Si docTipoValue es null, no cumple la condición
                    if (docTipoValue == null)
                        return false;

                    // Ahora sí podemos llamar Contains de forma segura
                    return (!validDocTipos.Contains(docTipoValue));
                })
                .ToList();

            return tabulatedData;


        }

        private static string RemoveInvalidFileNameChars(string input)
        {
            foreach (char c in Path.GetInvalidFileNameChars())
            {
                input = input.Replace(c.ToString(), "_");
            }
            return input;
        }
    }
}

