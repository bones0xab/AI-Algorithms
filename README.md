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


