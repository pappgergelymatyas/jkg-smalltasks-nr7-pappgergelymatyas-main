from homework.dictionary.dictionary import dict_operations

class TestDictOperations:
    def test_add_and_return_dict(self):
        commands = [
            "add student John",
            "add grade 90",
            "update grade 95",
            "return"
        ]
        result = dict_operations(commands)
        assert result == {"student": "John", "grade": 95}

    def test_add_update_remove_return_dict(self):
        commands = [
            "add city Paris",
            "add country France",
            "add population 2148000",
            "update population 2200000",
            "remove country",
            "return"
        ]
        result = dict_operations(commands)
        assert result == {"city": "Paris", "population": 2200000}

    def test_return_keys(self):
        commands = [
            "add name Alice",
            "add age 25",
            "update name Bob",
            "return keys"
        ]
        result = dict_operations(commands)
        assert set(result) == {"name", "age"}

    def test_return_values(self):
        commands = [
            "add fruit apple",
            "add number 42",
            "update fruit orange",
            "return values"
        ]
        result = dict_operations(commands)
        assert set(result) == {"orange", 42}

    def test_clear_and_return_dict(self):
        commands = [
            "add key1 value1",
            "add key2 value2",
            "clear",
            "return"
        ]
        result = dict_operations(commands)
        assert result == {}

    def test_empty_dict_return(self):
        commands = ["return"]
        result = dict_operations(commands)
        assert result == {}

    def test_single_key_removal(self):
        commands = [
            "add animal cat",
            "remove animal",
            "return"
        ]
        result = dict_operations(commands)
        assert result == {}

    def test_no_return_command(self):
        commands = [
            "add item1 value1",
            "add item2 value2"
        ]
        result = dict_operations(commands)
        assert result is None

