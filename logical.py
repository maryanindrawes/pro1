print("Hello, please add your mark:")
mark = input()
mark = int(mark)
if mark > 100 or mark < 0:
    print("invalid")
elif mark >= 50:
    print("pass")
else:
    print("fail")
print("Thank you")

