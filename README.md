# FactoryPWMW
## Autorki: Maria Woryna i Patrycja Waniołka

---

**Projekt ma przedstawiać współpracę pomiędzy klientem, usługą transportową oraz konkretnymi typami transportu.**

---

## ⚙️ Instalacja

Klonowanie repozytorium: [tu repozytorium](https://github.com/patrysia1912/FactoryPWMW.git)
i instalowanie bibliotek pytest i sphinx

    git clone <https://github.com/patrysia1912/FactoryPWMW.git>
    cd FactoryPWMW

    pip install pytest sphinx

---

## 🚀 Uruchomienie

![Python logo](cosmetics/Python-logo-notext.svg.png)

`python main.py`

---

## 📁 Struktura projektu

- `main.py`
- `customer.py`
- `services.py`
- `transport.py`
- `tests.py`
- `README.md`
- `cosmetics file` z  logo pythona

---

## 🧠 Opis wzorca Factory Method

**Factory Method (Metoda Fabrykująca)** to jeden z najważniejszych kreacyjnych wzorców projektowych. Jego głównym zadaniem jest rozwiązanie problemu bezpośredniego powoływania obiektów do życia w głównym kodzie aplikacji, co często prowadzi do silnych zależności i trudności w rozbudowie systemu.

**Jak to działa?**

Zamiast tworzyć obiekty bezpośrednio za pomocą wywołań konkretnych klas, wzorzec ten deleguje to zadanie do specjalnej "metody fabrykującej". Program opiera się na zdefiniowaniu wspólnego interfejsu dla tworzonych produktów, a decyzyjność o tym, jaki dokładnie obiekt ma powstać, zostaje zepchnięta do wyspecjalizowanych klas podrzędnych (tzw. konkretnych fabryk). Dzięki temu główny kod (klient) zgłasza jedynie zapotrzebowanie, nie wnikając w techniczne szczegóły procesu konstrukcji.

**Główne zalety takiego rozwiązania:**
* **Zasada otwarte-zamknięte:** Aplikacja jest gotowa na rozwój. Można swobodnie wprowadzać nowe typy produktów do systemu (tworząc dla nich nowe fabryki), bez konieczności modyfikowania już istniejącego, przetestowanego kodu.
* **Separacja odpowiedzialności:** Kod zajmujący się logiką biznesową jest całkowicie oddzielony od kodu odpowiedzialnego za techniczne tworzenie nowych obiektów. 
* **Łatwiejsze utrzymanie i testowanie:** Tworzenie instancji znajduje się w wyznaczonych, izolowanych miejscach w projekcie, co znacząco zmniejsza ryzyko błędów przy ewentualnych zmianach.

---

## Przykłady działania kodu

