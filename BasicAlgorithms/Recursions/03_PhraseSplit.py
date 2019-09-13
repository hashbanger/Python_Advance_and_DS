def word_split(phrase, word_list, output = None):

    if output is None:
        output = []

    for word in word_list:
        if phrase.startswith(word):

            output.append(word)

            return word_split(phrase[len(word):], word_list, output)

    return output

if __name__ == "__main__":
    
    phrase = input('Enter the phrase\t')
    print('Enter space separated words\t')
    word_list = [str(word) for word in map(str, input().strip().split())]
    print(word_split(phrase, word_list))