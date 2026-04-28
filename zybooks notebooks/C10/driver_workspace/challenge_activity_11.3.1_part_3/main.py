from si_conversion import m_to_cm
from tri_shape import area
base_in_m = int(input())
height_in_m = int(input())
area_m2 = area(base_in_m, height_in_m)
base_in_cm = m_to_cm(base_in_m)
height_in_cm = m_to_cm(height_in_m)
area_cm2 = area(base_in_cm, height_in_cm)
print(f"Triangle area is {area_m2} m^2 or {area_cm2} cm^2.")