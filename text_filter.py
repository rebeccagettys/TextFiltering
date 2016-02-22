from pattern.web import *
import pickle

def initial_color_dict_func():
    "Just the initial dictionary of colors so that we have something to start from. I used my brain, crayola crayon colors, + this link \
    (http://www.colourlovers.com/blog/2007/07/24/32-common-color-names-for-easy-reference) to come up with color names\
    and tried as much as possible avoid ones that could be misinterpretted (ex: plum the color vs plum the food)"
    initial_color_dict = {'red': 0, 'orange': 0, 'yellow':0, 'green':0, 'blue':0, 'purple':0, 'brown':0, 'grey':0,
    'black':0, 'white':0, 'pink':0, 'ivory':0, 'tan':0, 'silver':0, 'gold':0, 'rose':0,'gray':0, 'olive':0, 'crimson':0, 'maroon':0,
    'fushcia':0, 'teal':0, 'lavender':0, 'lilac':0, 'aqua':0, 'azure':0, 'beige':0, 'indigo':0, 'magenta':0, 'cyan':0, 'scarlet':0,
    'canary':0, 'periwinkle':0, 'pale':0, 'dark':0}
    return initial_color_dict

def text_import():
    "Imports pickled fairy tale data from disk."
    # Load data from a file (will be part of your data processing script)
    andersen_input_file = open('andersen_tales','r')
    andersen_tales = pickle.load(andersen_input_file)
    #grimm_input_file = open('grimm_tales','r') #todo: add this back in later
    #grimm_tales = pickle.load(grimm_input_file) #todo: add this back in later
    perrault_input_file = open('perrault_tales','r')
    perrault_tales = pickle.load(perrault_input_file)
    return (andersen_tales ,perrault_tales) #todo: add grimm_tales

def color_searching(tale):
    "Searches the tale for a list of color words and counts the instances of these words up using a dictionary."
    color_dict = dict()
    color_dict = dict()
    for word in tale: #need to slice each tale into a list of words for this to work
        if word in color_dict:
            current_val = color_dict.get(word,0)
            val = current_val + 1
            color_dict[word] = val #made a dictionary of the string (color, frequnecy)
            return color_dict


def tale_searches(*taletuple):
    "Runs color_searching on each of the fairy tales and returns their dictionaries"
    final_dict_list = [] #empty list
    for tale in taletuple:
        tale_dict=color_searching(tale)
        final_dict_list.extend(tale_dict) #TODO:add grimm later, check if this needs to be 'append' or 'extend' - we want this to be a list of dictionaries
    return final_dict_list

def tale_slicing(*taletuple): #TODO: make sure that this runs on the tales BEFORE tale_searches/color_searching and add grimm tales back in
    "Slices the tales up into a list of words without spaces"
    for tale in taletuple:
        continue #todo: figure out how the data in each tale comes in from pickle so that you can appropriately process it


initial_color_dict_func()
text_import()
tale_slicing (andersen_tales, perrault_tales)
output_dicts = tale_searches(andersen_tales,perrault_tales) #todo: add grim tales later