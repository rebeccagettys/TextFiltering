from pattern.web import *
import urllib2
import pickle
import string
import seaborn as sns



def initial_color_dict_func():
    """Just the initial dictionary of colors so that we have something to start from. I used my brain, crayola crayon colors, + this link \
    (http://www.colourlovers.com/blog/2007/07/24/32-common-color-names-for-easy-reference) to come up with color names\
    and tried as much as possible avoid ones that could be misinterpretted (ex: plum the color vs plum the food). Because this
     function returns things in random order, I didn't write a docstring for it, but by calling it you should have all of the colors
      returned in the dictionary  = 0.

    """

    initial_color_dict = {'red': 0, 'orange': 0, 'yellow':0, 'green':0, 'blue':0, 'purple':0, 'brown':0, 'grey':0,
    'black':0, 'white':0, 'pink':0, 'ivory':0, 'tan':0, 'silver':0, 'gold':0, 'rose':0,'gray':0, 'olive':0, 'crimson':0, 'maroon':0,
    'fuchsia':0, 'teal':0, 'lavender':0, 'lilac':0, 'aqua':0, 'azure':0, 'beige':0, 'indigo':0, 'magenta':0, 'cyan':0, 'scarlet':0,
    'canary':0, 'periwinkle':0}
    return initial_color_dict #

def text_import():
    """Imports previously-pickled fairy tale data (in string format from disk and returns a list of the strings.
    Arguements: none
    Returns: list of pickle-imported strings"""
    # Load data for each from from a file (will be part of your data processing script)
    andersen_input_file = open('andersen_tales.pickle','r')
    andersen_tales = pickle.load(andersen_input_file)
    grimm_input_file = open('grimm_tales.pickle','r')
    grimm_tales = pickle.load(grimm_input_file)
    perrault_input_file = open('perrault_tales.pickle','r')
    perrault_tales = pickle.load(perrault_input_file)
    return [andersen_tales,perrault_tales, grimm_tales]


def color_searching(tale, initial_color_dict):
    """Searches the tale for a list of color words and counts the instances of these words up using a dictionary.
    Arguments: object (in this contex a list) to search, dictionary to search with
    Returns: dictionary containing keys and key-occurance frequencies (how many times the word showed up in the object)
    Due to the non-orderedness of dicionaries, hard to use a doctest"""
    for word in tale: #need to slice each tale into a list of words for this to work
        color_dict = initial_color_dict
        if word in color_dict:
            current_val = color_dict.get(word)
            val = current_val + 1
            color_dict[word] = val #made a dictionary of the string (color, frequnecy)
    return color_dict



def tale_searches(talelist):
    """Runs color_searching on each of the fairy tales and returns their dictionaries
    Arguments: list of tales (which are lists of strings (words))
    Returns: list of dictionaries, one for each tale (inside each dictionary, format is color-frequency)"""
    final_dict_list = [] #empty list
    for tale in talelist:
        tale_dict=color_searching(tale, initial_color_dict)
        final_dict_list.append(tale_dict)
    return final_dict_list

def tale_slicing(tale_list_text):
    """Slices the tales (strings) up into a list of words without spaces or punctuation and then puts each of those lists into another list.
     NOTE: https://mail.python.org/pipermail/tutor/2001-October/009454.html explains punctuation removal method that I used
    Arguments: list of strings (texts of the gutenberg tales)
    Returns: list of lists of words (a list containing lists whose items are the words of each tale)"""
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



def is_punct_char(char):
    """From python.org (link above), all this does is check if a character is puncutation or not! the ultimate helper funcion!
    Arguments: character
    Returns: True/False if the character it is given is a puncuation mark - 1 is punctuation, 0 is not """
    return char in string.punctuation #1 is punctuation, 0 is not punctuation


initial_color_dict = initial_color_dict_func()
text_lists = text_import() #this is a list of strings we need to make it a list of lists
#andersen, perrault, grimm is always the order
tale_lists = tale_slicing(text_lists)
output_dicts = tale_searches(tale_lists)


# Now just a ton of data processing
# just to make life easier, assign each dict inside output dict it's own variable
andersen_dict = output_dicts[0]
perrault_dict = output_dicts[1]
grimm_dict = output_dicts[2]
# dump dictionary to list of tuples
andersen_item_dump = andersen_dict.items()
perrault_item_dump = perrault_dict.items()
grimm_item_dump = grimm_dict.items()


def list_dumping (list):
    """This method I found on #http://stackoverflow.com/questions/7558908/unpacking-a-list-tuple-of-pairs-into-two-lists-tuples;
    just a convenient snippet of code which converts from the .items output to 2 lists in correct order
    Arguments: list (of two-item-tuples) that need to be seperated into lists
     Outputs: a list containing keys as items in one list, values as items in the other list, in the correct order"""
    color = []
    frequency = []
    for i in list:
        color.append(i[0])
        frequency.append(i[1])
    return [color, frequency]
# turn the lists of tuples into a list of 2 lists each
andersen_color_freq= list_dumping(andersen_item_dump)
perrault_color_freq = list_dumping(perrault_item_dump)
grimm_color_freq = list_dumping(grimm_item_dump) #


## patrick is amazing for helping with this!!

def graph_func(andersen, perrault, grimm):
    sns.set( font_scale=.8)
    sns.axlabel('Color', 'Frequency' )
    #colors from http://www.color-hex.com and wikipedia
    flatui = ["#521515", "#fffff0", "#4b0082","#ffd700", "#7fffd4", "#e6e6fa", "#ffff00",
              "#dc143c", "#ffc0cb", "#660000", "#808000", "#00ffff", "#d2b48c", "#c0c0c0",
              "#ff00ff", "#0000ff", "#808080", "#ffec8b","#ab82ff", "#ee4000", "#993299",
              "#ffaeb9", "#FF00FF", "#808080", '#f0ffff', "#008000", "#f5f5dc", "#008080",
              "#CCCCFF","#ffa500", "#000000", "#ffffff", "#ff0000"]
    custom_palette = sns.color_palette(flatui)
    colors = andersen[0]
    occurences = andersen[1]
    ax = sns.barplot(colors, occurences, palette = custom_palette)
    fig = ax.get_figure()
    for item in ax.get_xticklabels():
        item.set_rotation(45)
    sns.plt.title('Color Word Frequencies in Hans Christian Andersen Stories')
    fig.savefig('andersen_chart.png')
graph_func(andersen_color_freq,perrault_color_freq,grimm_color_freq)