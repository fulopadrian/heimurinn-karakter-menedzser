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

## Technikai jellemzők
Az alkalmazás **Python 3.14.0**-ben íródott **PySide6 6.10.2** és **sqlite3** használatával.