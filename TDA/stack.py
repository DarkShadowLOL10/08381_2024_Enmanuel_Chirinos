def poner(s, datos): #el pass es para que no tire error, se puede borrar sintaxis de python
    s.append(datos)
    return(s)

def quitar(s):
    s = s[0:largo(s)-1]
    return(s)

def largo():
    s = []
    return(len(s))

def top(s):
    e = s[len(s)-1]
    return(e)