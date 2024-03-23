# Icon Maker

This is a simple command-line tool for creating icons with customizable background color, border radius, and icon image.

## Usage

```
im [-h] [-c COLOR] [-r RADIUS] -i ICON [-s SAVE]
```

### Arguments

* `-h`, `--help`: Show help message and exit.
* `-c COLOR`, `--color COLOR`: Specify background color in hexadecimal format (default: #0A1423).
* `-r RADIUS`, `--radius RADIUS`: Specify border radius in pixels (default: 16 px).
* `-i ICON`, `--icon ICON`: Path to the icon image (required).
* `-s SAVE`, `--save SAVE`: Specify the path to save the generated icon image. If not provided, it will be saved in the 'Downloads' directory with the filename 'icon.png'.

## Example

```
im -c '#FF5733' -r 20 -i my_icon.png -s my_custom_icon.png
```

This command will create an icon with a background color of #FF5733, border radius of 20 pixels, using the image 'my_icon.png' as the icon, and save the generated icon as 'my_custom_icon.png'.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
