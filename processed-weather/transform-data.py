import os


folder_path = 'downloaded_files'


substring1 = 'Weg zonder naam, Amsterdam, Netherlands'
substring2 = 'Weg zonder naam Amsterdam Netherlands'


for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    with open(file_path, 'r') as file:
        content = file.read()


    content = content.replace(substring1, f'"{substring2}"')



    with open(file_path, 'w') as file:
        file.write(content)

