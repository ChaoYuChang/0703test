#image_handler.py
# --------------------------------------------------------------
# Author: Thomas Huang
# Date: 2024-06-26
# Description: image_handler
# --------------------------------------------------------------
import cv2

class ImageHandler:
    def __init__(self, camera_index=0):
        # 初始化相機
        self.cap = cv2.VideoCapture(camera_index)
        self._check_camera()
    
    def _check_camera(self):
        # 檢查相機是否打開
        if not self.cap.isOpened():
            print("Error: Could not open webcam.")  # 錯誤提示
            exit()
    
    def read_frame(self):
        # 讀取一幀影像
        ret, frame = self.cap.read()
        if not ret:
            print("Error: Could not read frame from webcam.")  # 錯誤提示
        return ret, frame
    
    def release(self):
        # 釋放相機資源
        self.cap.release()
    
    def save_frame(self, frame, filename):
        # 保存當前影像
        cv2.imwrite(filename, frame)
