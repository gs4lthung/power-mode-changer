# Define power plans GUIDs for common modes (these are system defaults)
$powerSaver = "a1841308-3541-4fab-bc81-f71556f20b4a"      # Power Saver
$balanced = "381b4222-f694-41f0-9685-ff5bb260df2e"        # Balanced
$highPerformance = "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c" # High Performance

# Display options for the user
Write-Host "Choose the power mode:"
Write-Host "1. Power Saver"
Write-Host "2. Balanced"
Write-Host "3. High Performance"

# Get the user's choice
$choice = Read-Host "Enter the number corresponding to the power mode:"

# Map the numeric input to the corresponding power plan GUID
switch ($choice) {
    "1" { $planGUID = $powerSaver; $mode = "Power Saver" }
    "2" { $planGUID = $balanced; $mode = "Balanced" }
    "3" { $planGUID = $highPerformance; $mode = "High Performance" }
    default { Write-Host "Invalid choice. Exiting..."; exit }
}

# Set the power plan using powercfg command
Write-Host "Changing power mode to $mode..."
powercfg /S $planGUID
Write-Host "Power mode changed to $mode."
