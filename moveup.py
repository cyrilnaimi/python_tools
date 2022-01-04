import shutil
import os

cst_extension = [
                '.mkv',
                '.avi',
                '.mp4',
                '.mp3',
                '.ogg',
                ]

class Torrentupper(object):
    """docstring for Torrentupper"""
    def __init__(self):
        super(Torrentupper, self).__init__()

    def scanfolder(self,afolder):
        result = {}
        for root, dirs, files in os.walk( afolder,topdown=False):
            for name in files:
                if name[-4:].lower() in cst_extension:
                    result[name] = os.path.join(root, name)
        return result

    def moveup(self,target_folder,dict_files):
        for file in dict_files.keys():
            if os.path.exists(os.path.join(target_folder, file)):
                print('Duplicate file : {} - {}'.format(file, dict_files[file]))
            else:
                print('move from {} to {}'.format(dict_files[file], target_folder))
                shutil.move(dict_files[file], os.path.join(target_folder, file))


def main():
    upper = Torrentupper()
    s = upper.scanfolder('.')
    print(s.items())
    upper.moveup('.',s)


if __name__ == "__main__":
    main()

