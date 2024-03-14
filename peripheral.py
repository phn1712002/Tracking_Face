
import cv2, numpy as np
from geo import Rectangle, Point
from PIL import ImageFont, ImageDraw, Image


class Camera:
    def __init__(self, COM, resolution=[1280, 720], flip=False, key_stop='q', path_font='font/arial.ttf',name=None):
        self.COM = COM
        self.resolution = resolution
        self.flip = flip
        self.key_stop = key_stop
        self.path_font = path_font
        self.rec = Rectangle(list_point=[Point(), Point(x=resolution[0]), Point(y=resolution[1]), Point(resolution[0], resolution[1])])
        self.name = name
        
        
        self.cap = cv2.VideoCapture(self.COM)
        if not self.cap.isOpened():
            raise RuntimeError("Camera error")
        else:
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])

    def close(self):
        self.cap.release()
        cv2.destroyAllWindows()
        
    def get_frame(self):
        ret, image = self.cap.read()
        if not ret: image = None
        elif self.flip: image = cv2.flip(image, 1)
        return image
    
    def live_view(self, frame):
        cv2.imshow("Camera", frame)
        stop = (cv2.waitKey(1) & 0xFF == ord(self.key_stop))
        return stop
    
    def draw_circle(self, frame, window, *args, **kwargs):
        if not(window is None):
            frame = cv2.circle(img=frame, center=(int(window.point_center.x), int(window.point_center.y)), *args, **kwargs)
        return frame
         
    def draw_rec(self, frame, rec, *args, **kwargs):
        if not(rec is None):
            pt1 = (int(rec.point_base.x), int(rec.point_base.y))
            pt2 = (int(rec.point_base.x + rec.vertical), int(rec.point_base.y + rec.horizontal))
            frame = cv2.rectangle(frame, pt1, pt2, *args, **kwargs)
        return frame
    
    def write_text(self, frame, text, 
                  org=(0, 0),
                  color='red', size_text=35):
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(frame)
        font = ImageFont.truetype(self.path_font, size_text)
        draw = ImageDraw.Draw(pil_image)
        draw.text(org, text, font=font, fill=color)
        frame_add_text = np.asarray(pil_image)
        frame_add_text = cv2.cvtColor(frame_add_text, cv2.COLOR_RGB2BGR)
        return frame_add_text