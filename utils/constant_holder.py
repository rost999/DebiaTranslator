import os


APP_FONT = ("Verdana", 8)

RESOURCE_PATH = "res/"

GREETING_MESSAGE = """#######################
Debia Translator v0.1
With all the love from ZoomPal Team
Author = Darel
#######################"""

APP_NAME = "Debia Translator"
SUCCESS_ADDING_MESSAGE = "Successfully added the word to the dictionary"

TEXT_TO_TRANSLATE_LABEL = "Type here: "
TRANSLATION_RESULT_LABEL = "Result: "

TEXT_WORD_KEY = "Type here: "
TEXT_WORD_VALUE = "English version here: "

TRANSLATE_OPTION = "To translate phrase or word"
ADD_WORD_OPTION = "Add letter to the dictionary"
REMOVE_WORD_OPTION = "Remove letter from the dictionary"
MODIFY_WORD_OPTION = "Modify an existing word"

BUTTON_BACK_TEXT = "Go Back"
BUTTON_CONTINUE_TEXT = "Next"
BUTTON_SUBMIT_TEXT = "Submit"
BUTTON_EXIT_TEXT = "Exit"

# DISK_NAME = os.environ['SYSTEMROOT'][0:3]
INSERT_INTO = "INSERT INTO dictionary VALUES (?, ?)"
SELECT_WORD = "SELECT * FROM dictionary WHERE word_key=?"

SELECT_EVERYTHING = "SELECT * FROM dictionary"