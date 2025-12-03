def get_num_words(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    count = dict()
    for i in text.lower():
        count[i] = count.get(i,0) + 1
    return count


def sort_on(item):
    return item["num"]


def chars_dict_to_sorted_list(dict):
    list = []
    for item in dict:
        list.append({"char": item, "num": dict[item]})
    list.sort(reverse=True, key=sort_on)
    return list


