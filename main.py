# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import typing, time, cProfile, pathlib, sys, os


class Audiomack:
    def __init__(self, sourcedir: str, savedir: str):
        """
        Class we are going to use to add the dir of mp3s and output
        :param sourcedir:
        :param savedir:
        """
        self.sourcedir = sourcedir
        self.savedir = savedir
        self.log = ""

    def load_data(self, sourcedir: str) -> list:
        """
        :param sourcedir:
        :return: list
        """
        dir = self.sourcedir
        file_list = list()

        for entry in os.scandir(dir):
            f = os.path.join(dir, entry)

            if (os.path.isfile(f)):
                # print(f"{f}")

                str_path = str(f)

                chars = str_path[-4:]

                if chars == ".mp3" or chars == "mp3":
                    print(f"Boogie {str_path}")
                else:
                    os.rename(f, str_path + ".mp3")
            # else:
            # print(f"Not- {f}")

            # if entry[-4:-1] == ".mp3":
            #     print(f"song")

        return file_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(f"Arguments count: {len(sys.argv)} ")

    # audio = Audiomack(sys.argv[0], sys.argv[1])
    # audio.load_data(sys.argv[0])
    audio = Audiomack("C:\\music", "C:\\out")
    audio.load_data(audio.sourcedir)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
