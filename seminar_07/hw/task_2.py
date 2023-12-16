def create_init_file_with_function():
    init_file_content = '''
from os import listdir, rename

def rename_files(desired_name: str, num_digits: int, source_ext: str, target_ext: str, name_range: [int]=None) -> None:
     file_list = listdir('test_folder')
     file_list = [file for file in file_list if file.endswith(source_ext)]
     file_list.sort()

     for num, file in enumerate(file_list, 1):
         if name_range is None:
             name_range = [0, 0]
         if name_range[1] > (len(file) - len(source_ext) - 1):
             name_range[1] = len(file) - len(source_ext) - 1

         new_name = f'{file[name_range[0]: name_range[1]]}{desired_name}{num:0{num_digits}}.{target_ext}'
         rename(f'test_folder/{file}', f'test_folder/{new_name}')
    '''

    with open('__init__.py', 'w') as f:
        f.write(init_file_content)

if __name__ == '__main__':
    create_init_file_with_function()
