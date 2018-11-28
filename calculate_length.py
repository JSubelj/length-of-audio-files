from mutagen.mp3 import MP3
import os
import math
import multiprocessing
import queue
import pickle
import json
path = "/mnt/mount_point/ML_music_norm/"
genres = ["thrash", "black", "death", "heavy"]



def mp_length_featcher(no, genre):

    def worker(genre, paths, num):
        file_length_d = {}
        for f in paths:
            #print("working on", f)
            try:
                file_length_d[f] = MP3(f).info.length
                print("working on: "+f)
            except:
                pass
        print("putting in dict")
        with open("genre_pickles_norm/"+genres[genre]+str(num)+".pckl","wb") as f:
            pickle.dump(file_length_d, f)
        #with open("jsons_norm/"+genres[genre]+str(num)+".json","w") as f:
        #    json.dump(file_length_d, f)
        #out_q.put(file_length_d)

    paths = []
    for filename in os.listdir(path+genres[genre]):
        paths.append(path+genres[genre]+"/"+filename)

    chunk_size = int(math.ceil(len(paths)/float(no)))
    proc = []
    out_q = queue.Queue()
    for i in range(no):
        p = multiprocessing.Process(
            target=worker,
            args=(genre, paths[chunk_size*i:chunk_size*(i+1)], i)
        )
        proc.append(p)
        p.start()




    for p in proc:
        p.join()

    #return resultdict


if __name__ == "__main__":
    for i in range(len(genres)):
        mp_length_featcher(8, i)


