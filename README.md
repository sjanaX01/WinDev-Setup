# Development Tools Installers

Two Python scripts that automatically install essential development tools:
1. **Windows 11 Development Tools Installer** - Uses `winget` for system-level applications
2. **NPM Development Tools Installer** - Uses `npm` for global CLI tools and utilities

## Winget Installer Features

- ✅ Automatically installs 15+ essential development tools
- 🔄 Checks for updates to existing packages and prompts user per-package
- 🔍 Searches and verifies packages before installation
- 📊 Provides detailed installation progress and summary
- ⚡ Uses verified publishers when available
- 🛡️ Handles errors gracefully with timeouts
- 📝 Comprehensive logging of success/failure

## NPM Installer Features

- 🌐 Installs 45+ essential CLI tools and development utilities globally
- 🔄 Per-package update checking with user prompts
- 📋 Organized by categories (AI Tools, Frameworks, Testing, etc.)
- ⚡ Fast npm package management
- 🎯 Smart handling of already installed packages
- 📊 Comprehensive installation summary

## Winget Installer - Included Tools

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

## NPM Installer - Included Packages

### AI & Code Generation Tools
- Google Gemini CLI
- OpenAI CLI

### Core Development Languages & Frameworks
- TypeScript
- Create React App
- Next.js CLI
- Vue CLI
- Angular CLI

### Development Servers & Tools
- Nodemon
- Live Server
- HTTP Server
- JSON Server
- Concurrently

### Code Quality & Linting
- ESLint
- Prettier
- JSHint
- JavaScript Standard Style

### Build Tools & Bundlers
- Webpack CLI
- Vite
- Parcel
- Rollup

### Package Management & Publishing
- Yarn
- PNPM
- NPX
- NP (Better npm publish)
- Semantic Release

### Testing Tools
- Jest CLI
- Mocha
- Cypress
- Playwright

### Database & API Tools
- MongoDB Tools
- Prisma CLI
- GraphQL CLI
- Apollo CLI

### Deployment & DevOps
- Vercel CLI
- Netlify CLI
- Firebase CLI
- Heroku CLI

### Documentation & Generators
- JSDoc
- Storybook CLI
- Docusaurus

### Performance & Monitoring
- Lighthouse CLI
- Bundlephobia CLI
- Speed Test CLI

### Utility CLI Tools
- Lodash CLI
- Axios
- Chalk
- Commander

## Prerequisites

### For Winget Installer
- Windows 11
- `winget` (App Installer) - Usually pre-installed on Windows 11
- Python 3.7+

### For NPM Installer
- Node.js 16+ (includes npm)
- Python 3.7+

## Usage

### Winget Installer (System Applications)
```bash
# Basic installation with per-package update checking
python winget_dev_installer.py

# Skip package search verification (faster)
python winget_dev_installer.py --skip-search

# Show help
python winget_dev_installer.py --help
```

### NPM Installer (Global CLI Tools)
```bash
# Install all npm packages with update checking
python npm_dev_installer.py

# Show all packages by category before installing
python npm_dev_installer.py --show-categories

# Show help
python npm_dev_installer.py --help
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