import cv2

class ObjectTracker:
    def __init__(self, roi_size=40, tracker_type='CSRT', debug=False):
        self.center = None  # 中心點
        self.drawing = False  # 是否繪製矩形框
        self.tracking = False  # 是否正在追蹤
        self.tracker = None  # 追蹤器
        self.initBB = None  # 初始邊界框
        self.roi_size = roi_size  # ROI大小
        self.tracker_type = tracker_type  # 追蹤器類型
        self.debug = debug  # 調試模式
        self.frame = None  # 當前幀

    def draw_rectangle(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.center = (x, y)  # 設定中心點
            self.drawing = True  # 啟用繪製
            self.initBB = (self.center[0] - self.roi_size // 2, self.center[1] - self.roi_size // 2, self.roi_size, self.roi_size)  # 設定ROI的大小
            self.tracker = self._create_tracker()  # 創建追蹤器
            self.tracker.init(self.frame, self.initBB)  # 初始化追蹤器
            self.tracking = True  # 啟用追蹤

    def _create_tracker(self):
        if self.tracker_type == 'CSRT':
            return cv2.TrackerCSRT_create()  # 創建CSRT追蹤器
        elif self.tracker_type == 'KCF':
            return cv2.TrackerKCF_create()  # 創建KCF追蹤器
        elif self.tracker_type == 'MIL':
            return cv2.TrackerMIL_create()  # 創建MIL追蹤器
        elif self.tracker_type == 'TLD':
            return cv2.legacy.TrackerTLD_create()  # 創建TLD追蹤器
        elif self.tracker_type == 'MOSSE':
            return cv2.legacy.TrackerMOSSE_create()  # 創建MOSSE追蹤器
        else:
            print(f"Error: Unknown tracker type {self.tracker_type}. Falling back to CSRT.")
            return cv2.TrackerCSRT_create()  # 默認創建CSRT追蹤器

    def update_tracker(self, frame):
        self.frame = frame  # 更新當前幀
        if self.tracking and self.tracker:
            success, box = self.tracker.update(frame)  # 更新追蹤器
            if success:
                (x, y, w, h) = [int(v) for v in box]
                self.center = (x + w // 2, y + h // 2)  # 更新中心點
                top_left = (self.center[0] - self.roi_size // 2, self.center[1] - self.roi_size // 2)
                bottom_right = (self.center[0] + self.roi_size // 2, self.center[1] + self.roi_size // 2)
                cv2.rectangle(frame, top_left, bottom_right, (255, 0, 0), 2)  # 繪製矩形框
            else:
                self.drawing = False  # 停止繪製
                self.tracking = False  # 停止追蹤
                self.center = None  # 清除中心點

        if self.debug:
            self._draw_debug_info()  # 繪製調試資訊

    def stop_tracking(self):
        self.tracking = False  # 停止追蹤
        self.tracker = None  # 清除追蹤器
        self.center = None  # 清除中心點

    def _draw_debug_info(self):
        if self.tracking:
            cv2.putText(self.frame, f"Tracking: {self.tracking}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)  # 顯示追蹤狀態
            cv2.putText(self.frame, f"Center: {self.center}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)  # 顯示中心點
