from glob import glob
from PIL import Image, ImageOps
import ipdb


def image_grid(imgs, rows, cols):
    assert len(imgs) == rows*cols

    w, h = imgs[0].size
    grid = Image.new('RGB', size=(cols*w, rows*h))
    grid_w, grid_h = grid.size

    for i, img in enumerate(imgs):
        grid.paste(img, box=(i%cols*w, i//cols*h))
    return grid


def center_crop(image, new_width, new_height):
    width, height = image.size

    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2

    # Crop the center of the image
    image = image.crop((left, top, right, bottom))
    return image


def pad(image, delta_w=10, delta_h=10, fill=(255, 255, 255)):
    padding = (delta_w//2, delta_h//2, delta_w-(delta_w//2), delta_h-(delta_h//2))
    return ImageOps.expand(image, padding, fill=fill)


imgs = []
for i, p in enumerate(glob('qualitative_results_*/*/*JPEG')):
    img = center_crop(Image.open(p), 300, 300)
    if i % 3 == 0:
        #img = pad(img, fill=(255, 0, 0))
        img = pad(img, fill=(255, 255, 255))
    else:
        img = pad(img, fill=(255, 255, 255))
    img = img.resize((200, 200))
    imgs.append(img)

grid = image_grid(imgs[:18], rows=3, cols=6)
#grid.save('colored_grid.png')
grid.save('grid.png')


