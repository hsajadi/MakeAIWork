# Project deliverables 

<ol>

<li>

**Maak de relatieve Linux paden**

<p>Je kunt gebruik maken van het script <i>convert_path.py</i>

```sh
chmod +x convert_path.py && ./convert_path.py "relative\path\to\model"
```

</p>

<ul>

<li>In VsCode selecteer je het bestand met de rechtermuisknop en kies je 'Copy Relative Path'</li>
<li>Pas het pad aan als het om een sub-directory of juist hoger gelegen directory gaat</li>
<li>Test de start-scripts vanuit een (git bash) terminal</li>

</ul>

</li>
<br>

<li>

**Verwijder tijdelijke bestanden en directories**

<p>
Verwijder pycache directories

```bash
rm -r build/__pycache__
rm -r run/__pycache__
```

</p>

<p>
Verwijder checkpoint bestanden

```bash
rm notebook/*-checkpoint.ipynb
```
</p>

</li>

<li> 

**Maak zip-bestanden**

<p>
Maak een zip-bestand van de directoriees build, run en (indien van toepassing) sh
</p>

</li>

<li>

**Upload zip-bestanden**

<ul>
<li>
<p>
Upload de bestanden <u>build.zip</u> en <u>run.zip</u> naar je eigen Teams kanaal -> Deliverables periode 1/Project/Broncode
</p>
</li>

<li>
<p>
Upload het bestand <u>notebooks.zip</u> naar je eigen Teams kanaal -> Deliverables periode 1/Project/Notebooks
</p>
</li>

</li>

</ol>
