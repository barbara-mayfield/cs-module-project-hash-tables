# Input: Single string
# If input contains no ignored chars,
# return an empty dict.
# Output: Dict of LOWERCASE words and their counts,
#         example: { 'hello': 2 }

# Case should be ignored

# Key order irrelevant

# Split strs into words on any whitespace

# Ignore each of the following characters:
# " : ; , . - + = / \ | [ ] { } ( ) * ^ &


def word_count(s):
    # Your code here
    cache = {}

    # all words must be lowercase
    word = s.lower()

    # ignore chars and split the string at it's whitespace
    # so that it creates a list of ignored chars
    ignored = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(" ")

    for chars in ignored:
        # if there is an ignored char, replace it with whitespace
        word = word.replace(chars, "")

    for words in word.split():
        # if there are no words, continue
        if words == "":
            continue
        if words not in cache:
            cache[words] = 1
        else:
            cache[words] += 1
    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
