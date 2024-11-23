# OCR App

## Overview

The **OCR App** is a web-based application built using Flask and Google Cloud's Document AI API. It allows users to upload image files (JPEG, PNG) containing text, which are then processed to extract the text using Optical Character Recognition (OCR) technology. The extracted text is displayed on the webpage and can also be downloaded as a JSON file.

## Features

- **File Upload**: Users can upload images in JPEG or PNG format.
- **OCR Processing**: The app uses Google Cloud's Document AI API to extract text from the uploaded images.
- **Multi-language Support**: The app supports OCR in English, Tamil, and Sinhala.
- **Text Display**: Extracted text is displayed on the webpage for the user to review.
- **JSON Export**: Users can download the extracted text as a JSON file.
- **Responsive Design**: The app is designed to be simple and responsive for easy use across devices.

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask
- **OCR Engine**: Google Cloud Document AI API
- **Cloud Hosting**: Google Cloud Platform (GCP)
- **Python Libraries**: 
  - Flask (Web framework)
  - Google Cloud Client (Document AI API)
  - Pillow (Image processing)
  - OpenCV (Image handling)

## Setup Instructions

### Prerequisites

1. **Google Cloud Platform Account**:
   - Sign up for a free GCP account.
   - Enable the **Document AI API** and set up a **Service Account** with the required roles (Document AI User, Storage Admin).
   - Download the service account JSON file for authentication.

2. **Local Environment**:
   - Install Python 3.x.
   - Install required libraries using the `requirements.txt` file.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dilukshashamal/Document-AI.git
   cd OCR_APP
