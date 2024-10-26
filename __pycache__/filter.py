webinarlist=["milan@rafs","milan@orange.com","radah@mkn","vssyg@nn","bjhbb@bnzbc","orange.ocm","shehh@ds"]
orangepeople=lambda x:x.endswith("@orange.com")
outsidepeople=lambda y:not y.endswith("@orange.com")

orangelist=list(filter(orangepeople,webinarlist))
outsider=list(filter(outsidepeople,webinarlist))
# for x in webinarlist:
#    if(x.endswith("@orange.com")):
#       orangelist.append(x)
#    else:
#       outsider.append(x)
print("people attended from orange")
print(orangelist)
print("people from outsider orange")
print(outsider)   
