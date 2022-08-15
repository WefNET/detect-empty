## detect.py

import cv2
import numpy as np
import pyautogui as pg
import time

time.sleep(3)

screenshot = pg.screenshot()

screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

coords = []

for empty in pg.locateAllOnScreen('empty.png', confidence=0.95):

    # cv2.rectangle(
    #     screenshot,
    #     (empty.left, empty.top),
    #     (empty.left + empty.width, empty.top + empty.height),
    #     (255, 0, 0),
    #     1
    # )
    coord_pair = [empty.left + 9, empty.top + 9]
    coords.append(coord_pair)


print(coords)

# cv2.imshow('Scrren', screenshot)

# cv2.waitKey(0)

# cv2.destroyAllWindows()