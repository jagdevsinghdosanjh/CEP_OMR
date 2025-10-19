def extract_bubble_metadata(bubbles, blocks):
    """
    Extracts metadata from bubble blocks (e.g., School Mgmt, DOB, UDISE, Student ID).
    `blocks` is a dictionary of expected bubble positions for each metadata field.
    Returns a dictionary of extracted values.
    """
    metadata = {
        "school_mgmt": None,
        "dob": {"day": None, "month": None, "year": None},
        "udise": "",
        "student_id": ""
    }

    for field, positions in blocks.items():
        for label, grid in positions.items():
            for digit, center in grid.items():
                for bubble in bubbles:
                    bx, by = bubble["center"]
                    if abs(bx - center[0]) < 10 and abs(by - center[1]) < 10:
                        if field == "school_mgmt":
                            metadata["school_mgmt"] = label
                        elif field == "dob":
                            metadata["dob"][label] = digit
                        elif field == "udise":
                            metadata["udise"] += str(digit)
                        elif field == "student_id":
                            metadata["student_id"] += str(digit)

    print(f"📋 Bubble Metadata Extracted — School: {metadata['school_mgmt']}, UDISE: {metadata['udise']}, ID: {metadata['student_id']}")
    return metadata
