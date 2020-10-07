# Input: string of words with whitespace
#        only letters a - z utilized

# Output: string in same order but with duplicate words removed

# No extra spaces at the end of returned string

def no_dups(s):
    # Your code here
    cache = {}
    words = []

    for word in s.split():
        if word not in cache:
            cache[word] = 1
            words.append(word)
    return " ".join(words)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
