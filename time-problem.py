def convert_time_into_hour(h,m):
    if h == 12:
	    h = 0
    if m == 60:
        m = 0
        h += 1
        if(h>12):
            h = h-12
    return h,m

def calcAngle(time1,time2):
		
		
		h1,m1 = time1.split(":")
		h1,m1 = convert_time_into_hour(int(h1),int(m1))
		h2,m2 = time2.split(":")
		h2,m2 = convert_time_into_hour(int(h2),int(m2))
		
		# 360 degree into 12 hour then convert into minute.
		h1_angle = (360/12)/60 * (h1 * 60 + m1)
		h2_angle = (360/12)/60 * (h2 * 60 + m2)
		
		angle = abs(h1_angle - h2_angle)

		return angle

print(calcAngle("9:15","7:37"))
