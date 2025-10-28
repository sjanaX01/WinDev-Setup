#!/usr/bin/env python3
"""
Complete Development Environment Installer
Runs both winget and npm installers sequentially for a complete dev setup
"""

import subprocess
import sys
import os
import time
from pathlib import Path

class DevEnvironmentInstaller:
    def __init__(self):
        self.script_dir = Path(__file__).parent
        self.winget_script = self.script_dir / "winget_dev_installer.py"
        self.npm_script = self.script_dir / "npm_dev_installer.py"
    
    def check_scripts_exist(self) -> bool:
        """Check if both installer scripts exist"""
        missing_scripts = []
        
        if not self.winget_script.exists():
            missing_scripts.append("winget_dev_installer.py")
        
        if not self.npm_script.exists():
            missing_scripts.append("npm_dev_installer.py")
        
        if missing_scripts:
            print("❌ Missing required installer scripts:")
            for script in missing_scripts:
                print(f"   • {script}")
            print(f"\n💡 Make sure all scripts are in the same directory: {self.script_dir}")
            return False
        
        return True
    
    def run_script(self, script_path: Path, script_name: str, args: list = None) -> bool:
        """Run a Python script and return success status"""
        print(f"\n{'='*60}")
        print(f"🚀 Starting {script_name}")
        print(f"{'='*60}")
        
        try:
            # Prepare command
            cmd = [sys.executable, str(script_path)]
            if args:
                cmd.extend(args)
            
            # Run the script
            result = subprocess.run(
                cmd,
                cwd=self.script_dir,
                timeout=3600  # 1 hour timeout for each installer
            )
            
            if result.returncode == 0:
                print(f"\n✅ {script_name} completed successfully!")
                return True
            else:
                print(f"\n❌ {script_name} failed with return code {result.returncode}")
                return False
                
        except subprocess.TimeoutExpired:
            print(f"\n⏰ {script_name} timed out after 1 hour")
            return False
        except KeyboardInterrupt:
            print(f"\n⚠️  {script_name} was cancelled by user")
            return False
        except Exception as e:
            print(f"\n❌ Error running {script_name}: {e}")
            return False
    
    def prompt_user_continue(self, phase: str) -> bool:
        """Ask user if they want to continue to the next phase"""
        print(f"\n{'='*60}")
        print(f"📋 Ready to start {phase}")
        print(f"{'='*60}")
        
        while True:
            try:
                choice = input(f"Do you want to proceed with {phase}? (y/n): ").strip().lower()
                
                if choice in ['y', 'yes']:
                    return True
                elif choice in ['n', 'no']:
                    return False
                else:
                    print("Please enter 'y' for yes or 'n' for no.")
                    
            except KeyboardInterrupt:
                print("\n⚠️  Operation cancelled by user.")
                return False
    
    def show_summary(self, winget_success: bool, npm_success: bool):
        """Show final installation summary"""
        print(f"\n{'='*60}")
        print("📊 COMPLETE INSTALLATION SUMMARY")
        print(f"{'='*60}")
        
        print("Phase 1 - System Applications (Winget):")
        if winget_success:
            print("   ✅ Completed successfully")
        else:
            print("   ❌ Failed or was skipped")
        
        print("\nPhase 2 - CLI Tools & Utilities (NPM):")
        if npm_success:
            print("   ✅ Completed successfully")
        else:
            print("   ❌ Failed or was skipped")
        
        total_success = sum([winget_success, npm_success])
        print(f"\n🎉 Overall Result: {total_success}/2 phases completed successfully")
        
        if total_success == 2:
            print("\n🎊 Congratulations! Your complete development environment is now set up!")
            print("💡 You may need to restart your terminal to use all newly installed tools.")
        elif total_success == 1:
            print("\n⚠️  Partial installation completed. Some tools may be missing.")
        else:
            print("\n❌ Installation was not successful. Please check the errors above.")
    
    def install_all(self, skip_winget_search: bool = False, show_npm_categories: bool = False, 
                   skip_winget: bool = False, skip_npm: bool = False):
        """Run both installers sequentially"""
        
        if not self.check_scripts_exist():
            return
        
        print("🔧 Complete Development Environment Installer")
        print("=" * 50)
        print("This will install:")
        print("📦 Phase 1: System applications using Winget")
        print("   • VS Code, Docker, browsers, utilities, etc.")
        print("🌐 Phase 2: CLI tools and utilities using NPM")
        print("   • TypeScript, React, testing tools, etc.")
        
        winget_success = True
        npm_success = True
        
        # Phase 1: Winget Installer
        if not skip_winget:
            if self.prompt_user_continue("Phase 1 (System Applications)"):
                winget_args = []
                if skip_winget_search:
                    winget_args.append("--skip-search")
                
                winget_success = self.run_script(
                    self.winget_script, 
                    "Winget Installer", 
                    winget_args
                )
                
                if winget_success:
                    print("\n⏳ Waiting 5 seconds before starting NPM installation...")
                    time.sleep(5)
            else:
                print("⏭️  Skipping Winget installation")
                winget_success = False
        else:
            print("⏭️  Winget installation skipped (--skip-winget flag)")
            winget_success = False
        
        # Phase 2: NPM Installer
        if not skip_npm:
            if self.prompt_user_continue("Phase 2 (CLI Tools & Utilities)"):
                npm_args = []
                if show_npm_categories:
                    npm_args.append("--show-categories")
                
                npm_success = self.run_script(
                    self.npm_script, 
                    "NPM Installer", 
                    npm_args
                )
            else:
                print("⏭️  Skipping NPM installation")
                npm_success = False
        else:
            print("⏭️  NPM installation skipped (--skip-npm flag)")
            npm_success = False
        
        # Show final summary
        self.show_summary(winget_success, npm_success)

def main():
    print("🔧 Complete Development Environment Setup")
    print("=" * 50)
    
    # Parse command line arguments
    skip_winget_search = "--skip-winget-search" in sys.argv
    show_npm_categories = "--show-npm-categories" in sys.argv
    skip_winget = "--skip-winget" in sys.argv
    skip_npm = "--skip-npm" in sys.argv
    
    # Show help if requested
    if "--help" in sys.argv or "-h" in sys.argv:
        print("\nUsage: python main.py [OPTIONS]")
        print("\nOptions:")
        print("  --skip-winget-search     Skip package search verification in winget installer")
        print("  --show-npm-categories    Show NPM packages by category before installing")
        print("  --skip-winget           Skip the entire winget installation phase")
        print("  --skip-npm              Skip the entire NPM installation phase")
        print("  --help, -h              Show this help message")
        print("\nPhases:")
        print("  Phase 1: System Applications (Winget)")
        print("    • Visual Studio Code, Git, Docker, browsers")
        print("    • Python, Node.js, VirtualBox, PowerToys")
        print("    • Communication tools, utilities")
        print("\n  Phase 2: CLI Tools & Utilities (NPM)")
        print("    • TypeScript, React, Vue, Angular CLIs")
        print("    • Testing tools, build tools, linters")
        print("    • Deployment tools, documentation generators")
        print("\nExamples:")
        print("  python main.py")
        print("  python main.py --skip-winget-search")
        print("  python main.py --show-npm-categories")
        print("  python main.py --skip-winget")
        print("  python main.py --skip-npm")
        return
    
    # Create installer and run
    installer = DevEnvironmentInstaller()
    installer.install_all(
        skip_winget_search=skip_winget_search,
        show_npm_categories=show_npm_categories,
        skip_winget=skip_winget,
        skip_npm=skip_npm
    )

if __name__ == "__main__":
    main()