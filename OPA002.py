
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
        if (exists("1522354426935.png")):
            break
    click("1522354588024.png") # Open case button
    type("ZEBRA,OPTIME" + Key.ENTER + Key.ENTER)
    type(Key.TAB + "SMH Main OR" + Key.TAB)
    type("ORMD" + Key.TAB)
    type("t+5")
    click("1522354668981.png")  # New case button
    wait(2)
    type("Inpatient")  # Patient Class
    type(Key.TAB + Key.TAB + Key.TAB)
    type("General" + Key.TAB)  # Service
    type("SMH MAIN OR")
    type(Key.TAB + Key.TAB + Key.TAB)
    type("P05.00" + Key.ENTER + Key.ENTER)  # Diagnosis
    click(Pattern("1522191047332.png").targetOffset(0, 15))  # Clicks box to ender p
    type("Craniotomy for Aneurysm")
    click(Pattern("1522191069162.png").targetOffset(0, 15))
    type("N/A")  # Laterality
    click(Pattern("1521838272064.png").targetOffset(0, 15))
    type("General")  # Anesthesia
    wait(2)
    type("Inpatient")  # Patient Class
    type(Key.TAB + Key.TAB + Key.TAB)
    type("General" + Key.TAB)  # Service
    type("SMH MAIN OR")
    type(Key.TAB + Key.TAB + Key.TAB)
    type("P05.00" + Key.ENTER + Key.ENTER)  # Diagnosis
    click(Pattern("1522191047332.png").targetOffset(0, 15))  # Clicks box to ender p
    type("Craniotomy for Aneurysm")
    click(Pattern("1522191069162.png").targetOffset(0, 15))
    type("N/A")  # Laterality
    click(Pattern("1522354869064.png").targetOffset(0, 15))
    type("General")  # Anesthesia
    click("1522356679271.png")  # Case Entry Form
    wait(4)
    click("1522356903531.png")
    type(Key.TAB + Key.ENTER)  # Hits Yes on PCP Listed
    click("1522357884191.png")  # Address and Phone
    type(Key.TAB + Key.ENTER)
    click(Pattern().targetOffset(0, 15))
    type("Yes" + Key.TAB)
    type("Spanish Interpreter")
    click("1522358364237.png")  # Latex Allergy
    type(Key.TAB + Key.TAB + Key.ENTER)
    click("1522358721822.png"  # Dye Allergy
    type(Key.TAB + Key.ENTER)  # NO
    type("1522359580669.png")
    while (!exists("1522359580669.png")):
        type(Key.TAB)
        wait(1)
    click("1522359580669.png") # TODO: Need to finish C11 step navigating that form



main()




