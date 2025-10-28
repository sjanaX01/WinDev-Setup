#!/usr/bin/env python3
"""
Windows 11 Development Tools Installer
Uses winget to automatically install essential development tools
"""

import subprocess
import sys
import json
import time
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
    
    def install_package(self, package: Package) -> bool:
        """Install a single package"""
        print(f"\n📦 Installing {package.name}...")
        
        try:
            # Use --accept-source-agreements and --accept-package-agreements to avoid prompts
            cmd = [
                "winget", "install", 
                "--id"
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
        """Install all packages"""
        if not self.check_winget_available():
            return
        
        self.update_winget_sources()
        
        print(f"\n🚀 Starting installation of {len(self.packages)} packages...")
        print("=" * 60)
        
        successful_installs = []
        failed_installs = []
        
        for i, package in enumerate(self.packages, 1):
            print(f"\n[{i}/{len(self.packages)}] Processing {package.name}")
            
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
            
            # Small delay between installations
            time.sleep(2)
        
        # Summary
        print("\n" + "=" * 60)
        print("📊 INSTALLATION SUMMARY")
        print("=" * 60)
        
        print(f"✅ Successfully installed ({len(successful_installs)}):")
        for package in successful_installs:
            print(f"   • {package}")
        
        if failed_installs:
            print(f"\n❌ Failed to install ({len(failed_installs)}):")
            for package in failed_installs:
                print(f"   • {package}")
        
        print(f"\n🎉 Installation complete! {len(successful_installs)}/{len(self.packages)} packages installed successfully.")

def main():
    print("🔧 Windows 11 Development Tools Installer")
    print("=" * 50)
    
    installer = WingetInstaller()
    
    # Check if user wants to skip search verification
    if len(sys.argv) > 1 and sys.argv[1] == "--skip-search":
        installer.install_all(skip_search=True)
    else:
        installer.install_all()

if __name__ == "__main__":
    main()