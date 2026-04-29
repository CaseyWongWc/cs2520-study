11.6 Packages
Instead of importing a single module at a time, an entire directory of modules can be imported all at once. A package is a directory that, when imported, gives access to all of the modules stored in the directory. Large projects are often organized using packages to group related modules.

participation activity
11.6.1: Packages group related modules together.


1

2

The "game" package contains subpackages "sound" and "graphics".
import sound.music
import sound.effects

sound.music.play_sound()
sound.effects.play_whoosh()
# ...
Soundmusic.pyeffects.pyspeech.py
import game.sound
import game.graphics

game.sound.speech.talk()
game.graphics.terrain.draw_gnd()
# ...
GameGraphicsmodels.pytextures.pyterrain.py
Static figure: Begin Python code 1: import sound.music import sound.effects sound.music.play_sound() sound.effects.play_whoosh() # ... End Python code. Begin Python code 2: import game.sound import game.graphics game.sound.speech.talk() game.graphics.terrain.draw_gnd() # ... End Python code. A tree is shown with the Game package as the root. Game has subpackages Sound and Graphics. Sound has modules music.py, effects.py, and speech.py. Graphics has modules models.py, textures.py, and terrain.py. Step 1: Packages such as "sound" contain subpackages, such as "music" and "effects". Once subpackages are imported, modules and definitions in the subpackages are reached via dot notation. Only the Sound package with the music.py, effects.py, and speech.py modules is shown and the first program begins to execute. Importing sound.music highlights the Sound package and music.py. Importing sound.effects highlights the Sound package and effects.py. Step 2:The "game" package contains subpackages "sound" and "graphics". The full package tree is shown and the second program begins to execute. The line "game.sound.speech.talk()" executes and Game, Sound, and speech.py are highlighted. The line "game.graphics.terrain.draw_gnd()" executes and Game, Graphics, and terrain.py are highlighted.

Captions
Playing step 2: The "game" package contains subpackages "sound" and "graphics".

Feedback?
To import a package, a programmer writes an import statement and gives the name of the directory where the package is located. To indicate that a directory is a package, the directory must include a file called __init__.py. The _init_.py file often is empty, but may include import statements that import subpackages or modules. The interpreter searches for the package in the directories listed in sys.path.

Consider the following directory structure. A package ASCIIArt contains a canvas module, as well as the subpackages' figures and buildings.

Figure 11.6.1: Directory structure.
draw_scene.py            Script that imports ASCIIArt package
ASCIIArt\                     Top-level package
        __init__.py
        canvas.py
        figures\              Subpackage for figures art
               __init__.py
               man.py
               cow.py
               ...
        buildings\            Subpackage for buildings art
               __init__.py
               barn.py
               house.py
               ...

Feedback?
The draw_scene.py script can import the ASCIIArt package using the following statement:

Figure 11.6.2: Importing the ASCIIArt package.
import ASCIIArt  # import ASCIIArt package

Feedback?
Specific modules or subpackages can be imported individually by specifying the path to the item, using periods in the import name. References to names within the imported module require that the entire path be specified.

Figure 11.6.3: Importing the canvas module.
import ASCIIArt.canvas  # imports the canvas.py module

ASCIIArt.canvas.draw_canvas()  # Definitions in canvas.py have full name specified

Feedback?
The from technique of importing also works with packages, allowing individual modules or subpackages to be directly imported into the global namespace. A benefit of this method is that higher-level package names need not be specified.

Figure 11.6.4: Import cow module from figures subpackage.
from ASCIIArt.figures import cow  # import cow module

cow.draw()  # Can omit ASCIIArt.figures prefix

Feedback?
Even individual names from a module can be imported, making that name directly available.

Figure 11.6.5: Import the draw function from the cow module.
from ASCIIArt.figures.cow import draw  # import draw() function

draw()  # Can omit ASCIIArt.figures.cow

Feedback?
When using syntax such as "import y.z", the last item z must be a package, a module, or a subpackage. In contrast, when using "from x.y import z", the last item, z, can also be a name from y, such as a function, class, or global variable.

Using packages helps to avoid module name collisions. Ex: Consider if another package called 3DGraphics also contained a module called canvas.py. Though both modules share a name, they are differentiated by the package that contains them, that is, ASCIIArt.canvas is different from 3DGraphics.canvas. A programmer should take care when using the from technique of importing. A common error is to overwrite an imported module with another package's identically named module.

participation activity
11.6.2: Importing packages.
Consider the directory structure of the ASCIIArt package above.

1)
Write a statement to import the figures subpackage.
import 

Check

Show answer
2)
Write a statement to import the cow module.
import 

Check

Show answer
3)
Write a statement that calls the draw() function of the imported house module.
from ASCIIArt.buildings.house import draw                                 



Check

Show answer
4)
Write a statement that imports the barn module directly using the "from" technique of importing.

Check

Show answer

Feedback?