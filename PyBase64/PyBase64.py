import base64
import pyperclip

#mount__
def app():
    br = '[ptbr]Ponha a imagem na mesma pasta do cbbl_base64.py.'
    en = '[en]Put the image in the same folder as cbbl_base64.py.\n'
    print(br,'\n',en)
    print('\n png and gif are best formats, jpg and bmp are biggest, crash...\n')
    ity = str(input('Image extension : png[0], jpg[1], gif[2], bmp[3] : ')).strip()
    if(ity=='' or ity=='0'):
        ity = 'png'
    elif(ity=='1'):
        ity = 'jpg'
    elif(ity=='2'):
        ity = 'gif'
    elif(ity=='3'):
        ity = 'bmp'
    else:
        print('Invalid format')
        exit()

    html = '<img src="data:image/{};base64,'.format(ity)
    hend = '"/>'

    file_name = str(input('File name - [only name, no the extension...] : '))

    # action___    
    with open(f"{file_name}.{ity}", "rb") as img_file:
         my_string = base64.b64encode(img_file.read())
    #print(my_string)
    img64 = (my_string.decode('utf-8'))
    img_mount = (html + img64 + hend)
    pyperclip.copy(img_mount)

    print(img_mount)
    print('\nhtml5 img > Copied to your clipboard!\n')
app()
fn = str(input('Close app? [y]yes | [n] no: ')).strip().lower()
if(fn=='y'):
    exit()
else:
    app()




