# Heimurinn Karakter Menedzser

Ez az asztali alkalmazás lehetővé teszi [Heimurinn](https://heimurinn.hu/) karakterek kényelmes kezelését beépített automatizmusokkal.

**Ez az alkalmazás nem helyettesíti a Heimurinn szerepjáték alapkönyvét!**

## Funkciók
### Amit tud
- Több karakter kezelése
- Szintlépéskor automatikus kalkuláció a származtatott értékekre osztálynak megfelelően
- Beépített próbadobó gyakori próbákhoz, illetve egy általános kockadobó
- Hordozható adatbázis

### Amit nem tud
**Ezek azért nem kerültek bele, mert a túl sok lehetséges változó miatt nem lehetett érdemben automatizálni. Manuálisan azonban kezelhetőek.**
- Életerőt nem számol
- Jártasság pontokat nem kezeli, szintlépésekkor sem kalkulálja
- Képességek hatásait nem kezeli azok sokasága miatt
- A hírnevet nem kezeli szigorúan 100-as skálán

## Használat
Az alkalmazás nem igényel telepítést. Csak töltsd le az előre buildelt fájlt, és futtasd.
Az első indításnál létrehozza a **hkm.db** adatbázist.

### Saját build forráskódból
Ha magad buildelnéd a forráskódból, azt is megtheted.

> [!NOTE]
> Az alkalmazás **Python 3.14.0** használatával készült.

Töltsd le a forráskódot, és futtasd a következőket:
```
pip install -r requirements.txt
pyinstaller --windowed --onefile main.py
```