import os


APP_FONT = ("Verdana", 8)

RESOURCE_PATH = "res/"

GREETING_MESSAGE = """#######################
Devia Translator v0.1
With all the love from ZoomPal Team
Author = Darel
#######################"""

APP_NAME = "Devia Translator"
SUCCESS_ADDING_MESSAGE = "Successfully added the word to the dictionary"
QUESTION_TO_MODIFY_TEXT = "Are you sure, you want to modify the english version of this word ?"

TEXT_TO_TRANSLATE_LABEL = "Type here: "
TRANSLATION_RESULT_LABEL = "Result: "

TEXT_WORD_KEY = "Type here: "
TEXT_WORD_VALUE = "English version here: "

TEXT_OLD_WORD_VALUE = "Old english version here: "
TEXT_NEW_WORD_VALUE = "New english version here: "

TRANSLATE_OPTION = "To translate phrase or word"
ADD_WORD_OPTION = "Add letter to the dictionary"
REMOVE_WORD_OPTION = "Remove letter from the dictionary"
MODIFY_WORD_OPTION = "Modify an existing word"

BUTTON_BACK_TEXT = "Go Back"
BUTTON_CONTINUE_TEXT = "Next"
BUTTON_SUBMIT_TEXT = "Submit"
BUTTON_EXIT_TEXT = "Exit"

KEY_TO_DELETE_TEXT = "Enter the key to delete"

# DISK_NAME = os.environ['SYSTEMROOT'][0:3]
INSERT_INTO = "INSERT OR IGNORE INTO dictionary VALUES (?, ?)"
SELECT_WORD = "SELECT * FROM dictionary WHERE word_key=?"
DELETE_WORD = "DELETE FROM dictionary WHERE word_key=?"
SELECT_EVERYTHING = "SELECT * FROM dictionary"

UPDATE_WORD_KEY_VALUE = "UPDATE dictionary SET word_value = ? WHERE word_key= ?"