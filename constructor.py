class laptop:
    def __init__(self,screensize,displaysurface,resolution_x,resolution_y,ppi,touchtechnology,multitouch):
        self.screensize=screensize
        self.displaysurface=displaysurface
        self.resolution_x=resolution_x
        self.resolution_y=resolution_y
        self.ppi=ppi
        self.touchtechnology=touchtechnology
        self.multitouch=multitouch
    def configuration(self):
        print(f"screensize:{self.screensize}")
        print(f"displaysurface:{self.displaysurface}")
        print(f"resolution_x:{self.resolution_x}")
        print(f"resolution_y:{self.resolution_y}")
        print(f"ppi:{self.ppi}")
        print(f"touchtechnology:{self.touchtechnology}")
        print(f"multitouch:{self.multitouch}")
class Hp(laptop):
    pass

Lap=laptop(13.3,"Glossy",3200,1800,276,"capactive","yes")
Lap.configuration()
HpLap=Hp(114.5,"Glossy",2300,1600,256,"capactive","yes")
HpLap.configuration()