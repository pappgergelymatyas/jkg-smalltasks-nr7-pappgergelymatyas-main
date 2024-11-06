# Dictionary Operations

Consider an empty dictionary (`dict = {}`). You can perform the following commands:

- `add key value`: Add a key-value pair to the dictionary.
- `remove key`: Remove the specified key from the dictionary.
- `update key value`: Update the value of the specified key.
- `return`: Return the dictionary.
- `return keys`: Return a list of all the keys in the dictionary.
- `return values`: Return a list of all the values in the dictionary.
- `clear`: Clear all entries from the dictionary.

## Task

Initialize an empty dictionary. Iterate through each command in your commands list (given as input) and perform the corresponding operation on the dictionary.

## Input Format

A list containing the commands described above as strings.

## Constraints

- Keys are strings, and values can be strings or integers.
- Operations are case-sensitive.
- There will be no duplicate keys during an `add` operation.

## Output Format

The output is the result of the return commands, which may include the whole dictionary, keys, or values.

## Samples

### Sample Input 1:

    add student John
    add grade 90
    add subject Math
    update grade 95
    remove subject
    return

### Expected Output 1:
    {"student": "John", "grade": 95}


### Sample Input 2:

    add name Alice
    add age 25
    update name Bob
    remove age
    return keys
    
### Expected Output 2:

    ["name"]



