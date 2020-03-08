
from PIL import Image, ImageDraw, ImageFont
import random
import pathlib
import os

PROJECT_ROOT = pathlib.Path(__file__).parent.absolute()


class MemeEngine(object):
    """ Class for generating a Meme
        1. Loading input image using Pillow
        2. Drawing Quotes on the image at some random position
        3. Saving the image to given output location
        4. Return the output Location of generated meme
    """

    def __init__(self, out_path):
        """ Arguments:
                out_path {str} -- Location where meme will be saved
        """
        self.out_path = out_path

    def make_meme(self, img_path, text, author, width=500) -> str:
        """ Arguments:
                img_path {str} -- Input Image
                text {str} -- Quote Body
                author {str} -- Quote Author
                width {str} -- Output Meme width

            :return: width {str} -- Location of generated meme
        """
        try:
            if os.path.exists(self.out_path):
                img_out_path = os.path.join(self.out_path, f'meme_{random.randint(0, 100000000)}.png')
            else:
                os.mkdir(self.out_path)
                img_out_path = os.path.join(self.out_path, f'meme_{random.randint(0, 100000000)}.png')

            img = Image.open(img_path)

            if width is not None:
                ratio = width / float(img.size[0])
                height = int(ratio * float(img.size[1]))
                img = img.resize((width, height), Image.NEAREST)

            draw = ImageDraw.Draw(img)

            text_x = random.randint(10, 50)
            text_y = random.randint(30, 350)

            author_x = text_x + 30
            author_y = text_y + 30

            if text is not None:
                font = ImageFont.truetype(f'{PROJECT_ROOT}/fonts/LilitaOne-Regular.ttf', size=30)
                draw.text((text_x, text_y), text, font=font, fill='yellow')

            if author is not None:
                font = ImageFont.truetype(f'{PROJECT_ROOT}/fonts/LilitaOne-Regular.ttf', size=25)
                draw.text((author_x, author_y), "- " + author, font=font, fill='red')

            img.save(img_out_path)
            return img_out_path

        except Exception as e:
            raise Exception(f'Exception while Generating Meme for '
                            f'Image: {img_path}, Text: {text} and Author: {author} with Msg: {e}')
