import sys
import os
import getopt
import time


def main(args):
    optlist, params = getopt.getopt(args, '', ['dir=', 'file='])
    dir_name = optlist[0][1]
    file_name = optlist[1][1]

    print('Current path is {}'.format(os.getcwd()))
    print('*****')
    print('Changing current directory...')
    print('*****')

    if os.path.isdir(dir_name):
        os.chdir(dir_name)
        print('Directory successfuly changed')
        print('*****')
        print('Current path is {}'.format(os.getcwd()))
        print('*****')
        print('Searching for {}...'.format(file_name))
        search_file(dir_name, file_name)
    else:
        print('Error: Path does not exist')
        print('*****')


def search_file(path, file_name):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file_name == file:
                print('File path: {}'.format(os.path.join(root, file)))
                return
            print(os.path.join(root, file), end='\r', flush=True)
            sys.stdout.write('\033[K')
            time.sleep(0.2)
    print('File was not found')


if __name__ == '__main__':
    main(sys.argv[1:])
