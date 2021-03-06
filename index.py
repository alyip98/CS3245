#!/usr/bin/python3
import sys
import getopt
import time

from inverted_index import InvertedIndex


def usage():
    print("usage: " + sys.argv[0] + " -i directory-of-documents -d dictionary-file -p postings-file")


"""
    build index from documents stored in the input directory,
    then output the dictionary file and postings file
"""

def build_index(in_dir, out_dict, out_postings):

    print('Indexing...')

    # This is an empty method
    # Pls implement your code in below

    start_time = time.perf_counter()
    inverted_index_class = InvertedIndex(in_dir, out_dict, out_postings)
    inverted_index_class.construct_index()
    end_time = time.perf_counter()
    print("Indexed in {:.2f}s".format(end_time-start_time))



input_directory = output_file_dictionary = output_file_postings = None

try:
    opts, args = getopt.getopt(sys.argv[1:], 'i:d:p:')
except getopt.GetoptError:
    usage()
    sys.exit(2)

for o, a in opts:
    if o == '-i': # input directory
        input_directory = a
    elif o == '-d': # dictionary file
        output_file_dictionary = a
    elif o == '-p': # postings file
        output_file_postings = a
    else:
        assert False, "unhandled option"

if input_directory == None or output_file_postings == None or output_file_dictionary == None:
    usage()
    sys.exit(2)

build_index(input_directory, output_file_dictionary, output_file_postings)
