# EMEmanationSEEMOO
Keyboard EM Emanations side channel attack 
Zhengkun Li Niklas Miller Erik Kubaczka

Variables:

bksp_rate: 
The speculated rate of person under attak, default: 0(0%percent chance of typo)

file_path: 
The imported article in form of txt: default: Harry Potter 1 2 3.(Can be changed based on the information of person under attack, if no such information avaliable, a really long article could work)

test_file_path: 
Imported article in form of txt: default: introduction for Shakspeare. This file is used to generate the evaluation.

evaluation_switch: 
Wether go with the evaluation: default: True. Caution, this evaluation process will cause a lot of time. If it's not necessary please set it as Faulse.



**************************  Inference**************************************
in the main func:

Add a list of falling edge sequences, for example: obs = [21121121111,21121112111,21111121111,21121111211,21112112111,21121121111,21211211211,21112112111,21111121111,21211212111,21112112111]
    #shakspeare
Then call the viterbi functions with the added list as the first var. For example:    
    viterbi(obs,
            states,
            ave_start_probability,
            transition_probability,
            emission_probability)
The inference will be printed as :
The inference hidden states are:
s h a k e s p e a r e

Requirments
pandas
itertools
collections
matplotlib

