import sys
import os
import numpy as np


# Get current project directory
def current_file_path():

    dir_path = os.path.dirname(os.path.realpath(__file__))
    project_path = os.path.split(dir_path)[0]
    data_path = project_path + os.sep + 'data'
    return data_path


def read_w3c_file(filename):

    file = list(open(filename, "r").readlines())
    for line in file:
        if line != "" and line[0].isalpha():
            if "=" not in line and "to" not in line.lower() and "cc" not in line.lower():
                print line


def read_directory(file_dir):
    for filename in os.listdir(file_dir):
        if filename.endswith(".txt"):
            file_path = file_dir + os.sep + filename
            read_w3c_file(file_path)


def position_encoding(sentence_size, embedding_size):
    """
    Position Encoding described in section 4.1 [1]
    """
    encoding = np.ones((embedding_size, sentence_size), dtype=np.float32)
    ls = sentence_size+1
    le = embedding_size+1
    for i in range(1, le):
        for j in range(1, ls):
            encoding[i-1, j-1] = (i - (embedding_size+1)/2) * (j - (sentence_size+1)/2)
        print encoding
    encoding = 1 + 4 * encoding / embedding_size / sentence_size
    #print encoding
    # Make position encoding of time words identity to avoid modifying them
    encoding[:, -1] = 1.0
    return np.transpose(encoding)

if __name__ == "__main__":

    #file_dir = current_file_path() + "/w3c-emails"
    #read_directory(file_dir)

    print(position_encoding(20, 2))

