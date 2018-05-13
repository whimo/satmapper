import math


def deg2num(lat_deg, lon_deg, zoom=16):
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    return xtile, ytile


def num2deg(xtile, ytile, zoom=16):
    n = 2.0 ** zoom
    lon_deg = xtile / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
    lat_deg = math.degrees(lat_rad)
    return lat_deg, lon_deg


def pix2deg(x, y, abs_tile_x, abs_tile_y):
    xtile = abs_tile_x + x / 256
    ytile = abs_tile_y + y / 256
    return list(num2deg(xtile, ytile))


def img2list(img, abs_tile_x, abs_tile_y):
    for i in range(len(img)):
        for j in img[i]:
            if img[i][j] == 1:
                yield pix2deg(i, j, abs_tile_x, abs_tile_y)
