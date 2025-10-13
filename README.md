Image to ASCII Art Converter

A Python GUI tool that converts images into ASCII art using a pixelation-based brightness mapping. Built with `customtkinter` for an interactive interface.

---

## Features

- Select any image file from your computer
- Adjustable quality/pixelation via slider (10–80)
- Converts image to ASCII characters based on brightness
- Supports shading levels: ░ ▒ ▓ █
- Saves output as `output.txt` on desktop
- Automatically opens ASCII output after conversion
- Lightweight, responsive GUI

---

## How to Use

1. Run the program:
```bash
python <script_name>.py
````

2. Adjust the **Quality** slider to control ASCII resolution.
3. Click **Select File** to open an image.
4. The program generates ASCII art and saves it as `output.txt` on your desktop.
5. The output file opens automatically for viewing.

---

## Requirements

* Python 3.x
* Packages:

  * `customtkinter`
  * `Pillow` (`PIL`)
* Optional: `os`, `shutil`, `time`, `threading` (standard library)

Install dependencies with:

```bash
pip install customtkinter pillow
```

---

## Notes

* Higher quality values produce smaller ASCII representations (more pixelated).
* Shading is determined by brightness averaging of RGB values.
* Only RGB images are supported; other modes are converted automatically.
* Output file is overwritten on each conversion.
