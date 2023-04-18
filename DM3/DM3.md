# DM n°3
## Navette autonome

Pour faciliter le déplacement des touristes dans le centre commercial "Polygone Riviera", le propriétaire a fait appel à la société "AutoNav" qui est chargée de réaliser l'étude préalable du tracé et des caractéristiques. Cette société vous a embauché pour développer de nouveaux outils d'étude automatique pour ensuite proposer ses services à d'autres centres commerciaux.

Ce projet se focalise d'abord sur l'étude de la fréquentation et de la rentabilité avant de travailler sur le tracé du circuit.

## I / Fréquentation

On considère une liste d'entiers `freq` représentant le nombre de passagers par jour de la navette actuelle sur l'année dernière. 

1. Complétez la fonction `maxi` qui renvoie la valeur la plus haute de la liste passée en paramètre.
2. Expliquez la ligne `M = L[0]`.
3. En prenant exemple sur la fonction `maxi`, écrivez la fonction `mini` qui renvoie la valeur la plus basse.
4. Écrivez la fonction `moyenne` qui renvoie la moyenne de toutes les valeurs de la liste.
5. Écrivez une fonction qui retourne le nombre de jours où il y a eu plus de 50 passagers dans la navette.



## II / Rentabilité

1. La navette coûterait 16 000€ à exploiter par an, tout compris. Écrivez un programme qui calcul le total que ça rapporterait si le centre commercial faisait payer 1€ le trajet par personne. Cela recouvrerait-il les frais d'exploitation ? 
  
On considère maintenant que le tracé du parcours est représenté sous forme de liste de strings. Chaque lettre correspond à une action :
- "A" : avancer d'une distance d
- "G" : tourner à gauche de 90°
- "D" : tourner à droite de 90°

Pour être valide, un tracé doit revenir au point de départ dans la même orientation (faire une boucle). Un demi-tour ne peut pas être physiquement réalisé et est donc à proscrire du tracé.
La fonction `trace` pourra être utilisée pour visualiser le tracé des parcours proposés.

2. complétez la fonction `distance` qui prend en entrée un tracé et la distance d et retourne la distance totale du tracé
3. complétez la fonction `orientation` qui prend en argument le tracé du circuit et renvoie `True` si le circuit termine dans la même orientation qu'initialement, `False` sinon.
   On rappelle qu'il peut y avoir 4 orientations distinctes, que la fonction `%` peut être utilisée.
4. Complétez la fonction `demi_tour` qui renvoie `True` si le tracé comprend au moins un demi-tour.
5. Compléter le code de la fonction `est_valide` qui vérifie si un tracé est valide.
