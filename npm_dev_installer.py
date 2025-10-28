#!/usr/bin/env python3
"""
NPM Development Tools Global Installer
Installs essential CLI tools and development utilities globally using npm
"""

import subprocess
import sys
import json
import time
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass

@dataclass
class NpmPackage:
    name: str
    package_name: str
    description: str
    category: str

class NpmInstaller:
    def __init__(self):
        self.npm_cmd = self._get_npm_command()
        self.packages = [
            # AI & Code Generation Tools
            NpmPackage("Gemini CLI", "@google-ai/generativelanguage", "Google Gemini AI CLI tool", "AI Tools"),
            NpmPackage("OpenAI CLI", "openai", "OpenAI API CLI tool", "AI Tools"),
            
            # Core Development Languages & Frameworks
            NpmPackage("TypeScript", "typescript", "TypeScript compiler and language server", "Languages"),
            NpmPackage("React CLI", "create-react-app", "Create React applications", "Frameworks"),
            NpmPackage("Next.js CLI", "create-next-app", "Create Next.js applications", "Frameworks"),
            NpmPackage("Vue CLI", "@vue/cli", "Vue.js development tools", "Frameworks"),
            NpmPackage("Angular CLI", "@angular/cli", "Angular development CLI", "Frameworks"),
            
            # Development Servers & Tools
            NpmPackage("Nodemon", "nodemon", "Auto-restart Node.js applications", "Development"),
            NpmPackage("Live Server", "live-server", "Development server with live reload", "Development"),
            NpmPackage("HTTP Server", "http-server", "Simple HTTP server", "Development"),
            NpmPackage("JSON Server", "json-server", "Mock REST API server", "Development"),
            NpmPackage("Concurrently", "concurrently", "Run multiple commands concurrently", "Development"),
            
            # Code Quality & Linting
            NpmPackage("ESLint", "eslint", "JavaScript/TypeScript linter", "Code Quality"),
            NpmPackage("Prettier", "prettier", "Code formatter", "Code Quality"),
            NpmPackage("JSHint", "jshint", "JavaScript code quality tool", "Code Quality"),
            NpmPackage("Standard", "standard", "JavaScript Standard Style", "Code Quality"),
            
            # Build Tools & Bundlers
            NpmPackage("Webpack CLI", "webpack-cli", "Webpack bundler CLI", "Build Tools"),
            NpmPackage("Vite", "vite", "Fast build tool", "Build Tools"),
            NpmPackage("Parcel", "parcel", "Zero-config build tool", "Build Tools"),
            NpmPackage("Rollup", "rollup", "Module bundler", "Build Tools"),
            
            # Package Management & Publishing
            NpmPackage("Yarn", "yarn", "Fast package manager", "Package Management"),
            NpmPackage("PNPM", "pnpm", "Efficient package manager", "Package Management"),
            NpmPackage("NPX", "npx", "Package runner tool", "Package Management"),
            NpmPackage("NP", "np", "Better npm publish", "Package Management"),
            NpmPackage("Semantic Release", "semantic-release", "Automated package publishing", "Package Management"),
            
            # Testing Tools
            NpmPackage("Jest CLI", "jest", "JavaScript testing framework", "Testing"),
            NpmPackage("Mocha", "mocha", "JavaScript test framework", "Testing"),
            NpmPackage("Cypress", "cypress", "End-to-end testing", "Testing"),
            NpmPackage("Playwright", "playwright", "Browser automation testing", "Testing"),
            
            # Utility CLI Tools
            NpmPackage("Lodash CLI", "lodash-cli", "Lodash utility library CLI", "Utilities"),
            NpmPackage("Moment CLI", "moment", "Date manipulation library", "Utilities"),
            NpmPackage("Axios", "axios", "HTTP client library", "Utilities"),
            NpmPackage("Chalk", "chalk", "Terminal string styling", "Utilities"),
            NpmPackage("Commander", "commander", "Command-line interface builder", "Utilities"),
            
            # Database & API Tools
            NpmPackage("MongoDB Tools", "mongodb", "MongoDB driver and tools", "Database"),
            NpmPackage("Prisma CLI", "prisma", "Database toolkit", "Database"),
            NpmPackage("GraphQL CLI", "graphql-cli", "GraphQL command line tool", "API Tools"),
            NpmPackage("Apollo CLI", "@apollo/client", "GraphQL client", "API Tools"),
            
            # Deployment & DevOps
            NpmPackage("Vercel CLI", "vercel", "Vercel deployment CLI", "Deployment"),
            NpmPackage("Netlify CLI", "netlify-cli", "Netlify deployment CLI", "Deployment"),
            NpmPackage("Firebase CLI", "firebase-tools", "Firebase development tools", "Deployment"),
            NpmPackage("Heroku CLI", "heroku", "Heroku deployment CLI", "Deployment"),
            
            # Documentation & Generators
            NpmPackage("JSDoc", "jsdoc", "JavaScript documentation generator", "Documentation"),
            NpmPackage("Storybook CLI", "@storybook/cli", "Component development environment", "Documentation"),
            NpmPackage("Docusaurus", "@docusaurus/core", "Documentation website generator", "Documentation"),
            
            # Performance & Monitoring
            NpmPackage("Lighthouse CLI", "lighthouse", "Web performance auditing", "Performance"),
            NpmPackage("Bundlephobia CLI", "bundlephobia", "Bundle size analyzer", "Performance"),
            NpmPackage("Speed Test CLI", "speed-test", "Internet speed test", "Performance"),
        ]
    
    def _get_npm_command(self) -> str:
        """Get the correct npm command for the current platform"""
        try:
            # Try npm command first
            subprocess.run(
                ["npm", "--version"], 
                capture_output=True, 
                text=True, 
                check=True
            )
            return "npm"
        except FileNotFoundError:
            # Try npm.cmd on Windows
            try:
                subprocess.run(
                    ["npm.cmd", "--version"], 
                    capture_output=True, 
                    text=True, 
                    check=True
                )
                return "npm.cmd"
            except FileNotFoundError:
                return "npm"  # Default fallback
    
    def check_npm_available(self) -> bool:
        """Check if npm is available on the system"""
        try:
            result = subprocess.run(
                [self.npm_cmd, "--version"], 
                capture_output=True, 
                text=True, 
                check=True
            )
            print(f"✓ NPM version: {result.stdout.strip()}")
            return True
        except (FileNotFoundError, subprocess.CalledProcessError) as e:
            print("❌ NPM is not available. Please install Node.js first.")
            print("💡 Make sure Node.js is installed and npm is in your PATH.")
            print(f"Debug: Tried command '{self.npm_cmd}', error: {e}")
            return False
    
    def check_node_version(self) -> bool:
        """Check Node.js version"""
        try:
            result = subprocess.run(
                ["node", "--version"], 
                capture_output=True, 
                text=True, 
                check=True
            )
            node_version = result.stdout.strip()
            print(f"✓ Node.js version: {node_version}")
            
            # Extract version number and check if it's recent enough
            version_num = node_version.replace('v', '').split('.')[0]
            if int(version_num) >= 16:
                return True
            else:
                print(f"⚠️  Node.js version {node_version} is quite old. Consider upgrading to v18+ for best compatibility.")
                return True
                
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("❌ Node.js is not available. Please install Node.js first.")
            return False
        except ValueError:
            print("⚠️  Could not parse Node.js version, continuing anyway...")
            return True
    
    def check_package_installed_and_updatable(self, package: NpmPackage) -> Tuple[bool, Optional[str], Optional[str]]:
        """Check if npm package is installed globally and if update is available"""
        try:
            # Check if package is installed globally
            list_result = subprocess.run(
                [self.npm_cmd, "list", "-g", "--depth=0", package.package_name],
                capture_output=True,
                text=True
            )
            
            is_installed = list_result.returncode == 0 and package.package_name in list_result.stdout
            
            if not is_installed:
                return False, None, None
            
            # Get current version
            current_version = "Unknown"
            for line in list_result.stdout.split('\n'):
                if package.package_name in line and '@' in line:
                    try:
                        current_version = line.split('@')[-1].strip()
                    except:
                        current_version = "Unknown"
                    break
            
            # Check for available updates
            outdated_result = subprocess.run(
                [self.npm_cmd, "outdated", "-g", package.package_name],
                capture_output=True,
                text=True
            )
            
            if outdated_result.returncode == 0 and package.package_name in outdated_result.stdout:
                # Parse version information from outdated output
                lines = outdated_result.stdout.split('\n')
                available_version = "Unknown"
                
                for line in lines:
                    if package.package_name in line:
                        parts = line.split()
                        if len(parts) >= 4:
                            available_version = parts[3]  # Latest version
                        break
                
                return True, current_version, available_version
            else:
                return True, current_version, None  # Installed but no update available
                
        except subprocess.CalledProcessError:
            return False, None, None
    
    def prompt_user_for_package_update(self, package: NpmPackage, current_version: str, available_version: str) -> bool:
        """Ask user if they want to update a specific package"""
        print(f"\n🔄 {package.name} is already installed!")
        print(f"   Current version: {current_version}")
        print(f"   Available version: {available_version}")
        
        while True:
            try:
                choice = input(f"   Do you want to update {package.name}? (y/n): ").strip().lower()
                
                if choice in ['y', 'yes']:
                    return True
                elif choice in ['n', 'no']:
                    return False
                else:
                    print("   Please enter 'y' for yes or 'n' for no.")
                    
            except KeyboardInterrupt:
                print("\n⚠️  Operation cancelled by user.")
                return False
    
    def install_package(self, package: NpmPackage) -> bool:
        """Install a single npm package globally"""
        print(f"📦 Installing {package.name}...")
        
        try:
            cmd = [self.npm_cmd, "install", "-g", package.package_name]
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout per package
            )
            
            if result.returncode == 0:
                print(f"✅ Successfully installed {package.name}")
                return True
            else:
                print(f"❌ Failed to install {package.name}")
                if result.stderr:
                    print(f"Error: {result.stderr}")
                return False
                
        except subprocess.TimeoutExpired:
            print(f"⏰ Installation of {package.name} timed out")
            return False
        except Exception as e:
            print(f"❌ Error installing {package.name}: {e}")
            return False
    
    def upgrade_package(self, package: NpmPackage) -> bool:
        """Upgrade a single npm package"""
        print(f"⬆️  Upgrading {package.name}...")
        
        try:
            cmd = [self.npm_cmd, "update", "-g", package.package_name]
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout per package
            )
            
            if result.returncode == 0:
                print(f"✅ Successfully upgraded {package.name}")
                return True
            else:
                print(f"❌ Failed to upgrade {package.name}")
                if result.stderr:
                    print(f"Error: {result.stderr}")
                return False
                
        except subprocess.TimeoutExpired:
            print(f"⏰ Upgrade of {package.name} timed out")
            return False
        except Exception as e:
            print(f"❌ Error upgrading {package.name}: {e}")
            return False
    
    def update_npm_cache(self):
        """Update npm cache and registry info"""
        print("🔄 Updating npm cache...")
        try:
            subprocess.run(
                [self.npm_cmd, "cache", "clean", "--force"],
                capture_output=True,
                text=True,
                check=True
            )
            print("✅ NPM cache updated successfully")
        except subprocess.CalledProcessError:
            print("⚠️  Failed to update npm cache, continuing anyway...")
    
    def show_packages_by_category(self):
        """Display packages organized by category"""
        categories = {}
        for package in self.packages:
            if package.category not in categories:
                categories[package.category] = []
            categories[package.category].append(package)
        
        print("\n📋 Available packages by category:")
        print("=" * 60)
        
        for category, packages in categories.items():
            print(f"\n🔧 {category}:")
            for package in packages:
                print(f"   • {package.name} - {package.description}")
    
    def install_all(self, show_categories: bool = False):
        """Install all npm packages with per-package update checking"""
        if not self.check_node_version() or not self.check_npm_available():
            return
        
        if show_categories:
            self.show_packages_by_category()
            
            while True:
                try:
                    choice = input(f"\nDo you want to proceed with installation? (y/n): ").strip().lower()
                    if choice in ['y', 'yes']:
                        break
                    elif choice in ['n', 'no']:
                        print("Installation cancelled.")
                        return
                    else:
                        print("Please enter 'y' for yes or 'n' for no.")
                except KeyboardInterrupt:
                    print("\n⚠️  Installation cancelled by user.")
                    return
        
        self.update_npm_cache()
        
        print(f"\n🚀 Starting processing of {len(self.packages)} npm packages...")
        print("=" * 60)
        
        successful_installs = []
        successful_upgrades = []
        failed_installs = []
        skipped_packages = []
        
        for i, package in enumerate(self.packages, 1):
            print(f"\n[{i}/{len(self.packages)}] Processing {package.name}")
            
            # Check if package is already installed and has updates
            is_installed, current_version, available_version = self.check_package_installed_and_updatable(package)
            
            if is_installed and available_version:
                # Package is installed and has an update available
                if self.prompt_user_for_package_update(package, current_version, available_version):
                    # User wants to update
                    if self.upgrade_package(package):
                        successful_upgrades.append(package.name)
                    else:
                        failed_installs.append(package.name)
                else:
                    # User chose not to update
                    print(f"⏭️  Skipping update for {package.name}")
                    skipped_packages.append(package.name)
                    
            elif is_installed and not available_version:
                # Package is installed and up to date
                print(f"✅ {package.name} is already installed and up to date")
                skipped_packages.append(package.name)
                
            else:
                # Package is not installed, proceed with installation
                if self.install_package(package):
                    successful_installs.append(package.name)
                else:
                    failed_installs.append(package.name)
            
            # Small delay between operations
            time.sleep(0.5)
        
        # Summary
        print("\n" + "=" * 60)
        print("📊 NPM INSTALLATION SUMMARY")
        print("=" * 60)
        
        if successful_installs:
            print(f"✅ Successfully installed ({len(successful_installs)}):")
            for package in successful_installs:
                print(f"   • {package}")
        
        if successful_upgrades:
            print(f"\n⬆️  Successfully upgraded ({len(successful_upgrades)}):")
            for package in successful_upgrades:
                print(f"   • {package}")
        
        if skipped_packages:
            print(f"\n⏭️  Skipped ({len(skipped_packages)}):")
            for package in skipped_packages:
                print(f"   • {package}")
        
        if failed_installs:
            print(f"\n❌ Failed operations ({len(failed_installs)}):")
            for package in failed_installs:
                print(f"   • {package}")
        
        total_successful = len(successful_installs) + len(successful_upgrades)
        total_processed = len(self.packages)
        
        print(f"\n🎉 Processing complete! {total_successful} successful operations out of {total_processed} packages.")
        print("\n💡 Tip: You may need to restart your terminal to use newly installed CLI tools.")

def main():
    print("🔧 NPM Development Tools Global Installer")
    print("=" * 50)
    
    installer = NpmInstaller()
    
    # Parse command line arguments
    show_categories = "--show-categories" in sys.argv or "--list" in sys.argv
    
    # Show help if requested
    if "--help" in sys.argv or "-h" in sys.argv:
        print("\nUsage: python npm_dev_installer.py [OPTIONS]")
        print("\nOptions:")
        print("  --show-categories, --list    Show all packages by category before installing")
        print("  --help, -h                   Show this help message")
        print("\nExamples:")
        print("  python npm_dev_installer.py")
        print("  python npm_dev_installer.py --show-categories")
        return
    
    installer.install_all(show_categories=show_categories)

if __name__ == "__main__":
    main()