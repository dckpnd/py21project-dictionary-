import re
from dict import new_dict_word


voc_syll_reverse = {'А́': 'А', 'Е́': 'Е', 'И́': 'И', 'О́': 'О', 'У́': 'У', 'Ы́': 'Ы', 'Э́': 'Э', 'Ю́': 'Ю', 'Я́': 'Я',
                    'а́': 'а', 'е́': 'е', 'и́': 'и', 'о́': 'о', 'у́': 'у', 'ы́': 'ы', 'э́': 'э', 'ю́': 'ю', 'я́': 'я'}


def search_full_word(x):
    out = {}
    for key in new_dict_word:
        for key_reverse in voc_syll_reverse:
            if key_reverse in x:
                if x == key:
                    out[key] = new_dict_word[key]
                else:
                    if ', ' in key:
                        key_new = key.split(', ')
                        if x == key_new[0] or x == key_new[1]:
                            out[key] = new_dict_word[key]
            else:
                key_new = re.sub(key_reverse, voc_syll_reverse[key_reverse], key)
                if x == key_new:
                    out[key] = new_dict_word[key]
                else:
                    if ', ' in key_new:
                        key_new_new = key_new.split(', ')
                        if x == key_new_new[0] or x == key_new_new[1]:
                            out[key] = new_dict_word[key]
    return out


# y = input()
# for i, j in search_full_word(y).items():
#     print(str(i) + ':\n' + str(j))
