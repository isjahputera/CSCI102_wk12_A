# https://github.com/isjahputera/CSCI102_wk12_A.git
# Indiana Sjahputera
# CSCI 102 - Section E
# Week 11 - Part B
# The GITHUB REPO

# Function 1 - PrintOutput from previous lab 

def PrintOutput(string):
    print('OUTPUT', string)


# Function 2 - LoadFile 

def LoadFile(file):
    o_file = open(file, "r")
    e_list = []
    with o_file as f:
        f_list = f.readlines()
        for line in f_list:
            e_list.append(line.strip())
    return e_list


# Function 3 - UpdateString 

def UpdateSetting(string1, string2, num):
    new_string = string1[:num] + string2 + string1[num + 1:] #Saw this online/spoke with people
    print("OUTPUT", new_string)


# Function 4 - FindWordCount 

def FindWordCount(f_file, fstring1):
    n_list = []
    counts = 0
    for i in f_file:
        n_list = i.split()
        counts += n_list.count(fstring1)
    return counts
    

# Function 5 - ScoreFinder 

def ScoreFinder(players, scores, name):
    c_name = name.capitalize()
    if c_name in players:
        n_score = players.index(c_name)
        p1 = print("OUTPUT", name, "got a score of ", scores[n_score])
        return p1
    else:
        p2 = print("OUTPUT player not found")
        return p2


# Function 6 - Union 

def Union(list1, list2):
    list3 = list1 + list2
    return list3


# Function 7 - Intersection 

def Intersection(ilist1, ilist2):
    n_ilist = list(set(ilist1) & set(ilist2))
    return n_ilist

# Function 8 - NotIn

def NotIn(nlist1, nlist2):
    n_nlist = set(nlist1).difference(nlist2)
    return n_nlist
    
