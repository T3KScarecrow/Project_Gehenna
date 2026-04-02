import sys
import time

def Typer(text:type=str, sleep=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(sleep)
    time.sleep(0.35)

def LoadingDots():
    text = "..."
    Typer(text, 0.25)
    for i in range(3):
        for e in range(3):
            sys.stdout.write("\b")
            sys.stdout.flush()
        time.sleep(0.175)
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.25)
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.25)
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.3)

def LoopTyper(loops:type=int, val:type=int, sleep=0.01):
    bar_width = 100
    cube = '■'
    for i in range(loops):
        temp_text = str("\r\033[2K[" + cube * (i+val) + ' ' * (bar_width - (i+val)) + ']')
        sys.stdout.write(temp_text)
        sys.stdout.flush()
        time.sleep(sleep)