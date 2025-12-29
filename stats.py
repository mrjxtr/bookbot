def get_num_words(text: str) -> int:
    return len(text.split())


def get_num_chars(text: str) -> dict[str, int]:
    """
    Convert text to lowercase and return a dictionary
    with the count of each character (including symbols and spaces).
    """
    text = text.lower()  # assign back the lowercase string
    result = {}

    for ch in text:
        result[ch] = result.get(ch, 0) + 1  # increment count

    return result


def sort_char_counts(char_counts: dict[str, int]) -> list[dict[str, int]]:
    """
    Takes a dictionary of character counts and returns a sorted list of dictionaries
    with keys 'char' and 'num', sorted from greatest to least by count.
    """
    # Convert to list of dictionaries
    char_list = [{"char": k, "num": v} for k, v in char_counts.items() if k.isalpha()]

    # Sort by the 'num' key descending
    char_list.sort(key=lambda x: x["num"], reverse=True)

    return char_list
