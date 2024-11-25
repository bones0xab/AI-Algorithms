# Recherche Operationelle
---

## Graphes et modelisation
--

-Graph non oriente : tt graph dans laquelle on peut faire revenir au sommet precedent
-Graph oriente : tt graph dans laquelle on ne peut pas faire revient au prec.

**Degree d un sommet**
c'est le nombre de sommets voisin par exemple : d[M1] = 3 

**Theoremes :** 
- n = la somme des sommets d'un graph = ordre du graph.
- m = la somme des arretes d'un graph = taille du graph.
- la somme des adjacents entre les sommets : somme(d) = 2*m.
- Un graph est dit simple si il y a au plus un arrete entre sommet.
- Un graph d'ordre n est complet ssi chaque degre de sommet ecrit comme ca : d[M] = n-1, donc le graph est d'ordre n K[n].

**Sous Graph et Graph partiel**
> Pour un graph partiel en ne touch aucune sommet et les ligne sont coupee en extrait le graph donc.
> Pour un sous graph en elemine des sommets donc on le graph.


## Cheminement et connexite.
### Cas Graph non oriente
---
*Chaine : sequence de sommets {x0 x1 ... xk}*
*longeur d une chaine : nombre d arretes dans la chaine*
example : 

![image](https://github.com/user-attachments/assets/04ee608d-bb73-4513-a35a-0c5e88db9bb4)
*Chaine elementaire : tt les sommets sont distancts dans cette chaine*
*Cycle : chaine commmencant et terminant sur un meme sommet.*
*Boucle : cycle de longeur 1*

**Graph connexe**
la connexite c'est lorsque chaque paire de sommets du graph il existe au moins une chaine 


### Cas Graph oriente
---
*Chemin : Sequence de sommets {s0, .... sk}*
*Longeur d'un chemin : Nobre d'arcs dans le chemin*
*Chemin elementaire : tt sommets sont distincts*
*Circuit : chemin commencant et terminant par un meme sommet*
*Boucle : circuit de longeur 1*

$Un graph fortement connexe est dite ssi entre deux sommets x y il exist un chemin de x vers y et y vers x
![image](https://github.com/user-attachments/assets/cf391593-c4c5-4079-b676-db53d2c31820)

examples : 
![image](https://github.com/user-attachments/assets/2349c4d2-0411-4487-83fe-c92b7b178e95)

***

## Arbres et Arboresences
---
### Arbres
on'a ces proprietes pour verifie si on une arbre ou non.
![image](https://github.com/user-attachments/assets/a51c2334-f380-43b9-b0fe-76eaa82bff6a)

**Si l'une do ces proprietes sont verifie donc les autres aussi verifie**

### Foret 
![image](https://github.com/user-attachments/assets/780902af-26d1-4b33-a40d-3d323485500d)

---
```bash
Je vais expliquer les différences clés :

Arbre :


Un graphe connexe sans cycle
Il y a toujours un seul chemin entre deux sommets quelconques
Exemple : un arbre généalogique simple


Forêt :


C'est un ensemble d'arbres séparés (non connectés entre eux)
Chaque composante connexe est un arbre
Exemple : plusieurs arbres généalogiques distincts


Arborescence :


C'est un arbre orienté avec une racine
Tous les chemins partent de la racine vers les autres sommets
Il y a UN SEUL chemin de la racine vers chaque sommet
Exemple : une hiérarchie d'entreprise avec un PDG en haut

La différence principale :

Arbre : non orienté, pas de racine spécifique
Arborescence : orienté, avec une racine définie
Forêt : plusieurs arbres/arborescences séparés
```
---
![image](https://github.com/user-attachments/assets/e3fa3b81-8dfa-45d1-bf8f-44b909d8ae9d)


***

## Representation d'un graph en memoire
---

> Matrice adjacent
- Pour un graph non oriente on'a la symetrie.

  ![image](https://github.com/user-attachments/assets/28ed9115-92c7-4b52-bee5-3f1d3bb50363)
