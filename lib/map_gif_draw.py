import numpy as np
from PIL import Image
import base64
from IPython import display as dd


def make_track_arrays(point_list, map_array, v=5):
    map_arrays = []
    for p in point_list:
        array = map_array.copy()
        array[p.y][p.x] = v
        map_arrays.append(array)
    return map_arrays


def make_track_arrays_all(goal_list, map_array, max_track=30, v=5):
    map_arrays = []
    for i, point_list in enumerate(goal_list):
        if i >= max_track:
            break
        map_arrays += make_track_arrays(point_list, map_array, v)
    return map_arrays


def array_normalize(array: np.ndarray, max_v):
    array = array / max_v
    array *= 255
    return array.astype(np.uint8)


def array_to_img(array: np.ndarray, max_v=2, img_size=(64, 64)):
    img = Image.fromarray(array_normalize(array, max_v)).resize(img_size, Image.NEAREST).convert('P')
    return img


def arrays_to_gif(array_list,
                  save_path='sample.gif',
                  max_v=2,
                  img_size=(64, 64),
                  show=False,
                  duration=1000):
    images = [array_to_img(array, max_v, img_size) for array in array_list]
    images[0].save(save_path,
               save_all=True, append_images=images[1:], optimize=False, duration=duration, loop=0)
    if show:
        with open(save_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("ascii")

        display(dd.HTML(f'<img src="data:image/gif;base64,{b64}" />'))
