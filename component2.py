from engine import GrammarEngine

def component2a():
    engine = GrammarEngine(file_path="grammars/c2_grammar.txt")
    
    for i in range(3):
      output = engine.generate(start_symbol_name="LYRIC", debug=False) 
      print(f"{i} {output}\n")


def component2b():
    engine = GrammarEngine(file_path="grammars/c2_grammar.txt")
    
    for i in range(3):
      output = engine.generate(start_symbol_name="INDIRECT_REFERENCE", debug=False) 
      print(f"{i} {output}\n")


def component2c():
    engine = GrammarEngine(file_path="grammars/c2_grammar.txt")
    
    for i in range(3):
      output1 = engine.generate(start_symbol_name="ACT1", debug=False)
      output2 = engine.generate(start_symbol_name="ACT2",debug=False)
      print(f"{i} {output1}\n{output2}")
      print(" ")


def component2d():
    initial_state = {"name":"Yemi Shin","ID":"1998419","dorm":"Watson"}

    engine = GrammarEngine(file_path="grammars/c2_grammar.txt",initial_state=initial_state)
    
    for i in range(1):
      output = engine.generate(start_symbol_name="INTRO", debug=False) 
      print(f"{output}\n")

def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 2a -- ")
    component2a()
    print("\n\n-- Component 2b -- ")
    component2b()
    print("\n\n-- Component 2c -- ")
    component2c()
    print("\n\n-- Component 2d -- ")
    component2d()
