from functools import reduce

data = [(1, '2015-07-13; 24'), (2, '2012-07-11; 24'), (3, '2011-08-13; 43'), (4, '2015-09-11; 17')]


def map_function(key, value):
    # Split value into date and temperature
    date, temperature = value.split(';')
    # Extract year from date
    year = date.split("-")[0]
    # Return a tuple of (year, temperature)
    return (year, int(temperature))


def shuffle(mapped_values):
    shuffle = {}

    for key, value in mapped_values:
        if key in shuffle:
            shuffle[key].append(value)
        else:
            shuffle[key] = [value]
    return shuffle


# Apply map_function to each item in data using a lambda function
mapped = list(map(lambda key_value_pair: map_function(key_value_pair[0], key_value_pair[1]), data))
#shuffle which basically means append the values in a list with their keys
shuffled = shuffle(mapped)
#reduce by taking the max from the value list
reduced = [(key, reduce(lambda x, y: max(x, y), value)) for key, value in shuffled.items()]
print(reduced)
