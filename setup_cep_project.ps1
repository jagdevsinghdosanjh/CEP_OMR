# setup_cep_project.ps1
# Run this in VS Code terminal on Windows 11

$root = "cep_baseline_omr"
$folders = @(
    "$root/data/sample_omr_scans",
    "$root/data/exports",
    "$root/assets/overlays",
    "$root/assets/templates",
    "$root/config",
    "$root/core",
    "$root/interface",
    "$root/utils",
    "$root/tests"
)

# Create folders
foreach ($folder in $folders) {
    New-Item -ItemType Directory -Path $folder -Force | Out-Null
}

# Create placeholder files
New-Item "$root/README.md" -ItemType File -Force | Out-Null
New-Item "$root/requirements.txt" -ItemType File -Force | Out-Null
New-Item "$root/.gitignore" -ItemType File -Force | Out-Null
New-Item "$root/config/parameters.yaml" -ItemType File -Force | Out-Null
New-Item "$root/data/answer_key.json" -ItemType File -Force | Out-Null

Write-Host "✅ Project structure created successfully at $root"
