import numpy as np
import cv2
import threading
from copy import deepcopy

thread_lock = threading.Lock()
thread_exit = False

class CameraThread(threading.Thread):
    def __init__(self, camera_id, img_height, img_width):
        super(CameraThread, self).__init__()
        self.camera_id = camera_id  # 相機 ID
        self.img_height = img_height  # 影像高度
        self.img_width = img_width  # 影像寬度
        self.frame = None  # 初始化影像幀

    def get_frame(self):
        # 獲取影像幀的副本
        return deepcopy(self.frame)

    def run(self):
        global thread_exit
        cap = cv2.VideoCapture(self.camera_id)  # 開啟相機
        if not cap.isOpened():
            print("Error: Could not open camera.")
            thread_exit = True
            return

        while not thread_exit:
            ret, frame = cap.read()  # 讀取影像幀
            if ret:
                frame = cv2.resize(frame, (self.img_width, self.img_height))  # 調整影像大小
                thread_lock.acquire()
                self.frame = frame  # 更新影像幀
                thread_lock.release()
            else:
                thread_exit = True
        cap.release()  # 釋放相機
