import os, profile, re
import mediator, sr_interface, vc_globals


def dictate_pseudo_python():

    #
    # These words must be in the SR vocab, otherwise some of the say()
    # statements will faile
    #

    sr_interface.addWord(sr_interface.vocabulary_entry('aliases', 'aliases'))
    sr_interface.addWord(sr_interface.vocabulary_entry('globals', 'globals'))

    mediator.open_file('D:/blah.py')
        
    mediator.say(['import', 'modules', 'O.', 'S.', ', \\comma', 'R.', 'E.', ', \\comma', 'string', ', \\comma', 'system', 'new', 'statement'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['import', 'modules', 'auto', 'test', ', \\comma', 'natural', 'link', ', \\comma', 'V.', 'C.', 'globals', 'new', 'statement'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)

   
    mediator.say(['from', 'module', 'actions', 'C.', 'C.', 'P.', 'P.', ' import all\\import all', 'new', 'statement'] , user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['from', 'module', 'application', 'state', 'import', 'symbols', 'application', 'state', 'new', 'statement'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['from', 'module', 'context', 'generic', 'import', 'symbols', 'context', 'C.', 'comma', 'context', 'python', 'new', 'statement'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['from', 'module', 'context', 'sensitive', 'command', 'import', 'symbols', 'context', 'sensitive', 'command', 'new', 'statement'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['from', 'module', 'Ed', 'simulator', 'import', 'symbol', 'Ed', 'simulator', 'new', 'statement'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['from', 'module', 'object', 'import', 'symbol', 'object', 'new', 'statement'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['import', 'modules', 'Ed', 'simulator', 'comma', 'symbol', 'dictionary', 'new', 'statement'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['import', 'module',  'S.', 'R.', 'interface',  'new', 'statement'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['define', 'class', 'command', 'interpreter', 'sub class\\sub class', 'of', 'object', 'class', 'body'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['define', 'method', 'initialize', 'add', 'argument', 'on', 'application', 'equals', 'none', 'comma'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['symbol', 'dictionary', 'pickle', 'file', 'equals', 'none', 'comma', 'double', 'asterisk', 'attributes', 'method', 'body'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['self', 'dot', 'declare', 'attributes', 'with', 'arguments', 'brace', 'pair'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['single', 'quotes', 'un', 'translated', 'text', 'start', 'jump', 'out', ':\\colon', 'none', 'comma'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['single', 'quotes', 'un', 'translated', 'text', 'end', 'jump', 'out', ':\\colon', 'none', 'new', 'statement'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['self', 'dot', 'deep', 'construct', 'with', 'arguments', 'command', 'interpreter', 'comma', 'continue', 'statement'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['brace', 'pair', 'single', 'quotes', 'on', 'application', 'jump', 'out', ':\\colon', 'on', 'application', 'comma',], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['single', 'quotes', 'known', 'symbols', 'jump', 'out', ':\\colon', 'symbol', 'dictionary', 'dot', 'symbol', 'dictionary', 'without', 'arguments', 'comma', 'continue', 'statement'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    
    mediator.say(['single', 'quotes', 'language', 'specific', 'aliases', 'jump', 'out', ':\\colon', 'empty', 'dictionary', 'comma', 'continue', 'statement'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['single', 'quotes', 'last', 'loaded', 'language', 'jump', 'out', ':\\colon', 'none', 'comma', 'continue', 'statement'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['single', 'quotes', 'symbol', 'dictionary', 'pickle', 'file', 'jump', 'out', ':\\colon', 'symbol', 'dictionary', 'pickle', 'file', 'jump', 'out', 'comma', 'continue', 'statement'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['attributes', 'new', 'statement', 'new', 'statement'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    
    mediator.say(['define', 'method', 'spoken', 'form', 'regular', 'expression', 'add', 'argument', 'spoken', 'form', 'method', 'body'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['words', 'equals', 'R.', 'E.', 'dot', 'split', 'with', 'arguments'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['single', 'quotes',  'back', 'slash', 'S.', 'plus', 'sign', 'jump', 'out', 'comma', 'spoken', 'form', 'new', 'statement'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['regular', 'expression', 'equals', 'empty', 'single', 'quotes', 'new', 'statement'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['for', 'loop', 'a', 'word', 'in', 'list', 'words', 'loop', 'body'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['first', 'equals', 'a', 'word', 'at', 'index', '0', 'new', 'statement'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['rest', 'equals', 'a', 'word', 'at', 'index', '1', ':\\colon', 'new', 'statement'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['regular', 'expression', 'this', 'word', 'equals', 'single', 'quotes'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['open', 'bracket', 'jump', 'out', 'plus', 'string', 'dot', 'lower', 'with', 'arguments', 'first'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['jump', 'out', 'plus', 'string', 'dot', 'upper', 'with', 'arguments', 'first', 'new', 'statement'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['if', 'statement', 'not', 'regular', 'expression', 'equal', 'to', 'empty', 'single', 'quotes', 'if', 'body'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['regular', 'expression', 'equals', 'regular', 'expression', 'plus', 'single', 'quotes', 'back', 'slash', 'S.', 'asterisk', 'new', 'statement'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['regular', 'expression', 'equals', 'regular', 'expression', 'plus', 'regular', 'expression', 'this', 'word', 'new', 'statement'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.say(['return', 'regular', 'expression'], user_input='1\n1\n1\n1\n1\n1\n1\n', echo_utterance=1)
    
    mediator.quit(save_speech_files=0, disconnect=0)


def run():

    #
    # This file contains the native code that we will dictate
    #
    native_py_file = vc_globals.test_data + os.sep + 'native_python.py'
    native_py_file = re.sub('\\\\', '\\\\\\\\', native_py_file)

    #
    # Dictate some pseudo python where all symbols are already known
    #
    print '>>> Dictating Python when all symbols are known <<<\n'
    mediator.init_simulator()
    mediator.compile_symbols([native_py_file])
    mediator.print_symbols()
    dictate_pseudo_python()

    #
    # Dictate some pseudo python where only standard symbols are already known
    #
    print '\n>>> Dictating Python when only standard symbols are known <<<\n'    
    mediator.init_simulator()
    mediator.print_symbols()
    dictate_pseudo_python()    
    