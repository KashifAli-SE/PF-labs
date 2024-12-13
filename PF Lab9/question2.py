# 2.   Write a program which will remove 2 friends who left NED.

friends={"kashif", 'bilal', 'ahad', 'salman', 'daniyal'}
f1=input("enter first friend who left NED")
f2=input("enter second friend who left NED")

friends.remove(f1)
friends.remove(f2)

print(friends)
print(F"{f1} and {f2} left NED")