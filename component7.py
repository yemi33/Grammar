from engine import GrammarEngine

def component7():
    engine = GrammarEngine(file_path="grammars/c6_grammar.txt")
    print(engine.generate(start_symbol_name="INTRO"))
    print(" ")
    output = engine.generate(start_symbol_name="SCREENPLAY")
    output_list = output.split('\\n')
    for j in range (len(output_list)):
      print(f"{output_list[j]}")
    
    state = engine.export_state()

    engine2 = GrammarEngine(file_path="grammars/c7_grammar.txt",initial_state=state)
    output3 = engine2.generate(start_symbol_name="SYNOPSIS")
    print("_________SYNOPSIS_________\n")
    print(output3)
    print(" ")


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 7 -- ")
    component7()

grade()