from collections import Counter
from itertools import islice
import pandas as pd
import numpy as np
########################################## Vars
filePath = "C:/Users/97053/Desktop/originText.txt"


#############################words parser
traceDict = {
21111111111: {'<non-US-1>'},
21111111121: {'<Release key>'},
21111111211: {'F11','KP','KP0','SL'},
21111112111: {'8','u'},
21111121111: {'2','a'},
21111121211: {'Caps_Lock'},
21111211111: {'F4','‘'},
21111211211: {'-',';','KP7'},
21111212111: {'5','t'},
21112111111: {'F12','F2','F3'},
21112111121: {'Alt+SysRq'},
21112111211: {'9','Bksp','Esc','KP6','NL','o'},
21112112111: {'3','6','e','g'},
21112121111: {'1','CTRL_L'},
21112121211: {'['},
21121111111: {'F5','F7'},
21121111211: {'KP-','KP2','KP3','KP5','i','k'},
21121112111: {'b','d','h','j','m','x'},
21121121111: {'SHIFT_L','s','y'},
21121121211: {'’','ENTER',']'},
21121211111: {'F6','F8'},
21121211211: {'/','KP4','l'},
21121212111: {'f','v'},
21211111111: {'F9'},
21211111211: {',','KP+','KP.','KP9'},
21211112111: {'7','c','n'},
21211121111: {'Alt_L','w'},
21211121211: {'SHIFT_R','\\'},
21211211111: {'F10','Tab'},
21211211211: {'.','KP1','p'},
21211212111: {'Space','r'},
21212111111: {'F1'},
21212111211: {'0','KP8'},
21212112111: {'4','y'},
21212121111: {'q'},
21212121211: {'='}
}

removedItems = ['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12','Nl','Alt+SysRq','Tab',
                '<Release key>','<non-US-1>','Alt_L']

# nothingHappenState = 

observations = [observation for observation in traceDict]
#print(observations)
states = set()
for key in traceDict:
    states |= traceDict[key]
#print(states)

dictInDict = dict.fromkeys(states, 0) 
transition_probability = dict.fromkeys(states, dictInDict) 
#print(transition_probability)





def split_every(n, iterable):
    i = iter(iterable)
    j = iter(iterable[1:])
    piece1 = ''.join(list(islice(i, n)))
    piece2 = ''.join(list(islice(j, n)))
    while piece1 and piece2:
        yield piece1,piece2
        piece1 = ''.join(list(islice(i, n)))
        piece2 = ''.join(list(islice(j, n)))

def get_bigram_freq(text):
    """ return ngrams for text """
    freqs = Counter()
    for combo1,combo2 in split_every(2, text): # adjust n here
        freqs[combo1] += 1
        freqs[combo2] += 1
    dict(freqs)
    return freqs

def get_trans_mat_from_text(bigramDict:dict,transtest:dict):
    dftranstest=pd.DataFrame(transtest) 
    # set that need shift 
    noShiftSet = {',','.','/',';',"'",'[',']','\\',' '}
    shiftSet = {'!',"@",'#','$','%','^','&','*',"(",')','_','+','{','}','|',':','"','<','>','?'}
    shiftDict = {'!':'1',"@":'2','#':'3','$':'4','%':'5','^':'6','&':'7','*':'8',"(":'9',')':'0','_':'-','+':'=','{':'[','}':']','|':'\\',':':';','"':';','<':',','>':'.','?':'/'}
    #note if sure add 2, number and kp num add 1
    for i in bigramDict:
        firstToken = i[0]
        secondToken  = i[1]
    #sec1 checked 
        if firstToken.isalnum() and secondToken.isalnum(): 
            if firstToken.islower() and secondToken.islower() or firstToken.isupper() and secondToken.isupper():#ALAL alal
                dftranstest.loc[firstToken.lower(),secondToken.lower()] += 2 * bigramDict[i]
            elif firstToken.islower() and secondToken.isupper() or firstToken.isupper() and secondToken.islower():#ALal alAL
                dftranstest.loc[firstToken.lower(),'Caps_Lock'] += 2 * bigramDict[i]
                dftranstest.loc['Caps_Lock',secondToken.lower()] += 2 * bigramDict[i]
            elif (firstToken.isdigit() and secondToken.isdigit()):#numnum 
                dftranstest.loc[('KP'+str(firstToken)),('KP'+str(secondToken))] += 1 * bigramDict[i]
                dftranstest.loc[firstToken,secondToken] += 1 * bigramDict[i]
            elif (firstToken.isdigit() and secondToken.islower()):#numal
                dftranstest.loc[('KP'+str(firstToken)),secondToken] += 1 * bigramDict[i]
                dftranstest.loc[firstToken,secondToken] += 1 * bigramDict[i]
            elif (firstToken.islower() and secondToken.isdigit()):#alnum
                dftranstest.loc[firstToken,('KP'+str(secondToken))] += 1 * bigramDict[i]
                dftranstest.loc[firstToken,secondToken] += 1 * bigramDict[i]
            elif (firstToken.isdigit() and secondToken.isupper()):#numAL  problematic
                dftranstest.loc[firstToken,'Caps_Lock'] += 1 * bigramDict[i]
                dftranstest.loc['Caps_Lock',secondToken.lower()] += 1 * bigramDict[i]
                dftranstest.loc[('KP'+str(firstToken)),'Caps_Lock'] += 1 * bigramDict[i]
                dftranstest.loc['Caps_Lock',secondToken.lower()] += 1 * bigramDict[i]
            elif (firstToken.isupper() and secondToken.isdigit()):#ALnum  problematic
                dftranstest.loc[firstToken.lower(),'Caps_Lock'] += 1 * bigramDict[i]
                dftranstest.loc['Caps_Lock',secondToken] += 1 * bigramDict[i]
                dftranstest.loc[firstToken.lower(),'Caps_Lock'] += 1 * bigramDict[i]
                dftranstest.loc['Caps_Lock',('KP'+str(secondToken))] += 1 * bigramDict[i]
            print("alnm alnm")
            print(dftranstest)            
    #sec2 checked
        elif (firstToken.islower() and secondToken  in noShiftSet) or (secondToken.islower() and firstToken in noShiftSet) or(secondToken in noShiftSet and firstToken in noShiftSet):
            #alpun punal punpun
            dftranstest.loc[firstToken,secondToken] += 2 * bigramDict[i]
            print("no change alpun punal punpun")
            print(dftranstest)        
    #sec3 checked
        elif firstToken.isupper():
            if secondToken in shiftSet:#AL shpun
                dftranstest.loc[firstToken.lower(),'Caps_Lock'] += 2 * bigramDict[i]
                dftranstest.loc['Caps_Lock',"Shift"] += 2 * bigramDict[i]
                dftranstest.loc["Shift",shiftDict[secondToken]] += 2 * bigramDict[i]
            elif secondToken in noShiftSet:#AL pun
                dftranstest.loc[firstToken.lower(),'Caps_Lock'] += 2 * bigramDict[i]
                dftranstest.loc['Caps_Lock',secondToken] += 2 * bigramDict[i]
        elif firstToken.islower() and (secondToken in shiftSet):#al shpun
            dftranstest.loc[firstToken,"Shift"] += 2 * bigramDict[i]
            dftranstest.loc["Shift",shiftDict[secondToken]] += 2 * bigramDict[i]
      
            print("AL shpun AL pun al shpun")
            print(dftranstest) 
    #sec4 checked
        elif firstToken.isdigit():
            if secondToken in shiftSet:#num shpun
                dftranstest.loc[('KP'+str(firstToken)),"Shift"] += 1 * bigramDict[i]
                dftranstest.loc["Shift",shiftDict[secondToken]] += 1 * bigramDict[i]
                dftranstest.loc[firstToken,"Shift"] += 1 * bigramDict[i]
                dftranstest.loc["Shift",shiftDict[secondToken]] += 1 * bigramDict[i]
            elif secondToken in noShiftSet:#num pun
                dftranstest.loc[('KP'+str(firstToken)),secondToken] += 1 * bigramDict[i]
                dftranstest.loc[firstToken,secondToken] += 1 * bigramDict[i]
            print("num shpun num pun")
            print(dftranstest) 
    
    #sec5 checked
        elif firstToken in shiftSet:# maybe assert "release??????"
            if secondToken.isupper():#shpun AL
                dftranstest.loc[shiftDict[firstToken],'Caps_Lock'] += 2 * bigramDict[i]
                dftranstest.loc['Caps_Lock',secondToken.lower()] += 2 * bigramDict[i]
            elif secondToken.islower():#shpun al
                dftranstest.loc[shiftDict[firstToken],secondToken] += 2  * bigramDict[i]
            elif secondToken.isdigit():#shpun num
                dftranstest.loc[shiftDict[firstToken],('KP'+str(secondToken))] += 1 * bigramDict[i]
                dftranstest.loc[shiftDict[firstToken],secondToken] += 1  * bigramDict[i]   
            elif secondToken in shiftSet:#shpun shpun
                dftranstest.loc[shiftDict[firstToken],shiftDict[secondToken]] += 2 * bigramDict[i]
            elif secondToken in noShiftSet:#shpun pun
                dftranstest.loc[shiftDict[firstToken],secondToken] += 2  * bigramDict[i] 
            print("shpun AL shpun al shpun num shpun shpun shpun pun")
            print(dftranstest) 
            
    #sec 6 checked
        elif firstToken in noShiftSet:
            if secondToken.isupper():#pun AL
                dftranstest.loc[firstToken,'Caps_Lock'] += 2 * bigramDict[i]
                dftranstest.loc['Caps_Lock',secondToken.lower()] += 2 * bigramDict[i]
            elif secondToken.isdigit():#pun num
                dftranstest.loc[firstToken,('KP'+str(secondToken))] += 1 * bigramDict[i]
                dftranstest.loc[firstToken,secondToken] += 1   * bigramDict[i]
            elif secondToken in shiftSet:#pun shpun
                dftranstest.loc[firstToken,"Shift"] += 2 * bigramDict[i]
                dftranstest.loc["Shift",shiftDict[secondToken]] += 2 * bigramDict[i]
            print("pun AL pun num pun shpun")
            print(dftranstest)   
    return dftranstest
with open(filePath,'r', encoding='UTF-8') as handle:
    freqs = get_bigram_freq(handle.read()) 
###################################################################################

settest = set()  
sdasdasd = "/?"
if len(sdasdasd)%2 == 0:
    sdasdasd += " "
for i in sdasdasd:
    settest |= set(i.lower())
settest |= {"Caps_Lock"}
settest |= {"KP1"}
settest |= {"Shift"}
settest |= {" "}
dicttest = dict.fromkeys(settest, 0) 
transtest = dict.fromkeys(settest, dicttest)   


bigramDict = get_bigram_freq(sdasdasd)
print(get_bigram_freq(sdasdasd))


    
a = get_trans_mat_from_text(bigramDict,transtest)
    
print(a)
print(a[' ']['/'])


df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])
df2.index =['a','b','c']
print(df2)
df2['a']['b'] = 1
# df2['Col_sum'] = df2.apply(lambda x: x.sum(), axis=1)
# print(df2)
print(df2)
# transition_probability = {
#     'Healthy' : {'a': 0.7, 'b': 0.3},
#     'Fever' :   {'a': 0.4, 'b': 0.6},}
# print(transition_probability['Healthy']['b'])