#8-3
def make_shirt(size, text):
    print(f"The size of the shirt will be {size}.")
    print(f"The shirt text will be {text}.")

make_shirt("Medium", "LVC")
make_shirt("Large", "Lebanon Valley College")

#8-4
def make_shirt(size = "Large", text = "I love python"):
    print(f"The size of the shirt will be {size}.")
    print(f"The shirt text will be {text}.")

make_shirt()
make_shirt(size = "Medium")
make_shirt(size = "XL", text = "I do not love python")
