from subprocess import *
import subprocess
import os



# with open("crap.txt:cmd.exe", "rb") as ads:
#
#     stuff = ads.read()
#     print(stuff.__len__())
#     ads.close()
#
#
# subprocess.check_call('dir /r', shell=True)

#listFiles = os.listdir('C:\\Users\dclop\\PycharmProjects\\DFS510EVN')
#print(listFiles)


# with Popen(["dir /r"], stdout=PIPE) as proc:
#     # while proc.stdout.readline().:
#         list2= proc.stdout.read()
#
# stripList=[]





#dir = "C:\\Users\dclop\\PycharmProjects\\DFS510EVN"
#proc =subprocess.Popen("dir", stdout=subprocess.PIPE)
# proc =subprocess.Popen("dir "+dir, stdout=subprocess.PIPE)
#
#
# list2= proc.stdout.read()
# stripList= list2.split()
# files=[]
# for line in stripList:
#     line = line.decode()
#     #print("Line ",line.lstrip("b'"))
#     files.append(line.lstrip("b'"))




#output= subprocess.check_output("dir "+dir+' /r', shell=True)

#outputlist = output.split()
#
#
# end = len(outputlist)
#
# for x  in range(end):
#     l = outputlist[x]
#     l = l.decode()
#     if "$DATA" in l:
#         print("ADS Found at", x)
#         print("ADS: "+l)



def hasADS(dir):
    output = subprocess.check_output("dir " + dir + ' /r', shell=True)

    outputlist = output.split()

    end = len(outputlist)

    for x in range(end):
        l = outputlist[x]
        l = l.decode()
        if "$DATA" in l:
            print("ADS Found at", x)
            print("ADS: " + l)




def main():
    list2 = ""

    userDir = input("Enter directory/file to check for ADS")

    if(os.path.exists(userDir)):
        hasADS(dir)
