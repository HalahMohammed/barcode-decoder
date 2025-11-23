# Barcode-Decoder
A comprehensive Python-based solution for decoding 1D barcodes and 2D codes using MVTec Halcon. This application supports both image file processing and live camera acquisition for real-time code detection.

# Supported Code Types
## 1D Barcodes:

- Code 39

- Code 93

- Code 128

- 2D Codes:

## Data Matrix ECC 200

-QR Code

-GS1 DataMatrix

## Installation 

MVTec Halcon with Python interface installed

Python 3.6 or higher

Webcam (for camera functionality)

## Quick Start
```python
from decoder import process_image_file
```
# Process an image
```python
 barcode_results, code2d_results = process_image_file('path/to/your/image.jpg')
```
