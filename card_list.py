import requests
import card_search

names = []
costs = [] 
types = []
colours = []
inkable = []
#body_texts = []
#flavor_texts = []
artists = []
raritys = []
img_urls = []
images = []
set_names = []
set_ids = []
set_num = []
date_added = []
#classes = []
#strengths = []
#willpowers = []
#lore_values = []

def create_card_list():
    cards = card_search.fetch_card_data()
    if cards:
        names = [None] * len(cards)
        costs = [None] * len(cards) 
        types = [None] * len(cards)
        colours = [None] * len(cards)
        inkable = [None] * len(cards)
        #body_texts = [None] * len(cards)
        #flavor_texts = [None] * len(cards)
        artists = [None] * len(cards)
        raritys = [None] * len(cards)
        img_urls = [None] * len(cards)
        images = [None] * len(cards)
        set_names = [None] * len(cards)
        set_ids = [None] * len(cards)
        set_num = [None] * len(cards)
        date_added = [None] * len(cards)
        #classes = [None] * len(cards)
        #strengths = [None] * len(cards)
        #willpowers = [None] * len(cards)
        #lore_values = [None] * len(cards)

        for i in range(len(cards)):
            names[i] = cards[i]['Name'] 
            costs[i] = cards[i]['Cost']
            types[i] = cards[i]['Type']
            colours[i] = cards[i]['Color']
            inkable[i] = cards[i]['Inkable']
            #body_texts[i] = cards[i]['Body_Text']
            #flavor_texts[i] = cards[i]['Flavor_Text']
            artists[i] = cards[i]['Artist']
            raritys[i] = cards[i]['Rarity']
            img_urls[i] = cards[i]['Image']
            images[i] = card_search.img_from_url(img_urls[i])
            set_names[i] = cards[i]['Set_Name']
            set_ids[i] = cards[i]['Set_ID']
            set_num[i] = cards[i]['Set_Num']
            date_added[i] = cards[i]['Date_Added']
            #classes[i] = cards[i]['Classifications']
            #strengths[i] = cards[i]['Strength']
            #willpowers[i] = cards[i]['Willpower']
            #lore_values[i] = cards[i]['Lore']
    else:
        print("Error: Lorcana API inaccessible")

    #return cards

def getImages():
    return images

  