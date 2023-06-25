import os
from datetime import datetime

NOTES_DIR = r"C:\Users\vego\Documents\Notes"  # директория, в которой находятся заметки
DIR_PATH = NOTES_DIR or os.path.dirname(os.path.realpath(__file__))

DAILY_DIR_NAME = 'daily'
DATE_NOTE_FORMAT = '%Y-%m-%d'
DIR_WITH_NOTES = os.path.join(DIR_PATH, DAILY_DIR_NAME)


class UnsortedNotesIsNotInDir(Exception):
    def __init__(self):
        super().__init__('Unsorted notes is not in directory!')


def get_all_unsorted_notes() -> list[str] | None:
    return next(os.walk(DIR_WITH_NOTES), (None, None, []))[2]


def create_directory(dir_path: str) -> None:
    if os.path.exists(dir_path):
        return
    os.mkdir(dir_path)
    print(f'{dir_path} created successfully!')


def move_file(old_path: str, new_path: str) -> None:
    os.replace(old_path, new_path)
    print(f'Note {old_path} moved to -> {new_path}')


def sorted_notes():
    all_unsorted_notes = get_all_unsorted_notes()
    if not all_unsorted_notes:
        raise UnsortedNotesIsNotInDir
    for name_note in all_unsorted_notes:
        date_note = datetime.strptime(name_note.replace('.md', ''), DATE_NOTE_FORMAT)
        double_digit_month, month_short_name = date_note.strftime("%m"), date_note.strftime('%b')
        year_month_dir_name = os.path.join(DIR_WITH_NOTES, f'{date_note.year}_{double_digit_month}_{month_short_name}')
        create_directory(year_month_dir_name)

        old_note_path = os.path.join(DIR_WITH_NOTES, name_note)
        new_note_path = os.path.join(DIR_WITH_NOTES, year_month_dir_name, name_note)
        move_file(old_note_path, new_note_path)


if __name__ == '__main__':
    sorted_notes()
