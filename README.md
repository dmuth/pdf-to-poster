
# PDF to Poster

This app will go through a PDF page by page, scale up each page, and then tile that page across 
many pages.  Then you can print out the new PDF and take the individual pages together to
form a poster.


## Usage

`docker run dmuth1/pdf-to-poster -h`

Options are as follows:

```
usage: pdf-to-poster.py [-h] [--input INPUT] [--output OUTPUT] [--width WIDTH]
                        [--height HEIGHT] [--scale SCALE] [--dpi DPI]

Tile a PDF into smaller pages with options for scale and size.

options:
  -h, --help       show this help message and exit
  --input INPUT    The path to the input PDF file. Default is "input.pdf".
  --output OUTPUT  The path to the output PDF file. Default is "output.pdf".
  --width WIDTH    Width of the tile in pixels. Default is 850 pixels (8.5" x
                   11" at 150 DPI).
  --height HEIGHT  Height of the tile in pixels. Default is 1100 pixels (8.5"
                   x 11" at 150 DPI).
  --scale SCALE    Scaling factor for the PDF. Default is 1.0 (no scaling).
  --dpi DPI        Dots per inch (DPI). Default is 150.
```


## Development

- `./bin/docker-build.sh && ./bin/docker-dev.sh` 
  - This will spawn a shell in the dev docker contianer
  - The files from the parent host will be in `/mnt/`


## Notes and Bugs

- DPI is cursed.  I spent a lot of time struggling with it, and it looks like the DPI is actually
for the input document.  It's unclear what influences the DPI for the output document.  That means
that in order to the size you want, you may have to experment a little.  I apologize profusely for this
and if you have any resources, feel free to get in touch with me.


## Contact

- Email: **doug.muth AT gmail DOT com**
- ...or you can file an issue here in GitHub.




