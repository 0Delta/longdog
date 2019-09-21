#!python3
# -*- coding: utf-8 -*-

import argparse
from PIL import Image
from libsixel.encoder import Encoder as SixelEncoder
from libsixel import SIXEL_OPTFLAG_WIDTH, SIXEL_OPTFLAG_HEIGHT, SIXEL_FORMAT_PNG
from tempfile import NamedTemporaryFile


def writesixel(img):
    with NamedTemporaryFile(prefix="sixel-") as fd:
        img.save(fd, format="PNG")
        fd.flush()
        w, h = img.size
        encoder = SixelEncoder()
        encoder.setopt(SIXEL_OPTFLAG_WIDTH, w)
        encoder.setopt(SIXEL_OPTFLAG_HEIGHT, h)
        encoder.encode(fd.name)


def writefile(path, img):
    try:
        open(path, mode="r")
        print("file is exist.")
        return
    except FileNotFoundError:
        pass
    except ... as exp:
        print("file open error")
        print(exp)
    with open(path, "wb") as f:
        img.save(f, format="PNG")


def main():
    parser = argparse.ArgumentParser(
        description="print long dog image.")
    parser.add_argument("-l", "--length", type=int,
                        help="dog length (default 6)", default=6)
    parser.add_argument("-f", "--file", type=str, help="write to file")
    args = parser.parse_args()

    length = args.length

    # 元画像の読み込み
    img1 = Image.open("./images/data01.png")
    img2 = Image.open("./images/data02.png")
    img3 = Image.open("./images/data03.png")
    w1, h1 = img1.size
    w2, _ = img2.size
    w3, _ = img3.size
    w1 -= 1
    w2 -= 1
    w3 -= 1
    rw = w1 + w2 * length + w3 + 1
    rh = h1 - 1
    rimg = Image.new('RGBA', (rw, rh))

    # write image
    for y in range(rh):
        for x in range(rw):
            if x < w1:
                color = img1.getpixel((x, y))
            elif rw - w3 < x:
                color = img3.getpixel((x-w1-(w2*length), y))
            else:
                color = img2.getpixel(((x-w1) % w2, y))

            rimg.putpixel((x, y), (color[0], color[1], color[2], color[3]))

    # printing
    if args.file is not None:
        writefile(args.file, rimg)
    else:
        writesixel(rimg)
    print()


if __name__ == "__main__":
    main()
