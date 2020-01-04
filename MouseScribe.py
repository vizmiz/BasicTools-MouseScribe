import pyautogui
import sys
import os
FilePath = os.path.dirname(os.path.abspath(__file__))

print('Press Ctrl-C to quit.')
 


class MouseCom:
    def __init__(self,filename):
        self.filename = filename
        self.rawlist = []

    def WatchMouseXY(self):#turns on first
        try:
            while True: 
                x, y = pyautogui.position()
                positionStr =str(x)+','+str(y)
                if positionStr is not None:
                    self.rawlist.append("pyautogui.moveTo({})".format(positionStr))
                    print(positionStr, end='')
                    print('\b' * len(positionStr), end='', flush=True)
        except KeyboardInterrupt:
            self.MakePyFile()

    def MakePyFile(self): 
        print('\nWorking\n')        
        openfile=open("{0}/MouseMovementScripts/{1}.py".format(FilePath,filename),"w") 
        print("import pyautogui;pyautogui.PAUSE=0\n",file=openfile)
        self.GrabEveryXFromList(openfile)

    # X is more or less a speed setting for playback {Higher = Faster}
    # The raw input is far too slow in playback so this 
    # function selects every X sample to use in the playback
    def GrabEveryXFromList(self,openfile):
        count=0 
        X=4
        for each in self.rawlist:
            count=count+1
            if count % X == 0:
                print(each, file=openfile)
        print('\nDone')                
filename=input("\nName of script?\n")
run = MouseCom(filename)
run.WatchMouseXY()
