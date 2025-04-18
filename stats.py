

def num_words(text):
    word_list = text.split()
    return len(word_list)



def dic_count_chars(text):
    lowered_text = text.lower()
    char_count = {}
    for char in lowered_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count



def dicsList(dic):
    char_dicS_list = []
    for ch in dic:
        num = dic[ch]
        # Create a dictionary with consistent key names
        char_dicS_list.append({"char": ch, "count": num})
    return char_dicS_list







def sort_on_CharDicList(char_dic_list):
    # Apply the `.sort()` method directly on the list
    char_dic_list.sort(key=lambda dic: dic["count"], reverse=True)
    
    # Return the modified list
    return char_dic_list