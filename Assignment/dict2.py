class DictKeyNotFoundError(Exception):
    def __init__(self, key):
        self.key = key

    def __str__(self):
        return f"Key '{self.key}' not found"


class KeyValue:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class dict2:
    def __init__(self):
        self.data = []

    def __setitem__(self, key, value):
        for item in self.data:
            if item.key == key:
                item.value = value
                return
        self.data.append(KeyValue(key, value))

    def __getitem__(self, key):
        for item in self.data:
            if item.key == key:
                return item.value
        raise DictKeyNotFoundError(key)

    def __iter__(self):
        return iter(item.key for item in self.data)


# Example usage:
obj = dict2()
obj['a'] = 1
obj['b'] = 2
obj['c'] = 3

# Accessing values based on keys
val = obj['a']
print(val)  # Output: 1

# Custom exception for non-existing keys
try:
    val = obj['d']
except DictKeyNotFoundError as e:
    print(e)  # Output: Key 'd' not found

# Iterating through keys
for k in obj:
    print(f'key: {k}')
