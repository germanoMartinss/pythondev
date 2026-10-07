import glob, os, zipfile

#1- Diretório de trabalho atual
print(os.getcwd())

#2- Listar arquivos do diretório atual
print(glob.glob('manipulação_arquivos/dados/*.txt'))

#3- Compactar arquivos .txt
with zipfile.ZipFile('manipulação_arquivos/dados/arquivos.zip', 'w') as zip:
    for file in glob.glob('manipulação_arquivos/dados/*.txt'):
        zip.write(file)