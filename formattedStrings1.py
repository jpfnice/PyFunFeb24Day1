import math
nb=34

text=f"nb is {nb} cosine of {nb} is {math.cos(nb)}" # 3.6
print(text)

print("nb is", nb, "cosine of", nb, "is", math.cos(nb))

text="nb is {} cosine of {} is {}".format(nb, nb, math.cos(nb))
print(text)