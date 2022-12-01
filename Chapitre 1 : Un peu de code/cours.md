## Boucles et conditions

On sait maintenant travailler sur des variables, leur associer des valeurs, les convertir et faire des calculs avec.
Pour créer des programmes il ne reste plus qu'à répéter ces action et c'est là qu'interviennent les boucles.

Il existe deux types de boucles, les boucles **while** et les boucles **for**. La boucle while s'exécute tant que sa **condition** est vrai (Booléen True). La boucle for s'exécute pour un nombre d'itérations **connues à l'avance**.

Dans les deux cas l'**indentation** est primordiale !
Tout le code indenté (décalé d'un cran vers la droite avec la touche tab) sera exécuté dans la boucle, il faut redescendre l'indentation pour sortir de la boucle.

### La boucle while
La boucle while prend en argument une condition et exécute le code tant que cette condition est vraie (True : Boolean)
```python
while(condition):
	code à exécuter dans la boucle
code hors de la boucle
```

> :warning: Si la condition est toujours vrai cela génère une boucle infinie. Pour éviter la surchauffe de votre PC. On peut utiliser la commande `ctrl+c` pour interrompre le processus.

```
i = 0
while i < 3:
	print(i)
	i += 1
```
```python
0
1
2
```
> :warning: oublier la ligne `i += 1` va faire que i < 3 sera toujours vrai et génèrera donc une boucle infinie

___
### La boucle for
La boucle *for* permet de parcourir un objet.

En l'utilisant avec `range(D,F,P)` cela va parcourir l'intervalle de D à F (exclu) par pas de P :
> range(1,6,2) va générer l'intervalle comprenant [1, 3, 5]

```python
for i in range(4):
	print(i)
```
```python
0
1
2
3
```

Si l'objet est une liste elle va être parcourue et la variable va prendre la valeur des éléments de cette liste tour-à-tour :
```python
for element in ['a','b','c','d']:
	print(element)
```
```python
'a'
'b'
'c'
'd'
```
 et cela fonctionne exactement de la même manière avec une chaine de caractères :
```python
for element in ["abcd"]:
	print(element)
```
```python
'a'
'b'
'c'
'd'
```
___
### Les conditions (if)

les conditions permettent d'exécuter un code en fonctiondu résultat d'un test. Elle se définie avec une ligne commençant par **if**, se terminant avec `:` et comportant un test :
```python
a = 4
if a > 3:
	print("a est strictement supérieur à 3")
```
```python
"a est strictement supérieur à 3"
```

Dans cet exemple on test si notre variable a est supérieur à 3. Le test `a > 3` renvoie `True`, la condition étant vraie ce qui est indenté s'exécute. On peut ajouter un **else** qui s'exécute si la condition est fausse :
```python
a = 4
if a > 3:
	print("a est strictement supérieur à 3")
else:
	print("a n'est pas strictement supérieur à 3")
```
ici on peut traduire tout ça en français :
*Si a est strictement supérieur à 3, on affiche la première phrase, sinon on affiche la seconde phrase*

Il existe un dernier mot-clé : `elif`, qui est la contraction de *else* et *if*
Il permet de ne pas imbriquer de nombreuses conditions.

Voici quelque-chose à ne pas faire :
```python
if a > 3:
	print("a est strictement supérieur à 3")
else:
	if a < 0:
		print("a est un nombre négatif")
	else:
		print("a est compris entre 0 et 3 inclus")
```

il faut préférer écrire :
```python
if a > 3:
	print("a est strictement supérieur à 3")
elif a < 0:
	print("a est un nombre négatif")
else:
	print("a est compris entre 0 et 3 inclus")
```
Ici on peut traduire ça par :
*Si a est strictement supérieur à 3, on affiche la première phrase, sinon si a est strictement inférieu à 0 on affiche la deuxième phrase sinon on affiche la troisième phrase*

> :warning: Il est primordiale de faire très attention aux indentations pour les boucles et les conditions, c'est l'une des plus grande source d'erreurs, avec l'oublie des ':' et l'utilisation du '=\='
