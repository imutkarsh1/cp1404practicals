def count_word_occurrences(text):
    words = text.split()
    word_counts = {}

    for word in words:
        word = word.strip('.,?!()[]{}"\'').lower()

        if word:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

    return word_counts

def print_aligned_word_counts(word_counts):
    max_width = max(len(word) for word in word_counts)

    for word, count in sorted(word_counts.items()):
        print(f"{word:{max_width}} : {count}")


if __name__ == "__main__":
    user_input = input("Enter a string: ")
    word_counts = count_word_occurrences(user_input)
    print_aligned_word_counts(word_counts)
