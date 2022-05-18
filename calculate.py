
n=4
d=1
l=3

p=(n-d)/n
print(p)

last_pt=0.4444

pt=last_pt*p
print(pt)

v1=0.0167
#print("v1=",v1)
v2=0.0139
#print("v2=",v2)
v3=0.0179
#print("v3=",v3)
v4=0.0238
#print("v4=",v4)
v5=0.05
print("v5=",v5)
v6=d/(n*(n-d))

var=(pt**2)*(v1+v2+v3+v4+v5+v6)
print(var)
