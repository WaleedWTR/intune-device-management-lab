#!/usr/bin/env python3
from __future__ import annotations
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "synthetic_devices.csv"
POLICY = ROOT / "policies" / "windows-compliance-baseline.json"

def load_policy():
    return json.loads(POLICY.read_text(encoding="utf-8"))

def load_devices():
    with DATA.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))

def failures(device, policy):
    req = policy["requirements"]
    issues = []
    if req["bitLockerRequired"] and device["bitlocker"].lower() != "true":
        issues.append("BitLocker")
    if req["secureBootRequired"] and device["secure_boot"].lower() != "true":
        issues.append("Secure Boot")
    if req["firewallRequired"] and device["firewall"].lower() != "true":
        issues.append("Firewall")
    if req["antivirusRequired"] and device["antivirus"].lower() != "true":
        issues.append("Antivirus")
    if int(device["last_checkin_days"]) > req["maximumInactivityDays"]:
        issues.append("Stale check-in")
    return issues

def main():
    policy = load_policy()
    devices = load_devices()
    non_compliant = []
    for device in devices:
        issues = failures(device, policy)
        if issues:
            non_compliant.append((device["device_name"], issues))

    print(f"Devices assessed: {len(devices)}")
    print(f"Devices requiring attention: {len(non_compliant)}")
    for name, issues in non_compliant:
        print(f"- {name}: {', '.join(issues)}")

if __name__ == "__main__":
    main()
