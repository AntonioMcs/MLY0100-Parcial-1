# Script de configuración del entorno para MLY0100
# Ejecutar en PowerShell: .\setup_env.ps1

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Configuración del Entorno Virtual" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar si .venv existe
if (Test-Path .venv) {
    Write-Host "⚠ El entorno virtual .venv ya existe" -ForegroundColor Yellow
    $respuesta = Read-Host "¿Deseas recrearlo? (s/n)"
    if ($respuesta -eq "s" -or $respuesta -eq "S") {
        Write-Host "Eliminando entorno virtual anterior..." -ForegroundColor Yellow
        Remove-Item -Recurse -Force .venv
    } else {
        Write-Host "Usando entorno virtual existente" -ForegroundColor Green
    }
}

# Crear entorno virtual si no existe
if (-not (Test-Path .venv)) {
    Write-Host "📦 Creando entorno virtual..." -ForegroundColor Cyan
    python -m venv .venv
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ Error al crear el entorno virtual" -ForegroundColor Red
        exit 1
    }
    Write-Host "✓ Entorno virtual creado" -ForegroundColor Green
}

# Activar entorno virtual
Write-Host ""
Write-Host "🔧 Activando entorno virtual..." -ForegroundColor Cyan
& .\.venv\Scripts\Activate.ps1

if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠ Error de política de ejecución. Configurando..." -ForegroundColor Yellow
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
    & .\.venv\Scripts\Activate.ps1
}

Write-Host "✓ Entorno virtual activado" -ForegroundColor Green
Write-Host ""

# Actualizar pip
Write-Host "📥 Actualizando pip..." -ForegroundColor Cyan
python -m pip install --upgrade pip --quiet
Write-Host "✓ pip actualizado" -ForegroundColor Green
Write-Host ""

# Instalar dependencias
Write-Host "📚 Instalando dependencias desde requirements.txt..." -ForegroundColor Cyan
pip install -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Error al instalar dependencias" -ForegroundColor Red
    exit 1
}
Write-Host "✓ Dependencias instaladas" -ForegroundColor Green
Write-Host ""

# Verificar instalación
Write-Host "🔍 Verificando instalación..." -ForegroundColor Cyan
python -c "import pandas, numpy, matplotlib, seaborn, sklearn; print('✓ Todas las librerías instaladas correctamente')"
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Error en la verificación" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Instalar ipykernel para Jupyter
Write-Host "📓 Instalando ipykernel para Jupyter..." -ForegroundColor Cyan
pip install ipykernel --quiet
python -m ipykernel install --user --name=venv-mly0100 --display-name "Python (venv MLY0100)" --quiet
Write-Host "✓ Kernel de Jupyter configurado" -ForegroundColor Green
Write-Host ""

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "✅ Configuración completada!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Próximos pasos:" -ForegroundColor Yellow
Write-Host "1. Abre el notebook en VS Code/Cursor" -ForegroundColor White
Write-Host "2. Selecciona el kernel: 'Python (venv MLY0100)' o el intérprete de .venv" -ForegroundColor White
Write-Host "3. Ejecuta las celdas del notebook" -ForegroundColor White
Write-Host ""
Write-Host "Para verificar el kernel, ejecuta en el notebook:" -ForegroundColor Yellow
Write-Host "  import sys" -ForegroundColor White
Write-Host "  print(sys.executable)" -ForegroundColor White
Write-Host ""
