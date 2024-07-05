# Azure Audio-to-Text Converter

This project is a web application for converting audio files to text using Azure Cognitive Services Speech SDK. Users can upload audio files and receive the transcribed text output.

## Features

- **Upload Audio:** Users can upload audio files in various formats (MP3, WAV, etc.) for conversion.
- **Azure Cognitive Services:** Utilizes Azure Speech API for converting audio to text.
- **Download Text:** Option for users to download the transcribed text as a .txt file.
- **User Interface:** Simple and intuitive UI designed with Bootstrap for easy navigation and usage.

## Getting Started

To get started with this project, ensure you have Python 3.x installed. Then, install the project dependencies listed in `requirements.txt` by running:

```bash
pip install -r requirements.txt
```

This will install Flask, Azure Cognitive Services Speech SDK, and other necessary dependencies specified in `requirements.txt`.

**1. Clone the repository:**

```bash
git clone https://github.com/MahaaAlassaf/Azure-Audio-To-Text.git
cd Azure-Audio-To-Text
```

**2. Install dependencies:**

```bash
pip install -r requirements.txt
```

**3. Set up Azure Cognitive Services:**
- Sign up for Azure and create a Speech service resource.
- Obtain the API key and region information.
- Update `.env` file with your API key and region:

  ```
  API_KEY=your_api_key
  REGION=your_region
  LANGUAGE=en-US
  ```

**4. Run the application:**

```bash
python app.py
```
