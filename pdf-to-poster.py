#!/usr/bin/env python

import argparse

from PIL import Image, ImageOps
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

            # Add in a border
            tile = ImageOps.expand(tile, border=1, fill="black")

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

        #print(img) # Debugging
        img = img.resize(( width, height ))
        #print(img) # Debugging

        #img.save("test.pdf") # Debugging
        #img.save("test.png") # Debugging
        
        # Split into tiles
        tiles = split_image_into_tiles(img, tile_size)
    
        retval.extend(tiles)
    
    return(retval)

def parse_args():
    parser = argparse.ArgumentParser(description="Tile a PDF into smaller pages with options for scale and size.")
    
    # Arguments
    parser.add_argument(
        "--input", type = str, default = "input.pdf",
        help = "The path to the input PDF file. Default is \"input.pdf\"."
    )
    parser.add_argument(
        "--output", type=str, default = "output.pdf",
        help = "The path to the output PDF file. Default is \"output.pdf\"."
    )
    parser.add_argument(
        "--width", type=int, default = 850,
        help = "Width of the tile in pixels. Default is 850 pixels (8.5\" x 11\" at 150 DPI)."
    )
    parser.add_argument(
        "--height", type=int, default = 1100,
        help = "Height of the tile in pixels. Default is 1100 pixels (8.5\" x 11\" at 150 DPI)."
    )
    parser.add_argument(
        "--scale", type=float, default = 1.0,
        help = "Scaling factor for the PDF. Default is 1.0 (no scaling)."
    )
    parser.add_argument(
        "--dpi", type=float, default = 150,
        help = "Dots per inch (DPI). Default is 150."
    )
    
    return parser.parse_args()


def main():

    args = parse_args()
    #print(f"DEBUG: {args}") # Debugging

    print(f"Tiling file {args.input} into {args.output} at {args.width} x {args.height} pixels at {args.dpi} DPI with a scale factor of {args.scale}")

    images = convert_from_path(args.input, dpi = args.dpi)

    tiles = make_pdf_from_tiles(images, args.width, args.height, args.scale)

    tiles[0].save(args.output, save_all=True, append_images=tiles[1:], 
        resolution=100.0, quality=95)

    print("Done!")


main()

