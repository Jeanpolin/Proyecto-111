import os
import shutil

from_dir="F:/Users/ME/Downloads/imagenes proyecto 111"
to_dir = "F:/Users/ME/Documents/byjus/recibir imagenes proyecto 111"

list_of_files=os.listdir(from_dir)
print(list_of_files)
extension_to_move = ['.png','.jpg','.jpeg']
for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    if extension in extension_to_move:
        source_path = os.path.join(from_dir, file_name)
        destination_path = os.path.join(to_dir, file_name)

    shutil.move(source_path, destination_path)
    print(f"Moved {file_name} to {to_dir}")

print("cambiando de lugar los archivos")