import pickle
import operator
genres = ["thrash", "black", "death", "heavy"]

def sort_songs_by_length(d):
    return sorted(d.items(), key=operator.itemgetter(1), reverse=True)

if __name__ == "__main__":
    gen_length = {}
    sorted_gens = {}
    for g in genres:
        with open("genre_pickles/" + g + ".pckl", "rb") as f:
            d = pickle.load(f)
            gen_length[g] = d["full_length"]
            with open("genre_sorted_pickles/"+g+".pckl", "wb") as fa:
                sorted_gens[g] = sort_songs_by_length(d)
                pickle.dump(sorted_gens[g],fa)

    print(gen_length)
    lowest = 999999999999999999999999999999999999999
    lowest_g = ""
    for key, val in gen_length.items():
        if val < lowest:
            lowest = val
            lowest_g = key

    print(lowest_g,lowest)
    print()
    print(sorted_gens["thrash"])