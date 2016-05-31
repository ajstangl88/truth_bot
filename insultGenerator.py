import random
class insultMe:


    def constructInstult(self):

        cussing = [
            'Ass',
            'Bitch',
            'Butt',
            'Cock',
            'Cum',
            'Cunt',
            'Dick',
            'Douche',
            'Fart',
            'Fuck',
            'Jizz',
            'Schlong',
            'Shit',
            'Slut',
            'Snatch',
            'Tit',
            'Twat',
            'Wang',
            'Wank',
            'Whore',
        ]

        noun = [
            'Bagel',
            'Biscuit',
            'Blister',
            'Burger',
            'Bubble',
            'Bucket',
            'Camel',
            'Canoe',
            'Cocktail',
            'Cracker',
            'Cranker',
            'Dragon',
            'Dumpster',
            'Farmer',
            'Fister',
            'Guzzler',
            'Hatchet',
            'Monkey',
            'Muffin',
            'Muncher',
            'Nozzle',
            'Nugget',
            'Panda',
            'Pilot',
            'Pistol',
            'Pusher',
            'Sandwich',
            'Scratcher',
            'Scrubber',
            'Shitter',
            'Sucker',
            'Taco',
            'Twiddler',
            'Waffle',
            'Wanker',
            'Whistle',
        ]

        fuckingDescription = [
            "That verb noun just cut me off!",
            "My boss is a major verb noun!",
            "Don't tell her I said this, but that dude she's with is a real verb noun!",
            "Quit being such a verb noun!",
            "The only people who would vote for that guy are total verb nouns!",
            "What are you, some kind of verb noun?",
            "Dude's a real verb noun, you know what I mean?",
            "He's got an ego like a verb noun!",
            "She was being a real verb noun at the store today!",
            "That verb noun developer's code refuses to compile!",
            "Her kids are total verb nouns!",
            "Whoever wrote this API documentation is a complete verb noun!",
            "That guy has the personality of a verb noun!",
            "I'm pretty sure I was a total verb noun at the bar last night.",
            "What kind of verb noun buys pre-ground coffee?",
            "I'd rather get a verb noun to the eye than sit through this lecture.",
            "Wow, that verb noun just went off the deep end.",
            "I may be a jerk, but at least I'm not like that verb noun over there.",
            "I need that like I need a verb noun on my elbow.",
            "What kind of verb noun slows down to merge on the highway?",
            "You've got a face like a verb noun.",
            "Nothing personal, but you're a real verb noun.",
            "What a bunch of verb nouns.",
            "That verb noun is legally dead in 27 states - plus Guam.",
        ]
        noun = random.choice(noun)
        cuss = random.choice(cussing)
        sentence = random.choice(fuckingDescription)

        sentence = sentence.replace("noun", noun)
        sentence = sentence.replace("verb", cuss)
        return sentence

test = insultMe()
insult = test.constructInstult()
print insult