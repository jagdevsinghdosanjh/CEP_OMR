def map_bubbles_to_responses(bubbles, grid, tolerance=25):
    """
    Maps detected bubbles to question numbers and selected options.
    Returns: {question_number: selected_option_index}
    """
    responses = {}

    for q_no, centers in grid.items():
        for idx, center in enumerate(centers):
            for bubble in bubbles:
                bx, by = bubble["center"]
                if abs(bx - center[0]) < tolerance and abs(by - center[1]) < tolerance:
                    responses[q_no] = idx  # 0-based index for option
                    break
            if q_no in responses:
                break

    print(f"✅ Mapped {len(responses)} responses")
    return responses
