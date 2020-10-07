from engine import GrammarEngine

def supplementary_challenge2():
  engine = GrammarEngine(file_path="grammars/ch2_grammar.txt")
  for _ in range(10):
    output = engine.generate(start_symbol_name="sentence",debug=True)
    final_output = ""
    for i in range(len(output)):
      final_output+=output[i].capitalize()
    
    print(f"* {final_output}")
    print(" ")

def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Supplementary Challenge 2 -- ")
    supplementary_challenge2()

grade()