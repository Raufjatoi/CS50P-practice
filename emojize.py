import emoji

def replace_emoji(text):
    return emoji.emojize(text, use_aliases=True)

if __name__ == "__main__":
    user_input = input('Input: ')
    output = replace_emoji(user_input)
    print("Output:", output)
