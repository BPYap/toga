from .libs import Color

CACHE = {}


def native_color(c):
    try:
        color = CACHE[c]
    except KeyError:
        # implementation of android.graphics.Color
        # encoding method: int color = (A & 0xff) << 24 | (R & 0xff) << 16 | (G & 0xff) << 8 | (B & 0xff);
        # decoding method : int A = (color >> 24) & 0xff; // or color >> > 24
        #                   int R = (color >> 16) & 0xff;
        #                   int G = (color >> 8) & 0xff;
        #                   int B = (color) & 0xff;

        # here we convert c into a single int value using encoding method described above
        color = (c.rgba.a & 0xff) << 24 | (c.rgba.r & 0xff) << 16 | (c.rgba.g & 0xff) << 8 | (c.rgba.b & 0xff)
        CACHE[c] = color
    return color
