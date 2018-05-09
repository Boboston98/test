import numpy as np

# cd audio at 44,100 hz and 16 bits per sample
SAMPLES_S = 44_100
BITS_SAMPLE = 16

# wave header constants
CHUNK_ID = b'RIFF'
FORMAT = b'WAVE'
SUBCHUNK_1_ID = b'fmt '
SUBCHUNK_2_ID = b'data'

# PCM constants
SUBCHUNK_1_SIZE = (16).to_bytes(4, byteorder = 'little')
AUDIO_FORMAT = (1).to_bytes(2, byteorder = 'little')

def create_pcm(frequency):
    ang_freq = 2 * np.pi * frequency
    x_vals = np.arange(SAMPLES_S)
    y_vals = 32767 * .3 * np.sin(ang_freq * x_vals/SAMPLES_S)
    return np.int16(y_vals)

def wav_wav(channels, filename, *args):
    seconds = len(args)/2

    chunk_size = (int(36 + (seconds * SAMPLES_S * BITS_SAMPLE/8))).to_bytes(4, 'little')
    num_channels = (channels).to_bytes(2, byteorder = 'little')
    sample_rate = (SAMPLES_S).to_bytes(4, byteorder = 'little')
    byte_rate = (int(SAMPLES_S * channels * BITS_SAMPLE/8)).to_bytes(4, byteorder = 'little')
    block_align = (int(channels * BITS_SAMPLE/8)).to_bytes(2, byteorder = 'little')
    bits_per_sample = (BITS_SAMPLE).to_bytes(2, byteorder = 'little')
    subchunk_2_size = (int(seconds * SAMPLES_S * BITS_SAMPLE/8)).to_bytes(4, byteorder = 'little')

    my_pcm = []
    my_pcm2 = []

    #TAKE 'for arg' AND USE TO ADD FREQ TO SONG
    #MAKE PCM OUTSIDE OF FUNC DEF AND REPLACE *ARG WITH IT IN FUNCTION CALL
    for arg in args:
        my_pcm.append(create_pcm(arg))

    mat1 = np.array(my_pcm)

    for arg in args:
        my_pcm2.append(create_pcm(arg/3))
    mat2 = np.array(my_pcm)

    my_final = (mat1 + mat2)/2

    with open(f'{filename}.wav', 'wb') as fo:
        fo.write(
            CHUNK_ID +
            chunk_size +
            FORMAT +
            SUBCHUNK_1_ID +
            SUBCHUNK_1_SIZE +
            AUDIO_FORMAT +
            num_channels +
            sample_rate +
            byte_rate +
            block_align +
            bits_per_sample +
            SUBCHUNK_2_ID +
            subchunk_2_size +
            my_final.tobytes()
        )
