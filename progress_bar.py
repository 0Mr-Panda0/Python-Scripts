from progressbar import ProgressBar, Percentage, Bar, ETA
from time import sleep
from random import randint


progress, progress_maxval = 0, 10
pbar = ProgressBar(widgets=['Progress ', Percentage(), Bar(), ' ', ETA(), ],maxval=progress_maxval).start()

for i in range(progress_maxval):
    progress += 1
    sleep(randint(1,5))
    pbar.update(progress)

pbar.finish()