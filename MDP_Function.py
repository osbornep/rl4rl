def MDP_fn(states,actions,next_states):
    import pandas as pd
    import numpy as np
    import random
    state_list = states.unique()
    action_list = actions.unique()
    next_state_list = next_states.unique()
    MDP = pd.DataFrame()
    for state in state_list:
        for action in action_list:
            for next_state in next_state_list:
                MDP = MDP.append(pd.DataFrame({'state':state, 'action':action, 'next_state':next_state},index = [state] ))
                                 
    MDP = MDP.reset_index(drop=True)
    MDP = MDP.sort_values(['state','action'])
    
    MDP['s_a_count'] = 0
    MDP['s_a_ns_count'] = 0
    
    for obs in range(0,len(states)):
        state = states[obs]
        action = actions[obs]
        next_state = next_states[obs]
        
        MDP['s_a_count'] = np.where( (MDP['state']==state)&(MDP['action']==action),MDP['s_a_count']+1,MDP['s_a_count'])
        MDP['s_a_ns_count'] = np.where( (MDP['state']==state)&(MDP['action']==action)&(MDP['next_state']==next_state),MDP['s_a_ns_count']+1,MDP['s_a_ns_count'])
        
        
    MDP['s_a_prob'] = MDP['s_a_count']/sum(MDP['s_a_ns_count'])
    MDP['s_a_ns_prob'] = MDP['s_a_ns_count']/sum(MDP['s_a_ns_count'])
    MDP['ns_give_s_a_prob'] = np.where(MDP['s_a_prob']==0,0, MDP['s_a_ns_prob']/MDP['s_a_prob'])
    
    return(MDP)