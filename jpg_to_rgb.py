# convert_metal_jpgs_to_pixels.py
from PIL import Image
import numpy as np
from pathlib import Path
import sys

# Directory with JPGs (relative to script)
src_dir = Path(__file__).parent / "metal"

# Output directory for .npy pixel arrays
out_dir = Path(__file__).parent / "metal_pixels"
out_dir.mkdir(exist_ok=True)

if not src_dir.exists():
    print(f"Source directory not found: {src_dir}")
    sys.exit(1)

# Find jpg/jpeg files (case-insensitive)
jpg_files = sorted([p for p in src_dir.iterdir()
                    if p.suffix.lower() in {'.jpg', '.jpeg'}])

if not jpg_files:
    print(f"No .jpg/.jpeg files found in {src_dir}")
    sys.exit(0)

for p in jpg_files:
    try:
        with Image.open(p) as img:
            img = img.convert("RGB")            # ensure RGB
            arr = np.array(img)                # shape: (height, width, 3), dtype=uint8

        # Save as .npy using same base filename
        out_path = out_dir / (p.stem + ".npy")
        np.save(out_path, arr)
        print(f"Saved {p.name} -> {out_path.name}  (shape={arr.shape})")
    except Exception as e:
        print(f"Error processing {p.name}: {e}")
