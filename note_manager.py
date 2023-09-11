import json
import datetime

import text
from note import Note


class NoteManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.notes = []

    def save_notes(self, path):
        with open(path, 'w') as file:
            json.dump([note.__dict__ for note in self.notes], file)

    def read_notes(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                self.notes = [Note(**note_data) for note_data in data]

        except FileNotFoundError:
            print(text.checkName)

    def add_note(self):
        title = input(text.noteTitle)
        body = input(text.noteBody)
        id = len(self.notes) + 1
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note = Note(id, title, body, timestamp)
        self.notes.append(note)
        path = self.file_path
        self.save_notes(path)
        print(text.saveNote)

    def edit_note(self):
        result = False
        NoteManager.display_notes(self)
        id = int(input(text.noteNumber))
        for note in self.notes:
            if note.id == id:
                result = True
                NoteManager.print_notes(self, note)
                title = input(text.noteTitle)
                body = input(text.noteBody)
                note.title = title
                note.body = body
                note.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes(self.file_path)
                print(text.changesNote)
                break
        if not result:
            print(text.noteError)

    def delete_note(self):

        NoteManager.display_notes(self)
        try:
            id = int(input(text.deletingNote))
        except ValueError:
            print(text.checkNote)
            return -1

        if not NoteManager.search_notes(self, id):
            answer = input(text.agreement)
            if answer == text.yes:
                self.notes = [note for note in self.notes if note.id != id]
                self.save_notes(self.file_path)
                print(text.noteDel)

    def filter_notes(self, date):
        filtered_notes = [note for note in self.notes if note.timestamp.startswith(date)]
        for note in filtered_notes:
            NoteManager.print_notes(self, note)

    def display_notes(self):
        self.read_notes()
        for note in self.notes:
            NoteManager.print_notes(self, note)

    def print_notes(self, note):
        print(f"{text.numberNote} {note.id}")
        print(f"{text.nameNote} {note.title}")
        print(f"{text.textNote} {note.body}")
        print(f"{text.dateNote} {note.timestamp}")
        print()

    def search_notes(self, id):
        if self.notes:
            print(id)
            for note in self.notes:
                print(note.id)
                if note.id == id:
                    NoteManager.print_notes(self, note)
                    return False
            print(text.noteDelError)
            return True
        else:
            print(text.listIsEmpty)
            return True
