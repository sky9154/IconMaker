# Icon Maker

A Python command-line tool for generating square icons with a custom background, rounded corners, and an optional foreground image.

## About

Icon Maker creates a 450×450 icon canvas and lets you customize its background color and corner radius.

You can optionally place an image in the center of the canvas. The foreground image is resized to 256×256 pixels before being composited onto the background.

The tool also supports an optional grayscale filter for the foreground image.

Image generation is handled with Pillow, while NumPy and OpenCV are used for grayscale processing.

## Features

- Create 450×450 square icons
- Set the background color with a hexadecimal color value
- Configure the corner radius
- Add a foreground icon image
- Resize the foreground image to 256×256 pixels
- Apply an optional grayscale filter to the foreground image
- Save the generated icon to a custom path
- Save to `~/Downloads/icon.png` when no output path is provided

## Getting Started

### Prerequisites

To run the source code, you need:

- Python 3
- pip

The project depends on:

- `Pillow`
- `NumPy`
- `OpenCV`

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/sky9154/IconMaker.git
cd IconMaker
```

**2. Install the required packages**

```bash
pip install pillow numpy opencv-python
```

### Usage

Run the tool with:

```bash
python main.py [options]
```

Available options:

```text
-c COLOR, --color COLOR
    Background color.
    Default: #0A1423

-r RADIUS, --radius RADIUS
    Corner radius in pixels.
    Default: 16

-i ICON, --icon ICON
    Path to the foreground icon image.

-s SAVE, --save SAVE
    Output path for the generated icon.
    Default: ~/Downloads/icon.png

-g, --gray
    Apply a grayscale filter to the foreground image.
```

### Example

```bash
python main.py -c "#FF5733" -r 20 -i my_icon.png -s my_custom_icon.png
```

This creates an icon with a `#FF5733` background, a corner radius of 20 pixels, and `my_icon.png` centered on the canvas. The result is saved as `my_custom_icon.png`.

To apply the grayscale filter:

```bash
python main.py -i my_icon.png -g
```

If no save path is specified, the generated image is saved as:

```text
~/Downloads/icon.png
```

## Project Structure

```text
IconMaker/
├── LICENSE
├── README.md
├── icon.ico
├── im.exe
├── image.py
└── main.py
```

- `main.py` defines the command-line interface and controls the icon generation workflow.
- `image.py` contains the background and foreground image processing logic.
- `im.exe` is the executable included in the repository.
- `icon.ico` is the icon file included with the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
