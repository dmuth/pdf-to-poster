#!/usr/bin/env python

from PIL import Image
from pdf2image import convert_from_path

#
# Turn our PDF into tiles
#
def split_image_into_tiles(image, tile_size):

    retval = []
    width, height = image.size
    
    for top in range(0, height, tile_size[1]):
        for left in range(0, width, tile_size[0]):
            box = (left, top, left + tile_size[0], top + tile_size[1])
            tile = image.crop(box)
            retval.append(tile)

    return retval


#
# Smash our tiles together into a single PDF
#
def make_pdf_from_tiles(images, tile_width, tile_height, scale):

    retval = []

    tile_size = (tile_width, tile_height)

    for i, img in enumerate(images):
    
        print(f"Converting page {i+1}/{len(images)} at scale {scale}...")
        width = int(img.width * scale)
        height = int(img.height * scale)

        print(img)
        img = img.resize(( width, height ))
        print(img)

        #img.save("test.pdf")
        #img.save("test.png")
        
        # Split into tiles
        tiles = split_image_into_tiles(img, tile_size)
    
        retval.extend(tiles)
    
    return(retval)


#
# 150 DPI is good for basic printing
# The dimensions are for 8.5"x11" paper at that DPI.
#
dpi = 150
#tile_width = 1275
#tile_height = 1650
tile_width = 850
tile_height = 1100

filename = "source.pdf"
scale = 1

images = convert_from_path(filename, dpi = dpi)

tiles = make_pdf_from_tiles(images, tile_width, tile_height, scale)

tiles[0].save("output.pdf", save_all=True, append_images=tiles[1:], resolution=100.0, quality=95)

print("Done!")

#
# TODO:
# X Figure out image resizing bug
# X Figure out 8.5" x 11" pages
# - Figure out how to do borders
# - Doublecheck trying to print 8.5"x11", do I need to worry about padding
# - Figure out multi-page PDFs
# - Figure out how to do markings around borders


#from wand.image import Image as WImage


