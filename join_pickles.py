import pickle
import json
genres = ["thrash", "black", "death", "heavy"]


def join_pickle(name):
    wholedict = {}
    for i in range(8):
        with open("pickles_norm/"+name+str(i)+".pckl", "rb") as f:
            wholedict.update(pickle.load(f))

    return wholedict

if __name__ == "__main__":
    for g in genres:
        d = join_pickle(g)

        with open("genre_pickles_norm/"+g+".pckl", "wb") as f:
            pickle.dump(d, f)
        #with open("genre_jsons/"+g+".json", "w") as f:
        #    json.dump(d, f)

        print(d)