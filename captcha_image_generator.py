import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import matplotlib.pyplot as plt

class CaptchaImageGerator:

    def __init__(self, width=150, height=50, fonts=None):
        self.width = width
        self.height = height
        self.fonts = fonts
        self.color = None
        self.background = None  

    def generate(self, text):

        self.color = self._random_color(10, 200, np.random.randint(220, 255))
        self.background = self._random_color(240, 255)

        image = Image.new('RGB', (self.width, self.height), color=self.background)

        image = self.add_noise(image)
        image = self.add_text(image, text)

        return image

    def add_noise(self, image):
        step = 5

        width, height = image.size
        number_of_pixels = np.random.randint(1000 , 1200)

        for n in range(step, width, step):
          for y in range(step, height, step):
            ImageDraw.Draw(image).point((n, y), fill=self.color)

        image = image.filter(ImageFilter.GaussianBlur(0.5))

        for i in range(number_of_pixels):
            y_1 = np.random.randint(0, height - 1)
            x_1 = np.random.randint(0, width - 1)
            ImageDraw.Draw(image).point((x_1, y_1), fill=self.color)

        return image


    def add_text(self, image, text):

        width, height = image.size
        image_text = Image.new('RGBA', (width , height), color=(255, 255, 255, 0))
        type_font = np.random.choice(self.fonts)
        font = ImageFont.truetype(type_font, 30)

        ascent, descent = font.getmetrics()
        font_width = font.getmask(text).getbbox()[2]
        font_height = font.getmask(text).getbbox()[3] + descent

        text_width = (width - font_width) / 2 + font_width / 2
        text_height = (height - font_height) / 2 + font_height / 2

        draw = ImageDraw.Draw(image_text)

        draw.text(
            (text_width, text_height),
            text,
            font=font,
            fill=self.color,
            anchor="ms"
        )

        image_text = self._rotate(image_text)

        image.paste(image_text, mask=image_text)

        return image

    def _rotate(self, image):

        width, height = image.size

        image = image.rotate(np.random.uniform(-15, 15), Image.BILINEAR, expand=1)
        dx = width * np.random.uniform(0.025, 0.25)
        dy = height * np.random.uniform(0.05, 0.25)
        x1 = int(np.random.uniform(-dx, dx))
        y1 = int(np.random.uniform(-dy, dy))
        x2 = int(np.random.uniform(-dx, dx))
        y2 = int(np.random.uniform(-dy, dy))
        w2 = width + abs(x1) + abs(x2)
        h2 = height + abs(y1) + abs(y2)
        data = (
            x1, y1,
            -x1, h2 - y2,
            w2 + x2, h2 + y2,
            w2 - x2, -y1,
        )

        image = image.resize((w2, h2))
        image = image.transform((width, height), Image.QUAD, data)

        return image.resize((width, height))

    def _random_color(self, start, end, opacity=None):

        red = np.random.randint(start, end)
        green = np.random.randint(start, end)
        blue = np.random.randint(start, end)

        if opacity is None:
            return (red, green, blue)

        return (red, green, blue, opacity)
