# Azure Audio-to-Text Converter

This project demonstrates a web application for converting audio files to text using Azure Cognitive Services Speech SDK. Users can upload audio files or record audio directly on the website and receive the transcribed text output.

## Features

- **Upload Audio:** Users can upload audio files in various formats (MP3, WAV, etc.) for conversion.
- **Record Audio:** Integrated functionality to record audio directly on the web interface.
- **Azure Cognitive Services:** Utilizes Azure Speech API for converting audio to text.
- **Download Text:** Option for users to download the transcribed text as a .txt file.
- **User Interface:** Simple and intuitive UI designed with Bootstrap for easy navigation and usage.

## Requirements

Ensure you have the following installed:

- Python 3.x
- Flask (`pip install Flask`)
- Azure Cognitive Services Speech SDK (`pip install azure-cognitiveservices-speech`)

For other dependencies, refer to `requirements.txt`.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/MahaaAlassaf/Azure-Audio-To-Text.git
   cd Azure-Audio-To-Text
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up Azure Cognitive Services:
   - Sign up for Azure and create a Speech service resource.
   - Obtain the API key and region information.
   - Update `.env` file with your API key and region:

     ```
     API_KEY=your_api_key
     REGION=your_region
     LANGUAGE=en-US
     ```

4. Run the application:

   ```bash
   python app.py
   ```

5. Open your web browser and go to `http://localhost:5000` to use the application.

## Usage

- **Upload Page:** Navigate to `http://localhost:5000/upload` to upload an audio file or record audio.
- **Result Page:** After uploading or recording, view the transcribed text on `http://localhost:5000/result`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This README.md file now includes the revised Requirements section and a License section, which is standard practice for open-source projects. Adjust the `LICENSE` link accordingly if you have a specific LICENSE file in your project repository.
