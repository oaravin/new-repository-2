import argparse

def generate_greeting(name):
  """Generates a greeting for the given name."""
  return f"Hello, {name}!"

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="A medium complexity 'Hello, World!' program.")
  parser.add_argument("--name", default="World", help="The name to greet.")
  args = parser.parse_args()
  greeting = generate_greeting(args.name)
  print(greeting)
