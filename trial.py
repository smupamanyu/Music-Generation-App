from gooey import Gooey, GooeyParser
import os
@Gooey(optional_cols=2,program_name="Music Generator",image_dir='C:/Users/Upamanyu/Downloads/generate-music-main/imagedir',
       menu=[{
        'name': 'File',
        'items': [{
                'type': 'AboutDialog',
                'menuTitle': 'About',
                'name': 'Music Generator',
                'description': 'Music generator built as our final project during our 2nd year in college, studying CSE',
                'version': 'b1.0',
                'copyright': '2023',
                'website': 'https://www.linkedin.com/in/upamanyu-sinha-mahapatra-477100257/\nhttps://www.linkedin.com/in/upamanyu-sinha-mahapatra-477100257/',
                'developer': 'http://chriskiehl.com/',
                'license': 'Open Source'
            }, {
                'type': 'MessageDialog',
                'menuTitle': 'Information',
                'caption': 'My Message',
                'message': 'I am demoing an informational dialog!'
            }, {
                'type': 'Link',
                'menuTitle': 'Get Data',
                'url': 'https://data.ccca.ac.at/group/climaproof'
            }]
        },{
        'name': 'Help',
        'items': [{
            'type': 'Link',
            'menuTitle': 'Documentation',
            'url': 'https://www.readthedocs.com/foo'
        }]
    }]
       )
def parse_args():
    prog_descrip = 'A music generator by Kesav and Upamanyu'
    parser = GooeyParser(description=prog_descrip)

    sub_parsers = parser.add_subparsers(help='commands', dest='command')

    first_parser = sub_parsers.add_parser('Generation',help='You generate the melody here')

    first_parser.add_argument('--Bars',help='Enter number of bars [1-8]',type=int,widget='Slider', gooey_options={
    'min': 1, 
    'max': 8, 
    })
    first_parser.add_argument('--Notes',help='Enter number of Notes [1-4]',type=int,widget='Slider', gooey_options={
    'min': 1, 
    'max': 4, 
    })
    first_parser.add_argument('--Root',help='Enter root of scale [1-4]',type=int,widget='Slider', gooey_options={
    'min': 1, 
    'max': 4, 
    })
    first_parser.add_argument('--Population_Size',help='Enter population size [1-10]',type=int,widget='Slider', gooey_options={
    'min': 1, 
    'max': 10, 
    })
    first_parser.add_argument('--mutations',help='Enter number of mutations [1-2]',type=int,widget='Slider', gooey_options={
    'min': 1, 
    'max': 2, 
    })
    first_parser.add_argument('--bpm',help='Sets tempo of the song [1-250]',type=int,widget='Slider', gooey_options={
    'min': 1, 
    'max': 250, 
    })
    first_parser.add_argument( 
        "--Scale", choices=['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'],
        required=True,
        nargs='*',
        widget="Listbox",
        default='separate',
        help="Select Scale, choosing multiple will default to C"
    )

    first_parser.add_argument('--Pauses',help='Do you want to introduce pauses?',action='store_true')

    second_parser = sub_parsers.add_parser('How to use',help='helps the use understand how to use the program')

    #second_parser.add_argument('folder_path',help='Select a folder',type=str,widget='DirChooser')

    #second_parser.add_argument('--file-type',help='Specify file type with .jpg',type=str)

    args = parser.parse_args()

    return args
def func1(totalinput):
    file_name = 'example.txt'

    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(str(totalinput))
def func2(totalinput):
    file_name = 'example.txt'

    with open(file_name, 'a+', encoding='utf-8') as f:
        f.write(str(f'\n{totalinput}'))
def func3(totalinput):
    file_name = 'example.txt'

    with open(file_name, 'a+', encoding='utf-8') as f:
        f.write(str(f'\n{totalinput}'))
def func4(totalinput):
    file_name = 'example.txt'

    with open(file_name, 'a+', encoding='utf-8') as f:
        f.write(str(f'\n{totalinput}'))
def func5(totalinput):
    file_name = 'example.txt'

    with open(file_name, 'a+', encoding='utf-8') as f:
        f.write(str(f'\n{totalinput}'))
def func6(totalinput):
    file_name = 'example.txt'

    with open(file_name, 'a+', encoding='utf-8') as f:
        f.write(str(f'\n{totalinput}'))
def func7(totalinput):
    file_name = 'example.txt'

    with open(file_name, 'a+', encoding='utf-8') as f:
        f.write(str(f'\n{totalinput}'))
def func8(totalinput):
    file_name = 'example.txt'

    with open(file_name, 'a+', encoding='utf-8') as f:
        f.write(str(f'\n{totalinput}'))

''''
def print_file_name(path,filesize):
    """
    Inputs:
        path (str): filepath to file selected
        filezize (bool): whether to print the file size or not
    Prints file name of file from path given and if filesize is true then will print the total size of the file in bytes
    """
    print(os.path.basename(path))
    if filesize:
        print(f"File size: {os.path.getsize(path)} bytes")

def get_files_in_folder(path,extension):
    """
    Inputs:
        path (str): path to folder selected
        extension (str): extension to filter by
    Prints all files in folder, if an extension is given, will only print the files with the given extension
    """
    f = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        if extension:
            for filename in filenames:
                if filename.endswith(extension):
                    f.append(filename)
        else:
            f.extend(filenames)
    return f
    '''


if __name__ == '__main__':
    conf = parse_args()
    func1(conf.Bars)
    func2(conf.Notes)
    func3(conf.Root)
    func4(conf.Population_Size)
    func5(conf.mutations)
    func6(conf.Scale)
    func7(conf.Pauses)
    func8(conf.bpm)
    
    '''
    if conf.command == 'file':
        print_file_name(conf.file_path,conf.file_size)
    elif conf.command == 'folder':
        print(get_files_in_folder(conf.folder_path,conf.file_type))
        '''