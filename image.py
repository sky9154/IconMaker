from PIL import Image, ImageDraw
import numpy as np
import cv2


class Backround:
  def __init__(self, color: str, size: tuple[int, int]) -> None:
    self.color = color
    self.width = size[0]
    self.height = size[1]
    self.background = Image.new('RGB', size, color)

  def paste(self, icon: Image, box: tuple[int, int]):
    self.background.paste(icon, box, icon)

  def radius(self, radius: int) -> None:
    background = Image.new('RGBA', self.background.size, (255, 255, 255, 0))

    mask = Image.new('L', self.background.size, 255)
    draw = ImageDraw.Draw(mask)

    draw.rectangle([(0, 0), self.background.size], fill=0)
    draw.rounded_rectangle([(0, 0), self.background.size], radius * 2, fill=255)

    background.paste(self.background, (0, 0), mask)
    self.background = background

  def save(self, path: str) -> None:
    self.background.save(path)

class Icon:
  def __init__(self, path: str) -> None:
    self.path = path
    self.icon = Image.open(path)
    self.width = 0
    self.height = 0

  def resize(self, size: tuple[int, int]) -> None:
    self.icon = self.icon.resize(size)
    self.width = size[0]
    self.height = size[1]

  def grayscale_filter(self) -> None:
    gray_image = cv2.cvtColor(np.array(self.icon), cv2.COLOR_BGR2GRAY)
    self.icon = Image.fromarray(gray_image)