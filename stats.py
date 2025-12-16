

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_stat(text):
    letter_dict = {}
    text = text.lower()
    for char in text: 
        if char in letter_dict: 
            letter_dict[char] += 1
        else: 
            letter_dict[char] = 1
    return letter_dict

def dict_list(letter_dict): 
    report_list = []
    for letter in letter_dict: 
        if letter.isalpha():
            dict = {"char": letter, "num": letter_dict[letter]}
            report_list.append(dict)
    report_list.sort(reverse=True, key=sort_on)
    return report_list

def sort_on(items):
    return items["num"]
