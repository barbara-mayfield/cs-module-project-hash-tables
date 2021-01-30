# Input: string of words with whitespace
#        only letters a - z utilized

# Output: string in same order but with duplicate words removed

# No extra spaces at the end of returned string

def no_dups(s):
    # Your code here
    # instantiate dict
    cache = {}
    # store strings in a list
    words = []

    # for our values that are returned after
    # splitting the words in the string
    for word in s.split():
        # if our word isn't in the cache
        if word not in cache:
            # add it to the cache and append it to the list
            cache[word] = 1
            words.append(word)
    # our return is an empty string joined by the word strings in the list
    return " ".join(words)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
