# Barchart 

> A lightweight, robust, and dependency-free Python library for rendering beautiful text-based barcharts directly in the terminal, featuring TrueColor support and value highlighting.

## Key FeaturesPure Python & No Dependencies: 
- Works out-of-the-box using standard libraries.
- Fail-Fast Validation: Strict input sanitization (TypeError, ValueError) for types, boundaries, scales, signs, and RGB colors.
- ANSI TrueColor Support (24-bit): Custom global coloring via RGB tuples.
- Smart Highlighting: Automatically highlight maximum and minimum values with distinct custom colors.
- Chart Arithmetic: Seamlessly combine two charts using the + operator (aggregating values for overlapping keys).
- Fully Tested: Comprehensive test suite ensuring high reliability.

## Quick Start

### Installation
Simply copy chart.py into your project or include it as a module.

### Basic Usage

```Python
from chart import Barchart
```

### Initialize with data

```Python
data = {"Apple": 10, "Banana": 5, "Mango": 14}
chart = Barchart(data)
```

### Print the chart

```Python
print(chart)
```

### Advanced Customization

```Python
# Customize appearance
chart.scale = 1.5
chart.sign = "#"
chart.xunit = "%"
chart.value_at_end = True

# Add colors (RGB tuples: 0-255)
chart.color = (50, 200, 255)         # Global chart color (Blue/Cyan)
chart.highlight_max = (0, 255, 0)    # Highlight highest value in Green
chart.highlight_min = (255, 0, 0)    # Highlight lowest value in Red

print(chart)
```

### Combining Charts

You can add two charts together. Duplicate keys will automatically have their values aggregated:

```Python
chart1 = Barchart({"Apple": 10, "Banana": 5})
chart2 = Barchart({"Apple": 5, "Cherry": 7})

combined = chart1 + chart2
print(combined)
# Apple will now have a value of 15!
```

## Configuration Options

| Attribute | Type | Default | Description |
|---|---|---|---|
| scale | int / float | 1 | Multiplier for the bar length. Must be > 0 |
| sign | str | # | Character used to draw the bars (must be a single character) |
| xunit | str | "%" | Unit string displayed next to the value|
| value_at_end | bool | True | Whether to display the numerical value at the end of the bar |
| color | tuple | None | Global RGB color tuple (R, G, B) for the chart|
| highlight_max | tuple | None | RGB color tuple for the maximum value in the chart | 
| highlight_min | tuple | None | RGB color tuple for the minimum value in the chart.|

## Error Handling (Fail Fast)

Barchart follows a strict validation policy:
- Negative values or scales raise a ValueError.
- Invalid types (e.g., passing a string where a number is expected, or a color tuple with out-of-range values) raise a TypeError.
- Non-existent keys accessed via brackets raise a KeyError.

## Running Tests

To run the test suite, execute:

```Bash
pip install pytest

# runing test with:
pytest
```
