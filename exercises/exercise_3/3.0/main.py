from taipy.gui import Gui
import taipy.gui.builder as tgb

# images
cat_image = "assets/fake_cat.png"
bunny_image = "assets/fake_sad_rabbit.png"

# variables
word_input = ""
result = ""
counter = 0


def clear_result(state):
    state.result = ""


def palindrome(state):
    string = state.word_input.lower().replace(" ", "")
    if string == string[::-1]:
        state.counter += 1
        state.result = "✅ Correct!"
        state.cat_image = True
    else:
        state.counter -= 1
        state.result = "❌ Wrong answer!"
        state.bunny_image = True


def submit_word(state):
    palindrome(state)


# frontend layout
with tgb.Page() as page:
    tgb.text("# Palindrome game", mode="md")
    tgb.text("Type in a palindrome word:", mode="md")
    tgb.input(word_input, on_action=clear_result)

    tgb.button(label="Submit", on_action=submit_word)

    tgb.text("Palindrome = {result}.")
    tgb.text("Your current score is {counter}.")
    # tgb.image(cat_image)
    # tgb.image(bunny_image)

# run application
if __name__ == "__main__":
    Gui(page).run(use_reloader=True, port=8080)
