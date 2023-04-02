# file-compressor
The software file compresses the input file using Huffman coding algorithm. 
Huffman coding is a lossless data compression algorithm. The idea is to assign variable-length codes to input characters, lengths of the assigned codes are based on the frequencies of corresponding characters. 
The variable-length codes assigned to input characters are Prefix Codes, means the codes (bit sequences) are assigned in such a way that the code assigned to one character is not the prefix of code assigned to any other character. This is how Huffman Coding makes sure that there is no ambiguity when decoding the generated bitstream.
The software is written in Python3

How to use:
1. Add data to be compressed in the 'sample.txt' file.
2. Run compressor.py
3. File will be compressed in "temp.shin"
4. To view the file, run decompressor.
5. "Output.txt" will be your decompressed file.

Note: The algo is not very efficient when the text is too short or too uniform. In some cases, the compressed file may be larger in size than the original.


References:
https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/
https://www.youtube.com/watch?v=sXPOBiABDHQ
