import sys
import shutil
import scan
import normalize
from pathlib import Path

from files_generator import file_generator


def hande_file(path, root_folder, dist):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    path.replace(target_folder / normalize.normalize(path.name))


def handle_archive(path, root_folder, dist):

    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)


    new_name = normalize.normalize(path.name.replace('.zip', ''))

    new_name = normalize.normalize(path.name.replace('.gz', ''))

    new_name = normalize.normalize(path.name.replace('.rar', ''))

    new_name = normalize.normalize(path.name.replace('.tar', ''))

    archive_folder = root_folder / new_name
    archive_folder.mkdir(exist_ok=True)

    try:
        shutil.unpack_archive(str(path.resolve()), str(path.resolve()))

    except FileNotFoundError:
        archive_folder.rmdir()
        return

    except shutil.ReadError:
        archive_folder.rmdir()
        return
    path.unlink()


def remove_empty_folders(path):
    for item in path.iterdir():
        if item.is_dir():
            remove_empty_folders(item)
            try:
                item.rmdir()
            except OSError:
                pass


def get_folder_objects(root_path):
    for folder in root_path.iterdir():
        if folder.is_dir():
            remove_empty_folders(folder)
            try:
                folder.rmdir()
            except OSError:
                pass


def main(folder_path):
    scan.scan(folder_path)

    for file in scan.jpeg_files:
        hande_file(file, folder_path, "images")

    for file in scan.jpg_files:
        hande_file(file, folder_path, "images")

    for file in scan.png_files:
        hande_file(file, folder_path, "images")

    for file in scan.svg_files:
        hande_file(file, folder_path, "images")

    for file in scan.gif_files:
        hande_file(file, folder_path, "images")

    for file in scan.bmp_files:
        hande_file(file, folder_path, "images")

    for file in scan.tif_files:
        hande_file(file, folder_path, "images")

    for file in scan.tiff_files:
        hande_file(file, folder_path, "images")

    for file in scan.txt_files:
        hande_file(file, folder_path, "documents")

    for file in scan.docx_files:
        hande_file(file, folder_path, "documents")

    for file in scan.doc_files:
        hande_file(file, folder_path, "documents")

    for file in scan.pdf_files:
        hande_file(file, folder_path, "documents")

    for file in scan.xlsx_files:
        hande_file(file, folder_path, "documents")

    for file in scan.pptx_files:
        hande_file(file, folder_path, "documents")

    for file in scan.mp3_files:
        hande_file(file, folder_path, "audio")

    for file in scan.ogg_files:
        hande_file(file, folder_path, "audio")

    for file in scan.wav_files:
        hande_file(file, folder_path, "audio")

    for file in scan.amr_files:
        hande_file(file, folder_path, "audio")

    for file in scan.avi_files:
        hande_file(file, folder_path, "video")

    for file in scan.mp4_files:
        hande_file(file, folder_path, "video")

    for file in scan.mov_files:
        hande_file(file, folder_path, "video")

    for file in scan.mkv_files:
        hande_file(file, folder_path, "video")

    for file in scan.others:
        hande_file(file, folder_path, "OTHERS")

    for file in scan.archives:
        hande_file(file, folder_path, "archives")

    get_folder_objects(folder_path)

if __name__ == '__main__':
    path = sys.argv[1]
    print(f"Start in {path}")

    arg = Path(path)

    main(arg.resolve())