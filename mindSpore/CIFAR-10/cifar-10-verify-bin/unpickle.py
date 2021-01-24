x = "test_batch" # File name to be unpickled and turned into .bin

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    with open('data.bin', 'wb') as f:
        pickle.dump(dict, f, pickle.HIGHEST_PROTOCOL)

unpickle(x)