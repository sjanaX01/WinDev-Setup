#!/usr/bin/env python3
"""
Windows 11 Development Tools Installer
Uses winget to automatically install essential development tools
"""

import subprocess
import sys
import json
import time
import threading
import re
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class Package:
    name: str
    winget_id: str
    description: str
    verified_publisher: bool = False

class WingetInstaller:
    def __init__(self):
        self.packages = [
            # Code Editors & IDEs
            Package("Visual Studio Code", "Microsoft.VisualStudioCode", "Code editor", True),
            Package("Git", "Microsoft.Git", "Version control system", True),
            
            # Development Runtimes
            Package("Python 3.12", "Python.Python.3.12", "Python programming language", True),
            Package("Node.js", "OpenJS.NodeJS", "JavaScript runtime", True),
            Package("Docker Desktop", "Docker.DockerDesktop", "Containerization platform", True),
            
            # Browsers
            Package("Google Chrome", "Google.Chrome", "Web browser", True),
            Package("Brave Browser", "Brave.Brave", "Privacy-focused browser", True),
            
            # Virtualization
            Package("VirtualBox", "Oracle.VirtualBox", "Virtual machine software", True),
            
            # AI Tools
            Package("Claude Desktop", "Anthropic.Claude", "AI assistant desktop app", True),
            
            # System Utilities
            Package("PowerToys", "Microsoft.PowerToys", "Windows system utilities", True),
            Package("Windows Terminal", "Microsoft.WindowsTerminal", "Modern terminal", True),
            Package("7-Zip", "7zip.7zip", "File archiver", True),
            
            # Additional Dev Tools
            Package("Postman", "Postman.Postman", "API development tool", True),
            Package("Discord", "Discord.Discord", "Communication platform", True),
            Package("Slack", "SlackTechnologies.Slack", "Team communication", True),
            Package("Notion", "Notion.Notion", "Note-taking and organization", True),
            Package("OBS Studio", "OBSProject.OBSStudio", "Screen recording/streaming", True),
        ]
        
    def check_winget_available(self) -> bool:
        """Check if winget is available on the system"""
        try:
            result = subprocess.run(
                ["winget", "--version"], 
                capture_output=True, 
                text=True, 
                check=True
            )
            print(f"✓ Winget version: {result.stdout.strip()}")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("❌ Winget is not available. Please install App Installer from Microsoft Store.")
            return False
    
    def search_package(self, package: Package) -> Optional[str]:
        """Search for a package and verify it exists"""
        try:
            result = subprocess.run(
                ["winget", "search", package.winget_id, "--exact"],
                capture_output=True,
                text=True,
                check=True
            )
            
            if package.winget_id.lower() in result.stdout.lower():
                print(f"✓ Found: {package.name} ({package.winget_id})")
                return package.winget_id
            else:
                print(f"⚠️  Package not found: {package.name}")
                return None
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Error searching for {package.name}: {e}")
            return None
    
    def check_package_installed_and_updatable(self, package: Package) -> tuple[bool, Optional[str], Optional[str]]:
        """Check if package is installed and if update is available"""
        try:
            # Check if package is installed
            list_result = subprocess.run(
                ["winget", "list", "--id", package.winget_id, "--exact"],
                capture_output=True,
                text=True
            )
            
            is_installed = list_result.returncode == 0 and package.winget_id.lower() in list_result.stdout.lower()
            
            if not is_installed:
                return False, None, None
            
            # Check for available updates
            upgrade_result = subprocess.run(
                ["winget", "upgrade", "--id", package.winget_id, "--exact"],
                capture_output=True,
                text=True
            )
            
            if upgrade_result.returncode == 0 and package.winget_id.lower() in upgrade_result.stdout.lower():
                # Parse version information from output
                lines = upgrade_result.stdout.split('\n')
                current_version = "Unknown"
                available_version = "Unknown"
                
                for line in lines:
                    if package.winget_id.lower() in line.lower():
                        parts = line.split()
                        if len(parts) >= 3:
                            current_version = parts[1]
                            available_version = parts[2]
                        break
                
                return True, current_version, available_version
            else:
                return True, None, None  # Installed but no update available
                
        except subprocess.CalledProcessError:
            return False, None, None
    
    def prompt_user_for_package_update(self, package: Package, current_version: str, available_version: str) -> bool:
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
    
    def upgrade_package(self, package: Package) -> bool:
        """Upgrade a single package"""
        print(f"⬆️  Upgrading {package.name}...")
        
        try:
            cmd = [
                "winget", "upgrade", 
                "--id", package.winget_id,
                "--exact",
                "--accept-source-agreements",
                "--accept-package-agreements"
            ]
            
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
    
    def install_package(self, package: Package) -> bool:
        """Install a single package"""
        print(f"\n📦 Installing {package.name}...")
        
        try:
            # Use --accept-source-agreements and --accept-package-agreements to avoid prompts
            cmd = [
                "winget", "install", 
                "--id",
                package.winget_id,
                "--exact",
                "--accept-source-agreements",
                "--accept-package-agreements",
                # "--silent"
            ]
            
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
                print(f"Error: {result.stderr}")
                return False
                
        except subprocess.TimeoutExpired:
            print(f"⏰ Installation of {package.name} timed out")
            return False
        except Exception as e:
            print(f"❌ Error installing {package.name}: {e}")
            return False
    
    def update_winget_sources(self):
        """Update winget sources to ensure latest package info"""
        print("🔄 Updating winget sources...")
        try:
            subprocess.run(
                ["winget", "source", "update"],
                capture_output=True,
                text=True,
                check=True
            )
            print("✅ Sources updated successfully")
        except subprocess.CalledProcessError:
            print("⚠️  Failed to update sources, continuing anyway...")
    
    def install_all(self, skip_search: bool = False):
        """Install all packages with per-package update checking"""
        if not self.check_winget_available():
            return
        
        self.update_winget_sources()
        
        print(f"\n🚀 Starting processing of {len(self.packages)} packages...")
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
                # Search for package first (unless skipped)
                if not skip_search:
                    if not self.search_package(package):
                        failed_installs.append(package.name)
                        continue
                
                # Install package
                if self.install_package(package):
                    successful_installs.append(package.name)
                else:
                    failed_installs.append(package.name)
            
            # Small delay between operations
            time.sleep(1)
        
        # Summary
        print("\n" + "=" * 60)
        print("📊 OPERATION SUMMARY")
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

def main():
    print("🔧 Windows 11 Development Tools Installer")
    print("=" * 50)
    
    installer = WingetInstaller()
    
    # Parse command line arguments
    skip_search = "--skip-search" in sys.argv
    
    # Show help if requested
    if "--help" in sys.argv or "-h" in sys.argv:
        print("\nUsage: python winget_dev_installer.py [OPTIONS]")
        print("\nOptions:")
        print("  --skip-search    Skip package search verification (faster)")
        print("  --help, -h       Show this help message")
        print("\nExamples:")
        print("  python winget_dev_installer.py")
        print("  python winget_dev_installer.py --skip-search")
        return
    
    installer.install_all(skip_search=skip_search)

if __name__ == "__main__":
    main()