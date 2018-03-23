def main():
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
        if (exists("1521830437049.png")):
            break
    click("1521765117289.png")
    type("ZEBRA,OPTIME" + Key.ENTER + Key.ENTER)
    type(Key.TAB + "SMH Main OR" + Key.TAB)
    type("ORMD" + Key.TAB)
    type("t+5")
    click("1521831054847.png")
    wait(2)
    type("Inpatient")  # Patient Class
    type(Key.TAB + Key.TAB + Key.TAB)
    type("General" + Key.TAB)  # Service
    type("SMH MAIN OR")
    type(Key.TAB + Key.TAB + Key.TAB)
    type("P05.00" + Key.ENTER + Key.ENTER)  # Diagnosis
    click(Pattern("1521838235447.png").targetOffset(0, 15))  # Clicks box to ender p
    type("Craniotomy for Aneurysm")
    click(Pattern("1521838305611.png").targetOffset(0, 15))
    type("N/A")  # Laterality
    click(Pattern("1521838272064.png").targetOffset(0, 15))
    type("General")  # Anesthesia

main()
