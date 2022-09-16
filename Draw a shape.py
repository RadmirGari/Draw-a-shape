
print("  *       *   ")
print("              ")
print(" **       **  ")
print("  **     **   ")
print("   ******     ")

name = input("Hello! What is your name? My name is Bob :).: ")
##this is an easter egg in the code.
if name == 'Joe':
    yes = input("Who's Joe? ").lower()
    if yes == "joe mama":
        print("I hate you.")
##also an easter egg.
elif name == "Memphis":
    yes = 1
    while yes < 2:
        print("I hate you.")
##Below this comment is where the actual draw me a shape code starts.
else:
    print("Hello " + name + "!")
    shape = input("What shape do you want me to draw?: ").lower()
    if shape == "triangle":
        print("    *   ")
        print("   * *  ")
        print("  *   * ")
        print(" *******")
        yes = input("Did you like my triangle Yes or No?: ").lower()
        if yes == "no":
            print("You are very mean you make Bob sad.")
            print("  *       *   ")
            print("              ")
            print("    ******    ")
            print("  **     **   ")
            print(" *         *  ")
        else:
            print("You are very kind :) You make Bob happy.")
            
            print("  *       *   ")
            print("              ")
            print(" **       **  ")
            print("  **     **   ")
            print("   ******     ")
    if shape == "square":
        print(" ****** ")
        print(" *    * ")
        print(" *    * ")
        print(" ****** ")
        yes = input("Did you like my square Yes or No?: ").lower()
        if yes == "yes":
            print("You make Bob very happy. Bob likes to draw squares")
            print("  *       *   ")
            print("              ")
            print(" **       **  ")
            print("  **     **   ")
            print("   ******     ")
        else:
            print("You make Bob very unhappy. Bob likes to draw squares he thinks he is good at them")
            print("  *       *   ")
            print("              ")
            print("    ******    ")
            print("  **     **   ")
            print(" *         *  ")
    if shape == "circle":
        print("     *     ")
        print("   ** **   ")
        print("  *     *  ")
        print("   ** **   ")
        print("     *     ")
        yes = input("At least I tried. Did you like my circle Yes or No?: ").lower()
        if yes == "no":
            print("I know :( I can't draw circles")
        else:
            print("Why are you lying to me? You make Bob sad.")
            print("  *       *   ")
            print("              ")
            print("    ******    ")
            print("  **     **   ")
            print(" *         *  ")

