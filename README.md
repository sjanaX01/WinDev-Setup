# Automated Development Environment Setup

This script automates the process of setting up a complete development environment on a fresh Windows machine. It installs a curated list of essential development tools, runtimes, and applications, saving you the time and effort of manually installing everything.

## Features

*   **One-click setup:** Run a single script to install everything.
*   **Comprehensive toolset:** Installs a wide range of development tools, from code editors and compilers to browsers and communication apps.
*   **Silent installation:** Most applications are installed silently in the background, without requiring any user interaction.
*   **Interactive updates:** The script checks for existing installations and prompts you to update if a new version is available.
*   **Modern and minimal UI:** The script provides a clean and modern interface in your terminal, with clear status messages and loading animations.

## Prerequisites

*   Windows 10 or 11.
*   An internet connection.

## How to Use

1.  Ensure you have the following files in the same directory:
    *   `install.bat`
    *   `setup_dev_env.py`
2.  Open a command prompt or PowerShell **as an administrator**.
3.  Navigate to the directory where you saved the files.
4.  Run the following command:
    ```
    install.bat
    ```
5.  Sit back and relax while the script sets up your development environment.

## What it Installs

The script installs the following software:

### Core Compilers and Runtimes

*   MSYS2 (for C/C++ compiler)
*   Oracle JDK 25 (for Java)
*   Python 3.12
*   Node.js

### Development Tools

*   Visual Studio Code
*   Git
*   Docker Desktop
*   Postman
*   Windows Terminal
*   PowerToys
*   7-Zip

### Browsers

*   Google Chrome
*   Brave Browser

### Communication and Productivity

*   Discord
*   Slack
*   Notion
*   WhatsApp
*   Telegram Desktop

### Other Tools

*   VirtualBox
*   Claude Desktop
*   OBS Studio
*   VLC media player

### NPM Packages (globally installed)

A wide range of npm packages for web development, including:

*   **AI & Code Generation:** Gemini CLI, OpenAI CLI
*   **Frameworks:** React, Next.js, Vue, Angular
*   **Development Servers:** Nodemon, Live Server, HTTP Server
*   **Code Quality:** ESLint, Prettier, JSHint
*   **Build Tools:** Webpack, Vite, Parcel, Rollup
*   **Package Management:** Yarn, PNPM
*   **Testing:** Jest, Mocha, Cypress, Playwright
*   **And many more...**

## Notes

*   This script needs to be run with **administrator privileges** to be able to install software and modify system environment variables.
*   The script will install MSYS2 to `C:\msys64` and Oracle JDK to `C:\Program Files\Java\jdk-25`.
*   Some installations might take a while to complete. Please be patient.
