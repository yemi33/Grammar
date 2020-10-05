from engine import GrammarEngine

def component6():
  engine = GrammarEngine(file_path="grammars/c6_grammar.txt")
  print(engine.generate(start_symbol_name="INTRO"))
  print(" ")
  output = engine.generate(start_symbol_name="SCREENPLAY")
  output_list = output.split('\\n')
  for j in range (len(output_list)):
    print(f"{output_list[j]}")

def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 6 -- ")
    component6()

