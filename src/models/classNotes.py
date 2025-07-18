from collections import UserList

class Note:
    def __init__(self, note) -> None:
        self.note = note

    def __str__(self) -> str:
        return self.note


class Notes(UserList):

    def __exist_note(self, note):
        if self.find_note(note):
            raise Exception("Note already exist")
        
    def __does_not_exist_note(self, note):
        if not self.find_note(note):
            raise Exception("Note does not exist")
        

    def find_all_note(self) -> list:
        return [notes.note for notes in self.data]
    
    def find_note(self, note: str):
        for notes in self.data:
            if notes.note == note:
                return notes

    def add_note(self, note: str) -> str:

        self.__exist_note(note)
        self.data.append(Note(note))
        return f"{note} note added successfully"
    
    def edit_note(self, note: str, new_note: str) -> str:

        self.delete_note(note)
        self.add_note(new_note)
        return f"{note} note edited successfully"
    
    def delete_note(self, note: str) -> str:
 
        self.__does_not_exist_note(note)
        self.data.remove(self.find_note(note))
        return f"{note} note deleted successfully"
    
    def find_text_in_note(self, text: str) -> list:

        result = []
        for notes in self.data:
            if text in notes.note:
                result.append(notes.note)

        return result



    
if __name__ == "__main__":
    note = Notes()

    note.add_note("some note1")
    note.add_note("some note2")
    note.add_note("some note3")
    note.add_note("note about record")
    note.add_note("some note4")
    note.add_note("is a good palayer")
    
    print(note.find_all_note())

    print(note.find_note("some note4"))

    print(note.delete_note("some note4"))
    print(note.find_all_note())

    print(note.edit_note("some note1", "some note1222"))
    print(note.find_all_note())

    print(note.find_text_in_note("some"))
    print(note.find_text_in_note("palayer"))

