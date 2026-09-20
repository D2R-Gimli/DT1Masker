# DT1Masker

**DT1Mask Creator / Decoder for Diablo 2 Modding**

[![License: OCL v1.1 + SWAtt v1](https://img.shields.io/badge/license-OCL%20v1.1%20%2B%20SWAtt%20v1-blue)](LICENSE)
![Python](https://img.shields.io/badge/python-3.10%2B-3776AB?logo=python&logoColor=white)
![GUI](https://img.shields.io/badge/GUI-PySide6-41CD52)

DT1Masker converts between a list of DT1 files and the single `Dt1Mask` number used by Diablo 2 modding tools. Pick the files you want and get the mask, or paste a mask and see which files it stands for. Everything updates live as you type or click.

<img width="700" height="634" alt="screenshot" src="https://github.com/user-attachments/assets/54a1b6de-3612-473e-b66f-a14f68efb296" />


## Features

- **Files → Dt1Mask:** type file numbers or click them in the selector, and the mask is calculated instantly.
- **Dt1Mask → Files:** enter a mask and the matching DT1 files light up.
- **Visual file selector** for File 1 through File 32, with *Select All*, *Clear All* and *Invert Selection*.
- **One-click Copy** buttons for both results.
- **Flexible input:** `1,5,6,12`, `File 1, File 5, File 6, File 12` and `1 5 6 12` all work.
- **Input validation** with clear error messages for out-of-range files and masks.
- **Two versions:** a desktop app (Python / PySide6) and a single-file browser version that needs no installation.

## How the Dt1Mask works

The mask is a 32-bit number in which each DT1 file is one bit. File *N* has the value 2<sup>N−1</sup>, and the mask is the sum of all selected files.

| File | Value | | File | Value |
|-----:|------:|-|-----:|------:|
| 1 | 1 | | 17 | 65,536 |
| 2 | 2 | | 18 | 131,072 |
| 3 | 4 | | 19 | 262,144 |
| 4 | 8 | | 20 | 524,288 |
| 5 | 16 | | 21 | 1,048,576 |
| 6 | 32 | | 22 | 2,097,152 |
| 7 | 64 | | 23 | 4,194,304 |
| 8 | 128 | | 24 | 8,388,608 |
| 9 | 256 | | 25 | 16,777,216 |
| 10 | 512 | | 26 | 33,554,432 |
| 11 | 1,024 | | 27 | 67,108,864 |
| 12 | 2,048 | | 28 | 134,217,728 |
| 13 | 4,096 | | 29 | 268,435,456 |
| 14 | 8,192 | | 30 | 536,870,912 |
| 15 | 16,384 | | 31 | 1,073,741,824 |
| 16 | 32,768 | | 32 | 2,147,483,648 |

**Example:** Files 1, 5, 6 and 12 give 1 + 16 + 32 + 2048 = **2097**.

Valid masks range from `0` (no files) to `4,294,967,295` (all 32 files). The mask is entered and displayed as a decimal number.

## Getting started

### Option 1: Browser version (no install)

`DT1Masker.html` is a single self-contained file with no external dependencies.

- **Locally:** download it and open it in any modern browser.
- **Online:** if the repository has GitHub Pages enabled, it is available at  
  https://d2r-gimli.github.io/DT1Masker/DT1Masker.html

### Option 2: Desktop app (Python)

Requires **Python 3.10 or newer**.

```bash
# 1. Clone the repository
git clone https://github.com/D2R-Gimli/DT1Masker.git
cd DT1Masker

# 2. (Optional) create a virtual environment
python -m venv .venv
# Windows:      .venv\Scripts\activate
# Linux/macOS:  source .venv/bin/activate

# 3. Install the dependency
pip install -r requirements.txt

# 4. Run
python DT1Masker.py
```

The only dependency is [PySide6](https://pypi.org/project/PySide6/). The application icon is embedded in the script as SVG, so no extra image files are needed.

### Building a standalone `.exe` (optional)

You can package the desktop app with [PyInstaller](https://pyinstaller.org/):

```bash
pip install pyinstaller cairosvg pillow
python build.py
```

The executable will appear in the `dist/` folder and will have like 40Mb.

## Usage

1. **Files → Dt1Mask:** type file numbers into the input box (or click files in the *DT1 File Selector*). The Dt1Mask appears below. Use **Copy** to copy it.
2. **Dt1Mask → Files:** enter a mask value. The matching files are highlighted in green in the selector and listed below. Use **Copy** to copy the list.
3. Use **Select All**, **Clear All** or **Invert Selection** to change many files at once.

## Project files

| File | Description |
|------|-------------|
| `build.py` | For Compiling an .Exe |
| `DT1Masker.py` | Desktop application (Python / PySide6) |
| `DT1Masker.html` | Standalone browser version |
| `DT1Masker_version.txt` | Version infos |
| `requirements.txt` | Python dependencies |
| `LICENSE` | License terms (OCL v1.1 + SWAtt v1) |

## License

Copyright © 2026 GimliHC

DT1Masker is licensed under **OCL v1.1 + SWAtt v1** ([Open Community License](https://github.com/OpenCommunityLicence/OpenCommunityLicence) v1.1 with the [Software Attribution](https://github.com/OpenCommunityLicence/OpenCommunityLicence/blob/main/addons/SWAtt-v1.md) v1 add-on). See [LICENSE](LICENSE) for the full text.

In short:

- ✅ You may use, copy, modify and share DT1Masker for **non-commercial** purposes.
- ✅ Derivatives must stay under **OCL v1.1 + SWAtt v1** and keep **GimliHC** credited as the original creator, in both the source code and the user interface.
- ❌ You may not sell or otherwise commercially exploit DT1Masker or its derivatives without a separate license.

This summary is not a substitute for the license text. If in doubt, the [LICENSE](LICENSE) file applies.
