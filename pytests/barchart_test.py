import pytest
from chart import Barchart


def test_empty_barchart_has_zero_len():
    barty = Barchart()
    assert len(barty) == 0


def test_empty_barchart_has_zero_max():
    barty = Barchart()
    assert barty.max_value() == 0


def test_empty_barchart_has_zero_min():
    barty = Barchart()
    assert barty.min_value() == 0


def test_init_barchart_with_dict():
    valuedict = {
        "Plum": 3,
        "Orange": 20,
        "Apple": 10,
        "Banana": 4,
        "Mango": 14
    }
    barty = Barchart(valuedict)
    assert barty.max_value() == 20
    assert barty.min_value() == 3
    assert len(barty) == 5


def test_add_value_with_integer_key():
    barty = Barchart()
    barty.add_value(2025, 9)
    assert barty.datadict[2025] == 9
    assert len(barty) == 1


def test_add_value_with_string_key():
    barty = Barchart()
    barty.add_value("Cherry", 10)
    assert barty.datadict["Cherry"], 10
    assert len(barty) == 1


def test_add_value_negative_raises_error():
    barty = Barchart()
    with pytest.raises(ValueError):
        barty.add_value("BadItem", -5)


def test_add_invalid_value_raises_error():
    barty = Barchart()
    with pytest.raises(TypeError):
        barty.add_value("BadItem", "not_a_number")


def test_add_dict_to_empty_barchart():
    valuedict2 = {
        "Bluebarry": 13,
        "Rusbarry": 0
    }
    barty = Barchart()
    barty.add_dict(valuedict2)
    assert barty.max_value() == 13
    assert barty.min_value() == 0
    assert len(barty) == 2


def test_add_dict_to_barchart_with_dict():
    valuedict = {
        "Plum": 3,
        "Orange": 20,
        "Apple": 10,
        "Banana": 4,
        "Mango": 14
    }
    valuedict2 = {
        "Bluebarry": 13,
        "Rusbarry": 0
    }
    barty = Barchart(valuedict)
    barty.add_dict(valuedict2)
    assert barty.max_value() == 20
    assert barty.min_value() == 0
    assert len(barty) == 7


def test_add_dict_invalid_type_raised_error():
    valuedict = {
        "Bluebarry": 13,
        "Rusbarry": "not_a_number"
    }
    barty = Barchart()
    with pytest.raises(TypeError):
        barty.add_dict(valuedict)


def test_add_dict_negative_value_raised_error():
    valuedict = {
        "Bluebarry": 13,
        "Rusbarry": -10
    }
    barty = Barchart()
    with pytest.raises(ValueError):
        barty.add_dict(valuedict)


def test_user_scale():
    barty = Barchart({"Apple": 3})
    barty.scale = 1
    expected = "\nApple  | ### (3%)" "\n       +----"
    assert str(barty) == expected


def test_negative_scale_raised_error():
    barty = Barchart({"Apple": 3})
    with pytest.raises(ValueError):
        barty.scale = -1


def test_scale_invalid_type_raised_error():
    barty = Barchart({"Apple": 3})
    with pytest.raises(TypeError):
        barty.scale = "BadInput"


def test_user_sign():
    barty = Barchart({"Apple": 3})
    barty.sign = "|"

    expected = "\nApple  | ||| (3%)" "\n       +----"
    assert str(barty) == expected


def test_long_sign_raised_error():
    barty = Barchart({"Apple": 3})
    with pytest.raises(ValueError):
        barty.sign = "BadInput"


def test_str_output():
    barty = Barchart({"Apple": 2})
    barty.scale = 1
    barty.sign = "#"
    barty.xunit = "%"
    barty.value_at_end = True

    expected = "\nApple  | ## (2%)" "\n       +---"
    assert str(barty) == expected


def test_str_output_value_end_False():
    barty = Barchart({"Apple": 2})
    barty.scale = 1
    barty.sign = "#"
    barty.xunit = "%"
    barty.value_at_end = False

    expected = "\nApple  | ##" "\n       +---"
    assert str(barty) == expected


def test_repr_output():
    barty = Barchart({"Apple": 2})
    barty.scale = 1
    barty.sign = "#"
    barty.xunit = "%"
    barty.value_at_end = True

    expected = "Barchart(items=1, scale=1, sign=#, value_at_end=True, xunit=%)"
    assert repr(barty) == expected


def test_set_item_dict():
    barty = Barchart({"Apple": 10})
    barty["Banana"] = 5
    assert barty["Banana"] == 5


def test_set_item_invalid_type_raises_error():
    barty = Barchart()
    with pytest.raises(TypeError):
        barty["Banana"] = "not_a_number"


def test_set_item_negative_raises_error():
    barty = Barchart()
    with pytest.raises(ValueError):
        barty["Banana"] = -10


def test_get_item_dict():
    barty = Barchart({"Apple": 10})
    assert barty["Apple"] == 10


def test_get_invalid_item_raised_error():
    barty = Barchart({"Apple": 10})
    with pytest.raises(KeyError):
        element = barty["Banana"]


def test_add_chart_to_other():
    barty = Barchart({"Apple": 10, "Charry": 7})
    chart = Barchart({"Orange": 3})
    combined = barty + chart
    assert len(combined) == 3
    assert combined.max_value() == 10
    assert combined.min_value() == 3


def test_add_charts_with_overlapping_keys():
    barty = Barchart({"Apple": 10, "Banana": 5})
    chart = Barchart({"Apple": 5, "Cherry": 7})
    combined = barty + chart

    assert combined["Apple"] == 15
    assert combined["Banana"] == 5
    assert combined["Cherry"] == 7
    assert len(combined) == 3


def test_str_output_with_color():
    barty = Barchart({"Apple": 2})
    barty.color = (255, 0, 0)  # Rot setzen
    output = str(barty)
    assert "\033[38;2;255;0;0m" in output
    assert "\033[0m" in output


def test_set_invalid_chart_color_raised_error():
    barty = Barchart({"Apple": 3})
    with pytest.raises(ValueError):
        barty.color = (500, 0, 255)


