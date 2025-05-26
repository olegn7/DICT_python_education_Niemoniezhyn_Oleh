def print_help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    print("Special commands: !help !done")

def handle_list(list_type):
    while True:
        try:
            rows = int(input("Number of rows: "))
            if rows <= 0:
                print("The number of rows should be greater than zero")
                continue
            break
        except ValueError:
            print("The number of rows should be greater than zero")

    items = []
    for i in range(1, rows + 1):
        item = input(f"Row #{i}: ")
        if list_type == "ordered-list":
            items.append(f"{i}. {item}")
        else:
            items.append(f"* {item}")
    return "\n".join(items)

def save_to_file(text, filename="output.md"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

md_text = ""

while True:
    user_input = input("Choose a formatter: ")

    if user_input == "!help":
        print_help()
    elif user_input == "!done":
        save_to_file(md_text)
        break
    elif user_input == "plain":
        text = input("Text: ")
        md_text += text
    elif user_input == "bold":
        text = input("Text: ")
        md_text += f"**{text}**"
    elif user_input == "italic":
        text = input("Text: ")
        md_text += f"*{text}*"
    elif user_input == "inline-code":
        text = input("Text: ")
        md_text += f"`{text}`"
    elif user_input == "link":
        label = input("Label: ")
        url = input("URL: ")
        md_text += f"[{label}]({url})"
    elif user_input == "header":
        while True:
            try:
                level = int(input("Level: "))
                if 1 <= level <= 6:
                    break
                else:
                    print("The level should be within the range of 1 to 6")
            except ValueError:
                print("The level should be within the range of 1 to 6")
        text = input("Text: ")
        md_text += f"{'#' * level} {text}\n"
    elif user_input == "new-line":
        md_text += "\n"
    elif user_input == "ordered-list":
        md_text += handle_list("ordered-list") + "\n"
    elif user_input == "unordered-list":
        md_text += handle_list("unordered-list") + "\n"
    else:
        print("Unknown formatting type or command")

    print(md_text)
