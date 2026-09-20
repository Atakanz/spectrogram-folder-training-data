import librosa
import librosa.display
import IPython.display as ipd
import subprocess
import matplotlib.pyplot as plt
from scipy.stats import alpha
import numpy as np

classical_file = "classical.00083.wav"
disco_file = "disco.00001.wav"
pop_file = "pop.00076.wav"

classical, sr = librosa.load(classical_file, sr=None)
disco, sr = librosa.load(disco_file, sr=None)
pop, sr = librosa.load(pop_file, sr=None)

sample_duration = 1 / sr
print(f"Duration of 1 sample is :{sample_duration:.6f} seconds")
duration = sample_duration * len(classical)
print(f"Duration of the song :{duration:.6f} seconds")


FRAME_SIZE = 1024
def amplitude_envelope(signal, frame_size):
    amplitude_envelope = []
    for i in range(0, len(signal), frame_size):
        current_frame_amplitude_envelope = max(signal[i:i + frame_size])
        amplitude_envelope.append(current_frame_amplitude_envelope)
    return np.array(amplitude_envelope)

ae_classical = amplitude_envelope(classical, FRAME_SIZE)
ae_disco = amplitude_envelope(disco, FRAME_SIZE)
ae_pop = amplitude_envelope(pop, FRAME_SIZE)

frames_cl = range(0, ae_classical.size)
t_classical = librosa.frames_to_time(frames_cl, hop_length=FRAME_SIZE)
frames_pop = range(0, ae_pop.size)
t_pop= librosa.frames_to_time(frames_pop, hop_length=FRAME_SIZE)
frames_disco = range(0, ae_disco.size)
t_disco = librosa.frames_to_time(frames_disco, hop_length=FRAME_SIZE)

plt.figure(figsize=[15, 17])

plt.subplot(3, 1, 1, alpha=0.5)
librosa.display.waveshow(classical)
plt.plot(t_classical, ae_classical, color='blue')
plt.title("Classical")

plt.ylim([-1, 1])
plt.subplot(3, 1, 2, alpha=0.5)
librosa.display.waveshow(disco)
plt.plot(t_disco, ae_disco, color='red')
plt.title("Disco")
plt.ylim([-1, 1])

plt.subplot(3, 1, 3, alpha=0.5)
librosa.display.waveshow(pop)
plt.plot(t_pop, ae_pop, color='green')
plt.title("Pop")
plt.ylim([-1, 1])

plt.show()