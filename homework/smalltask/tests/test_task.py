from homework.smalltask.task import find_letter_occurrences

class TestFindLetterOccurrences:
    def test_basic_case(self):
        assert find_letter_occurrences(["abfg", "Bcd", "Ijk"], "b") == 2  # "abfg" and "Bcd" contain "b"

    def test_case_insensitivity(self):
        assert find_letter_occurrences(["Hello", "world", "Beautiful"], "b") == 2  # "Beautiful" and "world" contain "b" (case-insensitive)

    def test_no_occurrences(self):
        assert find_letter_occurrences(["apple", "orange", "grape"], "z") == 0  # None contain "z"

    def test_empty_list(self):
        assert find_letter_occurrences([], "e") == 0  # An empty list should return 0

    def test_letter_at_different_positions(self):
        assert find_letter_occurrences(["ball", "basket", "bat", "table"], "b") == 4  # All words contain "b"

    def test_single_letter_strings(self):
        assert find_letter_occurrences(["a", "b", "c", "d"], "b") == 1  # Only "b" contains the letter

    def test_large_list(self):
        assert find_letter_occurrences(["apple"] * 1000 + ["banana"], "a") == 1001  # Test with large input size

    def test_letter_not_present(self):
        assert find_letter_occurrences(["xyz", "mnop", "qrst"], "a") == 0  # "a" is not present in any string

    def test_all_strings_contain_letter(self):
        assert find_letter_occurrences(["aaaa", "bbaa", "ab", "a"], "a") == 4  # All strings contain "a"
#