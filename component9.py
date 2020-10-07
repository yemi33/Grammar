from engine import GrammarEngine

def component9():
  engine = GrammarEngine(file_path="grammars/c9_grammar.txt")
  for _ in range(3):
    print(engine.generate(start_symbol_name="sentence"))
    print(" ")


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 9 -- ")
    component9()


