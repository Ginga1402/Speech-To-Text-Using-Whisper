import whisper
import torch
import os,numpy as np
from flask import Flask, request
# import streamlit as st
# from audio_recorder_streamlit import audio_recorder
import torch
# import numpy as np
import os

    

torch.cuda.is_available()
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using torch {torch.__version__} ({DEVICE})")


model = whisper.load_model("small", device=DEVICE)

print(
    f"whisper small Model is {'multilingual' if model.is_multilingual else 'English-only'} "
    f"and has {sum(np.prod(p.shape) for p in model.parameters()):,} parameters."
)



def transcription(audio_location: str, target_langauge : str):
    audio_file = audio_location
    targetlanguage = target_langauge
    transcription = model.transcribe(audio_file,language = targetlanguage)
    transcribed_text = transcription["text"]
    return transcribed_text



from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/transcribe', methods=['POST'])
def transcribe_audio_file():
    audio_path = request.json.get('audio_path')
    target_langauge = request.json.get('target_langauge')

    if not audio_path:
        return 'Error: Audio path not provided', 400

    if not os.path.exists(audio_path):
        return 'Error: Audio file not found', 404

    try:
        transcription_result = transcription(audio_location=audio_path,target_langauge=target_langauge)
        return {'transcription': transcription_result}
    except Exception as e:
        return f'Error: {str(e)}', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1402)


    
