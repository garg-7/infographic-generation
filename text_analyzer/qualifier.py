import numpy as np

def cosineSim(vec1, vec2):
    dot_p = np.dot(vec1, vec2)/(np.linalg.norm(vec1) * np.linalg.norm(vec2))
    if dot_p>1:
        dot_p = 1
    return 1 - np.arccos(dot_p)/np.pi

def getSimilarity(check_word):

    inc_vec = []
    dec_vec = []
    try:
        inc_vec = np.load('inc_vec.npy')
        dec_vec = np.load('dec_vec.npy')
    except:
        with open('wiki-news-300d-1M.vec', 'r') as f:
            for line in f.readlines():
                line = line.strip().split()
                word = line[0]
                if word == 'increase':
                    vec = list(map(float, line[1:]))
                    inc_vec = np.asarray(vec)
                    np.save('inc_vec.npy', inc_vec)
                    print("increase vector noted")
                elif word == 'decrease':    
                    vec = list(map(float, line[1:]))
                    dec_vec = np.asarray(vec)
                    np.save('dec_vec.npy', dec_vec)
                    print("decrease vector noted")
        # inc_vec = np.load('inc_vec.npy')
        # dec_vec = np.load('dec_vec.npy')
    
    # print(inc_vec.shape)

    with open('wiki-news-300d-1M.vec', 'r') as f:
        for line in f.readlines():
            line = line.strip().split()
            word = line[0]
            if word == check_word:
                vec = list(map(float, line[1:]))
                vec = np.asarray(vec)
                break
    
    # get the similarity with increase and decrease
    inc_sim = cosineSim(vec, inc_vec)
    # print('with increase:', inc_sim)
    dec_sim = cosineSim(vec, dec_vec)
    # print('with decrease:', dec_sim)

    if inc_sim > dec_sim:
        print(word,  'increase')
    else:
        print(word, 'decrease')

if __name__ == '__main__':
    getSimilarity('hike')