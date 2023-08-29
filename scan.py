from pathlib import Path
import sys

jpeg_files = list()
png_files = list()
jpg_files = list()
svg_files = list()
gif_files = list()
bmp_files = list()
tif_files = list()
tiff_files = list()
txt_files = list()
docx_files = list()
doc_files = list()
pdf_files = list()
xlsx_files = list()
pptx_files = list()
folders = list()
archives = list()
mp3_files = list()
ogg_files = list()
wav_files = list()
amr_files = list()
avi_files = list()
mp4_files = list()
mov_files = list()
mkv_files = list()
others = list()
unknown = set()
extensions = set()


registered_extensions = dict(JPEG=jpeg_files, PNG=png_files, SVG=svg_files, GIF=gif_files, BMP=bmp_files, TIF=tif_files,
                             TIFF=tiff_files, JPG=jpg_files, TXT=txt_files, DOCX=docx_files, DOC=doc_files,
                             PDF=pdf_files, XLSX=xlsx_files, PPTX=pptx_files, ZIP=archives, GZ=archives, TAR=archives,
                             RAR=archives, MP3=mp3_files, OGG=ogg_files, WAV=wav_files, AMR=amr_files, AVI=avi_files,
                             MP4=mp4_files, MOV=mov_files, MKV=mkv_files)

def get_extensions(file_name):
    return Path(file_name).suffix[1:].upper()


def scan(folder):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('JPEG', 'PNG', 'JPG', 'TXT', 'DOCX', 'OTHERS', 'ARCHIVE',
                                 'SVG', 'GIF', 'BMP', 'TIF', 'TIFF', 'DOC', 'PDF', 'XLSX', 'PPTX',
                                 'GZ', 'TAR', 'RAR', 'MP3', 'OGG', 'WAV', 'AMR', 'AVI', 'MP4', 'MOV', 'MKV'):
                folders.append(item)
                scan(item)
            continue

        extension = get_extensions(file_name=item.name)
        new_name = folder/item.name
        if not extension:
            others.append(new_name)
        else:
            try:
                container = registered_extensions[extension]
                extensions.add(extension)
                container.append(new_name)
            except KeyError:
                unknown.add(extension)
                others.append(new_name)