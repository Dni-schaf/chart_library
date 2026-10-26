import pytest
from library.charts import Barchart_vertical, Barchart_horizontal, Barchart, Chart

CHART_CLASSES = [Barchart_vertical, Barchart_horizontal]
KEY_CHART_CLASSES = [Barchart_vertical, Barchart_horizontal]


LEN_TEST_DATA = [
    ({}, 0),
    ({"Apple": 3, "Banana": 4, "Mango": 14}, 3)
]
@pytest.mark.parametrize("chart_cls", CHART_CLASSES)
@pytest.mark.parametrize("data, expected_output", LEN_TEST_DATA)
def test_len_function(chart_cls, data, expected_output):
    chart = chart_cls(data)
    assert len(chart) == expected_output


MAX_TEST_DATA = [
    ({}, 0),
    ({"Apple": 3, "Banana": 4, "Mango": 14}, 14)
]
@pytest.mark.parametrize("chart_cls", CHART_CLASSES)
@pytest.mark.parametrize("data, expected_output", MAX_TEST_DATA)
def test_max_function(chart_cls, data, expected_output):
    chart = chart_cls(data)
    assert chart.max_value() == expected_output


MIN_TEST_DATA = [
    ({}, 0),
    ({"Apple": 3, "Banana": 4, "Mango": 14}, 3)
]
@pytest.mark.parametrize("chart_cls", CHART_CLASSES)
@pytest.mark.parametrize("data, expected_output", MIN_TEST_DATA)
def test_min_function(chart_cls, data, expected_output):
    chart = chart_cls(data)
    assert chart.min_value() == expected_output


@pytest.mark.parametrize("chart_cls", KEY_CHART_CLASSES)
def test_getitem_function(chart_cls):
    valuedict = {
        "Plum": 3,
        "Orange": 20,
        "Apple": 10,
    }
    chart = chart_cls(valuedict)
    assert chart["Plum"] == 3
    assert chart["Orange"] == 20
    assert chart["Apple"] == 10

    with pytest.raises(KeyError):
        _ = chart["Banana"]


@pytest.mark.parametrize("chart_cls", KEY_CHART_CLASSES)
def test_set_item(chart_cls):
    chart = chart_cls({"Apple": 10})
    chart["Banana"] = 5
    assert chart["Banana"] == 5
    assert chart["Apple"] == 10


SET_ITEM_TEST_DATA = [
    ("Apple", -9, ValueError),
    ("Mango", "0", TypeError),
    ("Plum", "not_a_number", TypeError),
]
@pytest.mark.parametrize("chart_cls", KEY_CHART_CLASSES)
@pytest.mark.parametrize("key, value, expected_error", SET_ITEM_TEST_DATA)
def test_set_item_invalid_type_raises_error(chart_cls, key, value, expected_error):
    chart = chart_cls()
    with pytest.raises(expected_error):
        chart[key] = value


ADD_VALUE_TEST_DATA = [
    (2025, 9),
    ("Mango", 0),
    (3.14, 10),
]
@pytest.mark.parametrize("chart_cls", CHART_CLASSES)
@pytest.mark.parametrize("data, expected_output", ADD_VALUE_TEST_DATA)
def test_add_value_function(chart_cls, data, expected_output):
    chart = chart_cls()
    chart.add_value(data, expected_output)
    assert chart.datadict[data] == expected_output


ADD_VALUE_TEST_DATA = [
    ("Apple", -9, ValueError),
    ("Mango", "0", TypeError),
    ("Plum", "not_a_number", TypeError),
]
@pytest.mark.parametrize("chart_cls", CHART_CLASSES)
@pytest.mark.parametrize("key, value, expected_error", ADD_VALUE_TEST_DATA)
def test_add_value_function(chart_cls, key, value,expected_error):
    chart = chart_cls()
    with pytest.raises(expected_error):
        chart.add_value(key, value)


@pytest.mark.parametrize("chart_cls", KEY_CHART_CLASSES)
def test_add_dict_function(chart_cls):
    valuedict = {
        "Blueberry": 13,
        "Cherry": 0
    }
    chart = chart_cls({"Plum": 3,"Orange": 20})
    chart.add_dict(valuedict)
    assert chart["Plum"] == 3
    assert chart["Orange"] == 20
    assert chart["Blueberry"] == 13
    assert chart["Cherry"] == 0


ADD_DICT_TEST_DATA = [
    ({"Apple": -9}, ValueError),
    ({"Mango": "0"}, TypeError),
    ({"Plum": "not_a_number"}, TypeError),
]
@pytest.mark.parametrize("chart_cls", CHART_CLASSES)
@pytest.mark.parametrize("data, expected_error", ADD_DICT_TEST_DATA)
def test_add_dict_invalid_type_raised_error(chart_cls, data, expected_error):
    chart = chart_cls()
    with pytest.raises(expected_error):
        chart.add_dict(data)


HBAR_SCALE_TEST_DATA = [
    (0.5, "\nApple  | # (3%)" "\n       +--"),
    (2, "\nApple  | ###### (3%)" "\n       +-------"),
    (3, "\nApple  | ######### (3%)" "\n       +----------")
]
@pytest.mark.parametrize("scale, expected", HBAR_SCALE_TEST_DATA)
def test_user_scale_horizontal_barchart(scale, expected):
    chart = Barchart_horizontal({"Apple": 3})
    chart.scale = scale
    assert str(chart) == expected


VBAR_SCALE_TEST_DATA = [
    (0.5, "|    \n| ## \n+----\n  Mo "),
    (2, "|    \n| ## \n| ## \n| ## \n| ## \n| ## \n| ## \n+----\n  Mo ")
]
@pytest.mark.parametrize("scale, expected", VBAR_SCALE_TEST_DATA)
def test_user_scale_vertical_barchart(scale, expected):
    chart = Barchart_vertical({"Mo": 3})
    chart.valuelabel = False
    chart.scale = scale
    assert str(chart) == expected


SCALE_TEST_DATA = [
    (-1, ValueError),
    ("BadInput", TypeError)
]
@pytest.mark.parametrize("chart_cls", CHART_CLASSES)
@pytest.mark.parametrize("scale, expected_error", SCALE_TEST_DATA)
def test_negative_scale_raised_error(chart_cls,scale, expected_error):
    chart = chart_cls({"Apple": 3})
    with pytest.raises(expected_error):
        chart.scale = scale


@pytest.mark.parametrize("chart_cls", CHART_CLASSES)
def test_user_sign(chart_cls):
    chart = chart_cls({"Apple": 3})
    chart.sign = ":"

    output = str(chart)
    assert ":" in output


@pytest.mark.parametrize("chart_cls", CHART_CLASSES)
def test_long_sign_raised_error(chart_cls):
    chart = chart_cls({"Apple": 3})
    with pytest.raises(ValueError):
        chart.sign = "BadInput"


def test_barchart_horizontal_str_output():
    chart = Barchart_horizontal({"Apple": 2})
    expected = "\nApple  | ## (2%)" "\n       +---"
    assert str(chart) == expected


def test_vertical_barchart_str_output_valuelabel_False():
    chart = Barchart_vertical({"Apple": 2})
    chart.valuelabel = False
    expected = "\nApple  | ##" "\n       +---"
    assert str(chart) == expected


def test_vertical_barchart_str_output_valuelabel_False():
    chart = Barchart_vertical({"Mo": 2,"Di": 3})
    chart.valuelabel = False
    expected = "|        \n|     ## \n| ##  ## \n| ##  ## \n+--------\n  Mo  Di "
    assert str(chart) == expected


@pytest.mark.parametrize("chart_cls", CHART_CLASSES)
def test_xunit(chart_cls):
    chart = chart_cls({"Apple": 2})
    chart.xunit = "m"
    output = str(chart)
    assert "m" in output

@pytest.mark.parametrize("chart_cls", KEY_CHART_CLASSES)
def test_barchart_repr_output(chart_cls):
    chart = chart_cls({"Apple": 2})
    chart.scale = 1
    chart.sign = "#"
    chart.xunit = "%"
    chart.valuelabel = True

    class_name = chart_cls.__name__
    expected = (
        f"{class_name}(items=1, scale=1, sign='#', valuelabel=True, xunit='%')"
    )


@pytest.mark.parametrize("chart_cls", KEY_CHART_CLASSES)
def test_add_chart_to_other(chart_cls):
    chart1 = chart_cls({"Apple": 10, "Charry": 7})
    chart2 = chart_cls({"Orange": 3})
    combined = chart1 + chart2
    assert combined["Charry"] == 7
    assert combined["Orange"] == 3
    assert combined["Apple"] == 10


@pytest.mark.parametrize("chart_cls", KEY_CHART_CLASSES)
def test_combine_charts_with_overlapping_keys(chart_cls):
    chart1 = chart_cls({"Apple": 10, "Banana": 5})
    chart2 = chart_cls({"Apple": 5, "Cherry": 7})
    combined = chart1 + chart2
    assert combined["Apple"] == 15
    assert combined["Banana"] == 5
    assert combined["Cherry"] == 7


@pytest.mark.parametrize("chart_cls", KEY_CHART_CLASSES)
def test_combine_chart_to_false_object(chart_cls):
    chart1 = chart_cls({"Apple": 10, "Banana": 5})
    false_object = {"Apple": 5, "Cherry": 7}
    with pytest.raises(TypeError):
        combined = chart1 + false_object


@pytest.mark.parametrize("chart_cls", KEY_CHART_CLASSES)
def test_str_output_with_color(chart_cls):
    chart = chart_cls({"Apple": 2})
    chart.color = (255, 0, 0)
    output = str(chart)
    assert "\033[38;2;255;0;0m" in output
    assert "\033[0m" in output


COLOR_DATA = [
    ((256, 0, 255), ValueError),
    ((-1, 0, 255), ValueError),
    ("BadItem", TypeError),
    ((0, 255), TypeError),
    (("BadItem", 0, 255), TypeError)
]
@pytest.mark.parametrize("chart_cls", CHART_CLASSES)
@pytest.mark.parametrize("data, expected_error", COLOR_DATA)
def test_set_invalid_chart_color_raised_error(chart_cls, data, expected_error):
    chart = chart_cls({"Apple": 3})
    with pytest.raises(expected_error):
        chart.color = data
