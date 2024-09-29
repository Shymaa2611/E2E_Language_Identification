import numpy as np
import librosa
from tensorflow.keras.models import load_model


def load_model():
    model = load_model('API/Model/model.h5')
    return model


def extract_mfcc(audio_path, max_pad_len=100):
    audio, sr = librosa.load(audio_path, mono=True)
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
    pad_width = max_pad_len - mfccs.shape[1]
    mfccs = np.pad(mfccs, pad_width=((0, 0), (0, pad_width)), mode='constant')
    return mfccs

