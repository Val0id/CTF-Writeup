import string

text = "࠴࠱࠼ࠫ࠼࠮ࡣࡋࡍࠨ࡛ࡍ࡚ࡇ࡛ࠩࡔࡉࡌࡥ"

numbers = {}
for i in range(32, 128):
    numbers[i + 2024] = chr(i)

for i in text:
    i = ord(i)

    print(numbers[i], end="")
