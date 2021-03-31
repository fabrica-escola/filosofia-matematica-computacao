
tam_tabuleiro = 10
tam_casa = 50
meia_casa = tam_casa / 2
borda = 55

from tabuleiro_a import tabuleiro as tabuleiro_a
from tabuleiro_a import nome_da_equipe as equipe_a

from tabuleiro_b import tabuleiro as tabuleiro_b
from tabuleiro_b import nome_da_equipe as equipe_b

visivel_a = []
visivel_b = []

def setup():
    size(1200, 600)
    textSize(20)
    textAlign(CENTER, CENTER)
    
def draw():
    background(200)
    draw_tabuleiro(tabuleiro_a, visivel_a)
    text(equipe_a, width / 4, height - meia_casa)
    translate(600, 0)
    draw_tabuleiro(tabuleiro_b, visivel_b)
    text(equipe_b, width / 4, height - meia_casa)
    
def draw_tabuleiro(tabuleiro, visivel):
    for i in range(tam_tabuleiro):
        for j in range(tam_tabuleiro):
            if (i, j) in visivel:
                if (i, j) in tabuleiro:
                    fill(200, 0, 0)
                else:
                    fill(0, 0, 200)
            else:
                fill(128)
            square(i * tam_casa + borda, 
                   j * tam_casa + borda, 
                   tam_casa)
            
    for n in range(tam_tabuleiro):
        fill(0)
        pos =  n * tam_casa + borda + meia_casa 
        text(n, meia_casa, pos)
        text(n, pos, meia_casa * 1.2)
        
    
def mouseClicked():
    mnta = mouse_no_tabuleiro(mouseX, mouseY)    
    modifica_tabuleiro(mnta, visivel_a)     
    mntb = mouse_no_tabuleiro(mouseX - 600, mouseY)    
    modifica_tabuleiro(mntb, visivel_b)
        
def modifica_tabuleiro(pos, visivel):
    if pos in visivel:
        visivel.remove(pos)
    else:
        visivel.append(pos)

def mouse_no_tabuleiro(x, y):
    i = (x - borda) / tam_casa 
    j = (y - borda) / tam_casa 
    if 0 <= i < tam_tabuleiro and 0 <= j < tam_tabuleiro:
        return (i, j)
    else:
        return None
