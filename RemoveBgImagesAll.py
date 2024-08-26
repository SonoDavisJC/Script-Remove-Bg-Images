import os
from rembg import remove
from PIL import Image
import glob

directory = 'ImagesBg'
output_directory = 'ImagesNoBg'


# List of images from ImaBg folder
def list_files(dir):
    files_routes = glob.glob(os.path.join(dir, '*'))
    return [rt for rt in files_routes if os.path.isfile(rt)]


routes = list_files(directory)


# Remove Bg from image list
for rt in routes:

    # Load the original image
    input_image_path = rt

    # Get the image name without extension
    nameImage = os.path.splitext(os.path.basename(input_image_path))[0]

    # Image Output Path
    output_image_path = os.path.join(output_directory, f'{nameImage}NoBg.png')

    print(f'Image to change the background: {input_image_path}')

    # Open Image
    input_image = Image.open(input_image_path)

    # Remove Image
    output_image = remove(input_image)

    # Save image without Bg
    output_image.save(output_image_path)
    print(f"Image without background saved as {output_image_path}")