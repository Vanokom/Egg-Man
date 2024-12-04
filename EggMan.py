def человек():
    return input()

def яйца(*args):
    print(*args)

def interpreter(code):
    code = code.replace("яйца", "print")
    code = code.replace("человек", "input")
    code = code.replace("яйЦа", "if")
    code = code.replace("яЙца", "else")
    code = code.replace("крутой", "elif")
    
    exec(code)

# Программу здесь пиши
code = """
яйца ("Сделан TimBoom, язык написан ради прикола, и так же можеть добовлять в этот py файл. Идея моя, но мне еще помогал Ivan Rulit 721, спасибо ему за идею и что вспомнил эту легенду. Создатель: Тот Самый, и песня называется: Человек Яйца")
ал = человек ()
яйЦа ал == "Сигма":
     яйца ("ПОСХАЛОК")
яЙца:
     яйца ("Все")
"""

interpreter(code)