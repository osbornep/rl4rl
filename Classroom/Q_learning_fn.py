#------------------------------------------------------------------------------------------
# Q LEARNING FUNCTION

def Q_learning(Q_table, start_state, num_episodes, epsilon, num_random_episodes, alpha, gamma):
    Q_value_tracker = pd.DataFrame()
    for episode in tqdm(range(0,num_episodes)):
        # Track episode number with tqdm or can use simple print function
        # print("Episodes Completed: ", np.round( (episode/num_episodes)*100,2),"%")
        
        # Add this so start state doesn't need to be given by user input
        if (start_state is None):
            state = random.choice(states)
        else:
            state = start_state
            
        # Initialise action loop    
        a = 1
        while True:
            # End loop at terminal states
            if (state == 'recycling')|(state == 'trash'):
                break
            else:
                # Apply epsilon-greedy
                #------
                # We set first few episodes to follow purely randomly selection for exploration
                greedy_rng = np.random.rand()
                if (episode<num_random_episodes):
                    action = random.choice(actions)
                # Randomly select with P=epsilon
                elif (greedy_rng <= epsilon):
                    action = random.choice(actions)
                # Greedy (max value currently) otherwise 
                else:
                    # Pick action in state with highest Q value, randomly select if multiple match same max value
                    Q_table_max = Q_table[Q_table['Q'] == max(Q_table['Q'])]
                    if len(Q_table_max)>1:
                        action = Q_table_max.sample().iloc[0]['action']
                    else:
                        action = Q_table_max.iloc[0]['action']
                #------
                
                
                # Environment probabilistric outcome
                #---
                # environment fn output: return(state, action, state_x, state_y, u, v, next_state, next_state_x, next_state_y, reward)
                outcome = environment(state, action)
                
                new_state = outcome[6]
                new_x = outcome[7]
                new_y = outcome[8]
                r = outcome[9]
                #------
                
                
                # Update Values
                #------
                # Update Q based on episode outcome
                # Q learning update: Q(s_{t},a_{t}) <-- (1-alpha)*Q(s_{t},a_{t}) + alpha[r + gamma*max(Q(s_{t+1},a))]
                Q_table_new_state = Q_table[Q_table['state']==new_state]
                max_Q_new_state = Q_table_new_state[Q_table_new_state['Q'] == max(Q_table_new_state['Q'])].iloc[0]['Q']
                
                Q_table['Q'] = np.where( (Q_table['state']==state)&(Q_table['action']==action), 
                                        ((1-alpha)*Q_table['Q']) + (alpha*(r + (gamma*max_Q_new_state))),
                                        Q_table['Q'] )
                #------
                
                # Move to next action, make the new state the current state
                #------
                a=a+1
                state=new_state
                #------

        Q_value_tracker = Q_value_tracker.append(pd.DataFrame({'episode':episode, 'mean_Q': Q_table['Q'].mean(),'total_Q':Q_table['Q'].sum()}, index=[episode]))
        
    return(Q_table, Q_value_tracker)
