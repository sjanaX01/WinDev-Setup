@echo off
title Advanced Cache Cleaner
color 0A
echo.
echo :::::::::::::::::::::::::::::::::::::
echo ::                                 ::
echo ::      ADVANCED CACHE CLEANER     ::
echo ::                                 ::
echo :::::::::::::::::::::::::::::::::::::
echo.

:: Check for administrator privileges
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if '%errorlevel%' NEQ '0' (
    echo [ERROR] Please run this script as an administrator.
    pause
    goto :eof
)

echo [INFO] Running with administrator privileges.
echo.

set "localAppDataFolderList=pip D3DSCache cache Temp uv npm-cache Boxstarter CEF Pub checkpoint-nodejs com.milisp.mcplinker CrashDumps SquirrelTemp CrashReportClient pypa pypoetry Rufus"
set "userProfileFolderList=.cache .thumbnails ansel"
set "systemFolderList=Prefetch Temp"
set "browserCacheList=Google\Chrome\User Data\Default\Cache Google\Chrome\User Data\Default\Code Cache Google\Chrome\User Data\Default\GPUCache Microsoft\Edge\User Data\Default\Cache Microsoft\Edge\User Data\Default\Code Cache Microsoft\Edge\User Data\Default\GPUCache"

echo [AppData Local Cleanup]
for %%i in (%localAppDataFolderList%) do (
    if exist "%LOCALAPPDATA%\%%i" (
        color 0C
        echo [DELETING] "%LOCALAPPDATA%\%%i"
        rmdir /s /q "%LOCALAPPDATA%\%%i"
        color 0A
    ) else (
        color 0E
        echo [NOT FOUND] "%LOCALAPPDATA%\%%i"
        color 0A
    )
)
echo.

echo [Browser Cache Cleanup]
for %%i in (%browserCacheList%) do (
    if exist "%LOCALAPPDATA%\%%i" (
        color 0C
        echo [DELETING] "%LOCALAPPDATA%\%%i"
        rmdir /s /q "%LOCALAPPDATA%\%%i"
        color 0A
    ) else (
        color 0E
        echo [NOT FOUND] "%LOCALAPPDATA%\%%i"
        color 0A
    )
)
echo.

echo [System Folders Cleanup]
for %%i in (%systemFolderList%) do (
    if exist "%SystemRoot%\%%i" (
        color 0C
        echo [DELETING] "%SystemRoot%\%%i"
        rmdir /s /q "%SystemRoot%\%%i" 2>nul
        color 0A
    ) else (
        color 0E
        echo [NOT FOUND] "%SystemRoot%\%%i"
        color 0A
    )
)
echo.

echo [User Directory Cleanup]
for %%i in (%userProfileFolderList%) do (
    if exist "%USERPROFILE%\%%i" (
        color 0C
        echo [DELETING] "%USERPROFILE%\%%i"
        rmdir /s /q "%USERPROFILE%\%%i"
        color 0A
    ) else (
        color 0E
        echo [NOT FOUND] "%USERPROFILE%\%%i"
        color 0A
    )
)

echo.
color 0B
echo ============================================
echo          CLEANUP COMPLETE!
echo ============================================
color 07
pause