import math
def circle_Area_Coverage(radiusOfCircle1, radiusOfCircle2):
    if not isinstance(radiusOfCircle1, int) and not isinstance(radiusOfCircle2, int):
        return "Must be an int."
    if radiusOfCircle1 < 0 or radiusOfCircle2 < 0:
        return "Must be a positive integer."

    larger_radius_of_circle= max(radiusOfCircle1, radiusOfCircle2)
    smaller_radius_of_circle= min(radiusOfCircle1, radiusOfCircle2)

    area_of_larger_circle = math.pi * (larger_radius_of_circle ** 2)
    area_of_smaller_circle = math.pi * (smaller_radius_of_circle ** 2)

    percentage_of_the_circles= (area_of_smaller_circle/area_of_larger_circle)*100
    return percentage_of_the_circles

print(circle_Area_Coverage(5,4))
print(circle_Area_Coverage(-9,8))

