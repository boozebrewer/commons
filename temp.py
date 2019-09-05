import commons
@commons.timer.timer
def asdf():
    print('hi')
asdf()

@commons.timer.timer
def poij():
    print('bye')
poij()

with commons.printer.PrintDone("ddddd"):
    commons.timer.time.sleep(1)