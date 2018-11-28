import pickle
genres = ["thrash", "black", "death", "heavy"]

def get_lenght(genre):
    with open("genre_sorted_pickles/" + genre + ".pckl", "rb") as fa:
        return pickle.load(fa)[0][1]

def get_files(genre):
    with open("genre_sorted_pickles/" + genre + ".pckl", "rb") as fa:
        return pickle.load(fa)[1:]

def get_dictionary(genre):
    with open("genre_pickles/" + genre + ".pckl", "rb") as fa:
        return pickle.load(fa)

def get_files_without_array_files(dic, arr):
    ret_dic = []
    for key in dic:
        if key in arr or key == "full_length":
            pass
        else:
            ret_dic.append(key)
    return ret_dic

def get_lowest_length(d):
    lowest = 999999999999999999999999999999999999999
    lowest_g = ""
    for key, val in d.items():
        if val < lowest:
            lowest = val
            lowest_g = key

    return lowest_g, lowest

def ok_length(length, l_wanted):
    return length-l_wanted < 0

def is_still_positive(l, l_w):
    return l-l_w > 0

def remove_list(t_g, length, length_wanted):
    remove_lst = []
    length_of_g = length

    for i in t_g:
        if is_still_positive(length_of_g-i[1], length_wanted):
            length_of_g -= i[1]
            remove_lst.append(i[0])
            if ok_length(length_of_g, length_wanted):
                return length_of_g, length_of_g-length_wanted, remove_lst

    return length_of_g, length_of_g - length_wanted, remove_lst



if __name__=="__main__":
    gen_len = {}
    gen_files = {}

    for g in genres:
        gen_len[g] = get_lenght(g)
        gen_files[g] = get_files(g)

    print(get_lowest_length(gen_len)[1])
    for g in genres:
        _, _, rem_lst = remove_list(gen_files[g], gen_len[g], get_lowest_length(gen_len)[1])
        with open("norm_genres/norm_"+g+".txt", "w") as fh:
            for f in get_files_without_array_files(get_dictionary(g),rem_lst):
                fh.write('"'+f+'"'+"\n")
