
def imatges(res):
    if res<=8:
        v="static/ocho.png"
    if res==9:
        v="static/nou.png"
    if res==10:
        v="static/deu.png"
    if res==11:
        v="static/onz.png"
    if res==12:
        v="static/dot.png"
    if res>=13:
        v="static/tre.png"
    return v