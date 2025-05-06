from taipy.gui import Gui
import taipy.gui.builder as tgb

# images
cat_image = "assets/fake_cat.png"
bunny_image = "assets/fake_sad_rabbit.png"
emoji = "assets/emoji.jpg"

# variables
word_input = ""
result = ""
current_image = ""
counter = 0


def clear_result(state):
    state.result = ""


def palindrome(state):
    string = state.word_input.lower().replace(" ", "")

    if not string:
        state.result = "⚠️ Please enter a word."
        state.current_image = "assets/emoji.jpg"
        return
    
    if string == string[::-1]:
        state.counter += 1
        state.result = "✅ Correct!"
        state.current_image = state.cat_image
    else:
        state.counter -= 1
        state.result = "❌ Wrong answer!"
        state.current_image = state.bunny_image


def submit_word(state):
    palindrome(state)


# frontend layout
with tgb.Page() as page:
    with tgb.part(class_name="container card"):
        tgb.text("# Palindrome game", mode="md")
        tgb.text(
            "Palindrome is a set of characters that is the same both ways, for example 'racecar'.",
            mode="md",
        )
        tgb.text(
            "Try and type in other palindromes to gather points but be careful because each non-palindrome give a minus point.",
            mode="md",
        )

        tgb.text("Type in a palindrome word:", mode="md")
        tgb.input(value="{word_input}", on_action=clear_result)

        tgb.button(label="Submit", class_name="plain", on_action=submit_word)

        tgb.text("{result}")
        tgb.text("Your current score is {counter}.")

        tgb.image("{current_image}", width="400px", height="400px")

# run application
if __name__ == "__main__":
    Gui(page).run(use_reloader=True, port=8080)
