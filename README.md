# Image Encryption Tool

A simple Python GUI application that encrypts and decrypts images using pixel manipulation. The application allows users to select an image, apply encryption with a secret key, preview the result, and save the processed image.

---

## Features

- Browse and select image files (JPG, PNG, BMP)
- Encrypt images using a secret key
- Decrypt images using the same secret key
- Live image preview inside the GUI window
- Save encrypted and decrypted images

---

## How It Works

Every digital image is made up of pixels. Each pixel contains three color values:

- **Red (R):** 0–255
- **Green (G):** 0–255
- **Blue (B):** 0–255

---

## Code Explanation

- `Image.open()` opens the selected image.
- `img.load()` loads the pixel data for manipulation.
- `(value + key) % 256` encrypts each RGB value.
- `(value - key) % 256` decrypts each RGB value.
- `filedialog.asksaveasfilename()` allows the user to choose where to save the output image.

---

## Technologies Used

- Python 3.13
- Tkinter (GUI)
- Pillow 12.2.0

---

## How to Run

### 1. Install the required library

```bash
py -m pip install Pillow
```

### 2. Open the project

Open `Image Encryption.py` in IDLE or any Python IDE.

### 3. Run the program

1. Select an image.
2. Enter a secret key.
3. Click **Encrypt** or **Decrypt**.
4. Save the output image.

---
## Example

Original Pixel:
(100, 150, 200)

Secret Key:
50

Encrypted Pixel:
(150, 200, 250)

Decrypted Pixel:
(100, 150, 200)
