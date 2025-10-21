# Motion Detection System

This project implements a real-time motion detection system using Python and OpenCV. It can detect and analyze motion in video streams, making it suitable for security monitoring and surveillance applications.

## Features

- Real-time motion detection
- Video frame processing and analysis
- Visual feedback with bounding boxes around detected motion
- Support for both webcam and video file input

## Installation

1. Clone this repository
2. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the main detection script:

```bash
python detection.py
```

Use different modes:

- Press 'q' to quit
- Press 'c' to clear the detection history
- Press 's' to save the current frame

## Project Structure

```
Detection/
├── detection.py     # Main motion detection implementation
├── utils/
│   └── draw.py     # Drawing utilities for visualization
├── config/
│   └── settings.py # Configuration settings
├── tests/          # Test files
└── requirements.txt
```

## Configuration

Modify `config/settings.py` to adjust detection sensitivity and other parameters.
<img width="100%" src="https://github.com/aryanedusomaiya/Crop-Disease-detection/blob/main/unnamed%20(1).png" alt="header-img" />
<img width="100%" src="https://github.com/aryanedusomaiya/Crop-Disease-detection/blob/main/unnamed.png" alt="header-img" />

## Requirements

- Python 3.7+
- OpenCV
- NumPy

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
