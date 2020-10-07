from engine import GrammarEngine

def component1a():
    engine = GrammarEngine(file_path="grammars/c1_grammar.txt")
  
    for i in range(5):
      output = engine.generate(start_symbol_name="NO_CORPUS", debug=False) 
      output = output.capitalize()
      print(f"{i} {output}")


def component1b():
    engine = GrammarEngine(file_path="grammars/c1_grammar.txt")
    
    for i in range(5):
      output = engine.generate(start_symbol_name="YES_CORPUS", debug=False) 
      output = output.capitalize()
      print(f"{i} {output}")


def component1c():
    engine = GrammarEngine(file_path="grammars/c1_grammar.txt")
    
    for i in range(5):
      output = engine.generate(start_symbol_name="MY_CORPUS", debug=False)
      output = output.capitalize() 
      print(f"{i} {output}\n")


def component1d():
    engine = GrammarEngine(file_path="grammars/c1_grammar.txt")
    
    for i in range(3):
      output = engine.generate(start_symbol_name="PARAGRAPH", debug=False)
      
      print(f"{i} {output}\n")


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 1a -- ")
    component1a()
    print("\n\n-- Component 1b -- ")
    component1b()
    print("\n\n-- Component 1c -- ")
    component1c()
    print("\n\n-- Component 1d -- ")
    component1d()

