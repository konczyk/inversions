# Inversions counter based on merge sort algorithm 

Count inversions in a list of all integers between 1-100000 in random order,
with no integer repeated:

    $ ./inversions_client.py -b 100000
    
    2500115203

Count inversions in a list of integers read from the standard input or file:

    $ ./inversions_client.py < numbers.txt

    2498660231

    $ ./inversions_client.py numbers.txt

    2498660231
