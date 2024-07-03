# zoom_handler.py
# --------------------------------------------------------------
# Author: Thomas Huang
# Date: 2024-05-03
# Description: Zoom
# --------------------------------------------------------------

import cv2

class ZoomHandler:
    def __init__(self):
        self.zoom_factor = 1.0

    def zoom_in(self):
        self.zoom_factor += 0.1

    def zoom_out(self):
        if self.zoom_factor - 0.1 >= 1.0:
            self.zoom_factor -= 0.1

    def zoom_reset(self):
        self.zoom_factor = 1.0

    def apply_zoom(self, frame):
        h, w, _ = frame.shape
        zoomed_frame = cv2.resize(frame, None, fx=self.zoom_factor, fy=self.zoom_factor, interpolation=cv2.INTER_LINEAR)
        zoomed_h, zoomed_w, _ = zoomed_frame.shape
        x_start = (zoomed_w - w) // 2
        y_start = (zoomed_h - h) // 2
        x_end = x_start + w
        y_end = y_start + h
        return zoomed_frame[y_start:y_end, x_start:x_end]
