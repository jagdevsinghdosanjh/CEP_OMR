import cv2
import numpy as np
import pytest

from core.bubble_scanner import detect_bubbles
from core.grid_mapper import generate_question_grid, draw_grid_overlay

def test_detect_bubbles_on_sample_image():
    """
    Loads a sample image and checks bubble detection count.
    """
    img = cv2.imread("data/sample_omr_scans/sample1.png")
    assert img is not None, "Sample image not found"

    bubbles = detect_bubbles(img)
    assert isinstance(bubbles, list), "Bubbles should be a list"
    assert len(bubbles) > 100, "Expected at least 100 bubbles"

def test_grid_generation_and_overlay():
    """
    Generates a grid and overlays it on a blank canvas.
    """
    blank = np.ones((1000, 800, 3), dtype=np.uint8) * 255
    grid = generate_question_grid(start_x=80, start_y=180, dx=38, dy=28, rows=54, cols=2)

    assert isinstance(grid, dict), "Grid should be a dictionary"
    assert len(grid) == 108, "Grid should contain 108 questions"

    overlay = draw_grid_overlay(blank.copy(), grid)
    assert overlay.shape == blank.shape, "Overlay should match input image shape"
