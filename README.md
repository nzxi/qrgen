# qrGEN

qrGEN is a lightweight terminal utility for generating QR codes without leaving the command line. It lets you encode URLs or arbitrary text, `mailto:` links, and telephone numbers, then saves the resulting image as a PNG file.

## Features

- Interactive CLI with a simple numbered menu.
- Generates QR codes for:
  - URLs or free-form text.
  - Email links (`mailto:`).
  - Phone numbers (`tel:`).
- Normalizes the output filename and ensures a `.png` extension.
- Cross-platform screen clearing (Windows, macOS, Linux).

## Prerequisites

- Python 3.8 or newer.
- The [`qrcode`](https://pypi.org/project/qrcode/) package (installs Pillow for image generation):

  ```bash
  pip install qrcode[pil]
  ```

## Running the CLI

From the project directory:

```bash
python gen.py
```

You'll see an ASCII banner and a menu similar to:

```
1. Default QR(URL)
2. Mail QR
3. Phone number QR
4. Exit
```

Choose an option, provide the requested data (URL, email, or phone number), then supply a filename when prompted. If you omit the `.png` suffix, qrGEN adds it automatically. The generated QR code is saved in the current working directory.

## Output

Each QR code is written as a PNG file. After saving, the program confirms the exact filename so you can open or share it immediately.

## License

This project is distributed under the terms of the MIT License. See `LICENSE` for details.
