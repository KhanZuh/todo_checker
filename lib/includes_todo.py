def includes_todo(notes):
    return any("#todo" in note.lower() for note in notes)
    
# Refactored for any("#TODO" in note for note in notes) for case insensitivity
