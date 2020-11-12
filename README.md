# 🚀 reflask

## Velkommen til workshop 16.11.2020!
Gjennom dette faggruppemøte ønsker vi å vise hvordan man enkelt kan benytte seg av React i Frontend og Python med Flask i backend. Vi kommer til å jobbe oss gjennom et eksempel som viser hvordan React kan kommunisere med et bibliotek i Python for bildeklassifisering gjennom et API.

Dette vil være en workshop for alle og man behøver ikke å ha kjennskap til noen av delene før oppmøte. Det kommer til å bli lagt opp til en del praktiske oppgaver da målet for sessjonen er å vise hvordan man får koblet sammen Frontend og Backend.

### For å kunne bruke mest mulig tid på selve implementasjonen, ber vi deg om å verifisere at du har en datamaskin satt opp for denne workshopen. 
Vi ønsker at alle har gjennomført/verifisert følgende punkter før workshopen:

1. [Python](#python)
2. [Node](#node)
3. [Git](#git)

## Python
### Dersom du *IKKE HAR* python installert på maskinen:
- Last ned 64-bit versjon av python 3.5-3.8 fra https://www.python.org/downloads/ . NOTE: Den nyeste versjonen som ligger der er 3.9.0, det er viktig at ikke denne lastes ned. Scroll litt lengre ned på siden for å finne Python 3.8.6.
- Det kan være en fordel å installere den gjeldende versjonen direkte på c:\python38 for eksempel dersom du bruker windows. Det er også viktig å "huke av" valget om å legge python til i PATH/environment variables dersom python installeres på windows.

Når installasjonen er ferdig åpne et command-shell og skriv inn `python`. Dersom installasjonen var vellykket skal man kunne se noe ala dette:
```
$ python
Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Skriv så `exit()` for å stoppe Python-terminalen.

### Dersom du *HAR* python installert på maskinen
Sjekk hvilken versjon av python du har installert. Vi skal senere installere en modul i Python som krever følgende:
- Python 3.5–3.8 64-bit
- pip 19.0 eller nyere

Dette kan sjekkes ved å kjøre `python -VV`. Man vil da se noe ala:
```
$ python -VV
Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)]
```

Sjekk så at du har pip 19.0 eller nyere med kommandoen `pip -V`:
```
$ pip -V
pip 20.2.1 from c:\python38\lib\site-packages\pip (python 3.8)
```

## Node
__TO-DO__


## Git
- Last ned nyeste versjon av Git dersom du ikke har dette installert på maskinen: https://git-scm.com/downloads
- Clone ned dette repoet

Etter å ha gjort alle stegene over er du klar til Workshop!