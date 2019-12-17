HEX_DICT = {"alice blue": "#f0f8ff", "azure": ["#f0ffff", "#e0eeee",
            "#c1cdcd", "#838b8b"], "beige": "#f5f5dc", "ghost white": "#f8f8ff",
            "light": "#eedd82", "light gray": "#d3d3d3", "linen": "#faf0e6",
            "medium": "#66cdaa", "medium aquamarine": "#66cdaa",
            "mint cream": "#f5fffa", "red": "#ff0000", "salmon": "#fa8072",
            "sandy brown": "#f4a460"}

hex_color = input("Color Name: ").lower()
while hex_color != "":
    if hex_color in HEX_DICT:  
        print(HEX_DICT[hex_color])
    else:
        hex_color = input("Color Name: ").lower()
    hex_color = input("Color Name: ").lower()
else:
    print("Good Day")
