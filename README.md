# **🎙️ Voice2Text: Seamless Speech Transcription with OpenAI Whisper**

### **Convert Your Voice Into Text with Ease – Powered by Whisper and Flask**


## **📌 Project Description**
Voice2Text is a simple yet powerful Python-based application that transcribes spoken audio into text using OpenAI’s Whisper model. Whether you're working on a voice assistant, automating meeting transcriptions, or just need fast and accurate speech-to-text conversion – this project has you covered.

This repository offers both a function-level implementation and a RESTful API using Flask, allowing you to integrate voice transcription into your Python apps or web-based services effortlessly. The transcription supports multiple languages and can be adjusted to use different Whisper model sizes based on performance and resource availability (default is small).

---

## **🛠️ Project Structure**

```
Speech-To-Text-Using-Whisper/
├── whisper_implementation.py
├── whisper_api.py
├── requirements.txt
├── outputs/
│   └── (transcription files will be saved here)
└── README.md
```

## **💡 Use Case**

#### Build voice-driven applications

1. Automate transcription of voice notes, podcasts, or interviews

2. Convert multilingual speech into text

3. Use as a backend service for AI-powered assistants or accessibility tools


## **Installation Instructions**

Follow these simple steps to get the Voice to Text functionality running on your local machine:

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/Ginga1402/Speech-To-Text-Using-Whisper.git
    ```
2. Navigate into the project directory:
    ```bash
    cd Speech-To-Text-Using-Whisper
    ```
3. Set up a virtual environment (recommended for Python projects):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
    ```
4. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```



## **Usage**

After the installation, you can use the provided scripts to convert Voice to Text.

### 1. **whisper_implementation.py**


```bash
python whisper_implementation.py
```

This will take a provided voice input and convert it's speech to text.

### 2. **whisper_api.py**


```bash
python whisper_api.py
```
Flask API that converts provided voice input to text using OpenAI's Whisper and handles requests asynchronously.


## **Technologies Used**
   
### This repository includes implementations of Text-to-Speech using the following technologies:

1. Python
2. OpenAI Whisper (small)
3. PyTorch
4. Flask

## **Contributing**
Contributions to this project are welcome! If you have ideas for improvements, bug fixes, or new features, feel free to open an issue or submit a pull request.

## **License**
This project is licensed under the MIT License - see the LICENSE file for details.

---



---







--- 

```
