from random import randint

random_bits = 0

for i in range(64):
    if ranint(0, 1):
        random_bits |= 1 << i

flavor_list = ["vanillz", "chocolate", "pecan", "stramberry"]

for flavor in flavor_list:
    print("%s is delicious " % (flavor, ))


for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print("%d : %s " % (i + 1, flavor))


for i, flavor in enumerate(flavor_list):
    print("%d : %s " % (i + 1, flavor))