# Participation Activity 11.6.2
1) Write a statement to import the figures subpackage.
import ASCIIArt.figures
2) Write a statement to import the cow module.
import ASCIIArt.figures.cow
3) Write a statement that calls the draw() function of the imported house module.
from ASCIIArt.buildings.house import draw
draw()
4) Write a statement that imports the barn module directly using the "from" technique of importing.
from ASCIIArt.buildings import barn
barn.draw()