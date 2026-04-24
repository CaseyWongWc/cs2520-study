"""4/23 - zyBooks 11.8 LAB: Artwork label (modules).

Standard inputs (newline-separated):
    Pablo Picasso
    1881
    1973
    Three Musicians
    1921

Expected output:
    Artist: Pablo Picasso (1881 to 1973)
    Title: Three Musicians, 1921
"""


class Artist:
    def __init__(self, name="unknown", birth_year=-1, death_year=-1):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year

    def print_info(self):
        b = "unknown" if self.birth_year == -1 else str(self.birth_year)
        if self.birth_year == -1:
            d = "unknown"
        elif self.death_year == -1:
            d = "present"
        else:
            d = str(self.death_year)
        print(f"Artist: {self.name} ({b} to {d})")


class Artwork:
    def __init__(self, title="unknown", year_created=-1, artist=None):
        self.title = title
        self.year_created = year_created
        self.artist = artist if artist else Artist()

    def print_info(self):
        self.artist.print_info()
        print(f"Title: {self.title}, {self.year_created}")


if __name__ == "__main__":
    name = input()
    by = int(input())
    dy = int(input())
    title = input()
    yc = int(input())
    a = Artist(name, by, dy)
    w = Artwork(title, yc, a)
    w.print_info()
