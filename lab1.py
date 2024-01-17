def max_word_count(file_path):
    """
    Takes a txt file and return the most common word.
    :param file_path: path to the input file
    :return: max word count and the most common word
    """
    word_count = {}
    with open(file_path, "r") as sample_file:  # Opening the txt file
        for line in sample_file:  # Reading the file line by line
            words = line.split()
            for word in words:  # Separating every word by removing whitespaces
                word = word.strip().lower()
                if word in word_count:  # Checking if the word exist in dictionary or not
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    max_count = 0  # Comment added
    most_common_word = None
    for word, count in word_count.items():  # Reading the key and value of dictionary to count max and common word
        if count > max_count:
            most_common_word = word
            max_count = count
    return max_count, most_common_word


file_path = "sample.txt"
max_count, most_common_word = max_word_count(file_path)
print(f"Most common word is: '{most_common_word}' = {max_count} times")
