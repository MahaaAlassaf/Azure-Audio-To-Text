```markdown
# Azure Audio to Text Conversion

![Azure Audio to Text Conversion](https://user-images.githubusercontent.com/86031983/175003761-99ee51cf-9900-45de-af49-9465279eaa39.png)

This project demonstrates converting audio files into text using Azure Cognitive Services Speech SDK within a Flask web application integrated with Azure Speech API.

## Features

- **Upload Audio:** Allows users to upload audio files for conversion to text.
- **Speech-to-Text Conversion:** Uses Azure Cognitive Services Speech SDK to convert uploaded audio files to text.
- **User-Friendly Interface:** Simple and intuitive web interface for uploading and viewing conversion results.

## Technologies Used

- **Python:** Flask framework for backend development.
- **Azure Cognitive Services:** Speech SDK for speech-to-text conversion.
- **HTML/CSS:** Frontend templates using Bootstrap for styling.
- **Git:** Version control and collaboration using GitHub.

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

This installs Flask and Azure Cognitive Services SDK.

### Azure Cognitive Services Setup

1. Create a Speech service resource in Azure.
2. Obtain your API key and region.
3. Update `.env` file with your API key and region details:

   ```
   API_KEY=<your_azure_api_key>
   REGION=<azure_region>
   LANGUAGE=en-US
   ```

   Replace `<your_azure_api_key>` with your actual API key from Azure Cognitive Services and `<azure_region>` with the region where your service is hosted.

## Usage

1. Run the application:

   ```bash
   python app.py
   ```

2. Open `http://localhost:5000` in your web browser.
3. Upload an audio file.
4. Wait for the file to be processed.
5. View the converted text on the result page.
6. Download the text file if needed.

## Contributing

Contributions are welcome! Fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
```

Let me know if you need any further adjustments or additions!
