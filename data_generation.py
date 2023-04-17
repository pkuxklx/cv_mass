# %%
import numpy as np
# %%
def get_data_from_contour(contour, draw: bool = False, seed: int = None):
    """
    This function returns a data matrix $X$ from a contour. $X$ is later used to fit an ellipse.

    Args:
        contour: a contour from cv2.findContours.

    Returns:
        X: data matrix.
    """
    assert contour.shape[1:] == (1, 2) and contour.shape[0] >= 6
    cnt = contour.squeeze()
    X = np.empty(shape = (len(cnt), 6))
    X[:, 0:2] = cnt * cnt
    X[:, 2] = np.prod(cnt, axis = 1)
    X[:, 3:5] = cnt
    X[:, 5] = 1
    if not draw:
        return X
    rng = np.random.default_rng(seed) # if seed is None, then random
    selected_cols = rng.choice(X.shape[0], size = 6, replace = False)
    return X[selected_cols, :]

if __name__ == '__main__':
    pass

# %%

# %%
seed = None
rng = np.random.RandomState(seed) if seed else np.random
# %%
a = ((1,2),(3,4),5)
x,y,b,a,z = **a
# %%
