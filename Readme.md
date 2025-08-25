## Présentation du projet FAQ API

Ce projet est une **application Flask** qui sert d’interface simple pour interagir avec l’API Perplexity Chat (completions endpoint). L’application permet de poser des questions et de recevoir des réponses générées par l’IA.

## Prérequis

- Python 3.8 ou plus récent[^1]
- Pip (gestionnaire de paquets Python)
- Un accès internet


## Installation

1. Clonez ce dépôt ou copiez le fichier `FAQ-API.py` sur votre machine.
2. Installez les dépendances requises avec pip :

```bash
pip install flask requests
```


## Utilisation

1. Lancez l’application :

```bash
python FAQ-API.py
```

2. Ouvrez votre navigateur à l’adresse suivante :

```
http://127.0.0.1:5000
```

3. L’interface vous permet de soumettre des questions et de visualiser les réponses fournies par l’API Perplexity.

## Fonctionnement

- Le serveur Flask expose une interface web.
- Lorsqu’une question est posée, l’application envoie la requête à l’API Perplexity et affiche la réponse sur la page web.
- Le fichier contient également une clé API d’exemple à remplacer par la vôtre au besoin.


## Personnalisation

- Vous pouvez modifier le template HTML ou l’adresse API si besoin dans le fichier `FAQ-API.py`.
- Pour toute extension, suivez la structure Flask au sein du fichier.

***

© 2025 – FAQ-API par [Votre Nom]

Ce README peut être copié dans un fichier nommé `README.md` placé à la racine de votre projet pour une documentation accessible et professionnelle.[^1]

<div style="text-align: center">⁂</div>

[^1]: FAQ-API.py

