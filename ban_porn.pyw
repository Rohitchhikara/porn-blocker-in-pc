import keyboard
import os

# Define the first function to be called when a key is pressed
def print_boy(event):
    global p, o, r, n

    if event.name in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'q', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
        p = False
        o = False
        r = False
        n = False

    if event.name == "p":
        p = True
    elif event.name == "o" and p:
        o = True
    elif event.name == "r" and p and o:
        r = True
    elif event.name == "n" and p and o and r:
        n = True
        if p and o and r and n:
            # print("All keys are true. Shutting down the PC...")
            os.system("shutdown /s /t 10")
            # keyboard.unhook_all()

# Define the second function to be called when a key is pressed
def printboy(event1):
    global s, e, x

    if event1.name in ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'y', 'z']:
        s = False
        e = False
        x = False

    if event1.name == "s":
        s = True
    elif event1.name == "e" and s:
        e = True
    elif event1.name == "x" and s and e:
        x = True
        if s and e and x:
            # print("shut down")
            os.system("shutdown /s /t 10")
            # keyboard.unhook_all()

# Define the third function to be called when a key is pressed
def printboy3(event2):
    global s, e, x, g, i, rr, l, pp

    if event2.name in ['a', 'b', 'c', 'd', 'f', 's', 'h', 'e', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'x', 't', 'u', 'v', 'w', 'y', 'z']:
        g = False
        i = False
        rr = False
        l = False
        pp = False

    if event2.name == "g":
        pp = True
    elif event2.name == "i" and pp:
        i = True
    elif event2.name == "r" and pp and i:
        rr = True
    elif event2.name == "l" and pp and i and rr:
        l = True
        if pp and i and rr and l:
            print("All keys are true. Shutting down the PC...")
            os.system("shutdown /s /t 10")
            # keyboard.unhook_all())

# Attach the functions to the keyboard.on_press event
keyboard.on_press(print_boy)
keyboard.on_press(printboy)
keyboard.on_press(printboy3)

# Wait for keyboard events
keyboard.wait()
