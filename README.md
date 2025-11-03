# Image to ASCII Art

A **Python GUI tool** that converts images into ASCII art. Users can select an image file, adjust the quality, and generate a text-based ASCII representation of the image directly on their Desktop. The application uses **CustomTkinter** for a modern interface and **Pillow** for image processing.

---

## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [Installation](#installation)
- [Mechanics & Design](#mechanics--design)
- [Author](#author)

---

## Features

- **Select image files** via an intuitive GUI.
- Adjust **conversion quality** using a slider.
- Convert images to ASCII art with shading for depth.
- Output automatically saved to Desktop as `output.txt`.
- **Immediate viewing**: Opens the generated file automatically.
- Lightweight and easy to extend with custom shading or effects.

---

## Usage

1. Run the program:
```bash
python main.py
````

2. Use the slider to select the desired **quality** (higher numbers = lower resolution ASCII).
3. Click **Select File** to open an image.
4. The program generates an ASCII version of the image and opens `output.txt` on your Desktop.

> Darker areas are represented with dense characters (`█`, `▓`) and lighter areas with lighter characters (`░`, `▒`) for a visual gradient effect.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/thisisavoiid/Image-To-ASCII-Art-Converter.git
```

2. Navigate into the project folder:

```bash
cd Image-To-ASCII-Art-Converter
```

3. Install dependencies:

```bash
pip install customtkinter pillow
```

4. Run the program:

```bash
python main.py
```

---

## Mechanics & Design

* **Image Processing**:

  * Opens the selected image using **Pillow**.
  * Converts image to **RGB** and rescales based on the quality slider.
  * Calculates **brightness per pixel** and maps it to ASCII characters.
* **ASCII Mapping**:

  * Brightness levels mapped to characters: `░`, `▒`, `▓`, `█`.
  * Creates a visually coherent representation of the original image.
* **GUI System**:

  * Built with **CustomTkinter** for a modern look.
  * Slider for quality, button for file selection, and label showing current value.
* **Output**:

  * Writes ASCII art to `output.txt` on Desktop.
  * Automatically opens the text file for user convenience.

---

## Author

**Jonathan Huber** – Developed as part of a Python GUI project for creative image manipulation.

---

> Made with ❤️ in Python
