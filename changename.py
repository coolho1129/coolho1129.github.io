import os
from natsort import natsorted
import argparse

def rename_files_in_folder(folder_path):
    file_list =natsorted(os.listdir(folder_path))
    #print(file_list)
    print()
    for i,filename in enumerate(file_list):
        old_filepath = os.path.join(folder_path, filename)
        new_filename = 'img'+str(i+1)+'.png'
        new_filepath = os.path.join(folder_path, new_filename)
        new_filepath=new_filepath.replace("\\", "/")
        os.rename(old_filepath, new_filepath)
        link = f"![{new_filename}]({{{'site.url'}}}/{new_filepath})" + "{: .align-center}"
        print(link)

if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description = '이미지 이름을 순서대로 img.png로 바꾸는 스크립트')
    # parser.add_argument('-src','-s', type = str, help = '이미지 파일 경로를 입력해주세요.')
    # args = parser.parse_args()
    # folder_path = args.src
    folder_path='images\CS231n\lecture02'
    rename_files_in_folder(folder_path)