import inflect

def bid_adieu(names):
    p = inflect.engine()
    num_names = len(names)
    if num_names == 1:
        return f"Adieu, adieu, to {names[0]}"
    elif num_names == 2:
        return f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        farewell = ", ".join(names[:-1])
        farewell += f", and {names[-1]}"
        return f"Adieu, adieu, to {farewell}"

if __name__ == "__main__":
    print("Enter names (one per line). Press Ctrl+D (Ctrl+Z on Windows) when finished:")
    names = []
    while True:
        try:
            name = input()
            names.append(name)
        except EOFError:
            break
    
    farewell_message = bid_adieu(names)
    print(farewell_message)
