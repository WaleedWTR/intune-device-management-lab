# Intune Device Management Lab

![Endpoint compliance tests](https://github.com/WaleedWTR/intune-device-management-lab/actions/workflows/tests.yml/badge.svg)

A portfolio endpoint-management project demonstrating device inventory, compliance analysis, configuration-baseline design and Microsoft Graph automation patterns.

> **Portfolio note:** All device records and policy examples are synthetic.

## What this project demonstrates

- Intune managed-device inventory
- compliance reporting
- security baseline design
- Microsoft Graph PowerShell
- structured endpoint data
- Python-based compliance analytics
- automated tests
- operational runbook design

## Architecture

```text
Managed Windows Devices
          |
          v
     Microsoft Intune
      /          \
Compliance    Configuration
      \          /
       Device Inventory
             |
             v
       Graph Export
             |
             v
     Analytics / Reporting
```

## Run the synthetic analysis

```bash
python scripts/compliance_report.py
```

## Key documentation

- [Windows compliance baseline](docs/compliance-baseline.md)
- [Operational runbook](docs/operational-runbook.md)
- [Synthetic device inventory](data/synthetic_devices.csv)
- [Microsoft Graph export script](scripts/export-intune-devices.ps1)
- [Technical references](docs/references.md)

## Skills demonstrated

**Microsoft Intune · Endpoint Management · Microsoft Graph · Compliance · Windows · PowerShell · Python · Operational Reporting**
