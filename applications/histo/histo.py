# Open the file and work through it to produce the output
# Print a histogram showing the word count for each word
# One hash mark for every occurence of the word
# Output will be first ordered by # of words, then by the word (alphabetically).
# The hash marks should be left justified two spaces after the longest word

# Ignore case, all output forced lowercase
# Split the strings into words on any whitespace
# Ignore chars: " : ; , . - + = / \ | [ ] { } ( ) * ^ &

# Decoded Hints:
# Items: `.items()` method on a dictionary might be useful.
# Sorting: it's possible for `.sort()` to sort on multiple keys at once.
# Sorting: negatives might help where `reverse` won't.
# Printing: you can print a variable field width in an f-string with
# nested braces, like so `{x:{y}}`

ignored_chars = '";:,.-+=/|\[]{}()*^&'

with open("robin.txt") as f:
    words = f.read().strip().split()

cache = {}

for char in words:

    new_word = char.strip(ignored_chars).lower()

    if new_word not in cache:
        cache[new_word] = 1

    else:
        cache[new_word] += 1

print(cache)

# TODO: Sort cache
