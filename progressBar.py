from tqdm import tqdm
from time import sleep

for i in tqdm(range(0, 100), desc ="Process In Progress"): 
    sleep(.1)