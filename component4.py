from engine import GrammarEngine

def component4():
  engine = GrammarEngine(file_path="grammars/c4_grammar.txt")
  for _ in range(10):
    output = engine.generate(start_symbol_name="sentence")
    final_output = ""
    for i in range(len(output)):
      final_output+=output[i].capitalize()
    
    print(f"* {final_output}")
    print(" ")


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 4 -- ")
    component4()

grade()