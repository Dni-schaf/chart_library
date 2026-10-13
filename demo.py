from library.charts import *

def main():
    barty = Barchart_vertical(valuedict)
    chart = Barchart_vertical(valuedict2)
    combined = barty + chart
    #combined.color = (50,200,255)
    combined.highlight_max = (0,100,255)
    #combined.highlight_min = (255,255,255)
    print(barty)
    print(chart)
    print(combined)

if __name__ == "__main__":
    main()
