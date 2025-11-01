# Create fastfetch config directory
$configDir = "$env:USERPROFILE\.config\fastfetch"
if (-not (Test-Path $configDir)) {
    New-Item -Path $configDir -ItemType Directory -Force
}

# Create ascii.txt
$asciiContent = @'
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
'@
[System.IO.File]::WriteAllText("$configDir\ascii.txt", $asciiContent, (New-Object System.Text.UTF8Encoding($false)))


# Create config.jsonc
$asciiPathForJson = (Join-Path $configDir 'ascii.txt').Replace('\', '/')
$jsonContent = @"
{
  "`$schema": "https://github.com/fastfetch-cli/fastfetch/raw/dev/doc/json_schema.json",
  "logo": {
    "type": "file",
    "source": "$asciiPathForJson",
    "color": {
      "1": "#F5E0DC",
      "2": "#F2CDCD",
      "3": "#F5C2E7",
      "4": "#FAB387",
      "5": "#F9E2AF",
      "6": "#A6E3A1",
      "7": "#94E2D5",
      "8": "#89DCEB",
      "9": "#74C7EC"
    },
    "padding": {
      "top": 1,
      "right": 3
    }
  },
  "display": {
    "separator": " "
  },
  "modules": [
    "break",
    {
      "type": "title",
      "color": {
        "user": "#F5E0DC",
        "at": "#CDD6F4",
        "host": "#89DCEB"
      }
    },
    "break",
    {
      "type": "os",
      "key": "",
      "keyColor": "#89DCEB"
    },
    {
      "type": "cpu",
      "key": "",
      "keyColor": "#F5C2E7"
    },
    {
      "type": "board",
      "key": "󰚗",
      "keyColor": "#FAB387"
    },
    {
      "type": "memory",
      "key": "",
      "keyColor": "#A6E3A1",
      "format": "{used} / {total} ({percentage})"
    },
    {
      "type": "disk",
      "key": "",
      "keyColor": "#94E2D5"
    },
    "break",
    {
      "type": "colors",
      "symbol": "circle"
    }
  ]
}
"@
$utf8NoBOM = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText("$configDir\config.jsonc", $jsonContent, $utf8NoBOM)


# Update PowerShell profile
$profilePath = $PROFILE
if (-not (Test-Path $profilePath)) {
    New-Item -Path $PROFILE -Type File -Force
}

$fastfetchConfigPath = "$env:USERPROFILE\.config\fastfetch\config.jsonc".Replace('\', '/')

$profileContentToAdd = @"
# Minimal profile: UTF‑8 + Oh My Posh (if installed) + Fastfetch with explicit config path
try {
    [Console]::InputEncoding  = [System.Text.Encoding]::UTF8
    [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
    `$OutputEncoding = [System.Text.UTF8Encoding]::new(`$false)
    chcp 65001 > `$null
} catch {}

Clear-Host

# Force Fastfetch to use YOUR config every time (bypass path confusion)
if (Get-Command fastfetch -ErrorAction SilentlyContinue) {
    fastfetch -c "$fastfetchConfigPath"
}
"@

$existingContent = Get-Content $profilePath -Raw
if (-not ($existingContent -match 'fastfetch -c')) {
    $newContent = $profileContentToAdd + "`n" + $existingContent
    Set-Content -Path $profilePath -Value $newContent
}
