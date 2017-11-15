# Introduction

If JARVIS had a trial version this would be it. 

Meet Olympia. She's an open-source, modular personal assistant. While Olympia boasts many built-in features, anyone can easily add their own features in, quite effortlessly.


# Installation

### Note: this has only been tested on Windows

1. Download the repository as a zip file

2. Navigate to the Olympia-master file in cmd/Terminal

3. run: pip install -r requirements.txt

4. run: python setup.py

5. Navigate to the Olympia-master/code file

6. run: python main.py

7. Enjoy!

## Features

### Currently, the personal assistant can do the following:

-Tell you the weather  

-Answer a question (e.g "What is a tree?" , or "what is astronomy")

-Answer any general-knowledge question (e.g "How far away is the Sun from the Earth?", or "Who is the CEO of Github?")

-Define, spell and find synonyms of a word

-Give you the news

-Tell you a joke

-Stream some music

-Answering math questions - what's 2+2, factorials, square roots, you get the idea.

-Reminders, alarms, to-do lists, etc.

-Showing you a random XKCD

### Things I'm currently working on:

-World domination

-Fixing bugs

-Having a basic conversational skills ("How are you?", "Have a nice day", etc.)

-Allowing you to translate a word from English to any other language


### Things I'm thinking on working on:

-RNatural Language Processing instead of looking for 'activation words'

-Using twilio to send text alerts

-Integrating it with Philips Smart Lights to turn lights on and off

-Sports news

-Making Olympia able to communicate and comprehend multiple languages.

## Modularity

To add a new module, it's just a matter of adding 3-4 lines of code in determiner.py file, which will help Olympia determine if your module is being activated, and coding the actual module itself - the module must take the form of a function that takes in inputs from the calling program (e.g what the user said) and returns what Olympia should "say" in return.

In retrospect, Olympia has a structure which is very similar to that used in neural networks - there's the input layer, where the user says a command, there's the hidden layer, where Olympia scrapes the web to meet the users demand, and finally, there's the ouptut layer - where Olympia meets the users request.

For example, imagine you were to implement a news module. You would write an IF statement checking if the user said something along the lines of "news" or "headlines", and if he did, execute some code.


## Quick-start guide

After spending about an hour ironing out errors with libraries, you should finally be able to run Olympia. To activate Olympia, simply say "Olympia". Wait for the single beep, and then speak your command. When you hear a double-beep, that means Olympia is processing what you just said.

## Commands

"Play (song name)"

"Give me the headlines"

"Give me the news from the (BBC/Washington Post/Fox News/CNN/Huffington Post)"

"What's the weather like tomorrow?"

"What's the weather like today?"

"What's the weather like in x days" (note: x cannot be larger than 10)

"Tell me a joke"

"What is (thing)"...."Tell me more about (thing)"

"Define (word)"

"What's the synonym of (word)?"

"Spell (word)"

"Can I ask you a question?" .... (question)

"Show me an xkcd"

"What's (maths question)"

"Set a reminder for the (date)"

"Set an alarm for (time in P.M./A.M.) on the (date)"

"Set a timer for 30 minutes"
