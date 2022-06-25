from pathlib import Path
import shutil
from file_parser import *
from normalize import normalize


def help_me(*args):
    return """Command format:
    help or ? - this help;
    parse folder_name- sorts files in the folder;
    good bye or close or exit or . - exit the program"""


def goodbye(*args):
    return 'Good bye!'


def handle_media(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / (normalize(filename.name[:-len(filename.suffix)]) + filename.suffix))


def handle_other(filename: Path, target_folder: Path):
    try:
        target_folder.mkdir(exist_ok=True, parents=True)
        filename.replace(target_folder / (normalize(filename.name[:-len(filename.suffix)]) + filename.suffix))
    except IsADirectoryError:
        return 'Unknown file'


def handle_archive(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()), str(folder_for_file.resolve()))
        #     normalize archive files
        for file in folder_for_file.iterdir():
            file.replace(folder_for_file / (normalize(file.name[:-len(file.suffix)]) + file.suffix))

    except shutil.ReadError:
        print(f'Not an archive {filename}!')
        folder_for_file.rmdir()
        return None
    filename.unlink()
    # .resolve gives absolute path


def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        return f"Folder deletion failed {folder}"


def file_parser(*args):
    try:
        folder_for_scan = Path(args[0])
        scan(folder_for_scan.resolve())
    except FileNotFoundError:
        return f"Not able to find '{args[0]}' folder. Please enter a correct folder name."
    except IndexError:
        return "Please enter a folder name."
    except IsADirectoryError:
        return 'Unknown file '
    for file in JPEG_IMAGES:
        handle_media(file, Path(args[0] + '/' + 'images' + '/' + 'JPEG'))
    for file in JPG_IMAGES:
        handle_media(file, Path(args[0] + '/' + 'images' + '/' + 'JPG'))
    for file in PNG_IMAGES:
        handle_media(file, Path(args[0] + '/' + 'images' + '/' + 'PNG'))
    for file in SVG_IMAGES:
        handle_media(file, Path(args[0] + '/' + 'images' + '/' + 'SVG'))
    for file in MP3_AUDIO:
        handle_media(file, Path(args[0] + '/' + 'audio' + '/' + 'MP3'))
    for file in OGG_AUDIO:
        handle_media(file, Path(args[0] + '/' + 'audio' + '/' + 'OGG'))
    for file in WAV_AUDIO:
        handle_media(file, Path(args[0] + '/' + 'audio' + '/' + 'WAV'))
    for file in AMR_AUDIO:
        handle_media(file, Path(args[0] + '/' + 'audio' + '/' + 'AMR'))
    for file in AVI_VIDEO:
        handle_media(file, Path(args[0] + '/' + 'video' + '/' + 'AVI'))
    for file in MP4_VIDEO:
        handle_media(file, Path(args[0] + '/' + 'video' + '/' + 'MP4'))
    for file in MOV_VIDEO:
        handle_media(file, Path(args[0] + '/' + 'video' + '/' + 'MOV'))
    for file in MKV_VIDEO:
        handle_media(file, Path(args[0] + '/' + 'video' + '/' + 'MKV'))
    for file in DOC_DOCUMENT:
        handle_media(file, Path(args[0] + '/' + 'document' + '/' + 'DOC'))
    for file in DOCX_DOCUMENT:
        handle_media(file, Path(args[0] + '/' + 'document' + '/' + 'DOCX'))
    for file in TXT_DOCUMENT:
        handle_media(file, Path(args[0] + '/' + 'document' + '/' + 'TXT'))
    for file in PDF_DOCUMENT:
        handle_media(file, Path(args[0] + '/' + 'document' + '/' + 'PDF'))
    for file in XLSX_DOCUMENT:
        handle_media(file, Path(args[0] + '/' + 'document' + '/' + 'XLSX'))
    for file in PPTX_DOCUMENT:
        handle_media(file, Path(args[0] + '/' + 'document' + '/' + 'PPTX'))
    for file in OTHER:
        handle_other(file, Path(args[0] + '/' + 'other'))

    for file in ARCHIVES:
        handle_archive(file, Path(args[0] + '/' + 'archives'))

    for folder in FOLDERS[::-1]:
        handle_folder(folder)

    return f"Files in {args[0]} sorted succesffully"


COMMANDS_F = {file_parser: ['parse '], help_me: ['?', 'help'], goodbye: ['good bye', 'close', 'exit', '.']}


def unknown_command(*args):
    return 'Unknown command! Enter again!'


def command_parser(user_command: str, COMMANDS: dict) -> (str, list):
    for key, list_value in COMMANDS.items():
        for value in list_value:
            if user_command.lower().startswith(value):
                args = user_command[len(value):].split()
                return key, args
    else:
        return unknown_command, []


def main():
    while True:
        user_command = input('Enter you command >>> ')
        command, data = command_parser(user_command, COMMANDS_F)
        print(command(*data), '\n')
        if command is goodbye:
            break
