from PIL.ImageWin import Window
from win32timezone import now

from libBot import *
import os

class Clicks:
    windowBar = (1201,1052)
    noxApps = (1790,980)
    starMap = (950,1018)
    armies = (70,370)
    mapSearch = (1761,993)
    mapSearchDropdown = (821,394)
    mapSearchButton = (1230, 385)
    resultFirstClosest = (1192, 507)
    mapCenter = (1956, 695)
    mapCollect = (1070, 460)
    #origin base selection
    nextButton = (1159, 902)
    heroSelectBtn = (1195, 576)
    firstAvail = (965, 311)
    heroSelectBtn2 = (1165, 920)
    maxTroopsBtn = (784, 908)
    mapDeploy = (1130, 920)
    mapPb = (762, 763)
    mapFood = (719, 553)
    mapFuel = (748,551)
    mapAda = (738,645)
    mapPlasma = (738, 680)
    mapCrystal = (742, 739)
    mapRss = ["res\\conquest\\stone_icon.png", "res\\conquest\\farm_icon.png"]
    mapRssOnMap = ["res\\conquest\\stone_source_map.png", "res\\conquest\\stone_source_map.png"]
    mapExplore = (1324, 900)
    events = (1680, 140)
    joinBreach = (1580,660)
    eventsClose = (1705, 85)
    trainButton = (1600, 900)
    back = (60, 30)

class GameState:
    lastRss = 0

def nextRss():
    print("getRSS: [",int(GameState.lastRss)," % 4] => ", GameState.lastRss % 4, sep='')
    icon = (Clicks.mapRss[GameState.lastRss % 4])
    GameState.lastRss+=1
    return icon


def gatherResources():
    print("Starting " + sys._getframe().f_code.co_name)
    print("switch to map")

    clickAbsolute(screenOpts, findImgOnScreen(screenOpts, 'res\\conquest\\world_view.PNG'), 2)
    clickAbsolute(screenOpts, findImgOnScreen(screenOpts, 'res\\conquest\\search.PNG'), 2)
    print("search random rss")
    clickAbsolute(screenOpts, findImgOnScreen(screenOpts, nextRss()), 2)
    clickAbsolute(screenOpts, findImgOnScreen(screenOpts, 'res\\conquest\\search_button_fr.png'), 3)
    clickAbsolute(screenOpts, findImgOnScreen(screenOpts, 'res\\conquest\\go_button_fr.png'), 3)
    clickAbsolute(screenOpts, findImgOnScreen(screenOpts, Clicks.mapRssOnMap[GameState.lastRss-1]), 3)
    clickAbsolute(screenOpts, findImgOnScreen(screenOpts, 'res\\conquest\\collect_wm.png'), 3)

    print("select appropriatley sized wb to collect")
    clickAbsolute(screenOpts, findImgOnScreen(screenOpts, 'res\\conquest\\Next_button.png'), 3)
    clickAbsolute(screenOpts, findImgOnScreen(screenOpts, 'res\\conquest\\wb_settings_button.png'), 3)
    clickAbsolute(screenOpts, findImgOnScreen(screenOpts, 'res\\conquest\\collect_rss_wb_settings_option.png'), 3)
    clickAbsolute(screenOpts, findImgOnScreen(screenOpts, 'res\\conquest\\launch_wb.png'), 3)

def helpFlag():
    print("Starting " + sys._getframe().f_code.co_name)
    Yoffset=710
    pointer = findImgOnScreen(screenOpts, 'res\\helpFlag.png', 0.8, Yoffset)
    if pointer != 0:
        pointer = (pointer[0]+20,pointer[1]+20)
        clickGame(screenOpts, pointer, 0.5)


def trainArmy():
    print("Starting " + sys._getframe().f_code.co_name)
    while True:
        pointer0 = findImgOnScreen(screenOpts, 'res\\conquest\\trainings.png')
        if pointer0 == 0:
            print("ERROR - trainButton")
            break
        clickGame(screenOpts, pointer0, 1)

        pointer = findImgOnScreen(screenOpts, 'res\\conquest\\go_button_fr.png', 0.8, 0, 330)
        if pointer != 0:
            pointer = (pointer[0] + 140, pointer[1] + 20)
            clickGame(screenOpts, pointer, 5)
        if pointer == 0:
            pointer = findImgOnScreen(screenOpts, 'res\\complete.png', 0.8, 0, 330)
            if pointer != 0:
                pointer = (pointer[0] + 140, pointer[1] + 0)
                clickGame(screenOpts, pointer, 5)
                # click building to get menu
                pointer = (int(screenOpts.x_len / 2), int(screenOpts.y_len / 2))
                clickGame(screenOpts, pointer, 2)

        if pointer != 0:
            time.sleep(2)
            pointer = findImgOnScreen(screenOpts, 'res\\trainUnit.png')
            if pointer != 0:
                pointer = (pointer[0] + 20, pointer[1] + 20)
                clickGame(screenOpts, pointer, 2)
                clickGame(screenOpts, Clicks.trainButton, 2)
                pointer = findImgOnScreen(screenOpts, 'res\\goTraining.png')
                if pointer != 0:
                    print("not enough resources")
                    clickGame(screenOpts, Clicks.back, 1)
                    clickGame(screenOpts, Clicks.back, 1)
                    break
            else:
                print("ERROR - trainUnit")
                break
        else:
            clickGame(screenOpts, pointer0, 0.5) #close menu
            break

def mainLoop():
    updateWindow(screenOpts)
    if(isWindowFocus(screenOpts)):
        gatherResources();

    loopDelay(5,-1,'res\\ding.mp3')

def main():
    updateWindow(screenOpts)

    #for testing single routines:
    #gatherResources()
    #joinBreach()
    #helpFlag()
    #dropship()
    #crashedApp()
    #trainArmy()
    #exit(0)

    while True:
        mainLoop()



if __name__ == '__main__':
    main()

