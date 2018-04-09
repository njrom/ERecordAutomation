def login():
    switchApp("Hyperspace URMC")
    type("ORSCHED")
    type(Key.TAB)
    type("model")
    type(Key.ENTER)
    keyDown(Key.SHIFT)  # Hold SHIFT to shift tab up to Department
    type(Key.TAB)
    keyUp(Key.SHIFT)
    type("SMH OPERATING ROOM" + Key.ENTER)
    wait(2)
    type(Key.ENTER + Key.ENTER)
    while (True):  # Waits for POC to load and be logged in
        if (exists("1522354426935-2.png")): 
            break
    wait(4)
def main():
    login()

main()