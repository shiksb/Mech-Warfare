import os
offset = 90
offset2 = 130
offset3 = 40


skDir="sketch"
if not os.path.exists(skDir):
    os.makedirs(skDir)
# ik_neutral=[512+offset, 512+offset2, 512-offset3, 512-offset, 512+offset2,512-offset3, 512+offset, 512+offset2, 512-offset3, 512-offset, 512+offset2, 512-offset3 ]
ik_neutral=[652, 553, 462,1024-652, 553, 462,652, 553, 462,1024-652, 553, 462 ]
signs="-+-++--+-++-"

# map servo name to ID
servoMap = dict()
servoMap["LF_COXA"]  = 1
servoMap["LF_FEMUR"] = 2
servoMap["LF_TIBIA"] = 3
servoMap["RF_COXA"]  = 4
servoMap["RF_FEMUR"] = 5
servoMap["RF_TIBIA"] = 6
servoMap["LR_COXA"]  = 10
servoMap["LR_FEMUR"] = 11
servoMap["LR_TIBIA"] = 12
servoMap["RR_COXA"]  = 7
servoMap["RR_FEMUR"] = 8
servoMap["RR_TIBIA"] = 9

# setup model parameters
params = dict()
params["legs"] = 4
params["dof"] = 3
params["@VAL_LCOXA"]     = 70
params["@VAL_LFEMUR"]    = 105
params["@VAL_LTIBIA"]    = 205
params["@VAL_XCOXA"]     = 89
params["@VAL_YCOXA"]     = 89
params["@VAL_MCOXA"]     = 50
params["@SERVO_COUNT"]   = 12
params["@SERVO_INDEXES"] = ""
for k,v in servoMap.items():
    params["@SERVO_INDEXES"] = params["@SERVO_INDEXES"] + "#define " + k + " " + str(v) + "\n"
params["@SERVO_MINS"] = "int mins[] = {"+str([256, 256, 250, 256, 256, 250, 256, 256, 250,256, 256, 250]).replace('[', '').replace(']', '')+"};"
params["@SERVO_MAXS"] = "int maxs[] = {"+str([768, 768, 768,768, 768, 768,768, 768, 768,768, 768, 768 ]).replace('[', '').replace(']', '')+"};"



# Simple Heuristics (TODO: Replace with a gait builder) 
params["@X_STANCE"] = str(params["@VAL_LCOXA"]) 
params["@Y_STANCE"] = str(params["@VAL_LCOXA"] + params["@VAL_LFEMUR"])
params["@Z_STANCE"] = str(int(0.75*params["@VAL_LTIBIA"]))
params["@LIFT_HEIGHT"] = str(int(0.2*params["@VAL_LTIBIA"]))
# 10 or 12-bit?
params["@RAD_TO_SERVO_RESOLUTION"] = str(100)

# load general parameters 
template = open("tools/models/core/template.ik", 'r').readlines()
code = dict()
current = ""
for line in template:
    if line.find("@") == 0 and current == "":
        current = line.strip().rstrip()
    elif line.find("@END_SECTION") > -1:                
        current = ""
    else:
        try:
            code[current] = code[current] + line
        except:
            code[current] = line
# load the parameters for our particular model
modelDir = "lizard3"
template = open("tools/models/"+modelDir+"/template.ik").readlines()
current = ""
for line in template:
    if line.find("@") == 0 and current == "":
        current = line.strip().rstrip()
    elif line.find("@END_SECTION") > -1:                
        current = ""
    else:
        try:
            code[current] = code[current] + line
        except:
            code[current] = line
code.pop("")

templates = dict()
# load default templates
templates["gaits.h"] = open("tools/models/core/gaits.h").read()
templates["nuke.h"] = open("tools/models/core/nuke.h").read()
templates["nuke.cpp"] = open("tools/models/core/nuke.cpp").read() 
sketch = os.path.split(skDir)[1]        
templates[sketch+".ino"] = open("tools/models/core/default.pde").read()     
# for each file
for fileName in templates.keys():
    # insert code blocks
    for var, val in code.items():
        templates[fileName] = templates[fileName].replace(var,val)
    # search and replace variables
    for var, val in params.items():
        if var.find("@") == 0:
            templates[fileName] = templates[fileName].replace(var,str(val))
    for k,v in servoMap.items():
        templates[fileName] = templates[fileName].replace("@NEUTRAL_"+k, str(ik_neutral[v-1]))        
        templates[fileName] = templates[fileName].replace("@SIGN_"+k, signs[v-1:v])
    # save and reopen as lines                
    open(skDir + "/temp","w").write(templates[fileName])
    template = open(skDir+"/temp").readlines()
    # process IF/ELSE/END            
    i = 0
    out = None
    if fileName.endswith(".pde"):
        if os.path.exists(skDir+"/"+fileName):
            # open a different file, not the actual sketch
            out = open(skDir+"/sketch.NEW","w")
        else:
            out = open(skDir+"/"+fileName,"w")
    else:
        out = open(skDir+"/"+fileName,"w")
    while i < len(template):
        if template[i].find("@IF") >= 0:
            # do we include this?
            line = template[i][template[i].find("@IF")+3:].strip().rstrip()
            var = line[0:line.find(" ")].rstrip()
            val = line[line.find(" ")+1:].strip().rstrip().split()
            i = i + 1   
            if params[var] in val:
                while template[i].find("@ELSE") < 0 and template[i].find("@END_IF") < 0:
                    print>>out, template[i].rstrip()
                    i = i + 1
                while template[i].find("@END_IF") < 0:
                    i = i + 1
            else:
                while template[i].find("@ELSE") < 0 and template[i].find("@END_IF") < 0:
                    i = i + 1
                if template[i].find("@ELSE") >= 0:
                    i = i + 1 # don't output @ELSE
                while template[i].find("@END_IF") < 0:
                    print>>out, template[i].rstrip()
                    i = i + 1
        else:
            print>>out, template[i].rstrip()
        i = i + 1
    out.close()

file = open(skDir + "/gaits.h", "r")
fileText = ""
for line in file.readlines():
    if not "MIDDLE" in line:
        fileText += line
file.close()
file = open(skDir + "/gaits.h", "w")
file.write(fileText)
file.close()








