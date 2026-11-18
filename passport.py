Countries = ("Spain", "Morocco", "France", "England")
can_go = (
    ("Morocco", "France"),
    ("England",),
    ("Spain", "England"),
    ("Morocco", "Spain"),
)

def Passport(Countries, can_go, countrie):
    """Devuelve los destinos permitidos según el país del pasaporte."""
    if countrie in Countries:
        index = Countries.index(countrie)
        return list(can_go[index])
    return []

def run():
    nationality = input("Enter your country: ").strip().title()
    print(Passport(Countries, can_go, nationality))

if __name__ == "__main__":
    run()
