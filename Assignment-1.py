students = {
    1: ('Ved', 'Electrical Engineering', [ 98,99]),
    2: ('Bhavya', 'Computer Science Engineering',[85,90]),
 }
print('Before=' , students)
students[3] = ('Dharya' , 'Civil Engineering',[89,85])
del students[2]
students[1] = ('Ved', 'Mechanical engineering', [98,99])
print('After=', students)