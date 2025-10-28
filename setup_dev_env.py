#!/usr/bin/env python3
"""
Unified Development Environment Setup Script

This script installs a curated list of development tools using winget and npm.
It checks for existing installations, and prompts for updates.
"""

import subprocess
import sys
import time
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass

try:
    from rich.console import Console
    from rich.prompt import Confirm
except ImportError:
    print("rich library not found. Installing...")
    subprocess.run([sys.executable, "-m", "pip", "install", "rich"], check=True)
    from rich.console import Console
    from rich.prompt import Confirm

console = Console()

@dataclass
class WingetPackage:
    name: str
    winget_id: str

@dataclass
class NpmPackage:
    name: str
    package_name: str

class DevEnvInstaller:
    def __init__(self):
        self.winget_packages = [
            WingetPackage("Visual Studio Code", "Microsoft.VisualStudioCode"),
            WingetPackage("Oh My Posh", "JanDeDobbeleer.OhMyPosh"),
            WingetPackage("JetBrainsMono Nerd Font", "Microsoft.NerdFonts.FiraCode"),
            WingetPackage("Fastfetch", "Fastfetch-cli.Fastfetch"),
            WingetPackage("Git", "Microsoft.Git"),
            WingetPackage("Node.js", "OpenJS.NodeJS"),
            WingetPackage("Docker Desktop", "Docker.DockerDesktop"),
            WingetPackage("Google Chrome", "Google.Chrome"),
            WingetPackage("Brave Browser", "Brave.Brave"),
            WingetPackage("VirtualBox", "Oracle.VirtualBox"),
            WingetPackage("Claude Desktop", "Anthropic.Claude"),
            WingetPackage("PowerToys", "Microsoft.PowerToys"),
            WingetPackage("Windows Terminal", "Microsoft.WindowsTerminal"),
            WingetPackage("7-Zip", "7zip.7zip"),
            WingetPackage("Postman", "Postman.Postman"),
            WingetPackage("Discord", "Discord.Discord"),
            WingetPackage("Slack", "SlackTechnologies.Slack"),
            WingetPackage("Notion", "Notion.Notion"),
            WingetPackage("OBS Studio", "OBSProject.OBSStudio"),
            WingetPackage("VLC media player", "VideoLAN.VLC"),
            WingetPackage("WhatsApp", "9NKSQGP7F2NH"),
            WingetPackage("Telegram Desktop", "Telegram.TelegramDesktop"),
        ]
        self.npm_packages = [
            NpmPackage("Gemini CLI", "@google-ai/generativelanguage"),
            NpmPackage("OpenAI CLI", "openai"),
            NpmPackage("TypeScript", "typescript"),
            NpmPackage("React CLI", "create-react-app"),
            NpmPackage("Next.js CLI", "create-next-app"),
            NpmPackage("Vue CLI", "@vue/cli"),
            NpmPackage("Angular CLI", "@angular/cli"),
            NpmPackage("Nodemon", "nodemon"),
            NpmPackage("Live Server", "live-server"),
            NpmPackage("HTTP Server", "http-server"),
            NpmPackage("JSON Server", "json-server"),
            NpmPackage("Concurrently", "concurrently"),
            NpmPackage("ESLint", "eslint"),
            NpmPackage("Prettier", "prettier"),
            NpmPackage("JSHint", "jshint"),
            NpmPackage("Standard", "standard"),
            NpmPackage("Webpack CLI", "webpack-cli"),
            NpmPackage("Vite", "vite"),
            NpmPackage("Parcel", "parcel"),
            NpmPackage("Rollup", "rollup"),
            NpmPackage("Yarn", "yarn"),
            NpmPackage("PNPM", "pnpm"),
            NpmPackage("NPX", "npx"),
            NpmPackage("NP", "np"),
            NpmPackage("Semantic Release", "semantic-release"),
            NpmPackage("Jest CLI", "jest"),
            NpmPackage("Mocha", "mocha"),
            NpmPackage("Cypress", "cypress"),
            NpmPackage("Playwright", "playwright"),
            NpmPackage("Lodash CLI", "lodash-cli"),
            NpmPackage("Moment CLI", "moment"),
            NpmPackage("Axios", "axios"),
            NpmPackage("Chalk", "chalk"),
            NpmPackage("Commander", "commander"),
            NpmPackage("MongoDB Tools", "mongodb"),
            NpmPackage("Prisma CLI", "prisma"),
            NpmPackage("GraphQL CLI", "graphql-cli"),
            NpmPackage("Apollo CLI", "@apollo/client"),
            NpmPackage("Vercel CLI", "vercel"),
            NpmPackage("Netlify CLI", "netlify-cli"),
            NpmPackage("Firebase CLI", "firebase-tools"),
            NpmPackage("Heroku CLI", "heroku"),
            NpmPackage("JSDoc", "jsdoc"),
            NpmPackage("Storybook CLI", "@storybook/cli"),
            NpmPackage("Docusaurus", "@docusaurus/core"),
            NpmPackage("Lighthouse CLI", "lighthouse"),
            NpmPackage("Bundlephobia CLI", "bundlephobia"),
            NpmPackage("Speed Test CLI", "speed-test"),
        ]

    def run(self):
        console.print("[bold cyan]Development Environment Setup[/bold cyan]")
        self.install_winget_packages()
        self.install_npm_packages()
        console.print("[bold green]All installations complete![/bold green]")

    def install_winget_packages(self):
        console.print("\n[bold blue]Installing Winget Packages...[/bold blue]")
        if not self._check_command_available("winget", "--version"):
            console.print("[bold red]Winget is not available. Please install it from the Microsoft Store.[/bold red]")
            return

        with console.status("[bold green]Processing winget packages...[/bold green]") as status:
            for package in self.winget_packages:
                status.update(f"[bold green]Processing {package.name}...[/bold green]")
                self._install_winget_package(package)

    def _install_winget_package(self, package: WingetPackage):
        try:
            list_result = subprocess.run(["winget", "list", "--id", package.winget_id, "--exact"], capture_output=True, text=True)
            if list_result.returncode == 0 and package.winget_id in list_result.stdout:
                console.print(f"[green]{package.name} is already installed.[/green]")
                upgrade_result = subprocess.run(["winget", "upgrade", "--id", package.winget_id, "--exact"], capture_output=True, text=True)
                if upgrade_result.returncode == 0 and package.winget_id in upgrade_result.stdout:
                    if Confirm.ask(f"[yellow]An update is available for {package.name}. Do you want to update?[/yellow]"):
                        self._run_command(["winget", "upgrade", "--id", package.winget_id, "--exact", "--accept-source-agreements", "--accept-package-agreements", "--silent"], f"Upgrading {package.name}")
                return

            self._run_command(["winget", "install", "--id", package.winget_id, "--exact", "--accept-source-agreements", "--accept-package-agreements", "--silent"], f"Installing {package.name}")
        except Exception as e:
            console.print(f"[bold red]Error processing {package.name}: {e}[/bold red]")

    def install_npm_packages(self):
        console.print("\n[bold blue]Installing NPM Packages...[/bold blue]")
        if not self._check_command_available("npm", "--version"):
            console.print("[bold red]NPM is not available. Please install Node.js first.[/bold red]")
            return

        with console.status("[bold green]Processing npm packages...[/bold green]") as status:
            for package in self.npm_packages:
                status.update(f"[bold green]Processing {package.name}...[/bold green]")
                self._install_npm_package(package)

    def _install_npm_package(self, package: NpmPackage):
        try:
            list_result = subprocess.run(["npm", "list", "-g", package.package_name], capture_output=True, text=True)
            if list_result.returncode == 0 and package.package_name in list_result.stdout:
                console.print(f"[green]{package.name} is already installed.[/green]")
                outdated_result = subprocess.run(["npm", "outdated", "-g", package.package_name], capture_output=True, text=True)
                if outdated_result.returncode == 0 and package.package_name in outdated_result.stdout:
                    if Confirm.ask(f"[yellow]An update is available for {package.name}. Do you want to update?[/yellow]"):
                        self._run_command(["npm", "update", "-g", package.package_name], f"Upgrading {package.name}")
                return

            self._run_command(["npm", "install", "-g", package.package_name], f"Installing {package.name}")
        except Exception as e:
            console.print(f"[bold red]Error processing {package.name}: {e}[/bold red]")

    def _check_command_available(self, command: str, version_arg: str) -> bool:
        try:
            subprocess.run([command, version_arg], capture_output=True, text=True, check=True)
            return True
        except (FileNotFoundError, subprocess.CalledProcessError):
            return False

    def _run_command(self, command: List[str], description: str):
        # No need to print description here as the status takes care of it
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            console.print(f"[green]  -> {description} - Success![/green]")
        except subprocess.CalledProcessError as e:
            console.print(f"[bold red]  -> {description} - Failed![/bold red]")
            console.print(e.stderr)

if __name__ == "__main__":
    installer = DevEnvInstaller()
    installer.run()