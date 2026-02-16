# setup_env.ps1 - Setup Python Development Environment

$ErrorActionPreference = "Stop"

function Write-Log {
    param([string]$Message)
    Write-Host "[SETUP] $Message" -ForegroundColor Cyan
}

# 1. Check Python
try {
    $pythonVersion = python --version
    Write-Log "Found Python: $pythonVersion"
} catch {
    Write-Error "Python is not installed or not in PATH."
    exit 1
}

# 2. Create Virtual Environment
if (-not (Test-Path ".venv")) {
    Write-Log "Creating virtual environment in .venv..."
    python -m venv .venv
} else {
    Write-Log "Virtual environment already exists."
}

# 3. Activate Virtual Environment
$venvScript = ".\.venv\Scripts\Activate.ps1"
if (Test-Path $venvScript) {
    Write-Log "Activating virtual environment..."
    # Note: We can't persist activation in the parent shell easily from a script, but we can set up the environment for subsequent commands in this script.
    # To use interactively, the user must dot-source this script: . .\setup_env.ps1
}

# 4. Install Dependencies
Write-Log "Upgrading pip..."
& ".\.venv\Scripts\python" -m pip install --upgrade pip

Write-Log "Installing dev tools and project dependencies..."
& ".\.venv\Scripts\python" -m pip install ruff mypy pytest langchain langchain-community langchain-openai python-dotenv pydantic

# 5. Copy Template Configuration (Optional)
$scriptPath = $MyInvocation.MyCommand.Path
$skillRoot = Split-Path (Split-Path $scriptPath -Parent) -Parent
$templateConfig = Join-Path $skillRoot "templates\pyproject.toml"
$targetConfig = ".\pyproject.toml"

if (Test-Path $templateConfig) {
    if (-not (Test-Path $targetConfig)) {
        Write-Log "Copying pyproject.toml template..."
        Copy-Item $templateConfig -Destination $targetConfig
    } else {
        Write-Log "pyproject.toml already exists. Skipping copy."
    }
} else {
    Write-Warning "Template pyproject.toml not found at $templateConfig"
}

Write-Log "Setup complete! To activate the environment, run: .\.venv\Scripts\Activate.ps1"
