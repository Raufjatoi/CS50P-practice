import emoji

def emojize(p):
    if '_' in p or ':' in p:
        return emoji.emojize(p)
    else:
        return emoji.emojize(p, use_aliases=True)

def main():
    emoji_input = input('Input: ')
    emojized = emojize(emoji_input)
    print(emojized)

if __name__ == "__main__":
    main()
