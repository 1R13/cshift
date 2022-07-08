# cshift
Python script for caesar shifting

This script can be used to shift and unshift texts using the caesar "encryption".

```
Usage: python3 cshift.py options "text"

Options:
-s <int>        Shift the supplied text by given offset.
-r <int>        Revert shift by given offset.
-f <filename>   Load text from file.
-d              Detect offset of shifted text using word detection.
-i              Read text from STDIN.
-l <en,de,fr>           Supply possible languages of original.
```

## Examples

### Supplying text as an argument.
```
python3 cshift.py -s 5 "The ham, green beans, mashed potatoes, and corn are gluten-free." | tee shifted.txt

Ymj mfr, lwjjs gjfsx, rfxmji utyfytjx, fsi htws fwj lqzyjs-kwjj.
```
### Reading from STDOUT 
```
cat shifted.txt | python3 cshift.py -i -r 5

The ham, green beans, mashed potatoes, and corn are gluten-free.
```

### Or read straight from a file
```
python3 cshfit.py -f shifted.txt -d

Possible offset of 1 with 1 words detected in en.
Possible offset of 3 with 2 words detected in en.
Possible offset of 4 with 6 words detected in de.
Possible offset of 7 with 17 words detected in de.
Die Wikipedia [ˌvɪkiˈpeːdia] ( anhören?/i) ist ein am 15. Januar 2001 gegründetes gemeinnütziges Projekt zur Erstellung einer freien Internet-Enzyklopädie in zahlreichen Sprachen mit Hilfe des sogenannten Wikiprinzips. Gemäß Publikumsnachfrage und Verbreitung gehört die Wikipedia unterdessen zu den Massenmedien.
```

## Language detection

cshift uses the langdetect module to find the most likely used language of a text and determine its offset from the original. The default lanuages are english and german, but can be changed in cshift.py or specified with the `-l` flag.





