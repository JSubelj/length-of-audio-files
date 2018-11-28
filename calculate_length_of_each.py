import pickle
import json
genres = ["thrash", "black", "death", "heavy"]


def calculate_length_pickle(genre):
    g_d = {}
    with open("genre_pickles_norm/" + genre + ".pckl", "rb") as f:
        g_d: dict = pickle.load(f)
        length = 0
        for key, leng in g_d.items():
            length += leng
        g_d["full_length"] = length
        return g_d

def calculate_length_json(genre):
    g_d = {}
    with open("genre_jsons/" + genre + ".json", "r") as f:
        g_d: dict = json.load(f)
        length = 0
        for key, leng in g_d.items():
            length += leng
        g_d["full_length"] = length
        return g_d


if __name__ == "__main__":
    for g in genres:
        #json_g = calculate_length_json(g)
        pickle_g = calculate_length_pickle(g)

        #if json_g["full_length"] != pickle_g["full_length"]:
        #    print("not same:",g,"json:",json_g["full_length"],"pickle:",pickle_g["full_length"])

        #with open("genre_pickles/"+g+".pckl", "wb") as f:
        #    pickle.dump(pickle_g, f)
        #with open("genre_jsons/"+g+".json", "w") as f:
        #    json.dump(json_g, f)

        #print(g, "json:", json_g["full_length"], "pickle:", pickle_g["full_length"])
        print(g, "pickle:", pickle_g["full_length"])
