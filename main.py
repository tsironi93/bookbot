from stats import ascci_dict, wc

def get_book_text(path:str) -> str:
    with open(path) as str:
        file_str = str.read()
    return file_str


def main():
    book_str = get_book_text("./books/frankenstein.txt")
    num_words = wc(book_str)
    print (f"{num_words} words found in the document")
    result = ascci_dict(book_str)
    for char, data in result.items():
        print(f"'{char}': {data}")

if __name__ == "__main__":
    main()

