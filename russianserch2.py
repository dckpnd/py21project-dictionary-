from dict import new_dict_word
dict_word = new_dict_word
from string import punctuation

def rus_concrete(request):
    out_r = {}
    u = 0
    for word, definition in dict_word.items():
        newnew_def = []
        new_def = definition.split()
        for i in new_def:
            for punct in punctuation:
                i = i.replace(punct, '')
            newnew_def += [i]
        for k in newnew_def:
            if k == request:
                u += 1
                out_r[word] = definition

    if u != 0:
        return out_r

def rus_2(request):
    out_semi = {}
    k = 0
    for word, definition in dict_word.items():
        if request in definition:
            k += 1
            out_semi[word] = definition

    if rus_concrete(request):
        for i in rus_concrete(request).keys():
            if i in out_semi.keys():
                del out_semi[i]
        out_2 = out_semi

    else: out_2 = out_semi
    if (k != 0) and out_2 != {}:
        return out_2

