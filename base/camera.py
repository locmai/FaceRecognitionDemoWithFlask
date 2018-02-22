import time
from base.base_camera import BaseCamera


class Camera(BaseCamera):

    @staticmethod
    def frames():
        while True:
            time.sleep(1)
            yield Camera.imgs[int(time.time()) % 3]
