from collections import UserList

class Tag:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return self.value
    
class Note:
    def __init__(self, note) -> None:
        self.note = note
        self.tags = []

    def __str__(self) -> str:
        return f"Note {self.note},\n Tags {[tag.value for tag in self.tags]}"
    
    def __exist_tag(self, tag):
        if self.find_tag(tag):
            raise Exception("Tag already exist")
    
    def show_all_tag(self):
        return [tag.value for tag in self.tags]

    def add_tags(self, tags: list):
        for t in tags:
            self.__exist_tag(t)
            self.tags.append(Tag(t))
        return f"{tags} tags added successfully"

    def find_tag(self, tag) -> Tag | None:
        for i in self.tags:
            if i.value == tag:
                return i      
    
    def delete_tag(self, tags):
        for t in tags:
            self.tags.remove(self.find_tag(t))

        return f"{tags} tags deleted successfully"

class Notes(UserList):

    def __exist_note(self, note):
        if self.find_note(note):
            raise Exception("Note already exist")
        
    def __does_not_exist_note(self, note):
        if not self.find_note(note):
            raise Exception("Note does not exist")
        
    def find_all_note(self) -> list:
        return [notes.note for notes in self.data]
    
    def find_note(self, note: str) -> Note:

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
    
    def find_notes_by_tag(self, tag: str) -> list:
        result = []
        for note in self.data:
            if any(t.value == tag for t in note.tags):
                result.append(note.note)
        return result

