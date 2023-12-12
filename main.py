with open("books/frankenstein.txt") as file:
    file_contents:str = file.read()
    def getWordCount(file_contents: str):
        array_of_words:list[str] = file_contents.split()
        return len(array_of_words)


def getCharacterCount(text: str) -> dict:
    character_counts: dict[str, int] = {}
    text = text.lower()
    for character in text:
        if character.isalpha():
            if character in character_counts:
                character_counts[character] += 1
            else:
                character_counts[character] = 1
    return character_counts

def printReport(file_contents: str):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{getWordCount(file_contents)} words found in the document \n")
    character_count = getCharacterCount(file_contents)
    formatted_list = list(character_count.values())

    formatted_list.sort(reverse=True)
    for item in formatted_list:
             for key, value in character_count.items():
                if value == item:
                    print(f"The '{key}' character was found {value} times")

    print("--- End report ---")

printReport(file_contents)