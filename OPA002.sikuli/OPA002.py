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
    wait(5)
    click("1522354588024.png") # Open case button
    type("ZEBRA,OPTIME" + Key.ENTER + Key.ENTER)
    type(Key.TAB + "SMH Main OR" + Key.TAB)
    type("ORMD" + Key.TAB)
    type("t+5")
    click("1522354668981.png") # New case button
    wait(2)
    type("Inpatient")  # Patient Class
    type(Key.TAB + Key.TAB + Key.TAB)
    type("General" + Key.TAB)  # Service
    type("SMH MAIN OR")
    type(Key.TAB + Key.TAB + Key.TAB)
    type("P05.00" + Key.ENTER + Key.ENTER)  # Diagnosis
    click(Pattern("1522436563595.png").targetOffset(0, 15))  # Clicks box to ender p
    type("Craniotomy for Aneurysm")
    click(Pattern("1522191069162.png").targetOffset(0, 15))
    type("N/A")  # Laterality
    click(Pattern("1522354869064.png").targetOffset(0, 15))
    type("General")  # Anesthesia
    click("1522356679271.png") # Case Entry Form
   


def test():
    switchApp("Hyperspace")
    wait(4)
    while(not exists("1522436664179.png")):
        wait(1) # Patient Information Header Check to see if page is loaded
    click("1522356903531.png")
    type(Key.TAB+Key.ENTER) # Hits Yes on PCP Listed
    click("1522357884191.png") # Address and Phone
    type(Key.TAB+Key.ENTER)
    click(Pattern("1522367277299.png").targetOffset(0,15))
    type("Yes"+Key.TAB)
    type("Spanish Interpreter")
    click("1522358364237.png") # Latex Allergy
    type(Key.TAB+Key.TAB+Key.ENTER)
    click("1522358721822.png") # Dye Allergy 
    type(Key.TAB+Key.ENTER)
    click("1522372124942.png")
    type(Key.TAB*15+Key.ENTER) # Selecteds NIDDM, This is a major limitation of the code
    while(not exists("1522372377542.png")):
        type(Key.PAGE_DOWN)
    click(Pattern("1522781153918.png").targetOffset(0,15))
    type("T+3") # Procedure Date
    type(Key.TAB+"2") # Days staying
    click("1522783340922.png") # Need to click out of text field so page down works
    while(not exists("1522436964040.png")):
        type(Key.PAGE_DOWN) # Scroll till you see the Patient Insurance header
    wait(1)
    click(Pattern("1522438227096.png").targetOffset(0,15))
    type("Primary"+Key.TAB)
    type("Aetna - University of Rochester"+Key.TAB)
    click("1522783376667.png")
    while(not exists("1522438630985.png")):
        type(Key.PAGE_DOWN)
    type(Key.PAGE_DOWN)
    click("1522438833623.png")
    type(Key.TAB+Key.ENTER+Key.ENTER)
    
    
    

    
test()  
    