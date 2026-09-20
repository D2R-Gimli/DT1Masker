from pathlib import Path
import subprocess
import sys
import tempfile

import cairosvg
from PIL import Image


# ============================================================
# Configuration
# ============================================================

PROJECT_DIR = Path(__file__).resolve().parent

MAIN_SCRIPT = PROJECT_DIR / "DT1Masker.py"

APP_NAME = "DT1Masker"

DIST_DIR = PROJECT_DIR / "dist"
BUILD_DIR = PROJECT_DIR / "build"


# ============================================================
# Import the SVG master
# ============================================================

sys.path.insert(0, str(PROJECT_DIR))

from DT1Masker import SVG_ICON


# ============================================================
# Create temporary ICO from SVG
# ============================================================

def create_temporary_ico(svg_data):

    if isinstance(svg_data, str):
        svg_data = svg_data.encode("utf-8")

    # Temporary files are created in the project directory so
    # that PyInstaller can access them normally on Windows.

    temp_png = PROJECT_DIR / "__temp_icon.png"
    temp_ico = PROJECT_DIR / "__temp_icon.ico"

    try:

        # ----------------------------------------------------
        # Render SVG at high resolution
        # ----------------------------------------------------

        cairosvg.svg2png(
            bytestring=svg_data,
            write_to=str(temp_png),
            output_width=1024,
            output_height=1024,
        )

        # ----------------------------------------------------
        # Convert PNG to ICO
        # ----------------------------------------------------

        image = Image.open(
            temp_png
        ).convert("RGBA")

        image.save(
            temp_ico,
            format="ICO",
            sizes=[
                (16, 16),
                (24, 24),
                (32, 32),
                (48, 48),
                (64, 64),
                (128, 128),
                (256, 256),
            ],
        )

        return temp_ico

    finally:

        if temp_png.exists():
            temp_png.unlink()


# ============================================================
# Build
# ============================================================

def main():

    print()
    print("=" * 60)
    print(" DT1Masker PyInstaller Build")
    print("=" * 60)
    print()

    if not MAIN_SCRIPT.exists():
        print(
            f"ERROR: Could not find {MAIN_SCRIPT}"
        )
        sys.exit(1)

    print("Creating temporary ICO from embedded SVG...")

    temp_ico = create_temporary_ico(
        SVG_ICON
    )

    print(
        f"Temporary icon: {temp_ico.name}"
    )

    try:

        # ----------------------------------------------------
        # PyInstaller command
        # ----------------------------------------------------

        command = [
            sys.executable,
            "-m",
            "PyInstaller",

            "--noconfirm",
            "--clean",

            "--onefile",
            "--windowed",

            "--name",
            APP_NAME,

            "--icon",
            str(temp_ico),

            str(MAIN_SCRIPT),
        ]

        print()
        print("Running PyInstaller...")
        print()

        subprocess.run(
            command,
            check=True
        )

        print()
        print("=" * 60)
        print(" BUILD SUCCESSFUL")
        print("=" * 60)
        print()
        print(
            f"Executable: {DIST_DIR / (APP_NAME + '.exe')}"
        )
        print()

    finally:

        # ----------------------------------------------------
        # Delete temporary ICO
        # ----------------------------------------------------

        if temp_ico.exists():
            temp_ico.unlink()

            print(
                "Temporary ICO deleted."
            )


if __name__ == "__main__":
    main()