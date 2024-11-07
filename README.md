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



* Facteur de branchement theorique associe au DFS *

  + L'algo DFS est souhaitable pour les espace de recherche fini et sous cycle + 
  Nombre de noeud Teste = b*0 + b*1 + ... + b*d

  en fair des estimation de la valeur de b* pour trouver une approximiter presque de nombre de noeud.

- Algorithme DFS : 
![image](https://github.com/user-attachments/assets/09ff1aba-02e2-4d90-af97-5056cfe15b5d)

---
