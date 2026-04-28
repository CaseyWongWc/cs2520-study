import si_units
import tri_shape
base_in_cm = int(input())
height_in_cm = int(input())

base_in_mm = si_units.cm_to_mm(base_in_cm)
height_in_mm = si_units.cm_to_mm(height_in_cm)

print(f"{base_in_cm} cm is {base_in_mm} mm")
print(f"{height_in_cm} cm is {height_in_mm} mm")
print(f"Triangle area in mm^2: {tri_shape.area(base_in_mm, height_in_mm)}")