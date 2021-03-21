import pandas as pd
from itertools import islice
from collections import Counter

file_path = "./Harry Potter.txt"
test_file_path = "./originText.txt"
bksp_rate = 0
evaluation_switch = True
[21111212111, 21121112111, 21112112111, 21211212111, 21121112111, 21111112111, 21211212111, 21121121111, 21121211211, 21112112111, 21121121111, 21212112111, 21121121111]

trace_dict = {
21111111111: {'<non-US-1>'},
21111111121: {'<Release key>'},
21111111211: {'F11','KP','KP0','SL'},# scroll lock key pad
21111112111: {'8','u'},
21111121111: {'2','a'},
21111121211: {'Caps_Lock'},
21111211111: {'F4',"'"},
21111211211: {'-',';','KP7'},
21111212111: {'5','t'},
21112111111: {'F12','F2','F3'},
21112111121: {'Alt+SysRq'},
21112111211: {'9','Bksp','Esc','KP6','NL','o'},#number lock
21112112111: {'3','6','e','g'},
21112121111: {'1','CTRL_L'},
21112121211: {'['},
21121111111: {'F5','F7'},
21121111211: {'KP-','KP2','KP3','KP5','i','k'},
21121112111: {'b','d','h','j','m','x'},
21121121111: {'Shift','s','y'},
21121121211: {'’',' ',']'},
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
21212121211: {'='}}



removed_items ={'F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12','NL','Alt+SysRq','Tab',
                '<Release key>','<non-US-1>','Alt_L','SHIFT_R','CTRL_L','SL','KP+','KP.','KP-','’'}


not_in_table = {'z','\n'}
def get_key (dictionary, value):
#####################################################################################################################
# This function can get key based on unique value                                                                      #
#####################################################################################################################    
    return str([k for k, v in dictionary.items() if value in v][0])
def split_every(n:int, iterable:str):
#####################################################################################################################
# This function is a iterator which generates a pair of bigrams for further use.                                    #
# Note:                                                                                                             #
# Input: n:int: 2 means bigram                                                                                      #
#        iterable:str: the text to be splited                                                                       #
#####################################################################################################################
    
    i = iter(iterable)
    j = iter(iterable[1:])
    
    piece1 = ''.join(list(islice(i, n)))
    piece2 = ''.join(list(islice(j, n)))
    while piece1 and piece2:
        yield piece1,piece2
        piece1 = ''.join(list(islice(i, n)))
        piece2 = ''.join(list(islice(j, n)))

def get_bigram_freq(text:str):
#####################################################################################################################
# This function generates a counter for frequence of each bigrams                                                    #
# Note:                                                                                                             #
# Input: text:str: text to be bigramed                                                                   #
#####################################################################################################################
    freqs = Counter()
    for combo1,combo2 in split_every(2, text): # adjust n here
        freqs[combo1] += 1
        freqs[combo2] += 1
    dict(freqs)
    return freqs

def get_count_matrix(bigram_dict:dict,count_mat:dict):
    #####################################################################################################################
    # This function could mapp plain text into the transition count matrix. It focuses only on the bigrams of the input # 
    # artilcles, counts each bigrams and generates a transition matrix of keyboard's press sequence.                    #
    # Note:
    # Input: bigram_dict:dict: the dictionary of the generates bigrams.
    #        count_mat:dict: the 2D dictionary which will save the count of transistions.
    #####################################################################################################################
    # set that need shift 
    dfcount_mat=pd.DataFrame(count_mat) 
    no_shift_set = {',','.','/',';',"'",'[',']','\\',' ',"\n"}
    shift_set = {'!',"@",'#','$','%','^','&','*',"(",')','_','+','{','}','|',':','"','<','>','?'}
    shift_dict = {'!':'1',"@":'2','#':'3','$':'4','%':'5','^':'6','&':'7','*':'8',"(":'9',')':'0','_':'-','+':'=','{':'[','}':']','|':'\\',':':';','"':';','<':',','>':'.','?':'/'}
    #note if sure add 2, number and kp num add 1
    for i in bigram_dict:
        firstToken = i[0]
        secondToken  = i[1]
    #sec1 checked 
        
        if firstToken.isalnum() and secondToken.isalnum(): 
            if firstToken.islower() and secondToken.islower() or firstToken.isupper() and secondToken.isupper():#ALAL alal
                dfcount_mat.loc[firstToken.lower(),secondToken.lower()] += 2 * bigram_dict[i]
            elif firstToken.islower() and secondToken.isupper() or firstToken.isupper() and secondToken.islower():#ALal alAL
                dfcount_mat.loc[firstToken.lower(),'Caps_Lock'] += 2 * bigram_dict[i]
                dfcount_mat.loc['Caps_Lock',secondToken.lower()] += 2 * bigram_dict[i]
            elif (firstToken.isdigit() and secondToken.isdigit()):#numnum 
                dfcount_mat.loc[('KP'+str(firstToken)),('KP'+str(secondToken))] += 1 * bigram_dict[i]
                dfcount_mat.loc[firstToken,secondToken] += 1 * bigram_dict[i]
            elif (firstToken.isdigit() and secondToken.islower()):#numal
                dfcount_mat.loc[('KP'+str(firstToken)),secondToken] += 1 * bigram_dict[i]
                dfcount_mat.loc[firstToken,secondToken] += 1 * bigram_dict[i]
            elif (firstToken.islower() and secondToken.isdigit()):#alnum
                dfcount_mat.loc[firstToken,('KP'+str(secondToken))] += 1 * bigram_dict[i]
                dfcount_mat.loc[firstToken,secondToken] += 1 * bigram_dict[i]
            elif (firstToken.isdigit() and secondToken.isupper()):#numAL  problematic
                dfcount_mat.loc[firstToken,'Caps_Lock'] += 1 * bigram_dict[i]
                dfcount_mat.loc['Caps_Lock',secondToken.lower()] += 1 * bigram_dict[i]
                dfcount_mat.loc[('KP'+str(firstToken)),'Caps_Lock'] += 1 * bigram_dict[i]
                dfcount_mat.loc['Caps_Lock',secondToken.lower()] += 1 * bigram_dict[i]
            elif (firstToken.isupper() and secondToken.isdigit()):#ALnum  problematic
                dfcount_mat.loc[firstToken.lower(),'Caps_Lock'] += 1 * bigram_dict[i]
                dfcount_mat.loc['Caps_Lock',secondToken] += 1 * bigram_dict[i]
                dfcount_mat.loc[firstToken.lower(),'Caps_Lock'] += 1 * bigram_dict[i]
                dfcount_mat.loc['Caps_Lock',('KP'+str(secondToken))] += 1 * bigram_dict[i]
            # print("alnm alnm")
            # print(dfcount_mat)            
    #sec2 checked
        elif (firstToken.islower() and secondToken  in no_shift_set) or (secondToken.islower() and firstToken in no_shift_set) or(secondToken in no_shift_set and firstToken in no_shift_set):
            #alpun punal punpun
            dfcount_mat.loc[firstToken,secondToken] += 2 * bigram_dict[i]
            # print("no change alpun punal punpun")
            # print(dfcount_mat)        
    #sec3 checked
        elif firstToken.isupper():
            if secondToken in shift_set:#AL shpun
                dfcount_mat.loc[firstToken.lower(),'Caps_Lock'] += 2 * bigram_dict[i]
                dfcount_mat.loc['Caps_Lock',"Shift"] += 2 * bigram_dict[i]
                dfcount_mat.loc["Shift",shift_dict[secondToken]] += 2 * bigram_dict[i]
            elif secondToken in no_shift_set:#AL pun
                dfcount_mat.loc[firstToken.lower(),'Caps_Lock'] += 2 * bigram_dict[i]
                dfcount_mat.loc['Caps_Lock',secondToken] += 2 * bigram_dict[i]
        elif firstToken.islower() and (secondToken in shift_set):#al shpun
            dfcount_mat.loc[firstToken,"Shift"] += 2 * bigram_dict[i]
            dfcount_mat.loc["Shift",shift_dict[secondToken]] += 2 * bigram_dict[i]
      
            # print("AL shpun AL pun al shpun")
            # print(dfcount_mat) 
    #sec4 checked
        elif firstToken.isdigit():
            if secondToken in shift_set:#num shpun
                dfcount_mat.loc[('KP'+str(firstToken)),"Shift"] += 1 * bigram_dict[i]
                dfcount_mat.loc["Shift",shift_dict[secondToken]] += 1 * bigram_dict[i]
                dfcount_mat.loc[firstToken,"Shift"] += 1 * bigram_dict[i]
                dfcount_mat.loc["Shift",shift_dict[secondToken]] += 1 * bigram_dict[i]
            elif secondToken in no_shift_set:#num pun
                dfcount_mat.loc[('KP'+str(firstToken)),secondToken] += 1 * bigram_dict[i]
                dfcount_mat.loc[firstToken,secondToken] += 1 * bigram_dict[i]
            # print("num shpun num pun")
            # print(dfcount_mat) 
    
    #sec5 checked
        elif firstToken in shift_set:# maybe assert "release??????"
            if secondToken.isupper():#shpun AL
                dfcount_mat.loc[shift_dict[firstToken],'Caps_Lock'] += 2 * bigram_dict[i]
                dfcount_mat.loc['Caps_Lock',secondToken.lower()] += 2 * bigram_dict[i]
            elif secondToken.islower():#shpun al
                dfcount_mat.loc[shift_dict[firstToken],secondToken] += 2  * bigram_dict[i]
            elif secondToken.isdigit():#shpun num
                dfcount_mat.loc[shift_dict[firstToken],('KP'+str(secondToken))] += 1 * bigram_dict[i]
                dfcount_mat.loc[shift_dict[firstToken],secondToken] += 1  * bigram_dict[i]   
            elif secondToken in shift_set:#shpun shpun
                dfcount_mat.loc[shift_dict[firstToken],shift_dict[secondToken]] += 2 * bigram_dict[i]
            elif secondToken in no_shift_set:#shpun pun
                dfcount_mat.loc[shift_dict[firstToken],secondToken] += 2  * bigram_dict[i] 
            # print("shpun AL shpun al shpun num shpun shpun shpun pun")
            # print(dfcount_mat) 
            
    #sec 6 checked
        elif firstToken in no_shift_set:
            if secondToken.isupper():#pun AL
                dfcount_mat.loc[firstToken,'Caps_Lock'] += 2 * bigram_dict[i]
                dfcount_mat.loc['Caps_Lock',secondToken.lower()] += 2 * bigram_dict[i]
            elif secondToken.isdigit():#pun num
                dfcount_mat.loc[firstToken,('KP'+str(secondToken))] += 1 * bigram_dict[i]
                dfcount_mat.loc[firstToken,secondToken] += 1   * bigram_dict[i]
            elif secondToken in shift_set:#pun shpun
                dfcount_mat.loc[firstToken,"Shift"] += 2 * bigram_dict[i]
                dfcount_mat.loc["Shift",shift_dict[secondToken]] += 2 * bigram_dict[i]
            # print("pun AL pun num pun shpun")
            # print(dfcount_mat)   
    return  dfcount_mat
def get_trans_mat_and_obs(trace_dict:dict, not_in_table:set, removed_items:set):
#####################################################################################################################
# This function could generate the empty transition matrix for hmm and viterbi algorthum, empty count mat, along
# with the obsersation list and state list
# Input:   trace_dict:dict
          # not_in_table:set :items that are not listed in the table
          # removed_items:set  : items that are irrelavent or not important
# Output: states:list
#         observations lsit:
#         transition_empty_mat dict:
#         count_mat dict:
#####################################################################################################################
    observations = [observation for observation in trace_dict]

    
    states_count = set()
    for key in trace_dict:
        states_count |= trace_dict[key]
    # print("states_in_table:"+str(len(states_count)))
    # print("not_in_table:"+str(len(not_in_table)))
    # print("removed_items:"+str(len(removed_items)))
    states_count |= not_in_table    
    # print("states_count:"+str(len(states_count)))
    dictInDict = dict.fromkeys(states_count, 0) 
    count_matrix = dict.fromkeys(states_count, dictInDict) 
    states_trans = set()
    for key in trace_dict:
        states_trans |= trace_dict[key]
    for key in removed_items:
        states_trans.remove(key)
    # print("states_trans:"+str(len(states_trans)))
    _ = dict.fromkeys(states_trans, 0) 
    transition_empty_mat = dict.fromkeys(states_trans, _) 
    states = list(states_trans)
    
    # observations = [_ for _ in]
    # print('observations'+str(observations))
    # print('states_trans'+str(states_trans))
    
    return states, observations, transition_empty_mat, count_matrix
def fill_trans_mat(count_mat,trans_mat:dict,bksp,states):
#####################################################################################################################
# This function could generate the transition matrix for hmm and viterbi algorthum. To generate the transition      #
# matrix, the keys in the count matrix has to be reduced.(Some keys which are not in the trace dictonary are going to 
# be removed.) Count number will be transformed into a double [0,1] which represents the probabilities of transition#
# And at last some hyperparameter will be set(eg. the probilities of key "backspace") to generate corresponding key #
# transition prob.
# Input: trans_mat:dataframe: the 2D dictionary which represents the transition matrix
#        count_mat:dict: the 2D dictionary which will store the count of transistions.
#        bksp:double: typo rate[0,1]
#        states: list or set
# Output: trans_mat: dict in dict
#         start_prob: df : first letter distribution (the next letter after Space)
#####################################################################################################################
    count_mat['Col_sum'] = count_mat.apply(lambda x: x.sum(), axis=1)
    num_tran_state = len(trans_mat)
    dftrans_mat =pd.DataFrame(trans_mat) # convet to df
    rest_prob = 1 - bksp
    if bksp>1 or bksp<0:
        raise RuntimeError("Probability should be between 1 and 0")
    else:
        print("bksp richtig")
    for i, row in dftrans_mat.iterrows(): #横向index
        for j, value in row.iteritems():
            if count_mat.loc[i,'Col_sum'] != 0:
                dftrans_mat.loc[i,j] =  count_mat.loc[i,j]/count_mat.loc[i,'Col_sum']*rest_prob
                
            else:
                dftrans_mat.loc[i,j] = 0
            if i == 'Space':
                dftrans_mat.loc['Space',j] =  count_mat.loc[' ',j]/count_mat.loc[' ','Col_sum']*rest_prob
            elif j == 'Space':
                dftrans_mat.loc[i,'Space'] =  count_mat.loc[i,' ']/count_mat.loc[i,'Col_sum']*rest_prob
           
    for l in dftrans_mat:
        dftrans_mat.loc['Bksp',l] = bksp/num_tran_state
        dftrans_mat.loc[l,'Bksp'] = bksp*100
    dftrans_mat.fillna(0, inplace = True)
    set(states)
    start_probability = dict()
    start_probability = dict.fromkeys(states, 0)
    for i in start_probability:
        start_probability[i] = dftrans_mat.loc[' ',i]# get the first letter distribution (the next letter after Space)
    return start_probability, dftrans_mat

def get_ave_start_prob(states:list):
#####################################################################################################################
# This function could generate the averaged start_probability . but the fuction fill_trans_mat() could generate     #
# better start_probability
#####################################################################################################################
    ave = 1/len(states)
    average_start_probability = dict()
    average_start_probability = dict.fromkeys(states, ave) 
    # print(average_start_probability)
    return average_start_probability

def get_emission_prob(states, observation, trace_dict):
#####################################################################################################################
# This function could generate the averaged emission prob
# input : states, list of states
#         observation, list of obs(int
#         trace_dict dictInDict
#####################################################################################################################
    em_mat = dict()
    st_dict = dict.fromkeys(states, 0)
    em_mat = dict.fromkeys(observation, st_dict)
    dfem_mat=pd.DataFrame(em_mat)
    # print(dfem_mat)
    for i in states:
        # print(i)
        # print(int(get_key(trace_dict,i)))
        dfem_mat[int(get_key(trace_dict,i))][i] = 1
    # print(dfem_mat)    
    return dfem_mat

def viterbi(obs, states, start_p, trans_p, emit_p):
#####################################################################################################################
# This function is the example function in wikipedia.
# https://en.wikipedia.org/wiki/Viterbi_algorithm
# Thanks to the writer and editors of this article
#####################################################################################################################
    V = [{}]
    for st in states:
        V[0][st] = {"prob": start_p[st] * emit_p[obs[0]][st], "prev": None}
    # Run Viterbi when t > 0
    for t in range(1, len(obs)):
        V.append({})
        for st in states:
            max_tr_prob = V[t - 1][states[0]]["prob"] * trans_p[st][states[0]]
            prev_st_selected = states[0]
            for prev_st in states[1:]:
                tr_prob = V[t - 1][prev_st]["prob"] * trans_p[st][prev_st]
                if tr_prob > max_tr_prob:
                    max_tr_prob = tr_prob
                    prev_st_selected = prev_st

            max_prob = max_tr_prob * emit_p[obs[t]][st]
            V[t][st] = {"prob": max_prob, "prev": prev_st_selected}

    # for line in dptable(V):
    #     print(line)

    opt = []
    max_prob = 0.0
    best_st = None
    # Get most probable state and its backtrack
    for st, data in V[-1].items():
        if data["prob"] > max_prob:
            max_prob = data["prob"]
            best_st = st
    opt.append(best_st)

    previous = best_st

    # Follow the backtrack till the first observation
    for t in range(len(V) - 2, -1, -1):
        
        opt.insert(0, V[t + 1][previous]["prev"])
        previous = V[t + 1][previous]["prev"]
                   

    print ("The inference hidden states are:\n" + " ".join(opt))
    return list(opt)
def dptable(V):
#####################################################################################################################
# This function is the example function in wikipedia.
# https://en.wikipedia.org/wiki/Viterbi_algorithm
# Thanks to the writer and editors of this article
#####################################################################################################################
    # Print a table of steps from dictionary
    yield " ".join(("%12d" % i) for i in range(len(V)))
    for state in V[0]:
        yield "%.7s: " % state + " ".join("%.7s" % ("%f" % v[state]["prob"]) for v in V)




def falling_trace_gen(string:str):
#####################################################################################################################
# This function is used to generate the falling edge trace to evaluate and test the sequence.
# input string :str
# output trace list:list
#####################################################################################################################
    resultlist = []
    for c in string.lower():
        if c != "\n":
            if c == ' ':
                tmp = 'Space'
            else:
                tmp = c
            for key, values in trace_dict.items():
                if tmp in values:
                    resultlist.append(key)
                    continue
    return resultlist

def keystroke_trace_gen(string:str):
#####################################################################################################################
# This function is used to generate the keystrokes trace to evaluate and test the sequence.
# input string:str 
# output string list:list
#####################################################################################################################
    resultlist = []
    for c in string.lower():
        if c != "\n":
            if c == ' ':
                c = 'Space'
            resultlist.append(c)
    return resultlist


def compare_list(list1:list, list2:list):
#####################################################################################################################
# This function is used to generate the compare result remove shift and Caps_Lock
# input string:str1, original 
#              str2 inference 
# output:same count: int count of same keystrokes
#        len of total keystrokes
#####################################################################################################################
    same_count = 0
    for i in list2:
        if i == "Shift":
            list2.remove("Shift")
    for i in list2:
        if i == "Caps_Lock":
            list2.remove("Caps_Lock")
    if len(list1) == len(list2):
        for i, item in enumerate(list1):
            if item == list2[i]:
                same_count += 1
    return same_count , len(list1)   


if __name__ == '__main__':
    states, observations, transition_empty, count_matrix = get_trans_mat_and_obs(trace_dict, not_in_table, removed_items)
    with open(file_path,'r', encoding='UTF-8') as handle:
        f = handle.read()
    ungrade_str = f if len(f)%2 == 1 else f[:-1]
    freqs = get_bigram_freq(ungrade_str)# if handle.read()%2 ==0 else handle.read()[:-1]) 
    #get count matrix
    count_matrix = get_count_matrix(freqs,count_matrix)
    # print(count_matrix)
    #fill transiton matrix based on count matrix & bksp prob
    start_probability, transition_probability = fill_trans_mat(count_matrix,transition_empty,bksp_rate,states)
    print()
    ave_start_probability = get_ave_start_prob(states)
    
    emission_probability = get_emission_prob(states,observations,trace_dict)
    
    states = tuple(states)
    observations = tuple(observations)
    
    
        
                
    
##############             *    *    *      make inference here      *     *      *                             ################################################    
    obs = [21121121111,21121112111,21111121111,21121111211,21112112111,21121121111,21211211211,21112112111,21111121111,21211212111,21112112111]
    #shakspeare
    viterbi(obs,
            states,
            start_probability,
            transition_probability,
            emission_probability)
    obs = [21121121111, 21121112111, 21111121111, 21121111211, 21112112111, 21121121111, 21211211211, 21112112111, 21111121111, 21211212111, 21112112111, 21211212111, 21211121111, 21111121111, 21121121111, 21211212111, 21121212111, 21112112111, 21211212111, 21121121111, 21212112111, 21211212111, 21121111211, 21211112111, 21121121111, 21112112111, 21211112111, 21111112111, 21211212111, 21112112111]
    viterbi(obs,
            states,
            start_probability,
            transition_probability,
            emission_probability)
    obs =[21211211211, 21111121111, 21121121111, 21121121111, 21211121111, 21112111211, 21211212111, 21121112111]    
    viterbi(obs,
            states,
            ave_start_probability,
            transition_probability,
            emission_probability)
    obs = [21121112111, 21112112111, 21121211211, 21121211211, 21112111211]
    viterbi(obs,
            states,
            ave_start_probability,
            transition_probability,
            emission_probability)
    
####################################################### evaluation ##########################################################################################
    if evaluation_switch == True:
        accuracy = {}
        for length in [3,5,10,15,20,30,40,50,70,90]:
            with open(test_file_path,'r', encoding='UTF-8') as handle:
                f = handle.read(130)
                sentence_list = []
                a = f.split(' ',1)
                sentence_list.append(a[1][0:length])
                while len(f)!= 0:
                     f = handle.read(120)
                     a = f.split(' ',1)
                     try:
                         sentence_list.append(a[1][0:length])
                     except:
                         print("\n")
            correct_count_sum = 0
            count_sum = 0
            i = 0
            for sent in sentence_list:
                obs = falling_trace_gen(sent)
                comp_list = keystroke_trace_gen(sent)
                try :
                    inference_list = viterbi(obs,states,ave_start_probability,transition_probability,emission_probability)
                    a , b = compare_list(comp_list, inference_list)
                    print(comp_list)
                    print(inference_list)
                    if a != 0:
                        i +=1
                        correct_count_sum += a
                        count_sum += b
                    print(f"corret inferenz: {a} total length: {b} accuracy:{a/b}")
                except:
                    print("")
                if i ==20:
                    break
            print(f"corret inferenz: {correct_count_sum} total length: {count_sum} accuracy:{correct_count_sum/count_sum}")
            accuracy[length] = {'inferenz': correct_count_sum,'length':count_sum,'accuracy':correct_count_sum/count_sum}
        for i in accuracy:
            print(f"input length {i}:{accuracy[i]}")

  