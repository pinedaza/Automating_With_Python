#!/usr/bin/env python3
import os
from PIL import Image


def reformat(image):
  im = Image.open(image)
  return im.rotate(90).resize((128,128))


def save_file(image, location, name):
  if image.mode != "RGB":
    image = image.convert("RGB")
  image.save("{}/{}.jpg".format(location, name))


if __name__ == "__main__":
  current_directory = os.getcwd()
  output_location = "/opt/icons"

  image_names = (image_name for image_name in os.listdir(current_directory))
  for image in image_names:
    if not image.endswith('48dp'):
      continue
    new_image = reformat(image)
    save_file(new_image, output_location, image)
  print('ran fine')
