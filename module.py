#Every python file - Module - import keyword - __name__
import Day4
'''
print(dir(Day4)) #dir - directory will return all available methods, attributes
print(type(Day4.employees))
print(type(Day4.details))


Day4.employees("Meenakshi", designation = "Trainee", location = "Visakhaptnam")

#print(Day4.details.keys())
print(Day4.details['Organization'])
Day4.details.update({'Batches' : ['PFS', 'JFS', 'DA', 'DAA', 'DS'],
                     'Employees': 500})
print(Day4.details)


#from keyword
from Day4 import employees, details
details.update({'Batches' : ['PFS', 'JFS', 'DA', 'DAA', 'DS'],
                     'Employees': 500})
#print(details)
print(Day4.__doc__)
'''

#Built-in modules - math, random, os, time, datetime

#We download modules - pypi (Python Package Index)

#Build a QRCode Scanner using python - LinkedIN URL, Instagram ......
#pyqrcode, png

import pyqrcode
import png
#Create a QRCode by giving a link
link = "https://github.com/Meenakshi1143"
qr = pyqrcode.create(link)
qr.png("scann.png", scale = 10)

