import numpy as np
import pandas as pd
import os.path
from tqdm import tqdm
# BIN LOCATION
bin_x = 0
bin_y = 0

# Probability Function
def probability(bin_x, bin_y, state_x, state_y, throw_deg):

    #First throw exception rule if person is directly on top of bin:
    if((state_x==bin_x) & (state_y==bin_y)):
        probability = 1
    else:
        
        
        # To accomodate for going over the 0 degree line
        if((throw_deg>270) & (state_x<=bin_x) & (state_y<=bin_y)):
            throw_deg = throw_deg - 360
        elif((throw_deg<90) & (state_x>bin_x) & (state_y<bin_y)):
            throw_deg = 360 + throw_deg
        else:
            throw_deg = throw_deg
            
        # Calculate Euclidean distance
        distance = ((bin_x - state_x)**2 + (bin_y - state_y)**2)**0.5

        # max distance for bin will always be on of the 4 corner points:
        corner_x = [-10,-10,10,10]
        corner_y = [-10,10,-10,10]
        dist_table = pd.DataFrame()
        for corner in range(0,4):
            dist = pd.DataFrame({'distance':((bin_x - corner_x[corner])**2 + (bin_y - corner_y[corner])**2)**0.5}, index = [corner])
            dist_table = dist_table.append(dist)
        dist_table = dist_table.reset_index()
        dist_table = dist_table.sort_values('distance', ascending = False)
        max_dist = dist_table['distance'][0]
        
        distance_score = 1 - (distance/max_dist)

        # First if person is directly horizontal or vertical of bin:
        if((state_x==bin_x) & (state_y>bin_y)):
            direction = 180
        elif((state_x==bin_x) & (state_y<bin_y)):
             direction = 0
        
        elif((state_x>bin_x) & (state_y==bin_y)):
             direction = 270
        elif((state_x<bin_x) & (state_y==bin_y)):
             direction = 90
              
        # If person is north-east of bin:
        elif((state_x>bin_x) & (state_y>bin_y)):
            opp = abs(bin_x - state_x)
            adj = abs(bin_y - state_y)
            direction = 180 +  np.degrees(np.arctan(opp/adj))

        # If person is south-east of bin:
        elif((state_x>bin_x) & (state_y<bin_y)):
            opp = abs(bin_y - state_y)
            adj = abs(bin_x - state_x)
            direction = 270 +  np.degrees(np.arctan(opp/adj))

        # If person is south-west of bin:
        elif((state_x<bin_x) & (state_y<bin_y)):
            opp = abs(bin_x - state_x)
            adj = abs(bin_y - state_y)
            direction =  np.degrees(np.arctan(opp/adj))

        # If person is north-west of bin:
        elif((state_x<bin_x) & (state_y>bin_y)):
            opp = abs(bin_y - state_y)
            adj = abs(bin_x - state_x)
            direction = 90 +  np.degrees(np.arctan(opp/adj))

        direction_score = (45-abs(direction - throw_deg))/45
      
        probability = distance_score*direction_score
        if(probability>0):
            probability = probability
        else:
            probability = 0
        
    return(probability)

print("Initializing the Environment...")
print("----------------------------")
print(" ")

# Load initliased Q Table, otherwise create
if os.path.isfile('./Q_table_init.csv'):
    Q_table_init = pd.read_csv('./Q_table_init.csv')
    # For some reason some of the angles are being put as str instead of int, manual fix this
    t_d_l = []
    m_d_l = []
    for n,row in Q_table_init.iterrows():
        if row['throw_dir']=='none':
            t_d = 'none'
        else:
            t_d = int(row['throw_dir'])
        t_d_l.append(t_d)

        if row['move_dir']=='none':
            m_d = 'none'
        else:
            m_d = int(row['move_dir'])
        m_d_l.append(m_d)
    Q_table_init['throw_dir'] = t_d_l
    Q_table_init['move_dir'] = m_d_l
    print("Pre-run Q Table Loaded")
    print(Q_table_init.head())
else:
    # STATE SPACE    
    #Define Q(s,a) table by all possible states and THROW actions initialised to 0
    Q_table = pd.DataFrame()
    print("TROW Actions Progress: ")
    for z in tqdm(range(0,360)):
        throw_direction = int(z)
        for i in range(0,21):
            state_x = int(-10 + i)
            for j in range(0,21):
                state_y = int(-10 + j)
                reward = 0
                Q = pd.DataFrame({'throw_dir':throw_direction,'move_dir':"none",'state_x':state_x,'state_y':state_y, 'reward': reward}, index = [0])
                Q_table = Q_table.append(Q)
    Q_table = Q_table.reset_index(drop=True)
    
    print("Q table 1 initialised")

    #Define Q(s,a) table by all possible states and MOVE actions initialised to 0
    print("MOVE Actions Progress: ")
    for x in tqdm(range(0,21)):
        state_x = int(-10 + x)
        for y in range(0,21):
            state_y = int(-10 + y)
            # 8 Possible move directions from [North, North-East, East, South-East, South, South-West, West, North-Wsest]
            for m in range(0,8):
                move_dir = int(m)
                # skip impossible moves starting with 4 corners then edges
                if((state_x==10)&(state_y==10)&(move_dir==0)):
                    continue
                elif((state_x==10)&(state_y==10)&(move_dir==2)):
                    continue
                    
                elif((state_x==10)&(state_y==-10)&(move_dir==2)):
                    continue
                elif((state_x==10)&(state_y==-10)&(move_dir==4)):
                    continue
                    
                elif((state_x==-10)&(state_y==-10)&(move_dir==4)):
                    continue
                elif((state_x==-10)&(state_y==-10)&(move_dir==6)):
                    continue
                    
                elif((state_x==-10)&(state_y==10)&(move_dir==6)):
                    continue
                elif((state_x==-10)&(state_y==10)&(move_dir==0)):
                    continue
                    
                elif((state_x==10) & (move_dir == 1)):
                    continue
                elif((state_x==10) & (move_dir == 2)):
                    continue
                elif((state_x==10) & (move_dir == 3)):
                    continue
                    
                elif((state_x==-10) & (move_dir == 5)):
                    continue
                elif((state_x==-10) & (move_dir == 6)):
                    continue
                elif((state_x==-10) & (move_dir == 7)):
                    continue
                    
                elif((state_y==10) & (move_dir == 1)):
                    continue
                elif((state_y==10) & (move_dir == 0)):
                    continue
                elif((state_y==10) & (move_dir == 7)):
                    continue
                    
                elif((state_y==-10) & (move_dir == 3)):
                    continue
                elif((state_y==-10) & (move_dir == 4)):
                    continue
                elif((state_y==-10) & (move_dir == 5)):
                    continue
                else:
                    reward = 0
                    Q = pd.DataFrame({'throw_dir':"none",'move_dir':move_dir,'state_x':state_x,'state_y':state_y, 'reward': reward}, index = [0])
                    Q_table = Q_table.append(Q)
    Q_table = Q_table.reset_index(drop=True)
    print("Q table 2 initialised")

    print(" ")
    print("Computing Probabilities")
    print("Total = ",len(Q_table))
    prob_list = pd.DataFrame()
    for n,action in tqdm(enumerate(Q_table['throw_dir'])):
        # Guarantee 100% probability if movement
        if(action == "none"):
            prob = 1
        # Calculate if thrown
        else:
            prob = probability(bin_x, bin_y, Q_table['state_x'][n], Q_table['state_y'][n], action)
        prob_list = prob_list.append(pd.DataFrame({'prob':prob}, index = [n] ))
    prob_list = prob_list.reset_index(drop=True)
    Q_table['prob'] = prob_list['prob']

    # For some reason some of the angles are being put as str instead of int, manual fix this
    t_d_l = []
    m_d_l = []
    for n,row in Q_table_init.iterrows():
        if row['throw_dir']=='none':
            t_d = 'none'
        else:
            t_d = int(row['throw_dir'])
        t_d_l.append(t_d)

        if row['move_dir']=='none':
            m_d = 'none'
        else:
            m_d = int(row['move_dir'])
        m_d_l.append(m_d)
    Q_table_init['throw_dir'] = t_d_l
    Q_table_init['move_dir'] = m_d_l

    Q_table.to_csv('./Q_table_init.csv')
    Q_table_init = Q_table
    
Q_table = Q_table_init.copy()

def action_request(state_x, state_y):
    Q_table_state = Q_table[(Q_table['state_x']==state_x)&(Q_table['state_y']==state_y)]
    throw_a_l = Q_table_state[Q_table_state['throw_dir']!='none']['throw_dir'].unique()
    move_a_l = Q_table_state[Q_table_state['move_dir']!='none']['move_dir'].unique()
    return(throw_a_l, move_a_l)


def environment(state_x, state_y, action_type, action_dir):

    if action_type == 'throw':
        Q_table_state_action = Q_table[(Q_table['state_x']==state_x)&(Q_table['state_y']==state_y)&(Q_table['throw_dir']==action_dir)]
        prob = Q_table_state_action['prob']
        # Reward depending on success of failure of throw
        rng_throw = np.random.rand()
        try: 
            if rng_throw <= prob:
                prob = prob
        except:
            prob = prob.iloc[0]
       
        if rng_throw <= prob:
            reward = 1
        else:
            reward = -1
        new_x = "none"
        new_y = "none"
    else:
        Q_table_state_action = Q_table[(Q_table['state_x']==state_x)&(Q_table['state_y']==state_y)&(Q_table['move_dir']==action_dir)]

        #Map this to actual direction and find next state position
        if(action_dir == 0):
            move_x = 0
            move_y = 1
        elif(action_dir == 1):
            move_x = 1
            move_y = 1
        elif(action_dir == 2):
            move_x = 1
            move_y = 0
        elif(action_dir == 3):
            move_x = 1
            move_y = -1
        elif(action_dir == 4):
            move_x = 0
            move_y = -1
        elif(action_dir == 5):
            move_x = -1
            move_y = -1
        elif(action_dir == 6):
            move_x = -1
            move_y = 0
        elif(action_dir == 7):
            move_x = -1
            move_y = 1

        new_x = state_x+move_x
        new_y = state_y+move_y
        reward = 0
    #print("[state_x state_y], [action_type action_dir], [new_x new_y], [reward]")
    #print("[",state_x, state_y,"],", "[",action_type, action_dir,"],", "[",new_x, new_y,"],", "[",reward,"]")

    return(state_x, state_y, action_type, action_dir, new_x, new_y, reward)
