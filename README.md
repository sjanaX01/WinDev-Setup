# Windows 11 Development Tools Installer

A Python script that automatically installs essential development tools on Windows 11 using the `winget` package manager.

## Features

- ✅ Automatically installs 15+ essential development tools
- 🔍 Searches and verifies packages before installation
- 📊 Provides detailed installation progress and summary
- ⚡ Uses verified publishers when available
- 🛡️ Handles errors gracefully with timeouts
- 📝 Comprehensive logging of success/failure

## Included Tools

### Code Editors & Development
- Visual Studio Code
- Git
- Windows Terminal

### Programming Languages & Runtimes
- Python 3.12
- Node.js

### Containerization & Virtualization
- Docker Desktop
- VirtualBox

### Browsers
- Google Chrome
- Brave Browser

### AI & Productivity Tools
- Claude Desktop
- Notion
- PowerToys

### Communication & Collaboration
- Discord
- Slack
- Postman

### Utilities
- 7-Zip
- OBS Studio

## Prerequisites

- Windows 11
- `winget` (App Installer) - Usually pre-installed on Windows 11
- Python 3.7+ (if not installed, the script will install Python 3.12)

## Usage

### Basic Installation
```bash
python winget_dev_installer.py
```

### Skip Package Search (Faster)
```bash
python winget_dev_installer.py --skip-search
```

## How It Works

1. **Verification**: Checks if winget is available on your system
2. **Source Update**: Updates winget sources for latest package information
3. **Search**: Verifies each package exists in winget repositories
4. **Installation**: Installs packages one by one with proper error handling
5. **Summary**: Provides a detailed report of successful and failed installations

## Error Handling

- **Timeout Protection**: 5-minute timeout per package installation
- **Graceful Failures**: Continues installing other packages if one fails
- **Detailed Logging**: Shows exactly what succeeded and what failed
- **Source Verification**: Ensures packages come from verified publishers

## Customization

To add or remove packages, edit the `packages` list in the `WingetInstaller.__init__()` method:

```python
Package("Tool Name", "winget.package.id", "Description", True)
```

## Troubleshooting

### Winget Not Found
If you get a "winget not available" error:
1. Install "App Installer" from Microsoft Store
2. Restart your terminal
3. Run the script again

### Package Installation Fails
- Some packages may require administrator privileges
- Run Command Prompt or PowerShell as Administrator
- Check if the package ID is correct using `winget search <package-name>`

### Slow Installation
- Use `--skip-search` flag to speed up the process
- Some packages (like Docker, VirtualBox) are large and take time to download

## License

This project is open source and available under the MIT License.