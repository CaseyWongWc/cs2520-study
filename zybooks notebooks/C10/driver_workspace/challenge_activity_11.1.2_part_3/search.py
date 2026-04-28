def find(one_sentence, search_list):
    words = one_sentence[:-1].split()
    for word in words:
        if word in search_list:
            return True
    return False