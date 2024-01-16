import sts_random as m

def shuffle(collection, java_random):
    size = len(collection)
    for i in range(size, 1, -1):
        j = java_random.nextInt(i)
        collection[i - 1], collection[j] = collection[j], collection[i - 1]