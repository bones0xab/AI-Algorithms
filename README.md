# AI-Algorithms
This is a repo for my educational courses about AI and the algorithms, also an operational search in the field of AI and Graphs. 
***



## AI Module
# Resolution of a problem
  **La résolution d un problem dans un espace de possibilite utilisant des heuristiques , `[Etat initial]` jusqu au etat `[Etat final]`, en cherchant le meuilleur  chemin.**

--- 

`Partie 1 :` Algorithmes de recherch non informe (Aveugle)

Le raisonnement sur un problem c'est de construire une arborecence de racine "Etat initial" en identifiant le chemin de raisonnement le plus interessant qui correspond a la solution.


b : Le facteur de branchement definir comme le nombre maximal des noeud fils de tous le noeuf parents. (b = le nbr de noeud max pour le plus grand parent exist).

m : Profondeur maximale de l arboresence.
d : profondeur de etat but dans l arboresence.


-Critere d'evaluation des algorithms generale de la recherche:
*Optimalite: Trouver la meuilleur solution parmi plusieur.
*Completude : Si une solution exist l algo garanti pour resoudre
*Comlexite en temps : Estimation du temps necessaire pour resoudre un problem donne.
*Complexite en memoire : Estimation de l espace memoire necessaire a l algo pour resoudre le problem.

---
## Algorithm general de recherche
![image](https://github.com/user-attachments/assets/f07bfc6a-c0a4-4f91-9920-5b00f9b2bb11)

![image](https://github.com/user-attachments/assets/d33eb7ac-ac80-4a2f-bab0-3ae29e046e7e)

---
## Concepts de base de recherche
un algorithme de recherche repose sur les elements suivants : 
-> Arboresence de recherch 
-> Expansion d'un noeud
-> Strategie de recherch : l etendre d un noeud a chaque etape , (cad : comment tu explore les noeuds a travers ordre alphabetique ou numerique)

---
## Classes des algorithmes de recherche 

### Algorithmes non informe ou aveugles
Faire tout la recherche sans utiliser aucune information concernant la structure de espace de recherch.

### Alforithmes informe
Utilisent des sources d information supplimentaure (Ces algo parvient par des performences meuilleures) 

---
![image](https://github.com/user-attachments/assets/c7a72692-f305-4166-a7cf-6f21fb624f68)

**Algorithme de recherche en largeur  BFS**.
C est le fait d explorer tous les noeuds d un niveau pour aller explorer les noeuds d un niveau suivant.

`Processus : Cest de start par l etat initial et mettre dans la file ainsi mettre dans la liste des noeuds ferme et enfiler les fils , et vise versa `

### Exemple : 

![image](https://github.com/user-attachments/assets/b073b71b-2157-45e7-9867-753485e1c1f8)
![image](https://github.com/user-attachments/assets/86cde390-1075-4917-9321-22f7f195d2b5)
![image](https://github.com/user-attachments/assets/bea85303-f715-41af-bbf6-710a8a475805)

---
### Estimation de la complexite en temps et en memoire de l'algorithme BFS
-- Complexite en temps : est mesure en fonction du nombre de noeud teste 
-- Comlexite en memoire  : par est donne par la taille maximale atteinte par OUVERT lors de l execution de Algo BFS.


## Pour estimer ces complexiter en prend le cas defavorable.

-> Complexiter en temps : 
Le nombre de noeud tests dans arboresence theorique : 
![image](https://github.com/user-attachments/assets/e4f2d0b1-3b9a-41c2-acda-bcaf13c5b2fc)


-> Complexiter en memoire : 
Le taille maximal qui peut atteindre S=OUVERT
![image](https://github.com/user-attachments/assets/689aec1f-0cdc-4948-ada3-3d78b31e87f6)



**Pour comparer les algorithmes de meme class on definir le facteur de branchement theorique b***

-L'algorithme le plus efficace est celui qu a un facteur de branchement proche de 1.
-Le calcule de l'algo est : 
![image](https://github.com/user-attachments/assets/e6456552-2716-45a9-82f1-5419eafb12c7)


## Exemple : 
![image](https://github.com/user-attachments/assets/1ae04ec1-2dc1-4603-a1ad-55e89e2ebd98)

** Algorithme de recherche en profondeur DFS**
Cette algorithm cert a faire la recherche en profondeur , c est de partir d etat initial et allez en profondeur jusquau en trouve pas un succeseur et en revien au precedent, et encore en complet. 
Lors de l enfilation dans OUVERT, si en trouve succeseur en defile le dernier et en  insere le noeud dans FERME et entre le nouveu noeud.
Jusqu'a atteint l etat but.
RQ : en fait la detruire de S, et en dessin le graph de S.


Exemple : 
![image](https://github.com/user-attachments/assets/e49b9fa3-19af-46ec-8918-523d7d754822)


b = 3
m = 4
d = 4

** Pour l algo DFS on a tout le temps m=d **

Tout information 
![image](https://github.com/user-attachments/assets/a13a86fe-c0db-4e57-b0ed-1e13aadca21d)

-> Estimation de la complexite de temps et d espace pour DFS

-Complixite en memoire : c est la taille maximal qu on peut atteindre au cour de OUVERT=pile lors de l execution de l algo DFS.
`Cm(b,d) = m.b = O(b.d4)`

 ![image](https://github.com/user-attachments/assets/aff2a7f8-18b2-4a1b-895e-5a0b9a333b9f)


 -Complexite en temps : Cette complexite est donne par le nombre de noeud testes
`Noeud Teste = b*0 + b*1 ... + b*d`
Ct(b,d) = b*0 + b*1 + ... + b*d = (b*(d+1) -1 )/(b - 1) = O(b*d)



* Facteur de branchement theorique associe au DFS *

  + L'algo DFS est souhaitable pour les espace de recherche fini et sous cycle + 
  Nombre de noeud Teste = b*0 + b*1 + ... + b*d

  en fair des estimation de la valeur de b* pour trouver une approximiter presque de nombre de noeud.

- Algorithm DFS : 
![image](https://github.com/user-attachments/assets/09ff1aba-02e2-4d90-af97-5056cfe15b5d)



`Recherche limité`
En trouve que le BFS utilise becaupe de memoire pour cela en travail juste avec le DFS dans la realite, mais le DFS manque de l optimalite au chemin , cad que le chemin peut etre loin d etre optimal.
Donc pour cela on peut corrige cette problem par avoir la profondeur d ou se trouve l etat but.
En limite la recherch a la profondeur h(limite) = d.


- Recherche en profondeur limité
  -> Startegie
  En recherche avec une limite d exploitation L
  le changement : 
![image](https://github.com/user-attachments/assets/18cca8ed-8d84-4b56-a16e-b6f8ad4f3dbc)

---

-Recherche par approfondissement iteratif
est un algorithme de recherche qui combine les avantages de la recherche en profondeur (DFS) et de la recherche en largeur (BFS). Cet algorithme est souvent utilisé dans les arbres ou les graphes lorsque la profondeur de la solution est inconnue et que la mémoire est une contrainte importante.

Le processus : 
Fixer une profondeur limite, notée 𝑑
d, et d'explorer en profondeur jusqu'à cette limite en utilisant DFS.
Incrémenter progressivement cette limite et relancer une recherche DFS jusqu'à atteindre cette nouvelle limite.
Répéter ce processus jusqu'à ce qu'une solution soit trouvée ou que l'ensemble du graphe soit exploré.
Chaque itération explore tous les chemins possibles jusqu'à la profondeur 
𝑑
d avant d'augmenter cette profondeur.

![image](https://github.com/user-attachments/assets/8cd1cb88-ff6b-44e1-ad00-062ce11d923b)

![image](https://github.com/user-attachments/assets/7cfbb6e5-fb5f-4fc0-9554-480c7dd35e71)
![image](https://github.com/user-attachments/assets/59d56487-50b6-421f-b684-9fa4ae52ff3c)
![image](https://github.com/user-attachments/assets/c02afc1c-e2b0-47e6-a685-47808452ee6c)


---

## Recherche informe ou heuristique
-> Recherche A 
C'est de donne une estimation du chemin complet (De noeud initial au final).

** Fonction d'evaluation **
f(n) = g(n) + h(n)
![image](https://github.com/user-attachments/assets/41693d6d-42ff-452e-99d5-2565b0cb0d69)


## Heuristique admissible (h)

-En dit qu'une heuristique est admissible si pour tout noeud h(n)<= h*(n)

![image](https://github.com/user-attachments/assets/ab0377be-5675-490c-9fe7-43f9940438b3)

`h* le vrai cout pour atteindre etat but a partir de n`
-Une heuristique admissible ne surestime jamais le cout pour atteindre le but E.I elle est optimal.

* h est admissible alors la solution retourner par l algorithme est optimal*
* Si on a h admissible donc A devient A* *

***
# CHATGPT
# Différences entre BFS, DFS et les Algorithmes Heuristiques

## 1. Qu'est-ce qu'une heuristique ?

Une **heuristique** est une méthode ou une stratégie permettant de prendre des décisions rapides et efficaces dans un problème donné, en s'appuyant sur des **estimations** ou des **approximations** plutôt que sur des calculs exhaustifs.

Dans les algorithmes, une heuristique est souvent une fonction qui aide à guider une recherche vers une solution potentielle plus rapidement, en exploitant des **connaissances spécifiques** sur le problème.

---

## 2. Différences entre BFS, DFS et les Algorithmes Heuristiques

| **Critères**          | **BFS**                                  | **DFS**                                  | **Algorithmes Heuristiques**              |
|-----------------------|-------------------------------------------|------------------------------------------|-------------------------------------------|
| **Principe**          | Explore les nœuds par **niveau**          | Explore les nœuds en **profondeur**      | Utilise une fonction d'heuristique pour guider la recherche. |
| **Optimalité**        | Trouve le chemin le plus court (dans graphes non pondérés). | Pas garanti de trouver le chemin optimal. | Peut trouver le chemin optimal avec une bonne heuristique. |
| **Exploration**       | Systématique, **épuise tout** à chaque niveau. | Explore un chemin entièrement avant de revenir en arrière. | Oriente la recherche vers des solutions prometteuses, en évitant des parties inutiles. |
| **Structure de données** | Utilise une **file**.                   | Utilise une **pile** ou récursivité.     | Souvent utilise une **file de priorité** (comme dans A\*). |
| **Complexité spatiale** | Élevée (stocke de nombreux nœuds).       | Moins gourmande que BFS.                 | Dépend de l'heuristique et de la structure de données. |
| **Exemples**          | Parcours d’un graphe, chemin le plus court. | Détection de cycles, exploration profonde. | A\* (A étoile), Algorithmes génétiques, etc. |

---

## 3. Algorithmes heuristiques : Fonctionnement et avantages

Les algorithmes heuristiques, comme **A\*** ou les **algorithmes génétiques**, utilisent une fonction heuristique pour **estimer** le coût ou la distance vers l'objectif final.

### Exemple : Algorithme A\*

- **f(n) = g(n) + h(n)** :
  - **g(n)** : coût du chemin réel depuis le nœud initial jusqu'au nœud \(n\).
  - **h(n)** : estimation heuristique du coût restant pour atteindre l'objectif.
- A\* explore les chemins qui **minimisent** cette fonction.

### Avantages des algorithmes heuristiques :

1. **Rapidité** : Ils permettent de réduire l'espace de recherche en se concentrant sur les chemins prometteurs.
2. **Optimalité** : Avec une heuristique admissible (ne surestime jamais le coût), ils peuvent trouver des solutions optimales (comme A\*).
3. **Efficacité** : Très utiles dans les grands espaces de recherche, comme les labyrinthes ou les jeux.

---

## 4. Comparaison en termes d'optimisation

### BFS/DFS

#### Avantages :
- **Simple** à implémenter.
- BFS garantit une solution optimale **dans des graphes non pondérés**.
- DFS a une **faible empreinte mémoire** (surtout pour des graphes peu denses).

#### Inconvénients :
- Peu efficace pour des problèmes complexes avec de grands espaces de recherche.
- BFS est **gourmand en mémoire**.
- DFS peut explorer inutilement de longs chemins qui ne mènent pas à une solution.

### Algorithmes heuristiques

#### Avantages :
- **Plus rapides** pour trouver une solution dans de **grands espaces de recherche**.
- Peuvent être **optimaux** (sous conditions, comme avec A\*).
- Moins de calculs exhaustifs, car ils exploitent des **estimations**.

#### Inconvénients :
- Dépendant de la **qualité de l'heuristique** : une mauvaise heuristique peut rendre l'algorithme inefficace.
- Plus **complexe** à implémenter.

---

## 5. Quand choisir BFS/DFS ou des algorithmes heuristiques ?

- **BFS** :
  - Idéal pour des graphes **non pondérés** où on cherche le chemin le plus court.
  - Quand on souhaite explorer tous les chemins possibles.

- **DFS** :
  - Utile pour des **parcours complets** (exploration de tous les chemins, détection de cycles).
  - Fonctionne bien pour des graphes peu profonds ou lorsqu'on ne se soucie pas d'optimalité.

- **Algorithmes heuristiques** (comme A\*) :
  - Nécessaires pour des problèmes complexes où l'espace de recherche est vaste (par exemple, les **jeux**, les **labyrinthes**, ou les **systèmes GPS**).
  - Quand une solution rapide **et** optimale est requise.

---

## Résumé

- **Heuristique** : stratégie pour guider la recherche.
- **BFS/DFS** : méthodes systématiques mais sans guidance spécifique.
- **Algorithmes heuristiques** : permettent d’explorer efficacement et de résoudre des problèmes complexes avec potentiellement des solutions optimales.

***

- Si h est admissible alors la solution retourne par l algo A est optimale.
- H admissible donc A devient A*

***
# CHATGPT
# Fonctionnement de l'algorithme A\* dans le cadre heuristique

## 1. Principes fondamentaux

L'algorithme **A\*** (A étoile) est un algorithme de **recherche informée** qui combine la recherche basée sur le coût réel avec une **heuristique** pour trouver le chemin optimal dans un graphe. Il cherche à minimiser la fonction de coût suivante pour chaque nœud \(n\) :

\[
f(n) = g(n) + h(n)
\]

- **\(g(n)\)** : Coût exact depuis le nœud de départ jusqu'au nœud \(n\).
- **\(h(n)\)** : Estimation heuristique du coût pour aller de \(n\) au nœud objectif (destination).
- **\(f(n)\)** : Estimation du coût total du chemin passant par \(n\).

L'algorithme explore en priorité les nœuds ayant la plus petite valeur de \(f(n)\).

---

## 2. Fonctionnement étape par étape

### Étape 1 : Initialisation
- Placez le **nœud de départ** dans une **file de priorité**, qui trie les nœuds en fonction de leur valeur \(f(n)\).
- Initialisez \(g(n)\) pour le nœud de départ à 0 et \(h(n)\) à la valeur heuristique estimée.

### Étape 2 : Parcours des nœuds
1. **Extraire** le nœud \(n\) avec la plus faible valeur \(f(n)\) de la file.
2. Si ce nœud est le **nœud objectif**, le chemin optimal est trouvé.
3. Sinon :
   - Marquez \(n\) comme **exploré** (déplacé dans une file fermée).
   - Pour chaque **voisin** \(v\) de \(n\) :
     - Calculez le **coût temporaire** du chemin \(g(v)\) via \(n\) :
       \[
       g(v) = g(n) + \text{coût(n, v)}
       \]
     - Calculez \(f(v) = g(v) + h(v)\).
     - Si \(v\) n'a pas encore été exploré ou si \(f(v)\) est meilleur que la valeur précédente, mettez à jour \(g(v)\) et ajoutez (ou mettez à jour) \(v\) dans la file ouverte.

### Étape 3 : Répéter
Répétez les étapes jusqu'à atteindre le **nœud objectif** ou que la **file ouverte** soit vide (ce qui signifie qu'il n'y a pas de chemin).

---

## 3. Rôle de l'heuristique (\(h(n)\))

L'heuristique aide à orienter la recherche vers les solutions prometteuses. Elle doit respecter deux propriétés clés :

- **Admissibilité** : \(h(n)\) ne doit jamais **surestimer** le coût réel vers l'objectif.
  - Exemple : La **distance à vol d'oiseau** est une heuristique admissible dans les graphes géographiques.
  
- **Consistance** (ou monotonicité) : Pour tout nœud \(n\) et son successeur \(m\), l'heuristique doit respecter :
  \[
  h(n) \leq \text{coût(n, m)} + h(m)
  \]

Si ces propriétés sont respectées :
- **Optimalité garantie** : A\* trouvera un chemin optimal.
- **Efficacité** : La recherche est plus rapide, car elle évite d'explorer des chemins inutiles.

---

## 4. Comparaison avec BFS

| **Critères**       | **BFS**                           | **A\***                          |
|--------------------|------------------------------------|----------------------------------|
| **Principe**       | Explore tous les nœuds par niveau | Oriente la recherche avec \(h(n)\) |
| **Optimalité**     | Optimal dans graphes non pondérés  | Optimal si \(h(n)\) est admissible |
| **Efficacité**     | Explore tout                     | Explore les chemins prometteurs |
| **Structure de données** | File (queue)              | File de priorité                |

### Points clés :
- **BFS** explore tous les nœuds et garantit le plus court chemin **dans un graphe non pondéré**.
- **A\*** est plus efficace, surtout dans les **grands graphes pondérés**, car il exploite une heuristique.

---

## 5. Avantages de l'algorithme A\*

1. **Optimalité garantie** (si l'heuristique est admissible et consistante).
2. **Flexibilité** : Peut s'adapter à différents types de problèmes avec des heuristiques spécifiques.
3. **Efficacité** : Réduit le nombre de nœuds explorés par rapport à BFS.

---

## 6. Exemple d'application

Dans un **système GPS**, A\* est utilisé pour calculer le chemin optimal :
- **\(g(n)\)** représente la distance déjà parcourue.
- **\(h(n)\)** est une estimation de la distance restante (par exemple, distance euclidienne ou "à vol d'oiseau").
- Le système peut rapidement trouver le chemin le plus court tout en évitant les chemins non prometteurs.

---

## Résumé

- **A\*** est un algorithme de recherche informée qui combine le coût réel \(g(n)\) et une estimation heuristique \(h(n)\).
- Il est plus rapide et plus efficace que BFS dans des problèmes complexes tout en garantissant une solution optimale si l'heuristique est correcte.
- Il est largement utilisé dans des domaines comme les **jeux vidéo**, la **robotique** ou les **systèmes de navigation**.

***


RQ : l heuristique la meuilleur qui a la plus temps vite.

`- The goal of the algorithm A c est la minimisation de cout total estime `

Min {f(n) = g(n) + h(n)}
g : Cout  de chemin allant d un noeud de depart au noeud courant.
h : Cout estime d un noeud au noeud destination.

h* : en connais tout (cout reel)
h : en connais mais n est pas tout

***

## Heuristique consistente.
Une heuristique est consistente si pour chaque noeud n et  successeurs n' generes par une action verifie : 

- H(n) <= H(n') + C(n,a,n')
  C : cout d'action allez de n a n'.
  a : action d un noeud au suivant.


- Optimalite de algo A* : 
Signifie aue trouver toujours le chemin le plus court entre le noeud depart et noeud destination sur la condition d'admissibilite :` h(n) <= h(n)*`

et la consistance aussi il faut de verifie la condition : 
`h(n) <= cout(n,m) + h(m)`

* Si une heuristique est consistante, elle est automatiquement admissible donc A* optimale *

***

## Algorithm Dijkstra

L'algorithme de Dijkstra est une méthode efficace pour trouver le chemin le plus court entre un nœud source et tous les autres nœuds d'un graphe pondéré (où les arêtes ont des poids positifs).
(En passe et si on a trouver encore un entre plus optimale en le remplace en elle et contnue ensuite jusqu au dernier)

`RQ : un noeud explorer si en le remplace de OUVERT a FERME et un noeud tester si elle est dans ouvert`

`RQ : Dans les noeuds si on trouver l etat but dans la file on compte avec les etat tester`

`RQ : Dans cette algorithme en calcule le cout de etat but vers etat initial en suite en Faire le tablaux de OUVERT et FERME et commance par Etat initial.`

***

# Algorithm de SMA*
---
- HI.
- Objectif de trouver un chemin optimal tout en limitant la memoire a une quentite definie.
- Elle fonctione exactement comme A*
- Quand en atteint la limite k noeuds on retire le noeud don t la valeur f(n) est le plus eleve .
- Avant de retirer un noeud en enregistre ses valeur au niveau de son parent
- si on a plusieur noeud de meme valeur et succeptible d etre elimines en retire le plus encien.
- s il y a plusieur noeuds de m valeur susceptibles etre etendu on choisie le plus recent.

  `The form (lettre , paire , f , g , -)
  Exemple 
![image](https://github.com/user-attachments/assets/671cf35f-754a-4f1c-b928-e9b7a238d4ec)

---

---





