using diantokensearchback.Services;
using Microsoft.AspNetCore.Mvc;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// Registrar servicios
builder.Services.AddSingleton<ScrapingService>();
builder.Services.AddSingleton<FileDownloadService>(); // Nuevo servicio para manejar descargas

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

// Endpoint para realizar scraping con fechas
app.MapGet("/scraping/test", async (ScrapingService scrapingService,
    [FromQuery] string authUrl,
    [FromQuery] string startDate,
    [FromQuery] string endDate) =>
{
    // Validar que el parámetro authUrl no esté vacío
    if (string.IsNullOrEmpty(authUrl))
    {
        return Results.BadRequest("El parámetro 'authUrl' es requerido.");
    }

    // Validar que las fechas no estén vacías
    if (string.IsNullOrEmpty(startDate) || string.IsNullOrEmpty(endDate))
    {
        return Results.BadRequest("Los parámetros 'startDate' y 'endDate' son requeridos.");
    }

    // Validar el formato de las fechas (opcional)
    if (!DateTime.TryParse(startDate, out var parsedStartDate) || !DateTime.TryParse(endDate, out var parsedEndDate))
    {
        return Results.BadRequest("Los parámetros 'startDate' y 'endDate' deben tener un formato válido (YYYY-MM-DD).");
    }

    // Validar que startDate no sea mayor a endDate
    if (parsedStartDate > parsedEndDate)
    {
        return Results.BadRequest("'startDate' no puede ser mayor a 'endDate'.");
    }

    try
    {
        // Llamar al servicio de scraping con los parámetros
        var extractedData = await scrapingService.AuthenticateAndNavigateAsync(authUrl, parsedStartDate.ToString("yyyy-MM-dd"), parsedEndDate.ToString("yyyy-MM-dd"));

        if (extractedData != null && extractedData.Count > 0)
        {
            return Results.Ok(new
            {
                message = "Scraping completado exitosamente",
                data = extractedData
            });
        }
        else
        {
            return Results.Ok(new { message = "No se encontraron datos en el rango de fechas proporcionado." });
        }
    }
    catch (Exception ex)
    {
        return Results.Problem($"Ocurrió un error al realizar el scraping: {ex.Message}");
    }
})
.WithName("TestScrapingWithDates")
.WithOpenApi();

app.MapPost("/tabledownload/full", async (TableDownloadService tableDownloadService,
    [FromQuery] string authUrl,
    [FromQuery] string startDate,
    [FromQuery] string endDate,
    [FromQuery] string? downloadPath,
    [FromQuery] bool recibidos,
    [FromQuery] bool enviados) =>
{
    Console.WriteLine($"FromQuwery {authUrl}");

    if (string.IsNullOrEmpty(authUrl))
    {
        return Results.BadRequest("El parámetro 'authUrl' es requerido.");
    }
    if (string.IsNullOrEmpty(startDate) || string.IsNullOrEmpty(endDate))
    {
        return Results.BadRequest("Los parámetros 'startDate' y 'endDate' son requeridos.");
    }
    // Validar que seleccione al menos una opción
    if (!recibidos && !enviados)
    {
        return Results.BadRequest("Debe seleccionar al menos una opción: 'recibidos' o 'enviados'.");
    }

    string defaultDownloadPath = Path.Combine(Directory.GetCurrentDirectory(), "Downloads");
    downloadPath ??= defaultDownloadPath;

    var (tabulatedData, downloadedFiles, totalSeconds, avgPerDoc) = await tableDownloadService.AuthenticateTabulateAndDownloadAsync(
        authUrl, startDate, endDate, downloadPath, recibidos, enviados);
    
    return Results.Ok(new
    {
        message = "Proceso completado.",
        totalTimeSeconds = totalSeconds,
        averageTimePerDocumentSeconds = avgPerDoc,
        tabulatedData,
        downloadedFiles
    });
})
.WithName("FullTableDownload")
.WithOpenApi();





// Endpoint para descargar archivos basados en el scraping
app.MapPost("/file/download-test", async (FileDownloadService fileDownloadService,
    [FromQuery] string authUrl,
    [FromQuery] string trackId,
    [FromQuery] string? downloadPath) =>
{
    if (string.IsNullOrEmpty(authUrl))
    {
        return Results.BadRequest("El parámetro 'authUrl' es requerido.");
    }
    if (string.IsNullOrEmpty(trackId))
    {
        return Results.BadRequest("El parámetro 'trackId' es requerido.");
    }

    // Ruta por defecto si no se proporciona downloadPath
    string defaultDownloadPath = Path.Combine(Directory.GetCurrentDirectory(), "Downloads");
    downloadPath ??= defaultDownloadPath;

    bool result = await fileDownloadService.AuthenticateAndDownloadFileAsync(authUrl, trackId, downloadPath);


    if (result)
    {
        return Results.Ok(new
        {
            message = "Archivo descargado y guardado exitosamente",
            filePath = Path.Combine(downloadPath, "prueba.zip")
        });
    }
    else
    {
        return Results.BadRequest("Error al descargar o guardar el archivo.");
    }
})
.WithName("DownloadTestFile")
.WithOpenApi();




app.Run();

// Record para el endpoint de WeatherForecast (puedes eliminar esto si ya no lo usas)
record WeatherForecast(DateOnly Date, int TemperatureC, string? Summary)
{
    public int TemperatureF => 32 + (int)(TemperatureC / 0.5556);
}
