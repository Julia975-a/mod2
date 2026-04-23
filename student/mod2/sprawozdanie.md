# Sprawozdanie – Analiza zużycia energii w systemie IoT

## 1. Cel zadania

Celem zadania była analiza danych pochodzących z systemu IoT monitorującego zużycie energii w domu oraz identyfikacja zależności i wzorców w danych.

---

## 2. Opis danych

Zbiór danych zawiera pomiary zużycia energii oraz parametrów środowiskowych, takich jak temperatura i wilgotność. Dane są zapisane w postaci szeregów czasowych.

---

## 3. Narzędzia

W analizie wykorzystano:

* język Python
* bibliotekę Pandas (analiza danych)
* Matplotlib i Seaborn (wizualizacja danych)

---

## 4. Analiza danych

### 4.1 Średnie zużycie energii wg dnia tygodnia

![wykres1](wykres1.png)

Wykres przedstawia średnie zużycie energii w zależności od dnia tygodnia.
Można zauważyć różnice pomiędzy dniami roboczymi a weekendem, co wskazuje na wpływ aktywności domowników.

---

### 4.2 Porównanie: czwartki vs weekend

![wykres2](wykres2.png)

Wykres pokazuje różnice w rozkładzie zużycia energii w ciągu dnia pomiędzy dniem roboczym (czwartek) a weekendem.
W weekend zużycie jest bardziej rozłożone w czasie, co sugeruje większą obecność domowników w domu.

---

### 4.3 Zużycie energii w ciągu dnia (wg godzin)

![wykres3](wykres3.png)

Wykres przedstawia średnie zużycie energii w zależności od godziny.
Widoczne są wyraźne wzorce dobowe, w tym godziny zwiększonego zużycia.

---

## 5. Wnioski

Na podstawie przeprowadzonej analizy można sformułować następujące wnioski:

* Zużycie energii wykazuje wyraźne wzorce dobowe – największe wartości występują w godzinach aktywności domowników.
* Występują różnice pomiędzy dniami roboczymi a weekendem, co wskazuje na wpływ stylu życia użytkowników.
* Rozkład zużycia energii w weekend jest bardziej równomierny niż w dni robocze.
* Dane mają potencjał do dalszej analizy oraz wykorzystania w modelach predykcyjnych.

---

## 6. Podsumowanie

Analiza danych IoT pozwoliła na identyfikację istotnych wzorców w zużyciu energii.
Wizualizacja danych umożliwiła lepsze zrozumienie zachowań użytkowników oraz czynników wpływających na zużycie energii.
