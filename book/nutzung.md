# Anleitungen und Beispiele

Wie schreibe ich ein Unterrichtsskript mit TeachBook/JupyterBook? Auf dieser Seite sammle ich Links zu wichtigen Manuals und Beispiele für inspirierende JupyterBooks.

## Allgemeine Quellen

Hier sammle ich Links, Workflows, Tipps und Tricks.

- [TeachBooks](https://teachbooks.tudelft.nl/) 
  - [Manual](https://teachbooks.tudelft.nl/jupyter-book-manual/intro.html)
  - [Template](https://github.com/TeachBooks/template) für neue Bücher
  - News
  
- [Jupyter Book](https://jupyterbook.org/en/stable/intro.html)
  - [Gallery: Beispiele für JupyterBooks](https://executablebooks.org/en/latest/gallery/) (oft mit Repository, so dass man sehen kann, wie's gemacht wurde)

### Bücher, die mit JupyterBook und/oder TeachBooks gemacht wurden
- Das wunderschöne [The Good Research Code Handbook](https://goodresearch.dev/)
  - Ein [tolles Kapitel](https://goodresearch.dev/decoupled) über guten Code, Refactoring usw.
  - Im [dazugehörigen Repository](https://github.com/patrickmineault/codebook) sieht man insb. auch das Styling mit [tufte.css](https://github.com/patrickmineault/codebook/blob/main/docs/_static/tufte.css) und den [dazugehörigen Fonts](https://github.com/patrickmineault/codebook/tree/main/docs/_static/et-book)
  - [hier als (nicht ganz so schönes) PDF](https://goodresearch.dev/_static/book.pdf), aber immerhin

## Wie mache ich...?

### [Einklappen vs Verstecken](https://jupyterbook.org/en/stable/interactive/hiding.html#hide-code-cell-content)
Man kann durch Zell-Tags...
- ganze Zellen (`cell`)
- nur den Code (`input`)
- nur den Output (`output`)
einklappen (`hide`) oder ganz verstecken (`remove`).

Bsp. Wenn ich das tag `remove-input` setze, wird der Code nicht angezeigt, aber das, was er produziert, z.B. ein Diagramm. Sehr praktisch!

