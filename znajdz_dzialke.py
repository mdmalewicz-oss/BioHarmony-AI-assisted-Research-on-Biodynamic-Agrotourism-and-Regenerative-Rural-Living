import urllib.parse
import webbrowser

def pokaz_rodzaje_dzialek():
    print("\nDostępne rodzaje działek w Polsce:")
    print("1. Budowlana (przeznaczona pod budowę domów)")
    print("2. Siedliskowa / Zagrodowa (dla rolników, pod zabudowę gospodarczą/mieszkalną)")
    print("3. Rolna (grunty orne, łąki, pastwiska)")
    print("4. Leśna (grunty pokryte lasem)")
    print("5. Rekreacyjna (np. ROD, pod domki letniskowe)")
    print("6. Inwestycyjna / Przemysłowa (pod hale, magazyny, usługi)")

def buduj_zapytanie():
    print("=== Generator Wyszukiwania Nieruchomości w Google ===")
    
    # 1. Rodzaj działki
    pokaz_rodzaje_dzialek()
    rodzaj = input("Wpisz rodzaj działki (np. budowlana, siedliskowa): ").strip()
    query_parts = [f'"{rodzaj}"', "działka OR dom OR nieruchomość"]

    # 2. Cena całkowita (Google obsługuje zakresy liczbowe operatorem "..")
    cena_min = input("Cena minimalna (PLN) [Enter aby pominąć]: ").strip()
    cena_max = input("Cena maksymalna (PLN) [Enter aby pominąć]: ").strip()
    if cena_min and cena_max:
        query_parts.append(f"{cena_min}..{cena_max} PLN")
    elif cena_max:
        query_parts.append(f"0..{cena_max} PLN")

    # 3. Cena za metr i wielkość (szukanie tekstowe, może być niedokładne)
    cena_m2_max = input("Maksymalna cena za m2 (np. 150) [Enter aby pominąć]: ").strip()
    if cena_m2_max:
        query_parts.append(f'0..{cena_m2_max} zł/m2 OR PLN/m2')
        
    pow_min = input("Minimalna wielkość działki (w m2) [Enter aby pominąć]: ").strip()
    if pow_min:
        query_parts.append(f'"{pow_min} m2" OR "{pow_min} mkw"')

    # 4. Dodatkowe informacje
    dodatki = input("Dodatkowe atuty (oddziel przecinkiem, np. las, jezioro, góry, widok): ").strip()
    if dodatki:
        dodatki_lista = [f'"{d.strip()}"' for d in dodatki.split(',')]
        query_parts.append("(" + " OR ".join(dodatki_lista) + ")")

    # 5. Infrastruktura i stan
    uzbrojona = input("Czy ma być uzbrojona / mieć media (T/N)? ").strip().upper()
    if uzbrojona == 'T':
        query_parts.append('("uzbrojona" OR "media" OR "prąd i gaz" OR "woda i prąd")')

    remont = input("Czy wymaga remontu? (T - tak, N - do zamieszkania, Enter - obojętnie): ").strip().upper()
    if remont == 'T':
        query_parts.append('("do remontu" OR "stan surowy")')
    elif remont == 'N':
        query_parts.append('("do zamieszkania" OR "gotowe do wprowadzenia" OR "wykończony")')

    # Łączenie zapytania
    pelne_zapytanie = " ".join(query_parts)
    
    # Dodanie filtrów popularnych polskich portali (opcjonalne, ale zwiększa skuteczność)
    pelne_zapytanie += " (site:otodom.pl OR site:nieruchomosci-online.pl OR site:olx.pl OR site:morizon.pl)"
    
    return pelne_zapytanie

def main():
    zapytanie = buduj_zapytanie()
    print("\nWygenerowane zapytanie dla Google:")
    print("-" * 40)
    print(zapytanie)
    print("-" * 40)
    
    # Tworzenie URL do Google
    url = f"https://www.google.com/search?q={urllib.parse.quote(zapytanie)}"
    
    otworzyc = input("\nCzy chcesz otworzyć to wyszukiwanie w przeglądarce? (T/N): ").strip().upper()
    if otworzyc == 'T':
        webbrowser.open(url)
        print("Otwieranie przeglądarki...")
    else:
        print("Możesz skopiować powyższe zapytanie i wkleić je w Google ręcznie.")

if __name__ == "__main__":
    main()
