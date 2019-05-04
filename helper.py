import numpy as np
from PIL import Image
import math



def get_image(image_path, width, height, mode):
    """
    Read image
    :param image_path: path of image
    :param width: width of image
    :param height: height of image
    :param mode: image mode
    :return Image data
    """
    image = Image.open(image_path)
    
    return np.array(image.convert(mode))
   

def get_batch(images, width, height, mode):
    data_batch = np.array(
        [get_image(files, width, height, mode) for files in images]).astype(np.float32)

    # Make sure the images are in 4 dimensions
    if len(data_batch.shape) < 4:
        data_batch = data_batch.reshape(data_batch.shape + (1,))

    return data_batch


def images_to_grid(images, mode):
    # size of grid
    size = math.floor(np.sqrt(images.shape[0]))
    # scale 0 to 255 rgb color
    images = (((images - images.min()) * 255) / (images.max() - images.min())).astype(np.uint8)
    
    # arrange images in square
    images_in_square = np.reshape(
            images[:size * size],
            (size, size, images.shape[1], images.shape[2], images.shape[3]))
    
    if mode == 'L':
        images_in_square = np.squeeze(images_in_square, 4)
    
    new_im = Image.new(mode, (images.shape[1] * size, images.shape[2] * size))
    
    # combine images
    for col_i, col_images in enumerate(images_in_square):
        for image_i, image in enumerate(col_images):
            im = Image.fromarray(image, mode)
            new_im.paste(im, (col_i * images.shape[1], image_i * images.shape[2]))
            
    return new_im
            
    print(new_im, images.shape[1] * size)