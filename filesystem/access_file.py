import sys
import os
import getopt


def main(arguments):
    options, params = getopt.getopt(arguments, '', ['path=', 'file='])
    print(os.path.join(options[0][1], options[1][1]))


if __name__ == '__main__':
    main(sys.argv[1:])
