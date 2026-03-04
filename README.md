# Perceptual Hash Function (PHF) — Image Hashing & Comparison

## Pre-requisites
- Python 3.10+
- `imagehash`
- `PIL` (Pillow)
- `operator`
- `json`
- `\Images` folder containing `.jpg` images

## Files
- `PHF Hash Extractor.py`
- `PHF Comparison.py`

## Environment
Developed locally using **Python 3.12.3** and **VS Code**.  

## Description
These two scripts generate and compare **Perceptual Hash Function (PHF)** values to estimate the similarity between images.

- **`PHF Hash Extractor.py`**
  - Generates hash values for images and stores them in a JSON file.
- **`PHF Comparison.py`**
  - Compares a user-submitted image against precomputed hashes from a JSON hash library.
  - Outputs results using a predefined **Hamming distance** threshold.

## Usage

### `PHF Hash Extractor.py`
1. Ensure a folder named `\Images` exists in the **same directory** as the scripts.
2. Place the `.jpg` images you want to hash into `\Images`.
3. Run the script directly.
4. For the **first** image, you will be prompted to choose a hash type:
   - `A` = Average Hash
   - `P` = Perceptual Hash (pHash)
5. The same prompt will appear for **each** image in the `\Images` folder.
6. When complete, a JSON file named **`PHF_Hashes.json`** will be generated:
   - Hashes are stored by hash type.

### `PHF Comparison.py`
1. Ensure **`PHF_Hashes.json`** (or a JSON file of the same format) is in the **same directory** as the script.
2. Run the script directly.
3. The script is preconfigured with a **Hamming distance of 10**.
   - You can change this by editing the value on the **final line** of the script.
4. When run, you will be prompted to choose a `.jpg` image in the same directory as the script to compare against the JSON hash library.
5. The script will:
   - Compute **Average Hash** and **Perceptual Hash** for the selected image.
   - Search the hash library for an exact or similar match.
6. Output behaviour:
   - **Exact match**: prints that the same image has been found.
   - **Within threshold (≤ 10)**: prints the matched file info and the Hamming distance.
   - **No match**: prints **"No Matches Found"**.
