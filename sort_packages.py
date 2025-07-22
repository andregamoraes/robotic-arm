def sort(width: float, height: float, length: float, mass: float) -> str:
    bulky = False
    heavy = False
    volume = width * height * length

    if volume >= 1000000 or width >= 150 or height >= 150 or length >= 150:
        bulky = True

    if mass >= 20:
        heavy = True

    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
