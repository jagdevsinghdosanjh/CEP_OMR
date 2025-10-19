import pytest
from core.metadata_extractor import extract_bubble_metadata

def test_extract_metadata_from_mock_bubbles():
    # Mock bubble centers near expected metadata positions
    bubbles = [
        {"center": (100, 100)},  # School Mgmt: Govt.
        {"center": (120, 100)},  # DOB Day: 01
        {"center": (140, 100)},  # DOB Month: 10
        {"center": (160, 100)},  # DOB Year: 25
        {"center": (200, 100)},  # UDISE digit: 4
        {"center": (220, 100)}   # Student ID digit: 1
    ]

    blocks = {
        "school_mgmt": {"Govt.": {(100, 100)}},
        "dob": {
            "day": {1: (120, 100)},
            "month": {10: (140, 100)},
            "year": {25: (160, 100)}
        },
        "udise": {4: (200, 100)},
        "student_id": {1: (220, 100)}
    }

    metadata = extract_bubble_metadata(bubbles, blocks)
    assert metadata["school_mgmt"] == "Govt."
    assert metadata["dob"]["day"] == 1
    assert metadata["dob"]["month"] == 10
    assert metadata["dob"]["year"] == 25
    assert metadata["udise"] == "4"
    assert metadata["student_id"] == "1"
