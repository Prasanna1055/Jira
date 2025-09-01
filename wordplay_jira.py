def words_ending_in_ime(words):
    return [w for w in words if w.endswith("ime")]

if __name__ == "__main__":
    with open("wordlist.txt") as f:
        wordlist = f.read().splitlines()

    print("a) Words ending in ime:", words_ending_in_ime(wordlist))
