# coding=utf-8
import os
import sys

#Convert NLP4J's output into CoNLL's 10-column format
def convert(inputFile):
    writer = open(inputFile + ".conll", "w")
    for line in open(inputFile, "r").readlines():
        eles = line.strip().split()
        if len(eles) == 0:
            writer.write("\n")
        else:
            eles[4] = "_"
            eles.insert(4, eles[3])
            writer.write("\t".join(eles) + "\n")

    writer.close()

if __name__ == "__main__":
    convert(sys.argv[1])