
def findpositionandspeed(uid,cur_speed):
    print(uid,cur_speed)




def generatebytime(distant,duration,nstation,start_time,current_speed,current_position,current_time,index):
    return generate(distant,duration,nstation,start_time,current_speed,current_position,current_time)[index]



def generate(distant,duration,nstation,start_time,current_speed,current_position,current_time):

#    print("generatebytime")
    LENRM = distant #3.736 #mm
    LENT = 0.480  #mm
    SPEED_MAX = 0.630 # mmps  --> 0.593 mps

    timetable = list()
    stime = duration

    remain_distant = distant - current_position
    remain_time = duration - (current_time-start_time)

    time_position = duration - remain_time

    SPEED_NORM = 0.492*SPEED_MAX
    # print(SPEED_NORM)
    timefora = 5
    timeframe = 0.5
    timeslot = int(timefora/timeframe)
    DIST_A = 1
    DIST_B = 0.9
    DIST_C = LENRM - DIST_A - DIST_B
    a1 = pow(SPEED_NORM,2)/(2*DIST_A)
    a2 = pow(SPEED_NORM,2)/(2*DIST_B)

    ctime = stime - (2*timefora)

    # print(SPEED_NORM,a1,a2)
    u = 0
    z = 0

    sumdist = 0
    li=[LENRM,stime,0,0,0]

    timetable.append(li)

    for x in range(0,timeslot):
        z=z+timeframe
        v = u+(a1*timeframe)
        s = u*timeframe + 0.5*a1*timeframe*timeframe
        sumdist=sumdist + s

        # print("1",z,"%.4f"%u,"%.4f"%v,sumdist)

        li=[LENRM,stime,u,sumdist,z]
        timetable.append(li)
        u = v


    dist_remain = LENRM - (sumdist*2)

    c = dist_remain/ctime
    for x in range(0,ctime*2):
        z=z+timeframe
        s = v*timeframe
        sumdist=sumdist + s
        # print("2",z,"%.4f"%u,"%.4f"%v,sumdist)
        li=[LENRM,stime,u,sumdist,z]
        timetable.append(li)


    for x in range(0,timeslot):
        z=z+timeframe
        v = u+(-a2*timeframe)
        s = u*timeframe + 0.5*a1*timeframe*timeframe
        sumdist=sumdist + s

        # print("3",z,"%.4f"%u,"%.4f"%v,sumdist)
        li=[LENRM,stime,u,sumdist,z]
        timetable.append(li)
        u = v

    #print(timetable)
    return timetable


#def generatebytime(distant,duration,nstation,start_time,current_speed,current_position,current_time):
if __name__ == "__main__":
    print(generatebytime(3.736,20,1,0,0,0,0,1))
    # print(generatebytime(3.736,20,1,0,0,0,1))
    # print(generatebytime(3.736,20,1,0,0,0,2))
