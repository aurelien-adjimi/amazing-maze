# amazing-maze

## *Description:*
Pour ce projet je devais créer plusieurs labyrinthes en me servant de différents algorithme mais aussi résoudre ces labyrinthe toujours avec plusieurs algorithmes. 
Ce projet a pour but d'apporter des bases un peu plus poussées sur l'algorithmie. 

## *Langage et bibliothèques utilisés:*
### Langage
- [X] Python
### Bibliothèques
- [X] Time
- [X] Random
- [X] OS
## *Algorithmes utilisés:*
- [X] Recursive Backtracking
- [X] Kruskal
- [X] A*

## *Expilcations:*
Je me suis servi du *recursive backtracking* deux fois dans ce projet: pour la génération et la résolution de labyrinthe.
Le *recursive backtracking* est un algorithme dont le but est d'utiliser la force brute pour trouver toutes les solutions à un problème.  
Il s'agit de constituer progressivement un ensemble de toutes les solutions possibles.
Il trouve une solution en la construisant étape par étape.
Dans tout algorithme de backtracking, l’algorithme recherche un chemin vers une solution réalisable qui inclut certains points de contrôle intermédiaires. Si les points de contrôle ne conduisent pas à une solution viable, le problème peut revenir aux points de contrôle et emprunter un autre chemin pour trouver une solution. 

*L'algorithme de Kruskal*, que j'ai utilisé pour la génération d'un labyrinthe, est un algorithme de recherche d'arbre recouvrant de poids minimum ou arbre couvrant minimum.
L'algorithme consiste à d'abord ranger par ordre de poids croissant ou décroissant les arêtes d'un graphe, puis a retirer une à une les arêtes selon l'ordre choisi et à les ajouter à l'arbre couvrant minimum cherché tant que cet ajout ne fait pas apparaitre un cycle. 

*L'algorithme Astar (A*)* est un algorithme de recherche de chemin dans un graphe entre un nœud initial et un nœud final. Il utilise une évaluation heuristique sur chaque nœud pour estimer le meilleur chemin y passant, et visite ensuite les nœuds par ordre de cette évaluation heuristique. C'est un algorithme simple, ne nécessitant pas de prétraitement, et ne consommant que peu de mémoire.



