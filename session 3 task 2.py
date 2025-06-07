magdy_dic = {'name' : 'magdy','grades' :[90,95,85]}
magdy_grads = magdy_dic["grades"]
lensum = len(magdy_grads)
# average equation = sum of values / total numbers of values
average_grade = (magdy_grads[0]+magdy_grads[1]+magdy_grads[2]) / lensum
print ( "student name : " ,magdy_dic["name"],"--- average grades :" ,average_grade)
hamada_dic = {'name' : 'hamada','grades' :[91,96,86]}
hamada_grads = hamada_dic["grades"]
lensum2 = len(hamada_grads)
average_grade2 = (hamada_grads[0]+hamada_grads[1]+hamada_grads[2]) / lensum2
print ( "student name : " ,hamada_dic["name"],"--- average grades :" ,average_grade2)
ali_dic = {'name' : 'ali','grades' :[92,97,87]}
ali_grads = ali_dic["grades"]
lensum3 = len(ali_grads)
average_grade3 = (ali_grads[0]+ali_grads[1]+ali_grads[2]) / lensum3
print ( "student name : " ,ali_dic["name"],"--- average grades :" ,average_grade3)
# my resault was student
# name :  magdy --- average grades : 90.0
# student name :  hamada --- average grades : 91.0
# student name :  ali --- average grades : 92.0