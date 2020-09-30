# Input: string of words with whitespace
# Output: string in the same order but w/ duplicate words removed
# No extra spaces at the end of your returned string
# Must be O(n)

def no_dups(s):
    cache = {}
    word_list = []

    for word in s.split():
        if word not in cache:
            cache[word] = 1
            word_list.append(word)
    return " ".join(word_list)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
