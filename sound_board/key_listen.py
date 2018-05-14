from playsound import playsound
from pynput import keyboard

def on_press(key):
    try:
        print('{0} pressed'.format(key.char))

        #THIS WORKS, USE FOR PRODUCING SOUNDS WITH KEYS

        # playsound('wav/q.wav')
        #Left Section
        if('{0}'.format(key.char) == 'q'):
            playsound('sounds/wav/pacman_dies_y.wav')

        if('{0}'.format(key.char) == 'w'):
            playsound('sounds/wav/w.wav')

        if('{0}'.format(key.char) == 'e'):
            playsound('sounds/wav/e.wav')

        if('{0}'.format(key.char) == 'a'):
            playsound('sounds/wav/a.wav')

        if('{0}'.format(key.char) == 's'):
            playsound('sounds/wav/s.wav')

        if('{0}'.format(key.char) == 'd'):
            playsound('sounds/wav/d.wav')

        if('{0}'.format(key.char) == 'z'):
            playsound('sounds/wav/z.wav')

        if('{0}'.format(key.char) == 'x'):
            playsound('sounds/wav/x.wav')

        if('{0}'.format(key.char) == 'c'):
            playsound('sounds/wav/c.wav')

        #Mid Section
        if('{0}'.format(key.char) == 'r'):
            playsound('sounds/wav/r.wav')

        if('{0}'.format(key.char) == 't'):
            playsound('sounds/wav/t.wav')

        if('{0}'.format(key.char) == 'y'):
            playsound('sounds/wav/y.wav')

        if('{0}'.format(key.char) == 'u'):
            playsound('sounds/wav/u.wav')

        if('{0}'.format(key.char) == 'f'):
            playsound('sounds/wav/f.wav')

        if('{0}'.format(key.char) == 'g'):
            playsound('sounds/wav/g.wav')

        if('{0}'.format(key.char) == 'h'):
            playsound('sounds/wav/h.wav')

        if('{0}'.format(key.char) == 'v'):
            playsound('sounds/wav/v.wav')

        #Right Section
        if('{0}'.format(key.char) == 'i'):
            playsound('sounds/wav/i.wav')

        if('{0}'.format(key.char) == 'o'):
            playsound('sounds/wav/o.wav')

        if('{0}'.format(key.char) == 'p'):
            playsound('sounds/wav/p.wav')

        if('{0}'.format(key.char) == 'j'):
            playsound('sounds/wav/j.wav')

        if('{0}'.format(key.char) == 'k'):
            playsound('sounds/wav/k.wav')

        if('{0}'.format(key.char) == 'l'):
            playsound('sounds/wav/l.wav')

        if('{0}'.format(key.char) == 'b'):
            playsound('sounds/wav/b.wav')

        if('{0}'.format(key.char) == 'n'):
            playsound('sounds/wav/n.wav')

        if('{0}'.format(key.char) == 'm'):
            playsound('sounds/wav/m.wav')

        if('{0}'.format(key.char) == 'Q'):
            print('WAV made')


    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    print('{0} released'.format(key))
    print(' ')

    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
def run_listen():
    with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
        listener.join()

run_listen()
