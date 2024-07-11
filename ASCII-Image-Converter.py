from PIL import Image

def image_to_ascii_convert(image, scale):

    # Load full image
    img = Image.open(image)
    h, w = img.size

    # Resize image to desired scale
    img = img.resize((h//scale, w//scale))

    # Load rescaled image
    h, w = img.size
    pix = img.load()

    # Set up grid, initialise all empty spots as X's to change to different ASCII pixels
    grid = []

    for height in range(h):
        grid.append(["X"] * w)

    # Loop to change grid's X's to ASCII pixels

    for height in range(h):
        for width in range(w):
            
            if sum(pix[height, width]) == 0:
                grid[height][width] = "-"
            if 1 <= sum(pix[height, width]) <= 100:
                grid[height][width] = "+"
            if 101 <= sum(pix[height, width]) <= 200:
                grid[height][width] = "="
            if 201 <= sum(pix[height, width]) <= 300:
                grid[height][width] = "%"
            if 301 <= sum(pix[height, width]) <= 400:
                grid[height][width] = "$"
            if 401 <= sum(pix[height, width]) <= 500:
                grid[height][width] = "#"
            if 501 <= sum(pix[height, width]) <= 600:
                grid[height][width] = "!"
            if 601 <= sum(pix[height, width]) <= 700:
                grid[height][width] = "@"
            if sum(pix[height, width]) >= 701:
                grid[height][width] = "?"

    with open("ImagetoASCII.txt",'r+') as file:
        file.truncate(0)

        for height in grid:
            file.write(f'{"".join(height)}\n')

    print("Completed")

image = 'amogus.jpg'

image_to_ascii_convert(image, 2)




        


