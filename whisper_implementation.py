import whisper
import torch
import os,numpy as np
# from flask import Flask, request
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




# file = "Your File path"

# transcribe = transcription(audio_location=file, target_langauge="hindi")

# print("Transcription result:" , transcribe)
