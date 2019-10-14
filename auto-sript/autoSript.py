# -*- coding: utf-8 -*-
num=0

times = 0

result = []

dia_action = True

lh_yes = False

f2 = open("C://Users/93464//Desktop//i.txt",'r')

f = open("C:/Users/93464/Desktop//f.txt","w")

for line in f2:
    result.append(line.strip('\n').split(','))

for i in result:

    i=str(i[0])


    if i == "":
        continue

    if i.find("[")>=0:
        
        pos1 = i.find("]")

        print pos1

        if i[i.find("[")+1:i.find("[")+3] == "场景" or i[i.find("[")+1:i.find("[")+3] == "CG":
            dia_action = False
            
        else:
            speaker = i[i.find("[")+1:pos1]

            dia = i[pos1+1:int(len(i))]

        if i.find("(")>=0 and dia_action==True:

            lh_yes = True
            
            pos2 = i.find(")")

            lh = i[i.find("(")+1:pos2]

            dia = i[pos2+1:int(len(i))]

        if dia_action==False:
            times+=1

            f.write("    # TODO "+str(times)+"\n")

            f.write("    \""+i+"\"\n")

        elif lh_yes==True:

            '''
            if speaker == "林琴":
                s = "l"
            elif speaker == "夏静":
                s = "x"
            elif speaker == "程祎琳":
                s = "c"
            elif speaker == "袁艳":
                s = "y"
            elif speaker == "我":
                s = "w"
            else:
                s = speaker
            '''
                
            f.write("    show "+speaker+" "+lh+" at ct with dissolve\n")

            f.write("    \""+speaker+"\" \""+dia+"\"\n")
            
        else:

            f.write("    \""+speaker+"\" \""+dia+"\"\n")
        
    else:

        f.write("    \""+i+"\"\n")

    dia_action = True
    lh_yes = False

    num+=1
    print num

print "end"
f.close()
f2.close()
