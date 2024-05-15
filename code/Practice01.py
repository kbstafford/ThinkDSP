import os
import matplotlib.pyplot as plt
from scipy.io import wavfile
from thinkdsp import read_wave
from thinkdsp import play_wave
from thinkdsp import CosSignal, SinSignal
from thinkdsp import decorate

cos_sig = CosSignal(freq=440, amp=1.0, offset=0)
sin_sig = SinSignal(freq=880, amp=0.5, offset=0)

mix = sin_sig + cos_sig
wave = mix.make_wave(duration=0.5, start=0, framerate=11025)
wave = read_wave(filename='cat.wav')

#cos_sig.plot()
#decorate(xlabel='Time (s)')

#from IPython.display import Audio
#cat_audio = Audio(data=wave.ys, rate=wave.framerate)

period = mix.period
segment = wave.segment(start=0, duration=period*3)
segment.plot()
decorate(xlabel='Time (s)')







