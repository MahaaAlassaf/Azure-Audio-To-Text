# Azure Audio to Text Conversion

This project converts audio files into text using Azure Cognitive Services Speech SDK within a Flask web application integrated with Azure Speech API.

## Features

- **Upload Audio:** Allows users to upload audio files for conversion to text.
- **Speech-to-Text Conversion:** Uses Azure Cognitive Services Speech SDK.
- **User-Friendly Interface:** Simple and intuitive web interface.

## Technologies Used

- **Python:** Flask framework.
- **Azure Cognitive Services:** Speech SDK.
- **HTML/CSS:** Bootstrap for styling.
- **Git:** Version control with GitHub.

## Installation

### Clone the repository

```bash
git clone https://github.com/MahaaAlassaf/Azure-Audio-To-Text.git
cd Azure-Audio-To-Text
```

### Install dependencies

Use `pip` to install required Python packages:

```bash
pip install -r requirements.txt
```

### Azure Cognitive Services Setup

1. Create a Speech service resource in Azure.
2. Obtain your API key and region.
3. Update `.env` file with your API key and region details:

   ```
   API_KEY=<your_azure_api_key>
   REGION=<azure_region>
   LANGUAGE=en-US
   ```

   Replace `<your_azure_api_key>` and `<azure_region>` with your actual API key and service region.

## Usage

1. Run the application:

   ```bash
   python app.py
   ```

2. Open `http://localhost:5000` in your browser.
3. Upload an audio file.
4. Wait for processing.
5. View converted text on the result page.
6. Download text file if needed.

## Contributing

Contributions welcome! Fork and submit a pull request.
