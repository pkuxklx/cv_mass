# %%
import numpy as np
import cv2
import matplotlib.pyplot as plt

# %%
def zoom_show_contour(image = None, contours = None, image_done = None, margin = 5):
    """
    Args:
        image: The original image. Use it to create a background of the same size.

        contours: some contour(s) to be zoomed and shown.

        image_done: An image that have been processed as binary. Directly zoom and show this image if it is not None. Previous parameters will be overridden.
        
        margin: If margin < 0, show the whole picture.

    Returns:
    """
    if image_done is not None:
        im_ran = image_done.max(axis = 2) if len(image_done.shape) == 3 else image_done
        
        points = [(x, y) for x in range(im_ran.shape[1]) for y in range(im_ran.shape[0]) if im_ran[y, x] > 0] # 注意，现在x是横轴
        points = np.array(points)
    else:
        contours = [contours] if type(contours) != list else contours
        image_done = cv2.drawContours(image = np.zeros_like(image), contours = contours, contourIdx = -1, color = 255, thickness = 1)

        points = np.array([point for cnt in contours for point in cnt.squeeze()])
        
    l, r = np.min(points[:, 0]) - margin, np.max(points[:, 0]) + margin
    u, d = np.min(points[:, 1]) - margin, np.max(points[:, 1]) + margin
    print(f'The boundary of this contour is from {(l, u)} to {(r, d)}.')
    
    if margin < 0:
        plt.imshow(image_done)
    else:
        plt.imshow(image_done[u:d, l:r])
    plt.show()

def zoom_show_ellipse(ellipse, ):
    """
    Args:
        ellipse: Parameters of an ellipse. From cv2.fitEllipse.

    """
    pass
# %%
