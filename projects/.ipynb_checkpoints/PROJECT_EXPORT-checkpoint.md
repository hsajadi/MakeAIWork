# Export van project

<ol>

<li>

Paden aanpassen

chmod +x convert_path.py && ./convert_path.py "relative\path\to\model"

<ul>

<li>In VsCode selecteer je het bestand met de rechtermuisknop en kies je 'Copy Relative Path'</li>
<li>Pas het pad aan als het om een sub-directory of juist hoger gelegen directory gaat</li>
<li>Test de start-scripts vanuit een (git bash) terminal</li>

</ul>

</li>
<br>

<li>
Pycache verwijderen

```bash
rm -r simulations/*/__pycache__
```
</li>

<li> 
Map p1 aanmaken en daarin alle code en data kopieren

```bash
mkdir p1 && cp -r simpylc p1/ && cp -r simulations p1/
```

Map p1 toevoegen en committen met git

```bash
git add p1 && git commit -m "Deliverable Periode 1"
```

</li>

<li>

Git export van p1 maken

```bash
git archive -o "../{voornaam}_{achternaam}_p1.zip" HEAD:p1
```

</li>

<li>

Testen en uploaden

<ol>

<li>p1.zip op een adere locatie uitpakken en testen</li>

<li>p1.zip uploaden naar eigen Teams kanaal -> Deliverables periode 1

</li>

</ol>
