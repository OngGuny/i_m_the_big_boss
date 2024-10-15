# 각 플레이어의 턴에
# 나온 주사위 수 만큼
# 보드 판 위를 이동함
import logging


class DollarMarker:
    def __init__(self):
        self.position = 1

    def move(self, dice_scale):
        logging.info(f"Current marker position: {self.position}")
        self.position = self.position + dice_scale
        logging.info(f"Marker is moved to {self.position}")
