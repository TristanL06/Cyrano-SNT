# TD n°1 SNT 

## Exercice 1 : Jouons un peu avec les boucles

1. Écrire un programme qui crée une liste de tous les nombres de 1 à 20
2. Écrire un programme qui crée une liste de tous les nombres paires de 1 à 20
3. Écrire un programme qui crée une liste de tous les nombres de 20 à 1
4. Écrire un programme qui crée une liste de tous les nombres de 1 à 20 divisibles par 7 ou 3
5. Écrire un programme qui crée une liste de tous les nombres premiers inférieurs à 20
6. Écrire un programme qui crée une liste des 10 premiers nombres divisibles par 7 ou 3


## Exercice 2 : Calculons une moyenne

💡la fonction `input()` permet de rentrer de l'information pendant l'exécution. Utilisation :
```python
a = input("Phrase à afficher : ")
print(a)
```

```python
>>> Phrase à afficher : Salut le monde
Salut le monde
```

1. Écrire un programme qui demande à l'utilisateur de rentrer ses notes (/20 coef 1 uniquement) et retourne la moyenne quand il entre `moyenne`
2. Utiliser la fonction `round()` en lisant la documentation pour arrondir la moyenne à deux chiffres après la virgule.
3. Ajouter la possibilité d'entrer le coef de la note.
4. Ajouter la possibilité de mettre une note sur autre chose que 20
5. Avec la fonction `split()` (lire la doc) permettre à l'utilisateur d'entrer la note, le dénominateur et le coef sur la même ligne :
```python
>>> Entrer la note sous la forme 10/20*1 (note : 10/20 coef 1) : 12/15*2
>>> Note enregistrée : 12/15, coefficient 2
```


## Exercice 3 : Passer à la caisse !

Voici la liste des articles d'un marchand de fruits et légumes
| ID | Nom | Prix (€/Kg) |
| -- | -- | -- |
| 1 | Pomme | 1.50 |
| 2 | Poire | 2.20 |
| 3 | Pêche | 3.25 |
| 4 | Banane | 0.96 |
| 5 | Abricot | 7.20 |

1. Écrire le dictionnaire prenant pour clé les ID des produits.
2. Écrire un code permettant d'entrer l'id d'un produit, puis le poids voulu et affiche le prix.
3. Écrire un code permettant d'entrer le nom d'un produit, puis le poids voulu et affiche le prix.
4. Pour la question précédente le dictionnaire est-il optimal ?
   Écrire un autre dictionnaire prenant en clé le nom.
5. Refaire la question 3 avec le nouveau dictionnaire
6. Prendre en entrée une liste de tuples `(nom, quantité)` et qui affiche le prix total.
7. Même question que précedemment mais qui affiche le détail
