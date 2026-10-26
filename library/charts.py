class Chart:
    def __init__(self, datalist = None):
        self.datadict = {}
        self.valuelabel = True
        self.xunit = "%"
        self.sign = "#"
        self.scale = 1
        self.color = None
        self.highlight_max = None
        self.highlight_min = None

        if datalist is not None:
            self.add_dict(datalist)

    def __setattr__(self, name, value):
        if name == "scale":
            if type(value) not in (int, float):
                raise TypeError(
                    f"Scale must be a number (int/float)"
                )

            if value <= 0:
                raise ValueError(f"Scale must be greater than 0")

        if name == "sign":
            if len(str(value)) > 1:
                raise ValueError(
                    f"Sign must be one Letter"
                )

        if name in ("color", "highlight_max", "highlight_min"):
            if value is not None:
                if not isinstance(value, (tuple, list)) or len(value) != 3:
                    raise TypeError(
                        f"{name} must be a tuple or list with 3 elements (R, G, B)"
                    )

                for item in value:
                    if type(value) == int:
                        raise TypeError(f"Color values must be integers (int)")
                    if not (0 <= item <= 255):
                        raise ValueError(f"Color values must be between 0 and 255")

        super().__setattr__(name, value)

    def _validate_item(self, key, value):
        if type(value) not in (int, float):
            raise TypeError(
                f"Just int and float are supported in this Chart. '{key}', '{value}' rejected."
            )
        elif value < 0:
            raise ValueError(
                f"Negative Values are not supported in this Chart. '{key}', '{value}' rejected."
            )

    def _longest_word(self):
        if not self.datadict:
            return 0
        return max(len(str(key)) for key in self.datadict.keys())

    def max_value(self):
        if not self.datadict:
            return 0
        return max(self.datadict.values())

    def min_value(self):
        if not self.datadict:
            return 0
        return min(self.datadict.values())

    def add_value(self, key, value):
        self._validate_item(key, value)
        self.datadict[key] = value

    def add_dict(self, userdict):
        for key, value in userdict.items():
            self._validate_item(key, value)
        self.datadict.update(userdict)

    def colorize(self, text, rgb):
        if rgb is None:
            return text
        r, g, b = rgb
        return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

    def __len__(self):
        return len(self.datadict)

    def __repr__(self):
        return f"Barchart(items={len(self.datadict)}, scale={self.scale}, sign='{self.sign}', valuelabel={self.valuelabel}, xunit='{self.xunit}')"

    def __add__(self, other):
        if not isinstance(other, Barchart):
            raise TypeError(
                f"Unsupported operand type for +: 'Barchart' and"
                f" '{type(other).__name__}'"
            )
        combined_dict = self.datadict.copy()
        for key, value in other.datadict.items():
            if key not in combined_dict:
                combined_dict[key] = value
            else:
                combined_dict[key] += value
        return type(self)(combined_dict)

    def __setitem__(self, key, value):
        self._validate_item(key, value)
        self.datadict[key] = value

    def __getitem__(self, key):
        if key not in self.datadict:
            raise KeyError()
        return self.datadict[key]

class Barchart(Chart):
    def __init__(self, datalist = None):
        super().__init__(datalist)

class Barchart_horizontal(Barchart):
    def __init__(self, datalist = None):
        super().__init__(datalist)

    def __str__(self):
        string = ""
        length_longest_word = self._longest_word() + 1
        max_value = self.max_value()

        for key, value in self.datadict.items():
            space = length_longest_word - len(key)
            label = f"{key}{space * ' '}"
            bar = int(self.scale * value) * str(self.sign)
            barvalue = (
                f"({value}{self.xunit})" if self.valuelabel else ""
            )

            row_color = self.color
            if self.highlight_max is not None and value == max_value:
                row_color = self.highlight_max
            elif self.highlight_min is not None and value == self.min_value():
                row_color = self.highlight_min

            c_label = self.colorize(label, row_color)
            c_pipe = self.colorize("|", self.color)
            c_content = self.colorize(f"{bar} {barvalue}".strip(), row_color)
            string += f"\n{c_label} {c_pipe} {c_content}"

        axis = f"\n{length_longest_word * ' '} +{(int(self.scale * max_value) + 1) * '-'}"
        string += self.colorize(axis, self.color)

        return string


class Barchart_vertical(Barchart):
    def __init__(self, datalist = None):
        super().__init__(datalist)

    def __str__(self):
        if not self.datadict:
            return "Empty Chart"

        # Standard-Scale ist 1.0 (kann jetzt auch 2 oder 0.5 sein)
        scale = getattr(self, "scale", 1.0)

        # Skalierte Werte berechnen (Multiplikation statt Division)
        max_val = max(self.datadict.values())
        max_val_scaled = int(
            max_val * scale
        )  # 'int' oder 'round' für ganze Zeilen

        # Mindestens 1 Zeile hoch, selbst wenn skaliert sehr klein
        if max_val_scaled < 1:
            max_val_scaled = 1

        label_len = self._longest_word()
        value_label_len = (
            len(str(max_val)) + len(str(self.xunit)) + 2
            if self.valuelabel
            else 0
        )
        space = max(label_len, value_label_len)

        diagram = []

        # Das Diagramm richtet sich nach der skalierten Maximalhöhe
        for _ in range(max_val_scaled + 1):
            diagram.append([self.colorize("|", self.color)])

        for key, value in self.datadict.items():
            bar_color = self.color
            if self.highlight_max is not None and value == max_val:
                bar_color = self.highlight_max
            elif self.highlight_min is not None and value == self.min_value():
                bar_color = self.highlight_min

            # Skalierter Wert für diesen spezifischen Balken
            scaled_value = int(value * scale)

            for i in range(max_val_scaled + 1):
                # Die Bedingung arbeitet jetzt mit dem Multiplikator
                sign = (
                           " " if i < max_val_scaled - scaled_value + 1 else self.sign
                       ) * space
                if self.valuelabel and i == max_val_scaled - scaled_value:
                    value_label_text = (
                        value if self.xunit == "" else str(value) + str(self.xunit)
                    )
                    sign = f"({value_label_text}){(space - len(str(self.xunit)) - (len(str(value))) - 2) * ' '}"

                diagram[i].append(" ")
                diagram[i].append(self.colorize(sign, bar_color))
                diagram[i].append(" ")

        axis_line = "+" + "-" * (len(self.datadict) * (space + 2))
        diagram.append([self.colorize(axis_line, self.color)])

        label_row = [" "]
        for key in self.datadict.keys():
            padded_key = str(key) + " " * (space - len(key))
            label_row.append(self.colorize(f" {padded_key} ", self.color))
        diagram.append(label_row)

        return "\n".join("".join(row) for row in diagram)
