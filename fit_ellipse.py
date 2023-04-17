# %%
# corresponds to one section in 2_contour.ipynb
# %%
import numpy as np
import cv2
im = cv2.imread('pic/after_morpho.png', flags = cv2.IMREAD_GRAYSCALE)
# %%
for j in range(1, 4):
    cnt = np.loadtxt(fname = f'data/contour/cnt{j}.txt', dtype =np.int32)[:, np.newaxis, :]
    # sq_cnt_moveForward = np.delete(sq_cnt, obj = 0, axis = 0)
    print(j, cnt.shape)

    from Ellipse import valid_ellipse

    elps_set = []
    rep = 2000
    start_i = 1012
    for i in range(start_i, rep):
        l = len(elps_set)
        print(i + 1, l, l / (i + 1))
        selected_cols = np.random.default_rng(i).choice(cnt.shape[0], size = 6, replace = False)
        points = cnt.squeeze()[selected_cols, :]

        bkg = np.zeros_like(im, dtype = np.uint8)
        cv2.drawContours(bkg, contours = [points], contourIdx = 0, color = 127, thickness = 2)

        ellipse = cv2.fitEllipse(points)
        cv2.ellipse(bkg, ellipse, color = 127, thickness = 2) 

        # print(ellipse)

        cv2.drawContours(bkg, contours = [cnt], contourIdx = 0, color = 255, thickness = 2)    
        # zoom_show_contour(image_done = bkg, margin = 10)

        if valid_ellipse(ellipse, cnt):
            elps_set.append(ellipse)
        
            
    print(f'{len(elps_set)} ellipses are collected.')

    data = [[*e[0], *e[1], e[2]] for e in elps_set] # flatten
    np.savetxt(fname = f'data/ellipse/elps_cnt{j}_i={i}.txt', X = data)
# %%
