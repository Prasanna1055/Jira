def words_ending_in_ime(words):
    return [w for w in words if w.endswith("ime")]

def words_with_rstlne(words):
    return [w for w in words if any(c in w for c in "rstlne")]

if __name__ == "__main__":
    with open("wordlist.txt") as f:
        wordlist = f.read().splitlines()

    print("a) Words ending in ime:", words_ending_in_ime(wordlist))
    print("b) Words with r,s,t,l,n,e:", words_with_rstlne(wordlist))
