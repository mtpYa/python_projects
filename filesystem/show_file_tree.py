import sys
import getopt


def main(args):
    optlist, arg1 = getopt.getopt(args, 'ab:', ['name=', 'surname='])

    print(optlist)
    print(arg1)


if __name__ == '__main__':
    main(sys.argv[1:])
