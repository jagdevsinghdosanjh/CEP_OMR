import cv2

def generate_question_grid(start_x, start_y, dx, dy, rows, cols):
    """
    Generates a grid of question bubble centers.
    Returns a dictionary: {question_number: [(x1, y1), (x2, y2), ...]}
    """
    grid = {}
    q_num = 1

    for r in range(rows):
        for c in range(cols):
            x = start_x + c * dx
            y = start_y + r * dy
            grid[q_num] = grid.get(q_num, []) + [(x, y)]
            if len(grid[q_num]) == 4:
                q_num += 1

    return grid

def draw_grid_overlay(img, grid, radius=10):
    """
    Draws grid centers on the image for calibration.
    """
    for q_no, centers in grid.items():
        for cx, cy in centers:
            cv2.circle(img, (int(cx), int(cy)), radius, (255, 0, 0), 2)
    return img
