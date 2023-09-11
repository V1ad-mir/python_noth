import os
import text
import shutil

import note_manager


class FileManager:

    def scan_folder(self):
        file_path = '.'
        rez = sorted(os.listdir(file_path))
        for n, item in enumerate(rez):
            if text.expansion in item:
                print(item)

    def delete_file(name_file):
        try:
            os.remove(name_file)
        except FileNotFoundError:
            print(text.errorFile)

    def save_file(name):
        print(text.currentFileName + name + text.newName)
        name1 = (input() + text.expansion)
        if (name1 == text.expansion):
            file_path = name
        else:
            file_path = name1
        return file_path
