import argparse
import os
from image import Backround, Icon


parser = argparse.ArgumentParser(
  description='Icon Maker',
  formatter_class=argparse.MetavarTypeHelpFormatter
)

parser.add_argument('-c', '--color', type=str, default='#0A1423', help='background color (default: #0A1423)')
parser.add_argument('-r', '--radius', type=int, default=16, help='border radius (default: 16 px)')
parser.add_argument('-i', '--icon', type=str, default='', help='icon path')
parser.add_argument('-s', '--save', type=str, default='', help='save path')

if __name__ == '__main__':
  try:
    args = parser.parse_args()

    backround = Backround(args.color, (450, 450))
    backround.radius(args.radius)

    if args.icon != '':
      icon = Icon(args.icon)
      icon.resize((256, 256))

      top = (backround.height - icon.height) // 2
      left = (backround.width - icon.width) // 2

      backround.paste(icon.icon, (top, left))

    if args.save == '':
      args.save = os.path.join(os.path.join(os.path.expanduser('~'), 'Downloads'), 'icon.png')

    backround.save(args.save)

  except argparse.ArgumentError:
    raise Exception('Inquire ChatGPT')