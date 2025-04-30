@echo off
setlocal

:: === SETUP ===
set PYTHON_VERSION=3.12.2
set PYTHON_INSTALLER=python-%PYTHON_VERSION%-amd64.exe
set PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/%PYTHON_INSTALLER%

echo [1/4] Downloading Python %PYTHON_VERSION%...
curl -o %PYTHON_INSTALLER% %PYTHON_URL%

echo [2/4] Installing Python silently...
%PYTHON_INSTALLER% /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

:: Refresh environment variables (for new PATH)
echo [3/4] Waiting for installation to complete...
timeout /t 10 >nul

:: Coba panggil python dan pip
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python tidak ditemukan setelah instalasi. Silakan restart PC dan jalankan ulang file ini.
    pause
    exit /b
)

echo [4/4] Installing pip packages: pandas, pywhatkit, openpyxl...
pip install pandas pywhatkit openpyxl

echo Selesai! Python dan semua paket berhasil di-install.
pause
endlocal