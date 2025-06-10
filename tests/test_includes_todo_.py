from lib.includes_todo import *

def test_includes_todo_returns_true_when_line_contains_todo():
    notes = [
        "pickup groceries",
        "#TODO buy milk",
        "call mom"
    ]
    result = includes_todo(notes)
    assert result == True
    
def test_includes_todo_returns_false_when_line_does_not_contain_todo():
    notes = [
        "pickup groceries",
        "call mom"
    ]
    result = includes_todo(notes)
    assert result == False

    notes_2 = [
        "pickup groceries",
        "TODO buy milk",
        "call mom"
    ]
    result_2 = includes_todo(notes_2)
    assert result_2 == False

def test_includes_todo_returns_false_for_empty_notes():
    notes = []
    result = includes_todo(notes)
    assert result == False

def test_includes_todo_returns_True_when_todo_not_at_start():
    notes = [
        "pickup groceries",
        "buy milk #TODO",
        "call mom"
    ]
    result = includes_todo(notes)
    assert result == True

