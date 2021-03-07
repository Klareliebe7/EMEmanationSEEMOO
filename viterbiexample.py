
def Viterbit(obs, states, s_pro, t_pro, e_pro):\
    path = { s:[] for s in states} # init path: path[s] represents the path ends with s
    curr_pro = {}
 	for s in states:
		curr_pro[s] = s_pro[s]*e_pro[s][obs[0]]
 	for i in xrange(1, len(obs)):
		last_pro = curr_pro
		curr_pro = {}
		for curr_state in states:
 			max_pro, last_sta = max(((last_pro[last_state]*t_pro[last_state][curr_state]*e_pro[curr_state][obs[i]], last_state) 
 				                       for last_state in states))
 			curr_pro[curr_state] = max_pro
 			path[curr_state].append(last_sta)

 	# find the final largest probability
 	max_pro = -1
 	max_path = None
 	for s in states:
		path[s].append(s)
		if curr_pro[s] > max_pro:
 			max_path = path[s]
 			max_pro = curr_pro[s]
		# print '%s: %s'%(curr_pro[s], path[s]) # different path and their probability
 	return max_path


if __name__ == '__main__':
 	obs = ['21111212111', '21121112111', '21112112111']
 	print Viterbit(obs, states, start_probability, transition_probability, emission_probability)