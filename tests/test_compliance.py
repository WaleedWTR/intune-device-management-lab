from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from compliance_report import failures, load_devices, load_policy  # noqa: E402

def test_synthetic_inventory_has_expected_size():
    assert len(load_devices()) == 6

def test_known_healthy_device_has_no_failures():
    device = next(d for d in load_devices() if d["device_name"] == "LAB-W11-001")
    assert failures(device, load_policy()) == []

def test_bitlocker_failure_is_detected():
    device = next(d for d in load_devices() if d["device_name"] == "LAB-W11-002")
    assert "BitLocker" in failures(device, load_policy())

def test_stale_device_is_detected():
    device = next(d for d in load_devices() if d["device_name"] == "LAB-W10-003")
    assert "Stale check-in" in failures(device, load_policy())
