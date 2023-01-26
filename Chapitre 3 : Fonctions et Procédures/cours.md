# Chapitre 3 : Fonctions et procédures

Pour effectuer une tâche il faut parfois répéter plusieurs **instructions**. Si on doit refaire la même tâche ailleurs dans le code on remarque que certains blocs vont être répétés régulièrement. Pour améliorer la **lisibilité** du code et réduire sa taille on peut alors utiliser des **procédures** ou des **fonctions** que l'on va **définir** une fois et que l'on va **appeler** lorsque l'on aura besoin d'exécuter les instructions qu'elles contiennent.

### Les instructions

C'est une suite de commandes, tapées dans l'invite de commande ou écrites à la suite dans l'éditeur de texte. Elles constituent la colonne vertébrale du programme et ne sont exécutées que suivant l'ordre d'écriture.

Par exemple, ces instructions permettent d'ajouter des élèves à une liste classe :

```python
élève = {}
élève["identite"] = "Alan Turing"
élève["âge"] = 16
élève["taille"] = 1.77
classe.append(élève)
```

Le programme aura bien enregistré les élèves dans la liste `classe` mais si on veut ajouter des élèves depuis plusieurs endroits dans le code il faudra recopier ces 5 lignes. Ça va donc augmenter la difficulté de lecture du code et compliquer la résolution d'erreurs.

---

On va donc utiliser les fonctions et procédures pour simplifier tout ça :

-   Une **procédure** est un objet que l'on peut appeler de n'importe où dans son code en lui donnant des arguments, qui va exécuter du code et **ne rien renvoyer**.
-   Une **fonction** est une procédure qui renvoi quelque-chose. (via `return`)

Que ce soit une fonction ou une procédure on les définit en utilisant le mot réservé `def` suivi des instructions indentées.

### Les procédures

Pour reprendre l'exemple de l'élève, on peut définir une procédure `ajout_élève` et l'appeler :

```python
def ajout_élève(prénom, nom, âge, taille):
	élève = {}
	élève["identite"] = prénom + " " + nom
	élève["âge"] = âge
	élève["taille"] = taille
	classe.append(élève)

ajout_élève("Alan", "Turing", 16, 1.77)
```
Ce code donne exactement le même résultat que plus haut mais ajouter un élève prend maintenant une seule ligne claire, beaucoup plus facile à comprendre dans un grand code.

### Les fonctions

Il y a cependant un problème, si on essaye d'exécuter la procédure `ajout_élève("Alan", 5, 16, 1.77)` cela va causer une erreur et arrêter le programme. On peut alors utiliser `try: ... except: ...` pour gérer cette erreur :

```python
def ajout_élève(prénom, nom, âge, taille):
	try:
		élève = {}
		élève["identite"] = prénom + " " + nom
		élève["âge"] = âge
		élève["taille"] = taille
		classe.append(élève)
		return True
	except:
		return False

réussi = ajout_élève("Alan", "Turing", 16, 1.77)
```

On a ici une fonction qui renvoi un booléen, True si l'ajout de l'élève s'est correctement déroulé, False sinon. On peut stocker le retour d'une fonction dans une variable.
