s1 = int(input('enter first side of triangle '))
s2 = int(input('enter second side of triangle '))
s3 = int(input('enter third side of triangle '))
if s1==s2 and s2==s3:
    print ("Equilateral triangle")
elif (s1==s2 and s3!=s1 or s3!=s2 and s2==s3 and s1!=s2 or s1!=s3 or s1==s3 and s2!=s1 or s2!=s3):
    print("isosceles triangle")
elif s1!=s2 and s2!=s3 and s1!=s3:
          print ("Scalene triangle")
