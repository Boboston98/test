#from https://pypi.org/project/pynput/

from playsound import playsound
from pynput import keyboard
import test_test as test

one = 0
two = 0
three = 0
four = 0
five = 0

def on_press(key):
    global one
    global two
    global three
    global four
    global five

    try:
        print('{0} pressed'.format(key.char))

#THIS WORKS, USE FOR PRODUCING SOUNDS WITH KEYS

# playsound('wav/q.wav')
        #Left Section
        if('{0}'.format(key.char) == 'q'):
            playsound('wav/q.wav')

        if('{0}'.format(key.char) == 'w'):
            playsound('wav/w.wav')

        if('{0}'.format(key.char) == 'e'):
            playsound('wav/e.wav')

        if('{0}'.format(key.char) == 'a'):
            playsound('wav/a.wav')

        if('{0}'.format(key.char) == 's'):
            playsound('wav/s.wav')

        if('{0}'.format(key.char) == 'd'):
            playsound('wav/d.wav')

        if('{0}'.format(key.char) == 'z'):
            playsound('wav/z.wav')

        if('{0}'.format(key.char) == 'x'):
            playsound('wav/x.wav')

        if('{0}'.format(key.char) == 'c'):
            playsound('wav/c.wav')

        #Mid Section
        if('{0}'.format(key.char) == 'r'):
            playsound('wav/r.wav')

        if('{0}'.format(key.char) == 't'):
            playsound('wav/t.wav')

        if('{0}'.format(key.char) == 'y'):
            playsound('wav/y.wav')

        if('{0}'.format(key.char) == 'u'):
            playsound('wav/u.wav')

        if('{0}'.format(key.char) == 'f'):
            playsound('wav/f.wav')

        if('{0}'.format(key.char) == 'g'):
            playsound('wav/g.wav')

        if('{0}'.format(key.char) == 'h'):
            playsound('wav/h.wav')

        if('{0}'.format(key.char) == 'v'):
            playsound('wav/v.wav')

        #Right Section
        if('{0}'.format(key.char) == 'i'):
            playsound('wav/i.wav')

        if('{0}'.format(key.char) == 'o'):
            playsound('wav/o.wav')

        if('{0}'.format(key.char) == 'p'):
            playsound('wav/p.wav')

        if('{0}'.format(key.char) == 'j'):
            playsound('wav/j.wav')

        if('{0}'.format(key.char) == 'k'):
            playsound('wav/k.wav')

        if('{0}'.format(key.char) == 'l'):
            playsound('wav/l.wav')

        if('{0}'.format(key.char) == 'b'):
            playsound('wav/b.wav')

        if('{0}'.format(key.char) == 'n'):
            playsound('wav/n.wav')

        if('{0}'.format(key.char) == 'm'):
            playsound('wav/m.wav')

        if('{0}'.format(key.char) == 'Q'):
            print('WAV made')
            test.wav_wav(1, 'sound', one, two, three, four, five)


    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    print('{0} released'.format(key))
    print(' ')

    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
