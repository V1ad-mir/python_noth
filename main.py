1import datetime
import shutil

import text
from note_manager import NoteManager
from file_manager import FileManager

note_manager = NoteManager(text.defaultFileName)
note_manager.save_notes(text.defaultFileName)
name = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + text.expansion

while True:
    command = input(text.textMenu)
    match command:
        case "1":
            note_manager.add_note()
        case "2":
            note_manager.edit_note()
        case "3":
            note_manager.delete_note()
        case "4":
            date = input(text.dateInput)
            note_manager.filter_notes(date)
        case "5":
            note_manager.display_notes()
        case "6":
            file_manager = FileManager()
            file_manager.scan_folder()
            print()
        case "7":
            try:
                name = (input(text.nameFile) + text.expansion)
                shutil.copy2(name, text.defaultFileName)
                note_manager.read_notes()
                print(text.successLoad)
            except FileNotFoundError:
                print(text.checkFile)

        case "8":
            note_manager.save_notes(FileManager.save_file(name))
        case "9":
            name_file = (input(text.nameFile) + text.expansion)
            FileManager.delete_file(name_file)
        case "0":
            answer = input(text.yesSave).lower()
            if answer == text.yes:
                note_manager.save_notes(FileManager.save_file(name))
            FileManager.delete_file(text.defaultFileName)
            break
        case _:
            print(text.menuError)
