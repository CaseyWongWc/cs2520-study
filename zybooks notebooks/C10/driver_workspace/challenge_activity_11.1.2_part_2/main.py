import si_units
import tri_shape

base_in_cm = int(input())
height_in_cm = int(input())

area_cm2 = tri_shape.area(base_in_cm, height_in_cm)

base_in_mm = si_units.cm_to_mm(base_in_cm)
height_in_mm = si_units.cm_to_mm(height_in_cm)

area_mm2 = tri_shape.area(base_in_mm, height_in_mm)

print(f"Triangle area is {area_cm2} cm^2 or {area_mm2} mm^2.")