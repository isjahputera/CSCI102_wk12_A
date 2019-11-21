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
    with o_file as f:
        f_list = list(f)
    return r_file


# Function 3 - UpdateString

def UpdateSetting(string1, string2, num):
    new_string = string1[:num] + string2 + string1[num + 1:] #Saw this online/spoke with people
    print("OUTPUT", new_string)


# Function 4 - FindWordCount

def FindWordCount(f_file, fstring1):
    counts = f_file.count(fstring1)
    print("OUTPUT", counts)
    

# Function 5 - ScoreFinder

def ScoreFinder(players, scores, name):
    if name in players:
        for i in enumerate(name, start=0):
            n_score = scores.index[i]
        print("OUTPUT", name, "got a score of ", n_score)
    else:
        print("OUTPUT player not found")

# Function 6 - Union

def Union(list1, list2):
    list3 = list1 + list2
    print("OUTPUT", list3)

# Function 7 - Intersection

def Intersection(ilist1, ilist2):
    n_ilist = list(set(ilist1) & set(ilist2))
    print("OUTPUT", n_ilist)

# Function 8 - NotIn

def NotIn(nlist1, nlist2):
    n_nlist = set(nlist1).difference(nlist2)
    print("OUTPUT", n_nlist)
    
