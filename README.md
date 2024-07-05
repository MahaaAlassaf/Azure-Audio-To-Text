Certainly! Here's the revised README.md text with the technologies discussed after the features section:

---

# Azure Audio to Text Conversion

Convert audio files into text using Azure Cognitive Services Speech SDK within a Flask web application integrated with Azure Speech API.

## Features

- **Upload Audio:** Easily upload audio files for conversion to text.
- **Speech-to-Text Conversion:** Utilizes Azure Cognitive Services Speech SDK for accurate transcription.
- **User-Friendly Interface:** Simple web interface for seamless user experience.

## Technologies Used

- **Python:** Utilizes Flask, a Python web framework, for backend development.
- **Azure Cognitive Services:** Speech SDK for converting speech into text.
- **HTML/CSS:** Bootstrap framework for responsive and intuitive web interface design.
- **Git:** Version control and collaboration using GitHub.

## How to Use

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MahaaAlassaf/Azure-Audio-To-Text.git
   cd Azure-Audio-To-Text
   ```

2. **Install dependencies:**

   Use `pip` to install required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Azure Cognitive Services Setup:**

   - Create a Speech service resource in Azure.
   - Obtain your API key and region.
   - Update `.env` file with your API key and region details:

     ```
     API_KEY=<your_azure_api_key>
     REGION=<azure_region>
     LANGUAGE=en-US
     ```

     Replace `<your_azure_api_key>` and `<azure_region>` with your actual API key and service region.

### Usage

1. **Run the application:**

   ```bash
   python app.py
   ```

2. **Access the web application:**

   Open `http://localhost:5000` in your browser.

3. **Upload an audio file:**

   - Select an audio file for conversion.
   - Wait for the file to be processed.

4. **View and download the converted text:**

   - Once processed, view the converted text on the result page.
   - Download the text file if needed.

## Contributing

Contributions are welcome! Fork the repository and submit a pull request with your enhancements.

---

This structure ensures that users understand the project's capabilities and technologies used, followed by clear instructions on how to install, use, and contribute to the project.
