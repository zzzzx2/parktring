health_data = {
    "brazil": ["Yellow fever", "Hepatitis A", "Typhoid"],
    "kenya": ["Yellow fever", "Typhoid", "Malaria"],
}

health_prevention = {
    "Yellow fever": "Yellow fever vaccine",
    "Hepatitis A": "Hepatitis A vaccine",
    "Typhoid": "Typhoid vaccine",
    "Malaria": "Antimalarial pills + mosquito repellent",
}

def health_recommendations(country: str) -> list[str]:
    return health_data.get(country.strip().lower(), [])

def run():
    name = input("Enter a country: ")
    illnesses = health_recommendations(name)

    for illness in illnesses:
        print(illness, "->", health_prevention.get(illness, "Ask your doctor"))

    if not illnesses:
        print("No relevant data for that country.")
    else:
        print("Ask your doctor about vaccines before travelling.")

if __name__ == "__main__":
    run()
