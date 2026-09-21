import os
from tkinter import filedialog, Tk
from spectrogram import plot_spectrogram
import librosa.display
import matplotlib.pyplot as plt
def folder_process():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askdirectory(title="Select genre folder containing audio files")
    file_name = os.path.basename(file_path)
    root.destroy()

    if not file_path:
        print("No files selected")
        return

    all_files = []
    file_types = ('.mp3', '.wav', '.m4a', '.flac')
    print(f"Processing files : {file_path}")

    for file in os.listdir(file_path):
        if file.lower().endswith(file_types):
            exact_path = os.path.join(file_path, file)
            try:
                print(f"Processing {file}")
                result, sr = plot_spectrogram(exact_path)

                plt.figure(figsize=(25, 10))
                librosa.display.specshow(
                    result,
                    sr=sr,
                    hop_length=512,
                    x_axis='time',
                    y_axis='linear'
                )
                plt.colorbar(format='%+2.0f dB')
                plt.title(file)

                output_dir = os.path.join(file_path, "spectrograms")
                os.makedirs(output_dir, exist_ok=True)

                output_name = os.path.splitext(file)[0] + ".png"
                output_path = os.path.join(output_dir, output_name)

                plt.savefig(output_path, dpi=150, bbox_inches='tight')
                plt.close()

                all_files.append(result)
            except Exception as e:
                print(f"Error {file} could not be processed")


if __name__ == "__main__":
    folder_process()
