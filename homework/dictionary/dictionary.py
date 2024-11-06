def dict_operations(commands_list: list) -> dict | list:
    dictionary = {}
    result = None

    for command in commands_list:
        parts = command.split()
        action = parts[0]

        if action == "add":
            key, value = parts[1], parts[2]
            dictionary[key] = int(value) if value.isdigit() else value

        elif action == "remove":
            key = parts[1]
            dictionary.pop(key, None)

        elif action == "update":
            key, value = parts[1], parts[2]
            dictionary[key] = int(value) if value.isdigit() else value

        elif action == "return":
            if len(parts) == 1:
                result = dictionary.copy()
            elif parts[1] == "keys":
                result = list(dictionary.keys())
            elif parts[1] == "values":
                result = list(dictionary.values())

        elif action == "clear":
            dictionary.clear()

    return result