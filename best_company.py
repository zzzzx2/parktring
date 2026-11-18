Ratings = (
    ("AutoVeloz", 4.3), ("RuedasExpress", 3.8),
    ("ViajeLibre", 4.7), ("CochesGlobal", 2.9),
    ("EcoDrive Rent", 4.1), ("MoveNow", 3.5),
    ("AlphaCar", 4.8), ("BetaRoute", 3.2),
    ("HorizonRent", 4.0), ("TurboMotion", 4.5),
)

def best_company() -> tuple[str, float]:
    """Devuelve (empresa, valoración) con la valoración más alta."""
    best = max(Ratings, key=lambda x: x[1])
    return best[0], best[1]

def run():
    company, rating = best_company()
    print(f"La mejor empresa de alquiler de coches es {company} con una valoración de {rating}.")

if __name__ == "__main__":
    run()
