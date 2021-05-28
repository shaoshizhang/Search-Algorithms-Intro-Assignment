# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
##### DFS definition

def get_node(name):
    node = {}
    node['name']=name
    node['children']=[]
    
    return node

def add_child(node, name):
    node['children'].append(get_node(name))
    

tree = get_node('root')
add_child(tree,'c1_d1')
add_child(tree,'c2_d1')
add_child(tree['children'][0],'c1_d2')
add_child(tree['children'][1],'c2_d2')


tree1 = get_node('root')
add_child(tree1,'c1_d1')
add_child(tree1,'c2_d1')
add_child(tree1,'c3_d1')
add_child(tree1,'c4_d1')
add_child(tree1['children'][0],'c1_1_d2')
add_child(tree1['children'][0],'c1_2_d2')
add_child(tree1['children'][0],'c1_3_d2')
add_child(tree1['children'][1],'c2_1_d2')
add_child(tree1['children'][1],'c2_2_d2')
add_child(tree1['children'][2],'c3_1_d2')
add_child(tree1['children'][2],'c3_2_d2')
add_child(tree1['children'][3],'c4_1_d2')
add_child(tree1['children'][3],'c4_2_d2')

#revise the for loop to define DFS
def DFS(init_state, goal_name):
    frontier = [init_state]
    explored = []
    
    while len(frontier):
        state = frontier.pop()
        explored.append(state['name'])
        
        print(explored)

        if state['name'] == goal_name:
            return True
        
        for child in state['children']:
            count = 0
            if child['name'] not in explored:
              frontier.append(child)
              count = count+1
        frontier = frontier[:len(frontier)-count+1]
        
                               
    return False

print(DFS(tree1,'c1_1_d2'))




#Refine the pop function to define DFS

def DFS(init_state, goal_name):

    frontier = [init_state]
    explored = []
    
    while len(frontier):
        state = frontier.pop(0)
        explored.append(state['name'])
        
        print(explored)

        if state['name'] == goal_name:
            return True
        
        for child in state['children']:
            if child['name'] not in explored:
                frontier.insert(0,child)
                
    return False

print(DFS(tree1,'c1_1_d2'))











###### Greedy Search 






# Node with heuristic
def get_node(name, heuristic=None):

    node = {}
    node['name'] = name
    node['children'] = []
    node['heuristic'] = heuristic
    node['path']=[]

    return node


def add_child(node, name, heuristic):
    child = get_node(name,heuristic)
    node['children'].append(child)
    child['path'].append(node['name'])
    child['path'].extend(node['path'])

    return node['children'][-1]


map =get_node('Kitchener',130)

# Children of Kitchener: Guelph, New Hamburg

add_child(map,'Guelph', 160)
add_child(map,'New Hamburg', 110)


# Children of New Hamburg: Startford 
add_child(map['children'][1], 'Stratford', 100)

# Children of Stratford: St. Marys, Drayton
add_child(map['children'][1]['children'][0], 'St. Marys', 130)
add_child(map['children'][1]['children'][0], 'Drayton', 100)

###children from route 2 
add_child(map['children'][1]['children'][0], 'St. Marys', 130)
add_child(map['children'][1]['children'][0], 'New Hamburg', 110)


# Children of St. Marys: Mitchell
add_child(map['children'][1]['children'][0]['children'][0], 'Mitchell', 100)

###children from route 2 
add_child(map['children'][1]['children'][0]['children'][0], 'Mitchell', 100)

# Children of Mitchell: Listowel
add_child(map['children'][1]['children'][0]['children'][0]['children'][0], 'Listowel' , 0)

###children from route 2 
add_child(map['children'][1]['children'][0]['children'][0]['children'][0], 'Listowel' , 0)



# Children of Drayton: Listowel, Guelph 
add_child(map['children'][1]['children'][0]['children'][1], 'Listowel', 0)

### children from route 2
add_child(map['children'][1]['children'][0]['children'][1], 'Listowel', 0)
add_child(map['children'][1]['children'][0]['children'][1], 'Stratford', 100)


 #########################################
 


# Children of Guelph: Drayton
add_child(map['children'][0], 'Drayton', 100) 

# Children of Drayton: Listowel, Stratford
add_child(map['children'][0]['children'][0], 'Listowel',0)
add_child(map['children'][0]['children'][0], 'Stratford', 100)

# Children of Stratford: New Hamburg, St. Marys
add_child(map['children'][0]['children'][0]['children'][1], 'New Hamburg',110)
add_child(map['children'][0]['children'][0]['children'][1],'St. Marys',130)

# Children of St. Marys: Mitchell
add_child(map['children'][0]['children'][0]['children'][1]['children'][1], 'Mitchell', 100)

# Children of Mitchell: Listowel
add_child(map['children'][0]['children'][0]['children'][1]['children'][1]['children'][0], 'Listowel',0)







def find_min_heuristic(frontier):
    min_h_i=0
    if len(frontier)>1:
        min_h = frontier[min_h_i]['heuristic']
        for i, state in enumerate(frontier):
            if state['heuristic']<min_h:
                min_h_i = i
                min_h = state['heuristic']
                
    return min_h_i


def GreedySearch(init_state,goal_name):
    frontier = [init_state]
    explored=[]
    
    
    while len(frontier):
        state = frontier.pop(find_min_heuristic(frontier))
        explored.append(state['name'])
        
        if state['name'] == goal_name:
            print(explored)
            return True
        for child in state['children']:
            if child['name'] not in explored:
                frontier.append(child)
    
    return False

print(GreedySearch(map, 'Listowel'))









