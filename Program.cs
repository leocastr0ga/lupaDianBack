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

app.Run();

// Record para el endpoint de WeatherForecast (puedes eliminar esto si ya no lo usas)
record WeatherForecast(DateOnly Date, int TemperatureC, string? Summary)
{
    public int TemperatureF => 32 + (int)(TemperatureC / 0.5556);
}
