import pyautogui, time

def main():
    print("robot starts")
    time.sleep(3)
    for x in range (1000):
        check_mystic()
        check_bookmark()
        scroll_down()
        check_mystic()
        check_bookmark()
        x, y = pyautogui.locateCenterOnScreen('Pictures/Refreshbttn.PNG',confidence=.80)
        pyautogui.click(x,y)
        time.sleep(0.5)
        x, y = pyautogui.locateCenterOnScreen('Pictures/Confirmbttn.PNG',confidence=.80)
        pyautogui.click(x,y)
        time.sleep(1.5)


def scroll_down():
    pyautogui.scroll(-1000)
    time.sleep(0.5)


def check_mystic():
    time.sleep(3)
    if (pyautogui.locateOnScreen('Pictures/Mystic.PNG', confidence=0.95) is not None):
        print("Mystic found")
        #Click buy mystic
        x,y = pyautogui.locateCenterOnScreen('Pictures/MysticPrice.PNG', confidence=0.98)
        pyautogui.click(x, y)
        time.sleep(0.5)
        #Click confirm mystic 
        x,y = pyautogui.locateCenterOnScreen('Pictures/MysticConfirm.PNG', confidence=0.98)
        pyautogui.click(x, y)
        time.sleep(1.5)

def check_bookmark():
    if (pyautogui.locateOnScreen('Pictures/Bookmark.PNG', confidence=0.95) is not None):
        print("Bookmark found")
        #Click buy mystic
        x,y = pyautogui.locateCenterOnScreen('Pictures/BookmarkPrice.PNG', confidence=0.95)
        pyautogui.click(x, y)
        time.sleep(0.5)
        #Click confirm mystic 
        x,y = pyautogui.locateCenterOnScreen('Pictures/BookmarkConfirm.PNG', confidence=0.95)
        pyautogui.click(x, y)
        time.sleep(1.5)

if __name__ == "__main__":
    main()


