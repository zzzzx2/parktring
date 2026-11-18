import passport
import best_price
import best_company
import health
import overbooking

options = {
    "1": ("Passport", passport.run),
    "2": ("Best price", best_price.run),
    "3": ("Best company", best_company.run),
    "4": ("Health recommendations", health.run),
    "5": ("Flight overbooking", overbooking.run),
}

def menu():
    while True:
        print("\n=== PARKTRING ===")
        for key, (name, _) in options.items():
            print(f"{key}. {name}")
        print("0. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "0":
            break
        if choice in options:
            options[choice][1]()
        else:
            print("Invalid option.")

if __name__ == "__main__":
    menu()
