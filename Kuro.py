from flask import Flask, request, send_file, redirect
from pystyle import *
from pystyle import Colors
from webbrowser import open_new as start
from socket import gethostname, gethostbyname
from os import listdir, chdir, name
from os.path import isfile
import os
import time


text = r'''
 _     _ _     _  ______  _____ 
 |____/  |     | |_____/ |     |
 |    \_ |_____| |    \_ |_____|
                                '''

kuro = r'''
                     /\                               ______,....----,
       /VVVVVVVVVVVVVV|===================""""""""""""       ___,..-'
       `^^^^^^^^^^^^^^|======================----------""""""
                     \/
             P R E S S   E N T E R   T O   C O N T I N U E...
                
                                
'''

a = r'''
     /\                    /\
     \ \                  / /
      \ \                / /
       \.\              /./
        \.\            /./
         \.\          /./
          \\\        ///
           \.\      /./
            \.\    /./
             \.\__/./
            _/)))(((\_       
            \|)\##/(|/
            _|)/##\(|_
            \|)))(((|/
             /o/  \o\
            /o/    \o\
           /_/      \_\
'''


banner = Add.Add(text, a, center=True)

def tui():
    System.Clear()
    print()
    print(Colorate.Diagonal(Colors.DynamicMIX([Colors.light_gray, Colors.dark_gray, Colors.light_gray, Colors.dark_gray]), Center.XCenter(banner)))
    System.Title("Kuro")
    print()
    print(f" {Col.Symbol('-_-', Col.white, Col.dark_gray)} {Col.white}Kuro{Col.dark_gray} - Simple {Col.light_gray}tools{Col.dark_gray} to share files on your {Col.white}local{Col.dark_gray} network{Col.reset} ")
    print()
    print(f" {Col.Symbol('<3', Col.white, Col.dark_gray)} {Col.dark_gray}Go to {Col.white}github.com/ZeusFuckYou/Kuro{Col.dark_gray} to download this tool{Col.white} !{Col.reset} ")
    print('\n')

app = Flask("Kuro")


def run(host: str, port: int):
    return app.run(host, port)


def render(filename: str):
    with open(filename, mode='r', encoding='utf-8') as f:
        return f.read()

def ren(text: str, status_code: int = 200) -> tuple:
    print(f"Returned {text} | Status code : {status_code}")
    return text, status_code


@app.route('/', methods=['GET'])
def main_route():
    return render('src/index.html')


@app.route('/upload', methods=['POST'])
def upload_route():
    try:
        name = request.args['filename']
        if not name.strip():
            return ren('are you sure you entered a correct file ?')
        f = request.files['file']
        f.save(f'db/{name}')
        return redirect('/')
    except Exception as e:
        return ren(f'error: {e}')

@app.route('/get/<filename>', methods=['GET'])
def get_route(filename):
    filename = f'db/{filename}'
    if isfile(filename):
        return send_file(filename, as_attachment=True)
    for file in listdir('db'):
        fullpath = 'db/' + file
        path = 'db/' + "".join(file.split('.')[0:-1])
        if path == filename:
            return send_file(fullpath, as_attachment=True)
    return send_file('db/kuro.jpg', as_attachment=True)


@app.route('/images/<image>', methods=['GET'])
def image_route(image):
    imagename = f'src/images/{image}'
    if isfile(imagename):
        return send_file(imagename, as_attachment=True)
    else:
        return send_file('db/kuro.jpg', as_attachment=True)

System.Title('Kuro')
Anime.Fade(Center.Center(kuro), Colors.white_to_black,
           Colorate.Diagonal, enter=True)

def main():
    tui()

    hostname = gethostname()
    local_ip = gethostbyname(hostname)

    host = input(f" {Col.Symbol('?', Col.white, Col.dark_gray)} {Col.dark_gray}Enter the host ( {Col.white}press 'enter' for your local ip address{Col.dark_gray} ) {Col.white}-> ")
    if host == '':
        host = local_ip

    print()

    port = input(f" {Col.Symbol('?', Col.white, Col.dark_gray)} {Col.dark_gray}Enter the port ( {Col.white}press 'enter' for 8080{Col.dark_gray} ) {Col.white}-> {Col.dark_gray}")
    if port == '':
        port = "8080"
    try:
        port = int(port)
    except ValueError:
        print(f" {Col.Symbol('!', Col.white, Col.dark_gray)} {Col.white}Error ! {Col.dark_gray}Port has to be an integer.")
        time.sleep('3')
        return

    print('\n')

    input(f" {Col.Symbol('+', Col.white, Col.dark_gray)} Press '{Col.white}enter{Col.dark_gray}' to start the {Col.white}server {Col.dark_gray}!")

    url = f"http://{host}:{port}/"
    start(url)
    tui()
    run(host=host, port=port)
    


if __name__ == '__main__':
    while True:
        main()
