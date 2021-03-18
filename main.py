import core
import model
import settings
import time

if __name__ == "__main__":
    model.database_init()
    #core.GetBasicStock()
    #core.GetDaily()
    #core.GetDailyBasic()
    #core.GetDailyBasicPool()
    #core.GetDailyPool()
    #core.GetAdjFactor2()
    #core.GetProBar()
    #core.SetDailyBasicPollHuiche()
    #core.GetIncom()
    core.GetExpress()

    #print(time.strftime('%Y%m%d', time.localtime(time.time())))
