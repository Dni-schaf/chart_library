from library.charts import *

popular_languages = {
    "Python":36,
    "C/C++":13,
    "Java":10,
    "R":6,
    "JavaScript":5,
    "Swift":3,
    "C#":3,
    "Rust":3,
    "PHP":3,
    "Objective-C":3
}
chart1 = Barchart_horizontal(popular_languages)
chart1.highlight_max = (80,120,255)
print("\nThe Most Popular Programming Languages Worldwide \nAccording to the PYPL Index in April 2026")
print(chart1)
print("Source: https://de.statista.com")
print()
print()
print()

python_pypi_downloads = {
    "2016": 0.5,
    "2017": 1.5,
    "2018": 1.8,
    "2019": 1.4,
    "2020": 0.5,
    "2021": 3.1,
    "2022": 6.9,
    "2023": 5.9,
    "2024": 2.2,
    "2025": 2.2,
}
chart2 = Barchart_vertical(python_pypi_downloads)
chart2.scale = 1
chart2.highlight_max = (80,120,255)
chart2.highlight_min = (255, 10, 100)
print("\nInflationsrate in Deutschland (Veränderung des Verbraucherpreisindex gegenüber Vorjahr).\n")
print(chart2)
print("Source: https://de.statista.com")
print()
print()



valuedict = {
            "Banana": 7,
            "Mango": 15
        }

valuedict2 = {
            "MO": 2,
        }

def draw():
    barty = Barchart_vertical(valuedict)
    chart = Barchart_vertical(valuedict2)
    combined = barty + chart
    #combined.color = (50,200,255)
    combined.highlight_max = (0,100,255)
    #combined.highlight_min = (255,255,255)
    combined.scale = 2
    print(barty)
    print(chart)
    print(combined)

    barty2 = Barchart_horizontal(valuedict2)
    barty2.highlight_max = (0, 100, 255)
    barty2.highlight_min = (255,10,100)
    barty2.add_value("Di", 3)
    barty2.valuelabel = False
    barty2.xunit = "cm"
    barty2.sign = "#"
    print(barty2)

    # Initialize data
    data = {"Apple": 11, "Banana": 5, "Orange": 21}

    # Render a vertical barchart
    chart_v = Barchart_vertical(data)
    chart_v.scale = 0.1
    print(chart_v)

    # Render a horizontal barchart
    chart_h = Barchart_horizontal(data)
    print(chart_h)

if __name__ == "__main__":
    draw()
