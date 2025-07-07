from PIL import Image
import pytesseract

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\user\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# Load image (make sure it's not in a protected folder)
img = Image.open("Screenshot 2025-06-27 114834.png")

# Extract text
text = pytesseract.image_to_string(img)

# Write to file in safe location
with open("Screenshot 2025-06-27 114834.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Done.")

