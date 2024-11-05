import whisper
import argparse


# parse arguments

parser = argparse.ArgumentParser()
parser.add_argument("input", type=str)
args = parser.parse_args()


model = whisper.load_model("turbo")

CHUNK_LIM = 480000
count = 1

audios = []
audio = whisper.load_audio(args.input)

# if smaller than 30 sec, move on
if len(audio) <= CHUNK_LIM:
    audio = whisper.pad_or_trim(audio)
    audios.append(audio)

# if larger than 30 sec, chunk it and pad last piece
else:

    for i in range(0, len(audio), CHUNK_LIM):
        chunk = audio[i: i + CHUNK_LIM]
        chunk_index = len(chunk)
        if chunk_index < CHUNK_LIM:
            chunk = whisper.pad_or_trim(chunk)
        audios.append(chunk)

results = ""

for chunk in audios:
    # print(chunk.shape)
    print("Part", count, "of", len(audios))
    # chunk = whisper.pad_or_trim(chunk)
    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(chunk, n_mels=128).to(model.device)

    # decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)
    # print(result.text)
    results += result.text
    count += 1

with open("whisper_output.txt", "w") as text_file:
    print(results, file=text_file)

print('Done.')
