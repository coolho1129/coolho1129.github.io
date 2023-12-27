import os
from natsort import natsorted

def rename_files_in_folder(folder_path):
    # 폴더 내의 파일 목록을 가져옴
    file_list =natsorted(os.listdir(folder_path))
    print(file_list)

    for i,filename in enumerate(file_list):
        old_filepath = os.path.join(folder_path, filename)
        new_filename = 'img'+str(i+1)+'.png'
        new_filepath = os.path.join(folder_path, new_filename)
        os.rename(old_filepath, new_filepath)

if __name__ == "__main__":
   
    folder_path = "images\MLRecog"  
    rename_files_in_folder(folder_path)