#!/usr/bin/env python
from checkmate import checkmate
import sys
def main():
    board = """\
.R.
.A.
.K.\
"""
    if len(sys.argv) > 1:
        for i in sys.argv[1:]:
            board = i
            checkmate(board)
    else:
        checkmate(board)
        


if __name__ == "__main__":
    main()
