import os
import matplotlib.pyplot as plt
from scipy.io import wavfile
from thinkdsp import read_wave
from thinkdsp import play_wave
from thinkdsp import CosSignal, SinSignal
from thinkdsp import decorate
from thinkdsp import SinSignal
signal = (SinSignal(freq=400, amp=1.0) + SinSignal(freq=600, amp=0.5) + SinSignal(freq=800, amp=0.25))
signal.plot()
plt.show()

wave2 = signal.make_wave(duration=1)
wave2.apodize()

audio = wave2.make_audio()
wave2.write(filename='blank.wav')

wav_array = (wave2.ys * 30000).astype(int)
wavfile.write('blank.wav', 40000, wav_array)

os.system('ffplay blank.wav')


wave3 = read_wave('170255__dublie__trumpet.wav')
wave3.normalize()
wave3.make_audio()

def stretch(wave, factor):
    wave.ts *= factor
    wave.framerate /= factor

stretch(wave3, 0.5)
wave3.make_audio()

wave3.plot()
plt.show()

#cos_sig = CosSignal(freq=400, amp=1.0, offset=0)
#sin_sig = SinSignal(freq=880, amp=0.5, offset=0)

#mix = sin_sig + cos_sig
#wave = mix.make_wave(duration=0.5, start=0, framerate=11025)
#wave = read_wave(filename='cat.wav')
#wave.normalize()
#wave.make_audio()
#wave.plot()
#plt.show()

#segment = wave.segment(start=0, duration=0.5)
spectrum = wave2.make_spectrum()
spectrum.plot(high=2000)
#spectrum.peaks()[:30]
#plt.show()
#segment.make_audio()

#Filters
#spectrum.low_pass(2000)

#wave = play_wave(filename='cat.wav', player='ffplay')
#cos_sig.plot()
#decorate(xlabel='Time (s)')

#from IPython.display import Audio
#cat_audio = Audio(data=wave.ys, rate=wave.framerate)

#period = mix.period
#segment = wave.segment(start=0, duration=period*3)
#segment.plot()
#decorate(xlabel='Time (s)')







