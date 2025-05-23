from taipy.gui import Gui
import taipy.gui.builder as tgb
import plotly.express as px

df = px.data.gapminder()
fig = px.line(df.query("country == 'Sweden'"), x="year", y="pop")

slider_value = 1
selected_fruit = "tomato"
number1 = 1
number2 = 1

sum_ = number1 + number2
difference = number1 - number2
product = number1 * number2
quotient = number1 / number2

def perform_calculation(state):
    state.sum_ = int(state.number1) + int(state.number2)
    state.difference = int(state.number1) - int(state.number2)
    state.product = int(state.number1) * int(state.number2)
    state.quotient = int(state.number1) / int(state.number2)


def clear_results(state):
    state.sum_ = ""
    state.difference = ""
    state.product = ""
    state.quotient = ""


with tgb.Page() as page:
    with tgb.part(class_name="container card"):
        with tgb.layout(columns="1 1 1"):
            with tgb.part() as column_fruit:
                tgb.text("# Hello there taipy", mode="md")
                tgb.text("Welcome to the world of reactive programming")

                # binds to slider_value variable and makes it dynamic
                tgb.slider(value="{slider_value}", min=1, max=50, step=1, continuous=False)
                tgb.text("Slider value is at {slider_value}")
                tgb.text("Slider value again is at {slider_value}")

                tgb.text("Select your favorite fruit", mode="md")
                tgb.selector(
                    value="{selected_fruit}",
                    lov=["tomato", "apple", "avocado", "banana"],
                    dropdown=True,
                )
                tgb.text("Picture of  {selected_fruit}")
                tgb.image("assets/{selected_fruit}.jpg")

            with tgb.part() as column_calculator:
                tgb.text("## Coolu calculatoru", mode="md")
                tgb.text("Type in a number")
                tgb.input("{number1}", on_change=clear_results)

                tgb.text("Type in another number")

                # on_change -> this function will run when value is changed
                tgb.input("{number2}", on_change=clear_results)

                tgb.text("You have typed in {number1} and {number2}", mode="md")

                # on_action -> this function will run when button is clicked
                tgb.button(label="CALCULATU", class_name="plain", on_action=perform_calculation)

                tgb.text("{number1} + {number2} = {sum_}", mode="md")
                tgb.text("{number1} - {number2} = {difference}", mode="md")
                tgb.text("{number1} * {number2} = {product}", mode="md")
                tgb.text("{number1} / {number2} = {quotient}", mode="md")

            with tgb.part() as column_data:
                tgb.table("{df}", page_size=10)
                tgb.chart(figure="{fig}")


if __name__ == "__main__":
    Gui(page).run(dark_mode=False, use_reloader=True, port=8080)