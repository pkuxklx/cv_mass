# %%
import numpy as np
import cv2
import matplotlib.pyplot as plt

# %%
class Shape:
    pass
# %%
def valid_ellipse(ellipse, contour = None) -> bool:
    """
    This function check whether the fitted ellipse is a proper one.

    Args:
    """
    x0, y0 = ellipse[0]
    b, a = ellipse[1]
    theta = ellipse[2]
    assert b <= a
    if not (0.2 < b / a < 0.4):
        return False

    overlap_ratio = 1
    # TODO
    # 统计contour的
    bkg = np.zeros((2000, 2000))
    cv2.drawContours(bkg, [contour], 0, 255, thickness = -1) # thickness<0，填充内部
    points = [(x, y) for x in range(bkg.shape[1]) for y in range(bkg.shape[0]) if bkg[y, x] > 0]
    points = np.array(points)
    S_ellipse = (np.pi * a * b) / 4 # 
    if not (18000 < S_ellipse < 30000):
        return False
    
    S_intersect = 0
    # theta，长轴逆时针旋转角度，单位是°
    # 斜椭圆的表达式是什么啊 - 天地無用的回答 - 知乎
    # https://www.zhihu.com/question/383833757/answer/1116489491
    for x, y in points:
        theta = theta / 180 * np.pi
        x -= x0
        y -= y0
        if ((x * np.cos(theta) - y * np.sin(theta)) / a) ** 2 + ((x * np.sin(theta) + y * np.cos(theta)) / b) ** 2 <= 1:
            S_intersect += 1
    overlap_ratio = S_intersect / S_ellipse
    # assert overlap_ratio <= 1
    print(f'overlap ratio {overlap_ratio}={S_intersect}/{S_ellipse}')
    return overlap_ratio > 0.6

# %%
# cv2.