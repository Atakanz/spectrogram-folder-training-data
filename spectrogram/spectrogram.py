import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np

FRAME_SIZE = 2048
HOP_SIZE = 512

def plot_spectrogram(path):
    data, sr = librosa.load(path, sr=None)

    stft = librosa.stft(
        data,
        n_fft=FRAME_SIZE,
        hop_length=HOP_SIZE
    )

    y_stft = np.abs(stft) ** 2
    y_log_stft = librosa.power_to_db(y_stft, ref=np.max)

    return y_log_stft, sr