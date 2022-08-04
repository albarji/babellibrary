import random

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'l', 
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
    'x', 'y', ' ', '.', ','
]

PAGES = 410
LINES = 40
LETTERS = 80

for page in range(PAGES):
    for line in range(LINES):
        print("".join(random.choices(alphabet, k=LETTERS)))
    print("")
