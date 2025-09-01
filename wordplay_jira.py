def words_ending_in_ime(words):
    return [w for w in words if w.endswith("ime")]

def words_with_rstlne(words):
    return [w for w in words if any(c in w for c in "rstlne")]

def words_no_vowels(words):
    vowels = "aeiou"
    return [w for w in words if not any(c in vowels for c in w)]

def words_with_all_vowels(words):
    vowels = "aeiou"
    return [w for w in words if all(v in w for v in vowels)]

def compare_word_lengths(words):
    tens = sum(1 for w in words if len(w) == 10)
    sevens = sum(1 for w in words if len(w) == 7)
    return "10-letter > 7-letter" if tens > sevens else "7-letter >= 10-letter"

def longest_word(words):
    return max(words, key=len)

if __name__ == "__main__":
    with open("wordlist.txt") as f:
        wordlist = f.read().splitlines()

    print("a) Words ending in ime:", words_ending_in_ime(wordlist))
    print("b) Words with r,s,t,l,n,e:", words_with_rstlne(wordlist))
    print("c) Words with no vowels:", words_no_vowels(wordlist))
    print("d) Words with all vowels:", words_with_all_vowels(wordlist))
    print("e) Compare 10 vs 7:", compare_word_lengths(wordlist))
    print("f) Longest word:", longest_word(wordlist))