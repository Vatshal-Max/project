# Age Prediction System

## Overview

The Age Prediction System is a real-time application that estimates a person's age based on facial images captured through a camera. Utilizing deep learning and image processing techniques, this system provides accurate age predictions, making it useful for various applications, such as security, marketing, and user engagement.

## Features

- **Real-Time Image Capture**: Capture live images using a webcam or camera feed.
- **Accurate Age Predictions**: Leverages convolutional neural networks (CNNs) trained on diverse datasets.
- **User-Friendly Interface**: Simple GUI for easy interaction and viewing of predictions.
- **Cross-Platform Compatibility**: Works on Windows, macOS, and Linux.

## Technology Stack

- **Programming Language**: Python
- **Libraries**: 
  - `OpenCV` for image processing
  - `TensorFlow`/`Keras` for machine learning
  - `Flask` or `Django` for the web interface (if applicable)

## Getting Started

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/rronak818/Age_Prediction.git
   cd age-prediction-system
2. **Install Dependencies**:
   - Create a virtual environment (optional but recommended) and activate it:
     ```bash
     python -m venv venv
     source venv/bin/activate #On Windows use .venv/Scripts/activate
    - Install required Libraries:
       ```bash
       pip insatll -r requirements.txt

## Model and Dataset

Both the model file and dataset are too large to be included in this repository. Here’s how to handle them:

Download Instructions
1. Dataset:
   - Download the dataset from `https://www.kaggle.com/code/shahraizanwar/age-gender-ethnicity-prediction/notebook`
   - Once downloaded, extract the files and place them in the data/ directory of the project.
2. Model File:
   - You will need to train your own model. Refer to the instructions below for training.

Training Your Own Model
1. Ensure the dataset is in the `data/` directory.
2. Run the training script:
   ```bash
   python main.ipynb

## Running the Application

1. Launch the Application:
   ```bash
   python age_gen.py

## Usage

- Start the application, and it will begin capturing images automatically.
- The predicted age will be displayed alongside the captured image.

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. 

### Acknowledgments

- OpenCV for image processing capabilities.
- TensorFlow for the machine learning framework.
- Contributors and community for support and inspiration.
