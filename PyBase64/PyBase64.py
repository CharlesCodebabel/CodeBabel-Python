import base64, pyperclip

#mount__
def app():
    inf_ = ["[ptbr]Ponha a imagem na mesma pasta do cbbl_base64.py.\n",
            "[en]Put the image in the same folder as cbbl_base64.py.\n",
            "png and gif are best formats, jpg and bmp are biggest, crash\n"
    ]
    
    print(inf_[0], inf_[1], inf_[2])
    image_format = int(input('Image extension : png [0], jpg [1], gif [2], bmp [3] : ')).strip()
    match image_format:
        case 0:
            image_format = 'png'
        case 1:
            image_format = 'jpg'
        case 2:
            image_format = 'gif'
        case 3:
            image_format = 'bmp'
        case _:
            print('Invalid format')
            exit()

    html = '<img src="data:image/{};base64,'.format(image_format); hend = '"/>'
    file_name = str(input('File name - [ only name, no the extension... ] : '))

    # action___    
    with open(f"{file_name}.{image_format}", "rb") as img_file:
         my_string = base64.b64encode(img_file.read())
    #print(my_string)
    img64 = (my_string.decode('utf-8')); img_mount = (html + img64 + hend); pyperclip.copy(img_mount)
    print(img_mount, '\n html5 img > Copied to your clipboard!\n')
app()

'{ close app }'
function_close = str(input('Close app? [y] yes | [n] no: ')).strip().lower()
if(function_close == 'y'):
    exit()
else:
    app()




