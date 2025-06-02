# xibrav_converter

A Python wrapper for the Xibrav video conversion API.

## Features
- Supports MP3 and MP4 conversion formats
- Easy to use

## Usage

```python
from xibrav_converter import XibravConverter

converter = XibravConverter()
result = converter.convert("2gIeTNufbIs", "mp3")
print(result)
