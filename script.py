from pydash.utilities import random
from lib.core.utils.get_verbs import get_verbs
from lib.core.utils.parse_arguments import get_arguments
from pydash.collections import includes
from termcolor import colored
from pydash.strings import capitalize, upper_case, join
from pydash.predicates import is_list

available_actions = [
    {
        "kind": "irregular",
        "tense": "infinitive",
        "ask": "infinitive",
        "options": ["past_simple", "past_participle"]
    },
    {
        "kind": "irregular",
        "tense": "past_simple",
        "ask": "past simple",
        "options": ["infinitive", "past_participle"]
    },
    {
        "kind": "irregular",
        "tense": "past_participle",
        "ask": "part participle",
        "options": ["past_simple", "infinitive"]
    
    },
]

def main():
    args = get_arguments()
    verbs = get_verbs()
    while True:
        # select a random action
        action = available_actions[random(0, len(available_actions) - 1)]
        
        # select a random verb
        verb = verbs['all'][random(0, len(verbs['all']) - 1)]
        
        # select a random tense of available options
        option = verb[action['options'][random(0, len(action['options']) - 1)]]
        if is_list(option): option = join(option, '/')
        beautiful_option = colored(capitalize(option), 'red', attrs=['reverse', 'blink', 'bold'])
        
        beautiful_ask = colored(capitalize(action['ask']), 'red', attrs=['blink', 'bold'])
        
        description = ''
        if hasattr(verb, 'description'): description = ' (%s)' % verb['description']
        
        # ask user for input
        question = '\nWhat is the %s of %s?%s: ' % (beautiful_ask, beautiful_option, description, )
        
        available_answers = verb[action['tense']]
        
        if not is_list(available_answers):
            available_answers = [available_answers]
        
        while True:
            print(question)
            answer = input().strip()
           
            if not includes(available_answers, answer):
                print(colored(upper_case('INCORRECT!!'), 'red', attrs=['reverse', 'blink', 'bold']))
            else:
                print(colored(upper_case('CORRECT!!'), 'green', attrs=['reverse', 'blink', 'bold']))
                break
            
        
        # stop if once if it's set
        if includes(args, 'once'):
            break

if __name__ == '__main__':
    main()