"""Functions to parse a file containing villager data."""


# def all_species(filename):
#     #Emily - Driver
# #     all_species(filename) → set[str]
# # Take in the name of a data file (as a string) and return a set of unique species found in the file.
#     """Return a set of unique species in the given file.

#     Arguments:
#         - filename (str): the path to a data file

#     Return:
#         - set[str]: a set of strings
#     """
#     # species = set()

#     # for line in filename:
#     #     species = line[1].add(species)
    
#     # print(species)

#     unique_species = set()

#     data = open(filename)
#     for line in data:
#         species = line.rstrip().split("|")[1]
#         unique_species.add(species)
        
#     print(unique_species)
#     return unique_species

# all_species("villagers.csv")


# def get_villagers_by_species(filename, search_string="All"):
##NEEDS TO BE ALPHABETIZED
#     #Isma - driver
#     """Return a list of villagers' names by species.

#     Arguments:
#         - filename (str): the path to a data file
#         - search_string (str): optional, the name of a species

#     Return:
#         - list[str]: a list of names
#     """
#     information = open(filename)
#     villagers = []
    
#     for line in information:
#         villager = line.rstrip().split("|")[0]
#         villagers.append(villager)
        


#     print(villagers)
#     return sorted(villagers)

# get_villagers_by_species("villagers.csv")

# def all_names_by_hobby(filename):
#     #Emily - driver
#     #     all_names_by_hobby(filename) → list[list[str]]
#     # Return a list of villagers, but group their names by hobby. 
#     #To group names together, put them in the same list. 
#     #Since there are six possible hobbies (Fitness, Nature, Education, Music, Fashion, and Play), 
#         #your return value should be a list with six lists inside.

#     # Make sure the six lists appear in this order:

#     # 1 Fitness

#     # 2 Nature

#     # 3 Education

#     # 4 Music

#     # 5 Fashion

#     # 6 Play

#     # Like before, the names in each list should appear in alphabetical order.

#     """Return a list of lists containing villagers' names, grouped by hobby.

#     Arguments:
#         - filename (str): the path to a data file

#     Return:
#         - list[list[str]]: a list of lists containing names
#     """
#     data = open(filename)
#     #make a list of lists
#     fitness = []
#     nature = []
#     education = []
#     music = []
#     fashion = []
#     play = []
    
#     for line in data:
#         #name, _, _, hobby, _ = line.rstrip().split("|")
#         #we are creating variable names for each index of the lines
#         name, dont_care, dont_care_again, hobby, dont_care_yet_again = line.rstrip().split("|")

#         if hobby == "Fitness":
#             fitness.append(name)
        
#         elif hobby == "Nature":
#             nature.append(name)

#         elif hobby == "Education":
#             education.append(name)

#         elif hobby == "Music":
#             music.append(name)

#         elif hobby == "Fashion":
#             fashion.append(name)

#         elif hobby == "Play":
#             play.append(name)


#     print(sorted(fitness))
#     return [
#         sorted(fitness),
#         # sorted(nature),
#         # sorted(education),
#         # sorted(music),
#         # sorted(fashion),
#         # sorted(play),
#     ]

# all_names_by_hobby("villagers.csv")

def all_data(filename):
    #Isma - driver
#     all_data(filename) → list[tuple[str]]
# Return all the data in a file as a list of tuples.
    #new_tup = (,)

# Each line in the file is a tuple of (name, species, personality, hobby, motto)

    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    data = open(filename)
    all_data = []

    for line in data:
        #all_data.append(tuple(line.rstrip().split("|")))
        all_data.append(tuple(line.rstrip().split("|")))
        
    
    print(all_data)
    return all_data

all_data("villagers.csv")

def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code

# find_motto("villagers.csv")

def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """
# find_likeminded_villagers("villagers.csv")
    # TODO: replace this with your code
