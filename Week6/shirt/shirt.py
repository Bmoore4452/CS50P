import sys, os.path
from PIL import Image, ImageOps


def main():
    file_type = (".jpg", ".jpeg", ".png")

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) >= 4:
        sys.exit("Too many command-line arguments")
    if not os.path.isfile(sys.argv[1]):
        sys.exit("Input does not exit")
    if sys.argv[2].endswith(file_type) == False:
        sys.exit("Invalid output")
    if len(sys.argv) == 3:
        first = os.path.splitext(sys.argv[1])
        second = os.path.splitext(sys.argv[2])
    if first[1] != second[1]:
        sys.exit("Input and output have different extensions")
    else:
        before = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        size = shirt.size
        im = Image.new("RGB", size)
        before = ImageOps.fit(before, size, Image.Resampling.BICUBIC, 0.0, (0.5, 0.5))
        im.paste(before)
        im.paste(shirt, shirt)
        im.save(sys.argv[2])


if __name__ == "__main__":
    main()
