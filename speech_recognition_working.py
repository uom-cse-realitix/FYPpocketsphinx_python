import os
from pocketsphinx import LiveSpeech, get_model_path

model_path = get_model_path()

speech = LiveSpeech(
    sampling_rate=16000,
    hmm=os.path.join(model_path, 'en-us'),
    lm='/home/dasun/Documents/FYPpocketsphinx_python/7723.lm.bin',
    dic='/home/dasun/Documents/FYPpocketsphinx_python/7723.dic'
)

for phrase in speech:
    print(phrase)