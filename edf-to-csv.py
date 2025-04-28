import numpy as np
import mne

edf = mne.io.read_raw_edf('2025-03-17_10.34.edf')
header = ','.join(edf.ch_names)
np.savetxt('2025-03-17_10.34.csv', edf.get_data().T, delimiter=',', header=header)
