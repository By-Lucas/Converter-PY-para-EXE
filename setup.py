from cx_Freeze import setup, Executable

base = None    

executables = [Executable("colocar qui o nome do arquivo.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<any name>", #Nome do arquivo convertido se deixar da forma que está, vai pegar o nome do arquivo padrão
    options = options,
    version = "<any number>", #versão
    description = '<any description>', #Descrição
    executables = executables
)