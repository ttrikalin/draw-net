import os

def read_data(filename):
    """Reads a file name into python"""
    infile = open(filename, "r") 
    study_index = {}
    study_list = []
    n_studies = 0
    # parse line by line 
    for line in infile:
        l= line.strip().split("\t")
        if (study_index.has_key(l[0])== False):
            study_index[l[0]] = n_studies
            study_list.append(study(l[0]))
            an_arm = arm(l[1:])
            study_list[n_studies].add_arm(an_arm)
            n_studies += 1  # augment if there's a new study
        else:
            an_arm = arm(l[1:])
            study_list[study_index[l[0]]].add_arm(an_arm)
    infile.close()
    return (study_index, study_list) 



def study_graph_str(study, level, allow_circular_edges):
    """Take a study and spitout its contribution to the 
    graph based on the level of the nodes names """
    if study.n_levels()[0]>=level: 
        n_arms =  study.n_arms()
        mystring = ''
        for arm1 in range(n_arms):
            for arm2 in range(arm1+1, n_arms, 1):
                name1 = study.arms[arm1].name[level]
                name2 = study.arms[arm2].name[level]
                if ((allow_circular_edges==False) & (name1==name2)):
                    mystring = mystring + '\t"' + name1 + '"\n'
                else:
                    mystring = mystring + '\t"'+ name1 + '" -- "' + name2 + '"\n'

        return mystring

    else:
        print "There are not so many levels in arm ", study.arm_ids[0] , "of study ", study.name
        return None 


def make_the_graph(filename, study_list, level, allow_circular_edges):
    """Takes a list of studies and a filename to overwrite and spits out a graph"""
    outfile = open(filename, "w")
    outfile.write("Graph {")
    for study in study_list:
        outfile.write(study_graph_str(study, level, allow_circular_edges))

    outfile.write("}")
    outfile.close()
    
    print "File ", filename, " contains the GraphViz data!"
    return 


