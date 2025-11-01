
'''
This script configures fastfetch in the same way as the provided PowerShell script.
It creates the necessary configuration files and updates the PowerShell profile.
'''
import os
import subprocess
import sys

def get_powershell_profile_path():
    """Determines the PowerShell profile path by executing a PowerShell command."""
    command = "Write-Output $PROFILE"
    try:
        # Execute the command using powershell.exe
        result = subprocess.run(
            ["powershell", "-NoProfile", "-Command", command],
            capture_output=True,
            text=True,
            check=True,
            encoding='utf-8'
        )
        profile_path = result.stdout.strip()
        if not profile_path:
            raise ValueError("PowerShell command returned an empty profile path.")
        return profile_path
    except (subprocess.CalledProcessError, FileNotFoundError, ValueError) as e:
        print(f"Error getting PowerShell profile path: {e}", file=sys.stderr)
        # Fallback to a common default if PowerShell isn't found or fails
        print("Falling back to a default profile path.", file=sys.stderr)
        return os.path.join(os.path.expanduser('~'), "Documents", "WindowsPowerShell", "Microsoft.PowerShell_profile.ps1")

def main():
    """Main function to set up fastfetch configuration."""
    print("Starting fastfetch configuration setup...")

    # 1. Define paths
    user_home = os.path.expanduser('~')
    config_dir = os.path.join(user_home, '.config', 'fastfetch')
    ascii_path = os.path.join(config_dir, 'ascii.txt')
    json_config_path = os.path.join(config_dir, 'config.jsonc')

    # 2. Create the configuration directory
    print(f"Ensuring configuration directory exists: {config_dir}")
    os.makedirs(config_dir, exist_ok=True)

    # 3. Create ascii.txt
    print(f"Creating ASCII file: {ascii_path}")
    ascii_content = r'''
$1    ⣀⡀
$1    ⣿⠙⣦⠀⠀⠀⠀⠀⠀⣀⣤⡶⠛⠁
$2    ⢻⠀⠈⠳⠀⠀⣀⣴⡾⠛⠁⣠⠂⢠⠇
$2    ⠈⢀⣀⠤⢤⡶⠟⠁⢀⣴⣟⠀⠀⣾
$3   ⠠⠞⠉⢁⠀⠉⠀⢀⣠⣾⣿⣏⠀⢠⡇
$3  ⡰⠋⠀⢰⠃⠀⠀⠉⠛⠿⠿⠏⠁⠀⣸⠁
$4  ⣄⠀⠀⠏⣤⣤⣀⡀⠀⠀⠀⠀⠀⠾⢯⣀
$4  ⣻⠃⠀⣰⡿⠛⠁⠀⠀⠀⢤⣀⡀⠀⠺⣿⡟⠛⠁
$5 ⡠⠋⡤⠠⠋⠀⠀⢀⠐⠁⠀⠈⣙⢯⡃⠀⢈⡻⣦
$5⢰⣷⠇   ⢀⡠⠃⠀⠀⠀⠀⠈⠻⢯⡄⠀⢻⣿⣷
$6 ⠉⠲⣶⣶⢾⣉⣐⡚⠋⠀⠀⠀⠀⠀⠘⠀⠀⡎⣿⣿⡇
$6 ⠀⠀⠀⠀⣸⣿⣿⣿⣷⡄⠀⠀⢠⣿⣴⠀⠀⣿⣿⣿⣧
$7 ⠀⠀⢀⣴⣿⣿⣿⣿⣿⠇⠀⢠⠟⣿⠏⢀⣾⠟⢸⣿⡇
$7 ⠀⢠⣿⣿⣿⣿⠟⠘⠁⢠⠜⢉⣐⡥⠞⠋⢁⣴⣿⣿⠃
$8 ⠀⣾⢻⣿⣿⠃⠀⠀⡀⢀⡄⠁⠀⠀⢠⡾ᵇʸ ᵗⁿᵏᵃ⠁
$8 ⠀⠃⢸⣿⡇⠀⢠⣾⡇⢸⡇⠀⠀⠀⡞
$9 ⠀⠀⠈⢿⡇⡰⠋⠈⠙⠂⠙⠢
$9 ⠀⠀⠀⠈⢧
'''.strip()
    with open(ascii_path, 'w', encoding='utf-8') as f:
        f.write(ascii_content)
    print("ASCII file created.")

    # 4. Create config.jsonc
    print(f"Creating JSON config file: {json_config_path}")
    ascii_path_for_json = ascii_path.replace('\\', '/')
    json_content = f'''
{{
  "$schema": "https://github.com/fastfetch-cli/fastfetch/raw/dev/doc/json_schema.json",
  "logo": {{
    "type": "file",
    "source": "{ascii_path_for_json}",
    "color": {{
      "1": "#F5E0DC",
      "2": "#F2CDCD",
      "3": "#F5C2E7",
      "4": "#FAB387",
      "5": "#F9E2AF",
      "6": "#A6E3A1",
      "7": "#94E2D5",
      "8": "#89DCEB",
      "9": "#74C7EC"
    }},
    "padding": {{
      "top": 1,
      "right": 3
    }}
  }},
  "display": {{
    "separator": " "
  }},
  "modules": [
    "break",
    {{
      "type": "title",
      "color": {{
        "user": "#F5E0DC",
        "at": "#CDD6F4",
        "host": "#89DCEB"
      }}
    }},
    "break",
    {{
      "type": "os",
      "key": "",
      "keyColor": "#89DCEB"
    }},
    {{
      "type": "cpu",
      "key": "",
      "keyColor": "#F5C2E7"
    }},
    {{
      "type": "board",
      "key": "󰚗",
      "keyColor": "#FAB387"
    }},
    {{
      "type": "memory",
      "key": "",
      "keyColor": "#A6E3A1",
      "format": "{{used}} / {{total}} ({{percentage}})"
    }},
    {{
      "type": "disk",
      "key": "",
      "keyColor": "#94E2D5"
    }},
    "break",
    {{
      "type": "colors",
      "symbol": "circle"
    }}
  ]
}}
'''.strip()
    with open(json_config_path, 'w', encoding='utf-8') as f:
        f.write(json_content)
    print("JSON config file created.")

    # 5. Update PowerShell profile
    print("Updating PowerShell profile...")
    profile_path = get_powershell_profile_path()
    print(f"Found PowerShell profile at: {profile_path}")

    profile_dir = os.path.dirname(profile_path)
    os.makedirs(profile_dir, exist_ok=True)

    if not os.path.exists(profile_path):
        with open(profile_path, 'w', encoding='utf-8-sig') as f:
            f.write('')
        print("Created new, empty profile file.")

    fastfetch_config_path_for_ps = json_config_path.replace('\\', '/')
    profile_content_to_add = f'''
# Minimal profile: UTF‑8 + Oh My Posh (if installed) + Fastfetch with explicit config path
try {{
    [Console]::InputEncoding  = [System.Text.Encoding]::UTF8
    [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
    $OutputEncoding = [System.Text.UTF8Encoding]::new($false)
    chcp 65001 > $null
}} catch {{}}

Clear-Host

# Force Fastfetch to use YOUR config every time (bypass path confusion)
if (Get-Command fastfetch -ErrorAction SilentlyContinue) {{
    fastfetch -c "{fastfetch_config_path_for_ps}"
}}
oh-my-posh init pwsh | Invoke-Expression
'''.strip()

    try:
        with open(profile_path, 'r', encoding='utf-8-sig') as f:
            existing_content = f.read()
    except UnicodeDecodeError:
        with open(profile_path, 'r', encoding='utf-8') as f:
            existing_content = f.read()

    if 'fastfetch -c' not in existing_content:
        print("Adding fastfetch command to profile.")
        new_content = profile_content_to_add + '\n\n' + existing_content
        with open(profile_path, 'w', encoding='utf-8-sig') as f:
            f.write(new_content)
        print("Successfully updated PowerShell profile.")
    else:
        print("Fastfetch command already found in PowerShell profile. No changes made.")

    print("Setup complete!")

if __name__ == "__main__":
    main()
