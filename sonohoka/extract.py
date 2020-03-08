import re

mydata = """
from 10.27.248.245

b'\r\nUSSR-DMVPN-RT01#ping 10.28.248.244\r\nType escape sequence to abort.\r\nSending 5, 100-byte ICMP Echos to 10.28.248.244, timeout is 2 seconds:\r\n!!!!!\r\nSuccess rate is 100 percent (5/5), round-trip min/avg/max = 19/19/20 ms\r\nUSSR-DMVPN-RT01#'
2020-01-10 13:55:18.117945
from 10.27.248.245

b'terminal length 0\r\nUSSR-DMVPN-RT01#ping 10.25.255.254\r\nType escape sequence to abort.\r\nSending 5, 100-byte ICMP Echos to 10.25.255.254, timeout is 2 seconds:\r\n!!!!!\r\nSuccess rate is 100 percent (5/5), round-trip min/avg/max = 10/28/62 ms\r\nUSSR-DMVPN-RT01#'
2020-01-10 13:55:22.126360
from 10.27.248.245

b'terminal length 0\r\nUSSR-DMVPN-RT01#ping 10.27.252.101\r\nType escape sequence to abort.\r\nSending 5, 100-byte ICMP Echos to 10.27.252.101, timeout is 2 seconds:\r\n!!!!!\r\nSuccess rate is 100 percent (5/5), round-trip min/avg/max = 2/2/2 ms\r\nUSSR-DMVPN-RT01#'
2020-01-10 13:55:26.131075
from 10.27.248.245

b'terminal length 0\r\nUSSR-DMVPN-RT01#ping 10.16.255.254\r\nType escape sequence to abort.\r\nSending 5, 100-byte ICMP Echos to 10.16.255.254, timeout is 2 seconds:\r\n!!!!!\r\nSuccess rate is 100 percent (5/5), round-trip min/avg/max = 86/86/87 ms\r\nUSSR-DMVPN-RT01#'
2020-01-10 13:55:30.136015
from 10.27.248.245

b'terminal length 0\r\nUSSR-DMVPN-RT01#ping 10.21.254.40\r\nType escape sequence to abort.\r\nSending 5, 100-byte ICMP Echos to 10.21.254.40, timeout is 2 seconds:\r\n!!!!!\r\nSuccess rate is 100 percent (5/5), round-trip min/avg/max = 72/72/73 ms\r\nUSSR-DMVPN-RT01#'
2020-01-10 13:55:34.140566
from 10.27.248.245

b'terminal length 0\r\nUSSR-DMVPN-RT01#ping 10.30.254.1\r\nType escape sequence to abort.\r\nSending 5, 100-byte ICMP Echos to 10.30.254.1, timeout is 2 seconds:\r\n!!!!!\r\nSuccess rate is 100 percent (5/5), round-trip min/avg/max = 161/161/162 ms\r\nUSSR-DMVPN-RT01#'
2020-01-10 13:55:38.142744
from 10.27.248.245
"""
#print (mydata)
#print(mydata[0])
# print(type(mydata))
pat1 = re.compile("from \d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}")
pat = re.compile("ping \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
pat2 = re.compile("\d{1,3}\spercent")
pat3 = re.compile("round-trip min/avg/max = \d{1,3}/\d{1,3}/\d{1,3} ms")

e = re.findall(r"2020-01-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}.\d{1,7}", mydata)
d = re.findall(r"from \d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", mydata)
a = re.findall(r"ping \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", mydata)
b = re.findall(r"\d{1,3}\spercent", mydata)
c = re.findall(r"round-trip min/avg/max = \d{1,3}/\d{1,3}/\d{1,3} ms", mydata)

print(d)
print (a)
print(b)
print(c)

#print(a, b, c)
print(type(a))
print(type(b))
print(type(c))
#res = list(map(list.__add__, list(a), list(b), list(c)))
#print(res)

iterable = [d, a,b,c, e]
result = list(zip(d, a,b,c,e))
print(result)
# b = mydata.split()
# print(b)
# # for line in mydata:
# #     print(line)
#     #a = re.findall(r"ping \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
#     #print(a)
