from engine import GrammarEngine

def component5():
  engine = GrammarEngine(file_path="grammars/c5_grammar.txt")
  for _ in range(3):
    print(engine.generate(start_symbol_name="GAME"))
    print(" ")


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 5 -- ")
    component5()
