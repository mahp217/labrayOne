import os
import shutil


def main():
    # input source folder address
    source_folder = input('Input source folder: ')
    # source_folder = 'C:\\Users\\xxx\\Source\\Repos\\xxx'

    # input target folder address
    target_folder = input('Input target folder: ')

    # input key words
    key_words = input('Input key word: ').split()

    print('Debug !!')
    print(source_folder)
    
    # loop folder using walk()
    for dirpath, dirnames, filenames in os.walk(source_folder):

        # for each file, get file name
        for filename in filenames:

            if 'obj' in dirpath or 'Bin' in dirpath:
                print(dirpath)
                continue

            if ".TMP" in filename:
                print(filename)
                continue

            # copy files from My Project folder
            count = 0
            for key_word in key_words:
                if key_word.upper() in filename.upper():
                    count += 1
                if key_word.upper() in dirpath and 'My Project' in dirpath:
                    count += 1
            if count == 0:
                continue

            source_filepath = os.path.join(dirpath, filename)

            # create folder in target folder
            target_dirpath = dirpath.replace(source_folder, target_folder)
            if not os.path.isdir(target_dirpath):
                os.makedirs(target_dirpath)

            # copy file to target folder
            target_filepath = os.path.join(target_dirpath, filename)
            shutil.copy2(source_filepath, target_filepath)

if __name__ == '__main__':
    main()
