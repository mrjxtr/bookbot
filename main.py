import sys

from stats import get_num_chars, get_num_words, sort_char_counts


def get_book_text(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filename = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filename}...")

    text = get_book_text(filename)

    # Word count
    wc = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")

    # Character count
    ch_counts = get_num_chars(text)
    sorted_chars = sort_char_counts(ch_counts)
    print("--------- Character Count -------")
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
