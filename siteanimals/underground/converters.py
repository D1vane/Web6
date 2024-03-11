class FourDigitYearConverter:
    regex = "[0-9]{4}"
# Преобразование фрагмента URL в целочисленный тип данных
    def to_python(self, value):
        return int(value)
# Преобразование целочисленного значения в строку для URL
    def to_url(self, value):
        return "%04d" % value