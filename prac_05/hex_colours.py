
COLOR_CODES = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff",
}
def get_color_code(color_name):
    return COLOR_CODES.get(color_name.lower(), "Invalid color name")

while True:
    user_input = input("Enter a color name (or blank to exit): ")

    if not user_input:
        break

    color_code = get_color_code(user_input)

    print(f"The code for {user_input} is {color_code}")