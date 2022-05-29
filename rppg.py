import numpy as np
from scipy import signal
from scipy.signal import butter, filtfilt
def maxvalue(arr1, arr2):
    value = np.argmax(arr1)
    value = arr2[value]
    return value

def filter_butterworth_bandpass(arr, srate, length, band, order=5):
    try:
        (minFreq, maxFreq) = band
        nyq = srate / 2.0
        n = len(arr)
        pad_factor = max(1, 60 * srate / length)
        n_padded = int(n * pad_factor)
        padded = np.zeros(n_padded)
        padded[:n] = arr[:]

        # filter butterworths
        filter = butter(order, [minFreq / nyq, maxFreq / nyq], 'bandpass')
        bandpassed = filtfilt(*filter, padded)
        bandpassed = bandpassed[:n]
        return bandpassed

    except ValueError:
        return []

def detrend_signal(arr, win_size): #trend removal
    if not isinstance(win_size, int):
        win_size = int(win_size)
    length = len(arr)
    norm = np.convolve(np.ones(length), np.ones(win_size), mode='same') #no of sample
    mean = np.convolve(arr, np.ones(win_size), mode='same') / norm #rolling mean
    return (arr - mean) / mean