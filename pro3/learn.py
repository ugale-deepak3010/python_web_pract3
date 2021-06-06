#!C:\Python27\python.exe
import cgi
# warning:first line is not a comment.

print "Content-type: text/html\n\n";

print("<html>")
print("<head>")
print("</head>")
print("<body>")
print("<div class='container'>")
print("Deepak Ugale")
""" multiline 
comment """
print("<br>ok")


x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

print "<br>"
a = "Hello, World!"
print(a[1])

a = "Hello, World!"
print(a[2:6])

import platform #plateform is bult in module...

x = platform.system()
print(x)

import datetime  #datetime module use

x = datetime.datetime.now()
print(x)
print "<br><br>"

print(x.year)
print(x.strftime("%A"))

x = datetime.datetime(2020, 5, 17)

print(x)
print "</div>"
print("</body>")
print("</html>")