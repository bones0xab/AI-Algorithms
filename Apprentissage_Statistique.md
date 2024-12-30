# Apprentissage.
---

L'image illustre les concepts fondamentaux d'un **Processus Décisionnel de Markov (MDP)**. Voici une explication claire des éléments :

1. **États (S)** :  
   - Ce sont les positions possibles sur la grille.  
   - Par exemple, chaque case correspond à un état unique.

2. **Actions (Actions(s))** :  
   - Ce sont les déplacements possibles dans un état donné :  
     - **E** : Aller à l'Est.  
     - **W** : Aller à l'Ouest.  
     - **N** : Aller au Nord.  
     - **S** : Aller au Sud.

3. **Modèle de transition (P(s' | s, a))** :  
   - Probabilité de passer d’un état `s` à un autre état `s'` en exécutant une action `a`.  
   - Par exemple, aller à l’Est peut échouer (glisser ou heurter un mur), entraînant des transitions imprévues.

4. **Récompense (R(s))** :  
   - Une fonction qui attribue une valeur à chaque état en fonction de son désirabilité.  
   - Dans l’image :  
     - Les cases proches de l'objectif (orange, `But`) ont une forte récompense (+1).  
     - Les autres cases ont une faible ou négative valeur (ex. -0.4).

5. **Hypothèse markovienne** :  
   - Le futur dépend uniquement de l'état actuel et de l'action choisie, et non des états précédents.

6. **Objectif** :  
   - Maximiser les récompenses cumulées à long terme en choisissant une politique optimale.

---

Points importants :
Une politique doit couvrir tous les états possibles ou, à défaut, les états pertinents (accessibles).
Politique optimale : La politique qui maximise les récompenses cumulées (à long terme), en tenant compte des incertitudes.
