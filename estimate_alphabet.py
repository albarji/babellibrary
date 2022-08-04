from itertools import chain

# Texts from the library mentioned in the tale
texts = [
    "mcv",
    "oh tiempo tus piramides",
    "trueno peinado",
    "cambiante yeso",
    "axaxaxas mlo"
]

unique = {c for c in chain(*texts)}
print(sorted(list(unique)))
print(len(unique))
