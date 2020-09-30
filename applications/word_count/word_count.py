# Ignore each of the following characters
# " : ; , . - + = / \ | [ ] { } ( ) * ^
# Key order doesn't matter
# Split the strings into words on any whitespace
# If the input contains no ignored chars, return empty dict
# returns dict of words and their counts


def word_count(s):
    cache = {}
    new_s = s.lower()
    ignored_chars = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(" ")

    for chars in ignored_chars:
        new_s = new_s.replace(chars, "")

    for words in new_s.split():
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
