param(
    [string]$OutputPath = "./managed-devices.csv"
)

$ErrorActionPreference = 'Stop'

if (-not (Get-Module -ListAvailable Microsoft.Graph.DeviceManagement)) {
    throw "Microsoft.Graph.DeviceManagement is required."
}

Import-Module Microsoft.Graph.DeviceManagement

if (-not (Get-MgContext)) {
    Connect-MgGraph -Scopes "DeviceManagementManagedDevices.Read.All"
}

$devices = Get-MgDeviceManagementManagedDevice -All

$devices |
    Select-Object Id, DeviceName, OperatingSystem, OSVersion,
        ComplianceState, ManagementAgent, LastSyncDateTime,
        Encrypted, AzureAdRegistered |
    Export-Csv -Path $OutputPath -NoTypeInformation -Encoding utf8

Write-Host "Exported $($devices.Count) managed devices to $OutputPath"
