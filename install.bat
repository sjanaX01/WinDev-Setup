@echo off
echo ===================================
echo  Full Development Environment Setup
echo ===================================

echo.
echo --- Installing MSYS2 (C/C++ Compiler) ---
echo Downloading MSYS2 installer...
curl -L -o msys2-installer.exe "https://github.com/msys2/msys2-installer/releases/download/2025-08-30/msys2-x86_64-20250830.exe"
echo Installing MSYS2...
start /wait "" msys2-installer.exe /S /D=C:\msys64
echo Deleting installer...
del msys2-installer.exe
echo MSYS2 installation complete.

echo.
echo --- Installing Oracle JDK (Java Compiler) ---
echo Downloading Oracle JDK 25...
curl -L -o jdk-25_windows-x64_bin.msi "https://download.oracle.com/java/25/latest/jdk-25_windows-x64_bin.msi"
echo Installing Oracle JDK 25...
start /wait msiexec.exe /i jdk-25_windows-x64_bin.msi 
echo Setting JAVA_HOME and updating PATH...
setx JAVA_HOME "C:\Program Files\Java\jdk-25" /m
setx PATH "%PATH%;%JAVA_HOME%\bin" /m
echo Deleting installer...
del jdk-25_windows-x64_bin.msi
echo Oracle JDK 25 installation complete.

echo.
echo --- Installing Python 3.12 ---
winget install --id Python.Python.3.12 --exact --accept-source-agreements --accept-package-agreements --silent
echo.

echo --- Running Python Setup Script for other dev tools ---
python setup_dev_env.py

echo.
echo ===================================
echo  Setup Complete
echo ===================================