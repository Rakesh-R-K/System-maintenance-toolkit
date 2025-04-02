@echo off
title System Maintenance Toolkit
color 0A
echo ===================================
echo     SYSTEM MAINTENANCE TOOLKIT    
echo ===================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python to proceed.
    pause
    exit /b
)

:: Run the Python script in a loop
python sys_monitor.py

echo.
echo Maintenance completed!
pause
