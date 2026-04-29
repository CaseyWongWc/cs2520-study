## 11.8 LAB: Artwork label (modules)
### LAB ACTIVITY: LAB: Artwork label (modules)
Define the `Artist` class in Artist.py with a constructor to initialize an artist's information. The constructor should by default initialize the artist's name to "unknown" and the years of birth and death to -1.
Define the `Artwork` class in Artwork.py with a constructor to initialize an artwork's information. The constructor should by default initialize the title to "unknown", the year created to -1, and the artist to use the `Artist` default constructor parameter values. Add an import statement to import the `Artist` class.
Add import statements to main.py to import the `Artist` and `Artwork` classes.
Ex: If the input is:
```
Pablo Picasso
1881
1973
Three Musicians
1921
```
the output is:
```
Artist: Pablo Picasso (1881 to 1973)
Title: Three Musicians, 1921
```
Ex: If the input is:
```
Brice Marden
1938
-1
Distant Muses
2000
```
the output is:
```
Artist: Brice Marden (1938 to present)
Title: Distant Muses, 2000
```
Ex: If the input is:
```
Banksy
-1
-1
Balloon Girl
2002
```
the output is:
```
Artist: Banksy (unknown)
Title: Balloon Girl, 2002
```
**Test Cases:**
| # | Input | Expected Output | Points |
|---|-------|-----------------|--------|
| 1 | `Pablo Picasso
1881
1973
Three Musicians
1921
` | `Artist: Pablo Picasso (1881 to 1973)
Title: Three Musicians, 1921` | 1 |
| 2 | `Brice Marden
1938
-1
Distant Muses
2000
` | `Artist: Brice Marden (1938 to present)
Title: Distant Muses, 2000` | 1 |
| 3 | `Banksy
-1
-1
Balloon Girl
2002
` | `Artist: Banksy (unknown)
Title: Balloon Girl, 2002` | 1 |
| 4 | `(none)` | `` | 2 |
| 5 | `(none)` | `` | 2 |
| 6 | `(none)` | `` | 2 |
| 7 | `(none)` | `` | 1 |
*Total: 10 points*
---
```python

```

```python

```
___
```python
class Artist:
    # TODO: Define constructor with parameters to initialize instance attributes
    #       (name, birth_year, death_year)
    def print_info(self):
        if self.birth_year >= 0 and self.death_year >= 0:
            print(
                f"Artist: {self.name} ({self.birth_year} to {self.death_year})"
            )
        elif self.birth_year >= 0:
            print(f"Artist: {self.name} ({self.birth_year} to present)")
        else:
            print(f"Artist: {self.name} (unknown)")
```
---
```python
from Artist import Artist
from Artwork import Artwork
if __name__ == "__main__":
    user_artist_name = input()
    user_birth_year = int(input())
    user_death_year = int(input())
    user_title = input()
    user_year_created = int(input())
    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)
    new_artwork = Artwork(user_title, user_year_created, user_artist)
    new_artwork.print_info()
```