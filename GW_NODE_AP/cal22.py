
#conan's part
node_list = dict()
sensors_list = list()
distab = dict()
distdest = dict()
ab_order = list()
ta = 0
tb = 0
tdiff = 0
pa = ''
pb = ''
sum_dist = 0
speed = 0
LENRM = 3736
LENT =  480


def define_order(line):
    print("LINE=",line)
    global pa
    global pb
    global ta
    global tb
    global sum_dist
    global speed
    global distab
    global distdest,ab_order
    global sensors_list
    ddist = 0
    tdiff = 0

    try:

        data_type = line[0]
        uid = line[1]
        dtime = line[2]
        if data_type == 1:
            ddtime = line[3][1]
        elif data_type == 0:
            ddtime = line[4][1]

#print(data_type,uid,dtime,ddtime)

        if data_type == 0:
            pa = pb
            pb = uid
            tb = float(dtime)
            tdiff = tb-ta

            if tdiff < 0.0001 or tdiff == 0 :
                return
            ta = tb

        if data_type == 1:
            if uid not in sensors_list:
                sensors_list.append(uid)

        sensors_text = ""
        for sr in sensors_list:
            sensors_text+=sr+' '

        if data_type == 1:
            speed = LENT/float(ddtime)


        if data_type == 0:
            ddist = tdiff*speed
            if ddist<1:
                return
            sum_dist+=ddist

        tag = "%s-%s"%(pa,pb)

        if tag in distab:
            print(tag,ddist)
            dd = distab[tag]
            if dd > 0:
                dd = (dd+ddist)/2
            else:
                dd = ddist

            distab[tag]=dd

        else:
            distab[tag]=ddist

        if pb in distdest:
            dds = distdest[pb]
            dds = (dds+sum_dist)/2
            distdest[pb]=dds
        else:
            distdest[pb] = sum_dist

        print(len(sensors_list),data_type,uid,"|",pa,pb,"|tdiff=","%01.06f"%tdiff,"|v=","%03.06f"%speed,"|s=","%03.06f"%(ddist),"|ss=","%04.04f"%sum_dist,end='\r')
        print(sensors_text)

#        send_speed(uid,speed)
        if sum_dist>LENRM:
            sum_dist = 0
            # print(data_type,uid,speed,end='\r')
        sensors_text = ""

    except Exception as e:
        print(e)
