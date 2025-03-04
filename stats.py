def count_words(text):
    words = text.split()
    return len(words)

def character_count_sorted(text):
    char_count = {}
    lower_char = text.lower()
    for char in lower_char:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

    return sorted_char_count



