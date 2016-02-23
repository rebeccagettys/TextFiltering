from pattern.web import *
import urllib2
import pickle
import string
import pygal
from IPython.display import SVG


def initial_color_dict_func():
    "Just the initial dictionary of colors so that we have something to start from. I used my brain, crayola crayon colors, + this link \
    (http://www.colourlovers.com/blog/2007/07/24/32-common-color-names-for-easy-reference) to come up with color names\
    and tried as much as possible avoid ones that could be misinterpretted (ex: plum the color vs plum the food)"
    initial_color_dict = {'red': 0, 'orange': 0, 'yellow':0, 'green':0, 'blue':0, 'purple':0, 'brown':0, 'grey':0,
    'black':0, 'white':0, 'pink':0, 'ivory':0, 'tan':0, 'silver':0, 'gold':0, 'rose':0,'gray':0, 'olive':0, 'crimson':0, 'maroon':0,
    'fushcia':0, 'teal':0, 'lavender':0, 'lilac':0, 'aqua':0, 'azure':0, 'beige':0, 'indigo':0, 'magenta':0, 'cyan':0, 'scarlet':0,
    'canary':0, 'periwinkle':0}
    return initial_color_dict #

def text_import():
    "Imports pickled fairy tale data from disk."
    # Load data from a file (will be part of your data processing script)
    andersen_input_file = open('andersen_tales.pickle','r')
    andersen_tales = pickle.load(andersen_input_file)
    grimm_input_file = open('grimm_tales.pickle','r')
    grimm_tales = pickle.load(grimm_input_file)
    perrault_input_file = open('perrault_tales.pickle','r')
    perrault_tales = pickle.load(perrault_input_file)
    return [andersen_tales,perrault_tales, grimm_tales]


def color_searching(tale, initial_color_dict):
    "Searches the tale for a list of color words and counts the instances of these words up using a dictionary."
    for word in tale: #need to slice each tale into a list of words for this to work
        color_dict = initial_color_dict
        if word in color_dict:
            current_val = color_dict.get(word)
            val = current_val + 1
            color_dict[word] = val #made a dictionary of the string (color, frequnecy)
    return color_dict



def tale_searches(talelist, initial_color_dict):
    "Runs color_searching on each of the fairy tales and returns their dictionaries"
    final_dict_list = [] #empty list
    for tale in talelist:
        tale_dict=color_searching(tale, initial_color_dict)
        final_dict_list.append(tale_dict)
    return final_dict_list

def tale_slicing(tale_list_text):
    "Slices the tales up into a list of words without spaces # https://mail.python.org/pipermail/tutor/2001-October/009454.html explains punctuation removal "
   #print len(tale_list_text)
    tale_lists = []
    for tale in tale_list_text:
        #print tale[0:100] #so both tales are coming in correctly so it is only going through index 1's input, ignoring index 0's
        tale_no_punc = ''
        for char in tale: #killing punctuation
            if not is_punct_char(char):
                tale_no_punc = tale_no_punc+char #so extend the string everytime we run into a letter
        list_of_words = []
        list_of_words = tale_no_punc.split() #splitting the string into the list
        #print list_of_words[0:100]
        tale_lists.append(list_of_words)
    return tale_lists

#def tale_slices(tale_text): make sure that this runs on the tales BEFORE tale_searches/color_searching and add grimm tales back in
#    "Slices the inputted tale up into a list of words without spaces # https://mail.python.org/pipermail/tutor/2001-October/009454.html explains punctuation removal "
#        tale_no_punc = ''
#        for char in tale: #killing punctuation
#            if not is_punct_char(char):
#                tale_no_punc = tale_no_punc+char #so extend the string everytime we run into a letter
#        list_of_words = []
#        list_of_words = tale_no_punc.split() #splitting the string into the list
#        print list_of_words[0:100]
#    return list_of_words

#def tale_slicing(tale_list_text):
#    tale_lists = []
#    for tale in tale_list_text:
 #       word_list = tale_slices(tale_text)


def is_punct_char(char):
    "From python.org (link above), all this does is check if a character is puncutation or not! the ultimate helper funcion!"
    return char in string.punctuation #1 is punctuation, 0 is not punctuation


initial_color_dict = initial_color_dict_func()
text_lists = text_import() #this is a list of strings we need to make it a list of lists
#andersen_tales_text = text_lists[0]
#perrault_tales_text = text_lists[1]
#grimm_tales_text = text_lists[2]
tale_lists = tale_slicing(text_lists)
#tale_lists= tale_slices (text_lists) #IGNORE
output_dicts = tale_searches(tale_lists, initial_color_dict)


# Now just a crap ton of data processing
andersen_dict = output_dicts[0]
perrault_dict = output_dicts[1]
grimm_dict = output_dicts[2]
andersen_item_dump = andersen_dict.items()
perrault_item_dump = perrault_dict.items()
grimm_item_dump = grimm_dict.items()


def list_dumping (list):
    color = []
    frequency = []
    for i in list:
        color.append(i[0])
        frequency.append(i[1])
    return [color, frequency]

andersen_color_freq= list_dumping(andersen_item_dump)
perrault_color_freq = list_dumping(perrault_item_dump)
grimm_color_freq = list_dumping(grimm_item_dump) #

def graphing_data_viz (output_dicts):
    andersen_bar_graph = pygal.Bar()
    andersen_bar_graph.title = 'Color Mention Frequency in Has Christian Andersen Stories'
    andersen_bar_graph.x_labels = 'Color'
    andersen_bar_graph.add = andersen_color_freq[1]
    andersen_bar_graph.render_to_file('andersen_chart.svg')
    #perrault_bar_graph
    #grimm_bar_graph
    #overall_bar_graph (add them all up or graph them all together)