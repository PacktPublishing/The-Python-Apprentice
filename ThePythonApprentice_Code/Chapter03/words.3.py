from urllib.request import urlopen


# This fetches the words and returns them as a list.
def fetch_words():
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


# This prints a list of words
def print_words(story_words):
    for word in story_words:
      print(word)


if __name__ == '__main__':
    words = fetch_words()
    print_words(words)
