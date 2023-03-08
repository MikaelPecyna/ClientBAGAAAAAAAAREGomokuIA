# Client pour le concours d'IA Gomoku

<!-- vscode-markdown-toc -->
* 1. [Introduction](#Introduction)
* 2. [Deroulement des parties](#Deroulementdesparties)
* 3. [Utilisation](#Utilisation)
* 4. [Les differents fichiers](#Lesdifferentsfichiers)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->



##  1. <a name='Introduction'></a>Introduction 
Dans le cadre de l'UE de [professionalisation](https://formations.univ-poitiers.fr/fr/index/licence-XA/licence-XA/licence-informatique-JB1Y4088/l3-parcours-informatique-JB1Y5EW2/ue5-anglais-et-professionnalisation-s5-JAXSMT81/outils-de-communication-professionnelle-et-preparation-au-stage-francais-et-anglais-s5-JDNL03C5.html) de la 3^(ieme) année de Licence d'informatique a l'Université de Poitiers, nous avons codé tout au long de l'année un [Gomoku](https://fr.wikipedia.org/wiki/Gomoku). L'une des partie de celui-ci était une IA. 

A la fin de l'année, nous avons organisé un "combat" entre toutes les IA. Ceci est le launcher pour les IA en python. 


##  2. <a name='Deroulementdesparties'></a>Deroulementdesparties 

Les parties sont jouées sur un serveur, trois personnes rejoignent une partie, deux joueur et un GameOwner. 

Les joueurs sont les IA qui s'affrontent. 

Le GameOwner est celui créer la partie et verifient que tous les coups proposés par les IA sont legaux.

##  3. <a name='Utilisation'></a>Utilisation 

En tant que player : Parametrer les infos de launcherPlayer puis lancer 

En tant que GameOwner : Parametrer les infos de launcherGameOwner puis lancer 



##  4. <a name='Lesdifferentsfichiers'></a>Lesdifferentsfichiers 

```client.py``` est la classe mère des classes suivantes.

```player.py``` implemente les fonctions neccessaires au player

```gameOwner.py``` implemente les fonctions neccessaires au gameOwner

```launcherPlayer.py``` est le fichier à lancer pour demarrer en tant que player 

```launcherGameOwner.py``` est le fichier à lancer pour demarrer en tant que GameOwner




## Auteur
[@MikaelPecyna](https://github.com/MikaelPecyna) 
> "Le sommeil est une perte de temps" 

