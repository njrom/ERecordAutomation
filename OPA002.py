def main():
    switchApp("Hyperspace URMC")
    type("ORSCHED")
    type(Key.TAB)
    type("model")
    type(Key.ENTER)
    keyDown(Key.SHIFT) # Hold SHIFT to shift tab up to Department
    type(Key.TAB)
    keyUp(Key.SHIFT)
    type("SMH OPERATING ROOM"+Key.ENTER)
    wait(2)
    type(Key.ENTER+Key.ENTER)
    while(True): # Waits for POC to load and be logged in
        if(exists("1521830437049.png")):
            break
    click("1521765117289.png")
    type("ZEBRA,OPTIME"+Key.ENTER+Key.ENTER)
    type(Key.TAB+"SMH Main OR"+Key.TAB)
    type("ORMD"+Key.TAB)
    type("t+5")
    click("1521831054847.png")
main()
