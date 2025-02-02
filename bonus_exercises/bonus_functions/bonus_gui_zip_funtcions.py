import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

def extract_archive(archive_path, dest_dir):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    user_action = input("zip or un-zip")
    if user_action == 'zip':
        make_archive(filepaths=['bonus_functions.py',
                                'bonus_gui_zip_creator.py'],
                                dest_dir='zip_test_dest')
    elif user_action == 'un-zip':
        extract_archive(archive_path='zip_test_dest/compressed.zip', dest_dir='zip_test_dest')