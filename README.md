CONTEXTE GLOBAL DU MÉMOIRE — à lire et garder en mémoire avant toute analyse


Titre projet (provisoire) :
Conception d’un système modulaire de navigation intelligente embarquée  — multi-usage (assistance aux personnes aveugles, télé-assistance, diagnostics, extensions futures).



 le système se dirige de plus en plus ver la modularité et l'utilisation dans plusieus domaine ! le système as donc plusieur module qui seront gerer par une interface qui permet de configurer le système pour une tache bien precise ! c'est a dire que par exemple l'utilisateur peut choisir le mode pour aveugle ! ce qui veut dire que le système seras utiliser comme une assistance pour les aveugles !  ou encore il peut choisir le mode de depanage a distance assister par un expert ! et le système permetras a un expert de se connecter et de voir  ce que l'utilisateur voir pour le guitder a distance ! etc... et chacun des modules peut ajouter des fonctionalités ! (par exemple tu peut ajouter l'option lidar dans l'assistance pour aveugle ! ou soit la reconaissance d'objet pour le depanage a distance ...) et tout le système doit etre personnalisable de A a Z ! le système offre des fonctionalités, des modes, des utlisations ! et beaucoup de parametre de personalisation ! la plateforme permetras aussi d'ajouter des nouoveau module qui sont disponible ! (par exemple module de detection des billet,  de gps, module de de reconnaissance des gestes de la main ) et quand on ajoute une fonctionalité elle peut etre ajouter a un module qui etais deja la ! par exemple ajouter la reconnaissance des gestes de la main pour commander le sytème de navigation pour aveugle ! ou la reconaissance des billet au module pour les aveugles !  tu comprend maintenant la nouvel direction ! donc l'assistance pour aveugles n'est que l'une des utilisations possible ! et il doit y avoir des modules principaux qui eux pouron ajouter des fonctionalité ! mais point important !  tout devras etre utilisable sur le le mème suport ! qui est le casque ( lunnettes) inteligent !  qui auras tout les capteur et composant pour faire fonctioner le système ! par exemple capteru a ultrason, cameras, capteur de luminausité, micro, bafle, flacheur, module de vibration, un MH-Real-Time, un ecrand lcd pour aficher des informations, une led RGB qui affiche une couleur en fonction du mode, un detecteur du niveau de bruit, un joystic, 4 boutons, unnDHT11 pour la temperature, une raspbery pi 4B comme serveau central, un ESP32CAM, une carte arduino UNO, etc ...     le système seras souvent utiliser dans les domaines suivent : assistance pour aveugle, assistance a la maintenance et au depanage ainsi qu'as la formations en milieu industriel ( mine, manipulation de grandes machine), voiture autonome, navigation pour robot, etude et lecture, assistance au travail par IA, formation, explorations d'un environement a distance.  tout ca devras fonctioner sur windows mais etre compatible avec les autres sysème !  chacun des module auras ces dependences a instaler, ca documentation, sont cros platforme, et les composant d'ont il as besoin.                                                ce que tuu doit faire : analyse bien cette structure et fait des recherche pour mieux comprendre l'utilité du système!   et les utilisation possible, les fonctionalités et sytèmes déja existant ! en suite donne moi une structure de 4 grand titres pour faire la revue de literature avec chacun plus de 5 sous titres de recherche bien sible et ou trouver ces articles ! et suite fait moi une structure complet du projet entier et comment les fonctionalités serons structurer !   puis fait moi la structure des composant et comment ils seront implementer !  en suite fait moi une structure de comment les couches de fonctionalité et des options serons etablis pour la partie de configuration. puis dit moi les avantages, incovenient, pointn fort, point, faibles, et ce qui faudrais revoir après avoir fait l'etude.  puis fait moi plusieurs recommendation d'ammelioration, de simplification, de reformulation, de fonctionalités avenir,. puis fait une critique productive pour analyser le potentiel economique et productif de ce sytème et dans quel domaine il serait le plus utiliser et utile !  pour ca soit soit critique et proffesionel comme un potentiel investisseur !    


Objectif général :
Développer une plateforme matérielle et logicielle modulaire, embarquée sur casque intelligentes, capable d’offrir plusieurs « modes » d’utilisation (ex : assistance pour aveugles, assistance à distance par un expert, diagnostic, lecture de billets), pilotés par une interface de configuration cross-platform. Le système doit être personnalisable (profils utilisateur), extensible (ajout simple de modules logiciels et matériels), et fonctionner prioritairement en quasi-temps réel sur support embarqué (Raspberry Pi 4B / ESP32 / Arduino / MCU TinyML selon le module).

Contraintes et exigences clés :
- **Matériel** : lunettes intelligentes comme support principal + capteurs divers (caméras RGB, ESP32CAM, ultrason, IMU, DHT11, micro, haut-parleur, vibreur, LED RGB, écran LCD optionnel, éventuel LiDAR / module depth) ; Raspberry Pi 4B comme serveur central embarqué ou edge-hub ; ESP32 / Arduino pour modules capteurs.
- **Performance** : perception et guidage quasi-temps réel (latence acceptable < 200–500 ms selon la tâche), consommation énergétique optimisée.
- **Architecture** : modules logiciels indépendants (plugins) orchestrés par un orchestrateur local ; communication interne via bus léger (MQTT / Mosquitto ou équivalent) ; possibilité d’extension via plug-and-play hardware.
- **Fonctionnalités principales** : détection d’obstacles, segmentation/segmentation temporelle, reconnaissance d’objets, OCR, reconnaissance de gestes, navigation guidée, interface vocale IA, mode expert distant (streaming vidéo + contrôle/annotation), profils utilisateurs, mise à jour OTA.
- **Sécurité & confidentialité** : chiffrement des flux sensibles (ex. vidéo), consentement explicite, minimisation de données, archivage structuré sécurisé.
- **UX / Acceptation** : charge cognitive minimale, modes d’interaction non intrusifs (vocal, haptique), personnalisation et contrôles d’accessibilité.

Direction générale du mémoire :
- **Apport scientifique** : proposer une architecture modulaire et portable, combinant perception embarquée (TinyML, event cameras en option) et orchestration logicielle, pour adapter des techniques de robotique/navigation à des lunettes assistives centrées utilisateur.
- **Contribution technique** : définition d’un référentiel (architecture hardware + software), pipelines optimisés pour TinyML, stratégie OTA, scénarios d’utilisation (use cases), protocole d’évaluation (tests utilisateurs, métriques de latence/consommation/robustesse).
- **Limites acceptées** : le mémoire proposera une preuve de concept et prototypes (soft+hard). Il n’ambitionne pas la commercialisation immédiate ni le développement d’un produit industriel finalisé. Les modules gourmands (p.ex. grands LLMs, volumetric VLN complets) seront évalués comme options *offloaded* (cloud) mais le focus restera sur capacités embarquées.

Points forts du projet :
- approche **modulaire** et multi-usage rare dans la littérature ;
- combinaison de technologies émergentes (TinyML, event cameras, haptique, LLM pour haut-niveau si nécessaire) ;
- forte orientation vers l’utilisateur final (profiles, UX, modes).

Faiblesses / risques :
- contrainte énergétique et de calcul sur lunettes ;
- complexité d’intégration multi-capteurs + latence ;
- validation utilisateur longue à déployer (nécessite éthique / tests réels) ;
- dépendance potentielle à des composants coûteux (LiDAR, event camera) si mal choisis.


Quelques affirmation : 

1, oui via un bus de message, oui les module peuvent etre dependent l'un de l'autre, pour gerer les resources il y as un système de priorité   2,  l'interface seras une app web et mobile, oui il y as un mode expert, via boutons physiques, interface, reconnaissance vocale  3, aussi les parametres dans les modules, oui  des profils utilisateurs avec configurations sauvegardées   4,  fait la repartition en fonction de la puissance, oui L'Arduino gère les capteurs bas niveau,  oui L'ESP32CAM est-il dédié uniquement à la vidéo streaming pour le dépannage à distance  5, 2 module max en simultané, oui il Faut un système de priorité  6, oui j'aurais un SDK/API pour que d'autres développeurs créent des modules, (python,C++), par moniteur serie  7, non, par bouton ou commende, 8, propose moi comment la securiser, par des autorisations   9, (LED RGB, feedback sonore/vibration), non juste une documentatio  10, oui une boutique, mise a jour manuel, propose mooi  11, la navigation, il faut tout recomencer

Contraintes et exigences clés :
- **Matériel** : lunettes intelligentes comme support principal + capteurs divers (caméras RGB, ESP32CAM, ultrason, IMU, DHT11, micro, haut-parleur, vibreur, LED RGB, écran LCD optionnel, éventuel LiDAR / module depth) ; Raspberry Pi 4B comme serveur central embarqué ou edge-hub ; ESP32 / Arduino pour modules capteurs.
- **Performance** : perception et guidage quasi-temps réel (latence acceptable < 200–500 ms selon la tâche), consommation énergétique optimisée.
- **Architecture** : modules logiciels indépendants (plugins) orchestrés par un orchestrateur local ; communication interne via bus léger (MQTT / Mosquitto ou équivalent) ; possibilité d’extension via plug-and-play hardware.
- **Fonctionnalités principales** : détection d’obstacles, segmentation/segmentation temporelle, reconnaissance d’objets, OCR, reconnaissance de gestes, navigation guidée, interface vocale IA, mode expert distant (streaming vidéo + contrôle/annotation), profils utilisateurs, mise à jour OTA.
- **Sécurité & confidentialité** : chiffrement des flux sensibles (ex. vidéo), consentement explicite, minimisation de données, archivage structuré sécurisé.
- **UX / Acceptation** : charge cognitive minimale, modes d’interaction non intrusifs (vocal, haptique), personnalisation et contrôles d’accessibilité.

Direction générale du mémoire :
- **Apport scientifique** : proposer une architecture modulaire et portable, combinant perception embarquée (TinyML, event cameras en option) et orchestration logicielle, pour adapter des techniques de robotique/navigation à des lunettes assistives centrées utilisateur.
- **Contribution technique** : définition d’un référentiel (architecture hardware + software), pipelines optimisés pour TinyML, stratégie OTA, scénarios d’utilisation (use cases), protocole d’évaluation (tests utilisateurs, métriques de latence/consommation/robustesse).
- **Limites acceptées** : le mémoire proposera une preuve de concept et prototypes (soft+hard). Il n’ambitionne pas la commercialisation immédiate ni le développement d’un produit industriel finalisé. Les modules gourmands (p.ex. grands LLMs, volumetric VLN complets) seront évalués comme options *offloaded* (cloud) mais le focus restera sur capacités embarquées.

Points forts du projet :
- approche **modulaire** et multi-usage rare dans la littérature ;
- combinaison de technologies émergentes (TinyML, event cameras, haptique, LLM pour haut-niveau si nécessaire) ;
- forte orientation vers l’utilisateur final (profiles, UX, modes).

Faiblesses / risques :
- contrainte énergétique et de calcul sur lunettes ;
- complexité d’intégration multi-capteurs + latence ;
- validation utilisateur longue à déployer (nécessite éthique / tests réels) ;
- dépendance potentielle à des composants coûteux (LiDAR, event camera) si mal choisis.

Attentes pour la revue de littérature  :
- Sois exhaustif, critique et comparatif. Utilise **uniquement** les documents fournis (PDFs / liens importés).  
- Pour chaque article : fournir 8 rubriques analytiques (présentation, méthodologie, apports, limites, réutilisabilité, technologies, gaps, recommandations pour mon projet).  
- Rédiger en style académique, formel, référencé. Donner des extraits cités (page/paragraph) lorsqu’ils sont pertinents.  
- Produire un tableau synthétique comparant tous les articles (colonnes : année, approche matérielle, IA embarquée, capteurs, feedback, validation utilisateur, modularité, pertinence pour my-project).
- Fournir une conclusion de la partie A concluant sur les gaps et positionnant clairement la contribution du mémoire.

NB : si une information n’apparaît pas dans les documents fournis, indiquer explicitement “non trouvé dans les sources”.
PROMPT : REVUE DE LITTÉRATURE — PARTIE A (Smart-glasses & assistive systems)

Instructions globales :
Tu es un chercheur/assistant de recherche. Utilise **uniquement** les documents (PDFs, URLs) importés dans ce notebook — ne cherche pas ailleurs. Respecte la structure, les citations et indique les pages pour tous les extraits cités.

Objectif :Rédige une section prête à être insérée dans un mémoire universitaire (niveau master/doctorat).

Liste des sources (A1 → F50) — Analyse ces 50 documents en priorité **(utilise exactement ces documents)** :
d'abord je te donne tout les articles de A a F ! les voici :    Cette liste correspond uniquement aux articles que nous avons validés ensemble


Tâches à accomplir (ordre impératif) :

1. **Plan détaillé (H2/H3)** de la Partie A a F : produis d’abord un plan hiérarchisé (champ lexique, sections et sous-sections), puis attends confirmation avant de rédiger chaque section complète. Le plan doit inclure : introduction, sous-sections par thème (matériel, perception, interfaces, validation utilisateur, modularité), synthèse comparative, gaps, et conclusion.

2. **Analyse article par article** (pour A1 → F50) : pour chaque article, rédige les 8 rubriques suivantes, chacune sous son propre sous-titre :
   1. Présentation générale (problématique, domaine, motivation)
   2. Approche méthodologique (architecture, algorithmes, capteurs, datasets)
   3. Apports et innovations (résultats quantitatifs si disponibles)
   4. Limites et faiblesses (techniques, UX, déploiement)
   5. Pertinence pour le mémoire (ce que l’on peut réutiliser)
   6. Technologies / implémentations réutilisables (code, modèles, pipelines)
   7. Gaps ouverts (ce que l’article ne couvre pas)
   8. Recommandations concrètes pour le projet (comment exploiter/éviter)

   - Pour chaque rubrique, cite précisément la source (nom du document + page/section).
   - Longueur cible : ~600–1000 mots par article en mode “




# II. REDÉFINITION COMPLÈTE DE L’ÉTAT DE L’ART 

## Positionnement global

L’état de l’art n’est **plus centré sur un seul domaine (aveugles)**, mais sur :

> **les systèmes intelligents embarqués capables de percevoir, d’interpréter et d’assister un utilisateur via une architecture modulaire et reconfigurable, adaptée à plusieurs domaines d’usage.**

---

## Axe 1 – Perception intelligente embarquée

Tu analyses ici :

* vision par ordinateur embarquée
* perception de distance (ultrason, LiDAR, profondeur)
* perception audio et environnementale
* fusion multi-capteurs
* IA embarquée à ressources contraintes

👉 Objectif : montrer que **les briques existent**, mais sont souvent **isolées et spécialisées**.

---

## Axe 2 – Assistance intelligente et interaction humaine

Tu montres que :

* les systèmes d’assistance existent (aveugles, téléassistance, guidage)
* mais sont souvent **monofonctionnels**
* peu personnalisables
* rarement extensibles
* rarement réutilisables hors de leur domaine initial

👉 Tu identifies un **manque de généralité et de flexibilité**.

---

## Axe 3 – Architectures modulaires et frameworks génériques

C’est **l’axe différenciant** de ton mémoire.

Tu montres que :

* la modularité est étudiée séparément (robotique, IoT, software)
* peu de travaux combinent :

  * modularité
  * IA embarquée
  * personnalisation totale
  * support unique
  * multi-domaines

👉 Tu mets en évidence un **vide scientifique clair**.

---

## Synthèse critique (clé pour le jury)

Tu conclus que :

* Les systèmes existants sont :

  * performants mais rigides
  * spécialisés mais non réutilisables
  * intelligents mais peu configurables

* Il manque :

  * un **framework unifié**
  * embarqué
  * modulaire
  * extensible
  * centré utilisateur
  * applicable à plusieurs usages

👉 **C’est exactement ce que ton travail propose.**

---

## Transition parfaite vers la suite du mémoire

Tu peux conclure l’état de l’art par une phrase de ce type (que tu pourras reprendre) :

> Cette analyse met en évidence l’absence d’une plateforme générique capable d’orchestrer dynamiquement des modules de perception et d’assistance sur un support embarqué unique, tout en s’adaptant à des usages multi-domaines via une personnalisation fine. Le framework proposé dans ce mémoire vise à combler ce manque.







# I. TABLE DES MATIÈRES 

Cette table des matières est pensée pour :

* un **mémoire académique solide**
* un **framework générique**
* une **démonstration claire de modularité et de réutilisabilité**
* un **équilibre architecture ↔ IA**
* un **support unique (casque a fabriquer! comme casque vr intelligentes mais sens ecrand !)**

---

## **INTRODUCTION GÉNÉRALE**

* Contexte et motivation
* Problématique générale
* Objectifs scientifiques et techniques
* Contributions du travail
* Organisation du mémoire

---

## **CHAPITRE 1 – ÉTAT DE L’ART DES SYSTÈMES DE PERCEPTION, DE NAVIGATION ET D’ASSISTANCE INTELLIGENTE**

### **1.1 Navigation autonome et perception de l’environnement**

* 1.1.1 Fondements de la perception pour la navigation autonome
* 1.1.2 Capteurs et modalités perceptives (vision, distance, audio, fusion)
* 1.1.3 Approches basées sur l’intelligence artificielle embarquée
* 1.1.4 Couplage perception–décision–action
* 1.1.5 Limites des approches existantes en contexte embarqué

### **1.2 Systèmes d’assistance intelligente centrés sur l’humain**

* 1.2.1 Assistance à la mobilité pour personnes aveugles et malvoyantes
* 1.2.2 Assistance guidée à distance et collaboration expert–utilisateur
* 1.2.3 Interfaces multimodales et feedback adaptatif
* 1.2.4 Personnalisation et profils utilisateurs
* 1.2.5 Contraintes ergonomiques et cognitives

### **1.3 Architectures modulaires et systèmes reconfigurables**

* 1.3.1 Modularité logicielle dans les systèmes embarqués
* 1.3.2 Orchestration dynamique de fonctionnalités
* 1.3.3 Frameworks génériques et réutilisabilité inter-domaines
* 1.3.4 Gestion des ressources et priorisation des modules
* 1.3.5 Limites des architectures existantes

### **1.4 Synthèse de l’état de l’art et positionnement du travail**

* 1.4.1 Comparaison transversale des approches étudiées
* 1.4.2 Lacunes identifiées
* 1.4.3 Justification de l’approche proposée

---

## **CHAPITRE 2 – SPÉCIFICATION DU FRAMEWORK MODULAIRE PROPOSÉ**

* 2.1 Vision globale du système
* 2.2 Hypothèses et contraintes
* 2.3 Définition des concepts clés (module, mode, profil)
* 2.4 Cas d’usage cibles multi-domaines
* 2.5 Exigences fonctionnelles et non fonctionnelles

---

## **CHAPITRE 3 – ARCHITECTURE DU SYSTÈME**

* 3.1 Architecture matérielle des lunettes intelligentes
* 3.2 Architecture logicielle en couches
* 3.3 Gestionnaire de modules
* 3.4 Orchestrateur de modes
* 3.5 Gestion de la personnalisation et des profils
* 3.6 Sécurité, robustesse et tolérance aux pannes

---

## **CHAPITRE 4 – MODULES DE PERCEPTION ET D’INTELLIGENCE EMBARQUÉE**

* 4.1 Modules de perception visuelle
* 4.2 Modules de perception de distance et environnement
* 4.3 Modules audio et interaction
* 4.4 Modules d’intelligence artificielle
* 4.5 Fusion de données et synchronisation
* 4.6 Optimisation pour l’embarqué

---

## **CHAPITRE 5 – MODES D’UTILISATION ET PERSONNALISATION**

* 5.1 Mode assistance à la navigation pour personnes aveugles
* 5.2 Mode assistance à distance par expert
* 5.3 Autres modes extensibles
* 5.4 Configuration dynamique des modes
* 5.5 Personnalisation avancée du système

---

## **CHAPITRE 6 – IMPLÉMENTATION ET VALIDATION**

* 6.1 Environnement matériel et logiciel
* 6.2 Implémentation du framework
* 6.3 Scénarios d’expérimentation
* 6.4 Résultats et analyses
* 6.5 Discussion

---

## **CONCLUSION GÉNÉRALE ET PERSPECTIVES**

* Bilan des contributions
* Limites du travail
* Perspectives d’évolution (nouveaux modules, nouveaux domaines)


   

Attentes pour la revue de littérature  :
- Sois exhaustif, critique et comparatif. Utilise **uniquement** les documents fournis (PDFs / liens importés).  
- Pour chaque article : fournir 8 rubriques analytiques (présentation, méthodologie, apports, limites, réutilisabilité, technologies, gaps, recommandations pour mon projet).  
- Rédiger en style académique, formel, référencé. Donner des extraits cités (page/paragraph) lorsqu’ils sont pertinents.  
- Produire un tableau synthétique comparant tous les articles (colonnes : année, approche matérielle, IA embarquée, capteurs, feedback, validation utilisateur, modularité, pertinence pour my-project).
- Fournir une conclusion de la partie A concluant sur les gaps et positionnant clairement la contribution du mémoire.

NB : si une information n’apparaît pas dans les documents fournis, indiquer explicitement “non trouvé dans les sources”.
PROMPT : REVUE DE LITTÉRATURE — PARTIE A (Smart-glasses & assistive systems)

Instructions globales :
Tu es un chercheur/assistant de recherche. Utilise **uniquement** les documents (PDFs, URLs) importés dans ce notebook — ne cherche pas ailleurs. Respecte la structure, les citations et indique les pages pour tous les extraits cités.

Objectif :Rédige une section prête à être insérée dans un mémoire universitaire (niveau master/doctorat).

Liste des sources (A1 → F50) — Analyse ces 50 documents en priorité **(utilise exactement ces documents)** :
d'abord je te donne tout les articles de A a F ! les voici :    Cette liste correspond uniquement aux articles que nous avons validés ensemble


🔹 A — Smart-glasses, wearables et systèmes assistifs pour déficients visuels

**A1.** YOLOv8-Based XR Smart Glasses Mobility Assistive System
🔗 [https://www.mdpi.com/2079-9292/14/3/425](https://www.mdpi.com/2079-9292/14/3/425)

**A2.** LLM-Glasses: GenAI-driven Glasses with Haptic Feedback for Navigation of Visually Impaired People
🔗 [https://arxiv.org/abs/2503.16475](https://arxiv.org/abs/2503.16475)

**A3.** Ultra-Efficient On-Device Object Detection on AI-Integrated Smart Glasses with TinyissimoYOLO
🔗 [https://arxiv.org/abs/2311.01057](https://arxiv.org/abs/2311.01057)

**A4.** A wearable obstacle avoidance device for visually impaired individuals with cross-modal learning
🔗 [https://www.nature.com/articles/s41467-025-58085-x](https://www.nature.com/articles/s41467-025-58085-x)

**A5.** Smart Assistive Navigation System for Visually Impaired People
🔗 [https://www.researchgate.net/publication/372645921](https://www.researchgate.net/publication/372645921)

**A6.** Making Smartglasses Accessible: Perspectives and Design Considerations
🔗 [https://www.nature.com/articles/s41598-025-22253-2](https://www.nature.com/articles/s41598-025-22253-2)

**A7.** Advancements in Smart Wearable Mobility Aids for the Visually Impaired: A Bibliometric Review
🔗 [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11679352/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11679352/)

**A8.** Design and Development of Assistive Smart Glasses for Visually Impaired People
🔗 [https://ieeexplore.ieee.org/document/9262184](https://ieeexplore.ieee.org/document/9262184)

**A9.** Empowering Vision Using AI-Enabled Smart Glasses: A Wearable Solution for Enhanced Navigation
🔗 [https://www.researchgate.net/publication/377941882](https://www.researchgate.net/publication/377941882)

**A10.** Smart Glasses for CVI: Co-Designing Extended Reality for Cerebral Visual Impairment
🔗 [https://arxiv.org/abs/2506.19210](https://arxiv.org/abs/2506.19210)

---

## 🔹 B — Perception embarquée, TinyML et IA on-device

**B11.** TinyissimoYOLO: A Quantized, Low-Memory Footprint TinyML Object Detection Network
🔗 [https://arxiv.org/abs/2306.00001](https://arxiv.org/abs/2306.00001)

**B12.** TActiLE: Tiny Active Learning for Wearable Devices
🔗 [https://arxiv.org/abs/2502.08761](https://arxiv.org/abs/2502.08761)

**B13.** Deploying Optimized Deep Vision Models for Eyeglasses on Low-Power Edge Devices
🔗 [https://www.mdpi.com/2079-9292/14/2/301](https://www.mdpi.com/2079-9292/14/2/301)

**B14.** Edge AI and TinyML: A Systematic Review
🔗 [https://www.nature.com/articles/s41598-025-88921-4](https://www.nature.com/articles/s41598-025-88921-4)

**B15.** Ultra-Efficient On-Device Object Detection on AI-Integrated Smart Glasses
🔗 [https://dl.acm.org/doi/10.1145/3629539.3656461](https://dl.acm.org/doi/10.1145/3629539.3656461)

**B16.** On-Device Learning and Personalization for TinyML Wearables
🔗 [https://arxiv.org/abs/2409.11821](https://arxiv.org/abs/2409.11821)

**B17.** Energy-Efficient Person Detection Using TinyML
🔗 [https://www.iaeng.org/publication/WCE2024/WCE2024_pp107-112.pdf](https://www.iaeng.org/publication/WCE2024/WCE2024_pp107-112.pdf)

**B18.** Designing Object Detection Models for TinyML
🔗 [https://dl.acm.org/doi/10.1145/3606841.3617502](https://dl.acm.org/doi/10.1145/3606841.3617502)

**B19.** Ultra-Efficient Vision Pipelines for Wearable Devices
🔗 [https://www.prophesee.ai/resources](https://www.prophesee.ai/resources)

**B20.** Active Learning Techniques for On-Device Embedded AI
🔗 [https://arxiv.org/abs/2410.04288](https://arxiv.org/abs/2410.04288)

---

## 🔹 C — Neuromorphic vision, event cameras et perception basse consommation

**C21.** Neuromorphic Perception and Navigation for Mobile Robots: A Review
🔗 [https://dl.acm.org/doi/10.1145/3656469](https://dl.acm.org/doi/10.1145/3656469)

**C22.** Recent Event Camera Innovations: A Survey
🔗 [https://arxiv.org/abs/2408.13627](https://arxiv.org/abs/2408.13627)

**C23.** Event-Based Vision: A Survey
🔗 [https://arxiv.org/abs/1904.08405](https://arxiv.org/abs/1904.08405)

**C24.** Application of Event Cameras and Neuromorphic Computing to VSLAM: A Survey
🔗 [https://www.researchgate.net/publication/377112948](https://www.researchgate.net/publication/377112948)

**C25.** Event-Based Eye Tracking: AIS 2024 Challenge Survey
🔗 [https://openaccess.thecvf.com/content/CVPR2024W/AIS/html/Wang_Event-Based_Eye_Tracking_AIS_2024_Challenge_CVPRW_2024_paper.html](https://openaccess.thecvf.com/content/CVPR2024W/AIS/html/Wang_Event-Based_Eye_Tracking_AIS_2024_Challenge_CVPRW_2024_paper.html)

**C26.** Event-Based Solutions for Human-Centered Applications
🔗 [https://www.frontiersin.org/articles/10.3389/frobt.2025.1298472](https://www.frontiersin.org/articles/10.3389/frobt.2025.1298472)

**C27.** Event Cameras: Datasets, Tools and Benchmarks
🔗 [https://rpg.ifi.uzh.ch](https://rpg.ifi.uzh.ch)

---

## 🔹 D — Navigation autonome, ObjectNav, VLN et SLAM

**D30.** Object Goal Navigation Using Goal-Oriented Semantic Exploration
🔗 [https://arxiv.org/abs/2007.00643](https://arxiv.org/abs/2007.00643)

**D31.** Training-Free Embodied Object Goal Navigation with Semantic Frontiers
🔗 [https://roboticsproceedings.org/rss19/p051.pdf](https://roboticsproceedings.org/rss19/p051.pdf)

**D32.** Auxiliary Tasks and Exploration Enable ObjectGoal Navigation
🔗 [https://openaccess.thecvf.com/content/ICCV2021/html/Ye_Auxiliary_Tasks_and_Exploration_Enable_ObjectGoal_Navigation_ICCV_2021_paper.html](https://openaccess.thecvf.com/content/ICCV2021/html/Ye_Auxiliary_Tasks_and_Exploration_Enable_ObjectGoal_Navigation_ICCV_2021_paper.html)

**D33.** Vision-Based Navigation and Perception for Autonomous Systems: A Review
🔗 [https://www.mdpi.com/2076-3417/15/4/1897](https://www.mdpi.com/2076-3417/15/4/1897)

**D34.** A Survey on Vision-Language Navigation
🔗 [https://arxiv.org/abs/2403.04751](https://arxiv.org/abs/2403.04751)

**D35.** Volumetric Environment Representation for Vision-Language Navigation
🔗 [https://openaccess.thecvf.com/content/CVPR2024/html/Liu_Volumetric_Environment_Representation_for_Vision-Language_Navigation_CVPR_2024_paper.html](https://openaccess.thecvf.com/content/CVPR2024/html/Liu_Volumetric_Environment_Representation_for_Vision-Language_Navigation_CVPR_2024_paper.html)

**D36.** Towards Long-Horizon Vision-Language Navigation
🔗 [https://arxiv.org/abs/2501.01864](https://arxiv.org/abs/2501.01864)

**D37.** Event-Based VSLAM: A Survey
🔗 [https://www.researchgate.net/publication/376982104](https://www.researchgate.net/publication/376982104)

**D38.** Semantic Frontier-Based Object Navigation
🔗 [https://research-collection.ethz.ch/handle/20.500.11850/632181](https://research-collection.ethz.ch/handle/20.500.11850/632181)

---

## 🔹 E — Fusion multimodale et perception conjointe

**E39.** Joint Perception and Prediction for Autonomous Driving: A Survey
🔗 [https://arxiv.org/abs/2412.14088](https://arxiv.org/abs/2412.14088)

**E40.** A Review of Multi-Sensor Fusion in Autonomous Driving
🔗 [https://www.mdpi.com/1424-8220/25/2/455](https://www.mdpi.com/1424-8220/25/2/455)

**E41.** A Comprehensive Survey on Deep Learning Multi-Modal Fusion
🔗 [https://cdn.techscience.cn/uploads/attached/file/20240507/20240507171202_19143.pdf](https://cdn.techscience.cn/uploads/attached/file/20240507/20240507171202_19143.pdf)

**E42.** Multimodal Perception-Driven Decision-Making for Human–Robot Systems
🔗 [https://www.frontiersin.org/articles/10.3389/frobt.2025.1305521](https://www.frontiersin.org/articles/10.3389/frobt.2025.1305521)

**E43.** Integrating Multi-Modal Sensors: A Review of Fusion Strategies
🔗 [https://arxiv.org/abs/2502.09114](https://arxiv.org/abs/2502.09114)

**E44.** Vision-Language-Action Models: A Survey
🔗 [https://www.sciencedirect.com/science/article/pii/S1566253525000124](https://www.sciencedirect.com/science/article/pii/S1566253525000124)

---

## 🔹 F — Architectures modulaires, frameworks et acceptabilité

**F45.** A Distributed Wearable Computing Framework for Human-Centric Sensing
🔗 [https://www.mdpi.com/2079-9292/14/7/1312](https://www.mdpi.com/2079-9292/14/7/1312)

**F46.** A Codesign Framework for Next-Generation Wearable Computing Systems
🔗 [https://www.researchgate.net/publication/379221904](https://www.researchgate.net/publication/379221904)

**F47.** Augmented Reality Smart Glasses: Acceptance and UX Review
🔗 [https://www.sciencedirect.com/science/article/pii/S1071581923000412](https://www.sciencedirect.com/science/article/pii/S1071581923000412)

**F48.** Development of Affordable Smart Glasses for Individuals with Visual Impairments
🔗 [https://rsisinternational.org/journals/ijrsi/articles/development-of-affordable-smart-glasses](https://rsisinternational.org/journals/ijrsi/articles/development-of-affordable-smart-glasses)

**F49.** Frameworks for Modular Hardware Integration in Wearables
🔗 [https://link.springer.com/chapter/10.1007/978-3-031-91989-3_5](https://link.springer.com/chapter/10.1007/978-3-031-91989-3_5)

**F50.** Survey of Assistive Technologies for the Visually Impaired
🔗 [https://dl.acm.org/doi/10.1145/3668395](https://dl.acm.org/doi/10.1145/3668395)







# 1) Plan détaillé (H2/H3) — séparé A, B, C, D, E, F (avec “protocoles & métriques” dans chaque partie)

## Introduction générale (Partie A→F)
### Motivation, contraintes et angle scientifique
### Hypothèses structurantes du mémoire (embarquée, latence, modularité, UX)
### Méthode de revue (axes d’analyse + critères comparatifs)
### Vue d’ensemble des parties A–F

---

## A — Smart-glasses & systèmes assistifs (A1–A10)
### A.1 Typologie des systèmes assistifs sur lunettes
#### A.1.1 Navigation micro (obstacles) vs macro (itinéraire)
#### A.1.2 Assistance contextuelle (OCR, objets, personnes) vs XR/AR
### A.2 Architectures typiques (on-device, edge-hub, cloud-offload)
#### A.2.1 Chaîne perception → décision → feedback
#### A.2.2 Gestion des modes et profils (personnalisation)
### A.3 Capteurs & matériels (lunettes, smartphone compagnon, modules)
#### A.3.1 RGB/Depth/IMU, audio, haptique
#### A.3.2 Contraintes de poids, autonomie, thermique
### A.4 Interfaces & feedback (UX)
#### A.4.1 Audio (guidage, surcharge, bruit)
#### A.4.2 Haptique (codage direction/distance, apprentissage)
#### A.4.3 XR/AR (affichage, accessibilité, acceptabilité sociale)
### A.5 **Protocoles d’évaluation & métriques (A)**
#### A.5.1 Latence E2E, FPS, précision détection, autonomie
#### A.5.2 Études utilisateurs : taux de collision/near-miss, temps de tâche, charge cognitive, SUS/UEQ (si présents)
### A.6 Synthèse A (leçons pour ton système modulaire)

---

## B — IA embarquée, TinyML, on-device learning (B11–B20)
### B.1 Contraintes compute/énergie/mémoire (MCU vs SBC)
### B.2 Détection embarquée ultra-efficiente (quantif, pruning, archis tiny)
### B.3 Déploiement & optimisation (runtime, scheduling, accélérateurs)
### B.4 Personnalisation & apprentissage embarqué
### B.5 **Protocoles d’évaluation & métriques (B)**
#### B.5.1 mAP/IoU, latence par stage, conso par inférence, mémoire
#### B.5.2 Reproductibilité (benchmarks, open-source, tests)
### B.6 Synthèse B (règles d’ingénierie IA pour l’orchestrateur)

---

## C — Vision neuromorphique & event cameras (C21–C27)
### C.1 Principes, promesses, limites pour lunettes
### C.2 Capteurs, datasets, outils (OpenEB, benchmarks)
### C.3 Algorithmes clés (reconstruction, détection, tracking, SNN)
### C.4 Intégration modulaire (option event + fusion RGB/IMU)
### C.5 **Protocoles d’évaluation & métriques (C)**
#### C.5.1 Latence micro-secondes → décision, débit d’événements, énergie
#### C.5.2 Robustesse (HDR, motion blur, low-light) vs complexité dev
### C.6 Synthèse C (event camera comme extension future “plug-in”)

---

## D — Navigation (ObjectNav, VLN, SLAM) (D30–D38)
### D.1 Transfert robot → lunettes (ce qui se transfère / ne se transfère pas)
### D.2 ObjectNav : exploration sémantique, frontiers, cartes
### D.3 VLN : langage + perception + mémoire (volumetric, long-horizon)
### D.4 SLAM/VSLAM (incl. pont vers event-based)
### D.5 **Protocoles d’évaluation & métriques (D)**
#### D.5.1 SPL, success rate, collisions, temps, généralisation
#### D.5.2 Coût compute vs gain (embarqué/offload)
### D.6 Synthèse D (stratégie multi-niveaux : réactif→sémantique→offload)

---

## E — Fusion multimodale & VLA (E39–E44)
### E.1 Taxonomie fusion (early/late/hybride, deep/proba)
### E.2 Robustesse multi-capteurs (défaillances, alignement, calibration)
### E.3 Joint perception & prediction (leçons transférables)
### E.4 Vision-Language-Action : potentiel et limites embarquées
### E.5 **Protocoles d’évaluation & métriques (E)**
#### E.5.1 Gain vs mono-modal (ablation), incertitude, safety metrics
### E.6 Synthèse E (fusion légère + bus de messages + fallback)

---

## F — Architectures modulaires, frameworks, acceptabilité (F45–F50)
### F.1 Frameworks wearables distribués (lunettes + modules)
### F.2 Co-design HW/SW (perf/énergie)
### F.3 Modularité matérielle (plug-and-play, abstraction, versioning)
### F.4 Acceptabilité & UX (stigma, esthétique, confidentialité)
### F.5 Sécurité, gouvernance des données, OTA
### F.6 **Protocoles d’évaluation & métriques (F)**
#### F.6.1 Adoption long-terme, acceptabilité, privacy-by-design
#### F.6.2 Maintenabilité : tests, compatibilité modules, OTA
### F.7 Synthèse F (spécification architecturale cible du mémoire)

---

## Conclusion transversale (A→F)
### Gaps majeurs (techniques, UX, sécurité, validation)
### Positionnement de ta contribution (architecture modulaire + orchestrateur + profils + quasi temps réel)
### Recommandations de design “prêtes à implémenter”
### Ouvertures (event camera, LiDAR, VLA/VLN offload, standardisation)

---

# 2) Mini-analyses ultra-condensées (≈100–150 mots) — A1 → F50
*(Quand je n’ai pas pu récupérer le contenu : je le dis explicitement. Quand le lien semble hors-sujet : je le dis explicitement.)*

## A — Smart-glasses & assistive systems

**A1. YOLOv8-Based XR Smart Glasses Mobility Assistive System**  
Système d’assistance à la mobilité basé sur lunettes XR (Xreal Light) + smartphone Android, exploitant plusieurs modèles YOLOv8n (cheminement/sécurité, infrastructures transport, obstacles) et une stratégie de scheduling (exécutions séquentielles pour répartir la charge). L’article insiste sur la contrainte de latence et propose des seuils de performance (E2E, capture→inférence→feedback) et une gestion du feedback audio/visuel pour limiter la surcharge. Très pertinent pour ton mémoire : illustre un design “lunettes + compute compagnon”, un pipeline de conversion (YOLO→ONNX→Unity), et une logique multi-modèles orchestrée temporellement. Limite typique : dépendance smartphone, scope plutôt “application monolithique” que plateforme modulaire. [Source](https://www.mdpi.com/2079-9292/14/3/425)

**A2. LLM-Glasses: GenAI-driven Glasses with Haptic Feedback for Navigation**  
Propose une architecture hybride : détection (YOLO-World) + raisonnement (GPT-4o) + feedback haptique (patterns sur les branches) pour guider la navigation. Les résultats mis en avant portent sur la reconnaissance de patterns haptique et la “decision accuracy” de guidage dans des scénarios contrôlés. Pertinent pour ton mémoire sur 3 points : (1) formalisation du feedback haptique comme canal principal (réduction charge audio), (2) couplage perception→raisonnement→action, (3) protocole d’évaluation multi-études. Limites : dépendance forte au cloud/LLM (latence, confidentialité), validité externe (environnements réels complexes) à démontrer. [Source](https://arxiv.org/abs/2503.16475)

**A3. Ultra-Efficient On-Device Object Detection… TinyissimoYOLO smart glasses**  
Travail centré sur l’“always-on” : plateforme lunettes basée sur processeur basse conso (GAP9 RISC‑V) + réseau TinyissimoYOLO (sub‑million params). Met en avant latence inférence très faible, énergie par inférence, et une autonomie de plusieurs heures sur petite batterie, avec une latence E2E incluant capture + post-processing. C’est une source clé pour justifier tes choix “quasi temps réel” et la séparation module perception ultra-léger vs modules plus lourds offload. Valeur directe : métriques énergie/latence au niveau système et ouverture code. Limite : focalisé sur détection d’objets, pas sur orchestration multi-modules ni UX assistive complète. [Source](https://arxiv.org/abs/2311.01057)

**A4. Wearable obstacle avoidance device… cross-modal learning (Nature)**  
Présente un dispositif lunettes + smartphone axé “ultra‑réactif/ultra‑fiable/ultra‑low‑power”, combinant IR + ToF (profondeur) avec compression “depth-aided” et détection cross‑modal (fusion au niveau features, Transformers). Met fortement l’accent sur des contraintes d’usage (E2E delay, autonomie, poids) et surtout sur validation prolongée avec volontaires, avec métriques sécurité (collision avoidance rate), délai E2E et consommation. Pour ton mémoire : modèle exemplaire d’architecture distribuée (capteurs/FPGA pour compression + smartphone pour IA), et démarche d’évaluation “terrain long”. Limites : complexité hardware (FPGA), coût, et architecture pas explicitement “plugin”. [Source](https://www.nature.com/articles/s41467-025-58085-x)

**A5. Smart Assistive Navigation System for Visually Impaired People**  
Contenu complet non récupéré (ResearchGate bloqué). Sur la base du titre uniquement : probable système d’assistance navigation, possiblement multi-capteurs et feedback. À exploiter plus tard via PDF direct. Pour ton mémoire : à classer “à vérifier” (capteurs, IA embarquée, validation utilisateur, modularité). **Non trouvé dans les sources récupérées** : méthodologie précise, métriques, résultats. [Source](https://www.researchgate.net/publication/372645921)

**A6. Making Smartglasses Accessible: Perspectives and Design Considerations**  
Étude centrée accessibilité/acceptabilité : met en avant barrières d’interaction (gestes fins, handicaps moteurs), surcharge cognitive liée à l’encombrement visuel, enjeux de stigma/esthétique, inquiétudes de surveillance (caméra/GPS), autonomie/batterie et coût. Approche participative/co‑design (dans le papier récupéré : aphasie, mais les implications “accessibility of smartglasses” sont généralisables). Pour ton mémoire : cadre solide pour justifier interface multi‑modal non intrusive, contrôle utilisateur, consentement, “privacy-by-design”, et profils (handicap moteur/visuel). Limite : moins technique sur pipelines IA embarqués. [Source](https://www.nature.com/articles/s41598-025-22253-2)

**A7. Advancements in Smart Wearable Mobility Aids… Bibliometric Review**  
Revue bibliométrique/narrative sur wearables pour déficients visuels : cartographie tendances (computer vision, obstacle detection, deep learning, multimodal feedback, capteurs ultrason, Raspberry Pi, etc.) et souligne tensions classiques : transfert d’information haptique/audio sans surcharge, intégration de matériaux intelligents, acceptabilité sociale et privacy. Utile pour ton mémoire comme “vue macro” justifiant la rareté des architectures réellement modulaires multi‑modes et la nécessité de standardiser évaluations. Limite : pas de contributions techniques directes; plutôt synthèse de tendances/angles. [Source](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11679352/)

**A8. Design and Development of Assistive Smart Glasses for Visually Impaired People**  
Contenu complet non récupéré (IEEE Xplore non accessible via crawl). À ce stade : **non trouvé dans les sources récupérées** (architecture, capteurs, métriques, validation). Pour ton mémoire, à garder en “source potentiellement clé” (IEEE souvent décrit prototype lunettes + feedback). [Source](https://ieeexplore.ieee.org/document/9262184)

**A9. Empowering Vision Using AI-Enabled Smart Glasses…**  
Contenu complet non récupéré (ResearchGate bloqué). **Non trouvé** : détails matériels, IA, validation. À re-télécharger via PDF direct si possible. [Source](https://www.researchgate.net/publication/377941882)

**A10. Smart Glasses for CVI: Co-Designing XR for Cerebral Visual Impairment**  
Travail HCI/co-design ciblant CVI (déficience visuelle cérébrale), avec diary study + ateliers + itérations prototypage sur Apple Vision Pro. Met en évidence besoins spécifiques : gestion attentionnelle, reconnaissance de personnes/objets, lecture, réduction stress sensoriel. Pour ton mémoire : apporte un angle “profils utilisateurs” (pas seulement cécité) et montre que les modes doivent être configurables et adaptatifs (intensité feedback, filtrage information). Limites : compute/embarqué peu central (plateforme puissante), transfert sur lunettes low‑power à discuter. [Source](https://arxiv.org/abs/2506.19210)

---

## B — IA embarquée / TinyML / on-device learning

**B11. TinyissimoYOLO: Quantized, low-memory TinyML object detection network**  
Propose un détecteur ultra-compact (quantifié, mémoire <0.5MB pour poids CNN) déployable sur MCU (ex. MAX78000) avec performances énergétiques très élevées (µJ/inférence) et FPS élevés sur accélérateur CNN embarqué. Très pertinent pour ton projet si tu veux un module “capteur intelligent” type ESP32/MCU TinyML : détection simple (quelques classes) mais robuste, always-on, très faible conso. Limites : nombre de classes restreint, pipeline complet “lunettes assistives” non traité, et intégration multi-capteurs/UX absente. [Source](https://arxiv.org/abs/2306.00001)

**B12. TActiLE: Tiny Active Learning for Wearable Devices**  
Document **hors-sujet** (selon contenu récupéré) : l’arXiv fourni décrit un modèle de rotation de phase GNSS/VLBI (géodésie), pas l’active learning TinyML wearable. Il y a très probablement une erreur de lien. Pour ton mémoire : à corriger (nouveau lien) sinon **non exploitable**. [Source](https://arxiv.org/abs/2502.08761)

**B13. Deploying Optimized Deep Vision Models for Eyeglasses on Low-Power Edge Devices**  
Accès non consolidé ici (crawl renvoie un article différent via MDPI). À ce stade : **non trouvé dans les sources récupérées** les informations spécifiques “eyeglasses low-power” (à re-crawler / PDF). [Source](https://www.mdpi.com/2079-9292/14/2/301)

**B14. Edge AI and TinyML: A Systematic Review**  
Contenu non récupéré (Nature access error). À garder comme revue structurante : typiquement classification des architectures TinyML, toolchains, contraintes énergie/mémoire, et directions (on-device learning). Mais ici : **non trouvé dans les sources récupérées**. [Source](https://www.nature.com/articles/s41598-025-88921-4)

**B15. Ultra-Efficient On-Device Object Detection on AI-Integrated Smart Glasses (ACM)**  
Contenu non récupéré (ACM paywall). À ce stade : **non trouvé**. Probable recouvrement avec A3 (version workshop/paper). [Source](https://dl.acm.org/doi/10.1145/3629539.3656461)

**B16. On-Device Learning and Personalization for TinyML Wearables**  
Document **hors-sujet** (selon contenu récupéré) : l’arXiv fourni porte sur un gradient isotopique 12C/13C (astrophysique), pas TinyML wearables. Lien à corriger. [Source](https://arxiv.org/abs/2409.11821)

**B17. Energy-Efficient Person Detection Using TinyML**  
Contenu non récupéré (PDF inaccessible via crawl). À ce stade : **non trouvé**. Intuitivement pertinent (détection personne + efficacité), mais non vérifiable ici. [Source](https://www.iaeng.org/publication/WCE2024/WCE2024_pp107-112.pdf)

**B18. Designing Object Detection Models for TinyML (ACM)**  
Contenu non récupéré (ACM paywall). **Non trouvé**. Cette source serait utile pour méthodologie de design (NAS, contraintes, quantif). [Source](https://dl.acm.org/doi/10.1145/3606841.3617502)

**B19. Ultra-Efficient Vision Pipelines for Wearable Devices (Prophesee resources)**  
Page ressource orientée “accès SDK/ressources”, mentionne OpenEB (open-source) et accès Metavision/SDK. Pertinent pour ton mémoire surtout comme **porte d’entrée outillage** event-based/neuromorphique (liaison avec partie C) et pour argumenter écosystème logiciel nécessaire (drivers, SDK, benchmarks). Limite : ce n’est pas un article scientifique structuré; contenu technique détaillé non livré librement (accès client). [Source](https://www.prophesee.ai/resources)

**B20. Active Learning Techniques for On-Device Embedded AI**  
Document **hors-sujet** (selon contenu récupéré) : l’arXiv traite de fusion de données satellites/sol pour monitoring CO₂, pas d’active learning on-device. Lien à corriger. [Source](https://arxiv.org/abs/2410.04288)

---

## C — Neuromorphic vision / event cameras

**C21. Neuromorphic Perception and Navigation for Mobile Robots: A Review (ACM)**  
Contenu non récupéré (ACM). **Non trouvé**. Probablement une revue utile pour relier perception event-based à navigation. [Source](https://dl.acm.org/doi/10.1145/3656469)

**C22. Recent Event Camera Innovations: A Survey**  
Survey recent sur event cameras : principes, comparaison frame vs event, panorama constructeurs, milestones, applications, datasets réels/synthétiques, simulateurs; mentionne ressource GitHub agrégée. Très utile pour ton mémoire : justifie event cameras comme option basse conso/low latency, et fournit un cadre pour décider “module optionnel” (maturité, datasets, outils). Limite : niveau “survey”, pas directement lunettes assistives, mais bon socle techno. [Source](https://arxiv.org/abs/2408.13627)

**C23. Event-Based Vision: A Survey (Gallego et al.)**  
Référence majeure : explique propriétés (µs latency, HDR, low power), et cartographie algorithmes (low-level à high-level, apprentissage, processeurs dédiés, SNN). Pour ton projet : fondation théorique/technique pour un futur module event-based (obstacle motion, low-light OCR, robustesse motion blur). Limite : intégration “produit lunettes” non abordée; nécessite design d’API et pipelines adaptés. [Source](https://arxiv.org/abs/1904.08405)

**C24. Application of Event Cameras and Neuromorphic Computing to VSLAM: A Survey**  
Contenu non récupéré (ResearchGate). **Non trouvé**. Potentiellement crucial pour relier event cameras à SLAM embarqué (partie D), mais pas exploitable ici. [Source](https://www.researchgate.net/publication/377112948)

**C25. Event-Based Eye Tracking: AIS 2024 Challenge Survey**  
Contenu non récupéré (CVF openaccess erreur). **Non trouvé**. Thématiquement pertinent si tu explores interaction/attention (eye gaze) sur lunettes, mais indisponible ici. [Source](https://openaccess.thecvf.com/content/CVPR2024W/AIS/html/Wang_Event-Based_Eye_Tracking_AIS_2024_Challenge_CVPRW_2024_paper.html)

**C26. Event-Based Solutions for Human-Centered Applications**  
Contenu non récupéré (Frontiers erreur). **Non trouvé**. Potentiellement pertinent (applications centrées humain), mais indisponible ici. [Source](https://www.frontiersin.org/articles/10.3389/frobt.2025.1298472)

**C27. Event Cameras: Datasets, Tools and Benchmarks (RPG UZH)**  
Page ressources/lab : donne accès à un écosystème (papers, code, datasets, liens) autour event cameras. Utile pour ton mémoire comme “infrastructure de recherche” et justification qu’un module event-based exige toolchain (calibration, replay, datasets). Limite : pas une publication unique; contenu large et hétérogène. [Source](https://rpg.ifi.uzh.ch)

---

## D — Navigation autonome, ObjectNav, VLN, SLAM

**D30. Object Goal Navigation Using Goal-Oriented Semantic Exploration**  
Système modulaire ObjectNav : construit une carte sémantique épisodique + stratégie d’exploration guidée par la catégorie d’objet cible. Montre l’intérêt d’architectures modulaires (cartographie + exploration + perception) vs end‑to‑end. Pour ton mémoire : transposable conceptuellement (lunettes = agent, mais action space différent) pour guider “macro décisions” (où aller, quel couloir) si tu as une carte/SLAM minimal. Limite : simulation/habitat/robots; compute et capteurs diffèrent fortement; intégration UX (feedback) non traitée. [Source](https://arxiv.org/abs/2007.00643)

**D31. Training-Free Embodied Object Goal Navigation with Semantic Frontiers**  
Contenu non récupéré : le PDF accessible via crawl renvoie un **autre** papier (agile locomotion RL), donc erreur de source récupérée. À ce stade : **non trouvé** pour Semantic Frontiers. [Source](https://roboticsproceedings.org/rss19/p051.pdf)

**D32. Auxiliary Tasks and Exploration Enable ObjectGoal Navigation**  
Réhabilite un agent learned (CNN/RNN) via tâches auxiliaires + reward d’exploration pour améliorer ObjectNav sans cartes explicites. Pour ton mémoire : utile pour argumenter que des signaux auxiliaires (depth prediction, semantics, etc.) peuvent stabiliser une politique/navigation, et que l’exploration explicite est cruciale. Limite : reste robot/sim, pas contrainte embarquée lunettes, et pas de dimension UX. [Source](https://openaccess.thecvf.com/content/ICCV2021/html/Ye_Auxiliary_Tasks_and_Exploration_Enable_ObjectGoal_Navigation_ICCV_2021_paper.html)

**D33. Vision-Based Navigation and Perception for Autonomous Systems: A Review (MDPI)**  
Le crawl a renvoyé un article MDPI hors-thème (motion prediction), donc la revue “navigation autonome” n’est pas récupérée. **Non trouvé**. [Source](https://www.mdpi.com/2076-3417/15/4/1897)

**D34. A Survey on Vision-Language Navigation**  
Document hors-sujet (selon contenu récupéré : arXiv quantique). Lien à corriger; **non exploitable** ici. [Source](https://arxiv.org/abs/2403.04751)

**D35. Volumetric Environment Representation for VLN (CVPR 2024)**  
Propose une représentation volumétrique (voxels) pour agréger multi-vues en 3D et soutenir VLN; multi-task (occupancy/layout/3D boxes) + mémoire épisodique. Pour ton mémoire : intéressant comme “option offload”/future extension, et comme argument qu’une meilleure représentation 3D améliore navigation langage. Limite : très coûteux compute/mémoire → peu réaliste on-device sur lunettes/RPi sans simplification; pas orienté assistance humaine. [Source](https://openaccess.thecvf.com/content/CVPR2024/html/Liu_Volumetric_Environment_Representation_for_Vision-Language_Navigation_CVPR_2024_paper.html)

**D36. Towards Long-Horizon Vision-Language Navigation**  
Contenu non récupéré (page arXiv non crawled ici). À ce stade : **non trouvé**. [Source](https://arxiv.org/abs/2501.01864)

**D37. Event-Based VSLAM: A Survey**  
Contenu non récupéré (ResearchGate). **Non trouvé**. [Source](https://www.researchgate.net/publication/376982104)

**D38. Semantic Frontier-Based Object Navigation (ETH)**  
Contenu non récupéré dans mes appels. **Non trouvé**. [Source](https://research-collection.ethz.ch/handle/20.500.11850/632181)

---

## E — Fusion multimodale & perception conjointe

**E39. Joint Perception and Prediction for Autonomous Driving: A Survey**  
Survey structurant sur modèles unifiés perception+prédiction, critique les pipelines séquentiels (propagation d’erreurs, absence d’incertitude), propose taxonomie (représentation d’entrée, modélisation contexte, représentation sortie) et discussion de gaps. Pour ton mémoire : transposable au guidage lunettes via “perception→anticipation risque” (obstacle dynamique, trajectoires) et au design de modules multi-tâches (détection + tracking + estimation mouvement). Limite : domaine automobile; adaptation au wearable exige simplifier capteurs et compute. [Source](https://arxiv.org/abs/2412.14088)

**E40. A Review of Multi-Sensor Fusion in Autonomous Driving (MDPI Sensors)**  
Le crawl a renvoyé un article sans lien direct à la fusion AD (armband santé). Donc : **non trouvé** pour la revue fusion automobile. [Source](https://www.mdpi.com/1424-8220/25/2/455)

**E41. A Comprehensive Survey on Deep Learning Multi-Modal Fusion (PDF techscience)**  
Contenu non récupéré (PDF inaccessible). **Non trouvé**. [Source](https://cdn.techscience.cn/uploads/attached/file/20240507/20240507171202_19143.pdf)

**E42. Multimodal Perception-Driven Decision-Making for Human–Robot Systems**  
Contenu non récupéré (Frontiers erreur). **Non trouvé**. [Source](https://www.frontiersin.org/articles/10.3389/frobt.2025.1305521)

**E43. Integrating Multi-Modal Sensors: A Review of Fusion Strategies**  
Non récupéré ici. **Non trouvé**. [Source](https://arxiv.org/abs/2502.09114)

**E44. Vision-Language-Action Models: A Survey**  
Non récupéré ici. **Non trouvé**. [Source](https://www.sciencedirect.com/science/article/pii/S1566253525000124)

---

## F — Architectures modulaires, frameworks, acceptabilité

**F45. A Distributed Wearable Computing Framework for Human-Centric Sensing**  
Non récupéré ici. **Non trouvé**. [Source](https://www.mdpi.com/2079-9292/14/7/1312)

**F46. A Codesign Framework for Next-Generation Wearable Computing Systems**  
Non récupéré ici (ResearchGate probable blocage). **Non trouvé**. [Source](https://www.researchgate.net/publication/379221904)

**F47. Augmented Reality Smart Glasses: Acceptance and UX Review**  
Non récupéré ici (ScienceDirect). **Non trouvé**. [Source](https://www.sciencedirect.com/science/article/pii/S1071581923000412)

**F48. Development of Affordable Smart Glasses for Individuals with Visual Impairments**  
Non récupéré ici. **Non trouvé**. [Source](https://rsisinternational.org/journals/ijrsi/articles/development-of-affordable-smart-glasses)

**F49. Frameworks for Modular Hardware Integration in Wearables (Springer chapter)**  
Non récupéré ici (Springer paywall). **Non trouvé**. [Source](https://link.springer.com/chapter/10.1007/978-3-031-91989-3_5)

**F50. Survey of Assistive Technologies for the Visually Impaired (ACM)**  
Non récupéré ici (ACM paywall). **Non trouvé**. [Source](https://dl.acm.org/doi/10.1145/3668395)

---

# 3) Tableau synthétique (version “minimaliste” faute d’accès complet)
Vu les blocages, je fournis un tableau **orienté disponibilité** + signaux clés quand connus. Les champs non confirmables = “non trouvé dans les sources récupérées”.

| ID | Année (si connue) | Matériel/approche | IA embarquée | Capteurs | Feedback | Validation utilisateur | Modularité | Pertinence projet |
|---|---:|---|---|---|---|---|---|---|
| A1 | 2025 | XR glasses + smartphone | YOLOv8n multi-modèles | RGB+IMU | audio+visuel | tests proto (chercheurs) | faible | très élevée |
| A2 | 2025 | lunettes + cloud LLM | YOLO-World + GPT-4o | RGB | haptique | études contrôlées | moyenne | élevée (haptique/raisonnement) |
| A3 | 2024/2025 | lunettes low-power (GAP9) | TinyissimoYOLO | RGB | n/a | bench système | moyenne | très élevée (latence/énergie) |
| A4 | 2025 | lunettes + smartphone + FPGA compression | cross-modal + RL compression | IR+ToF | audio+haptique | long terme volontaires | moyenne | très élevée (E2E, fiabilité) |
| A5 | ? | non trouvé | non trouvé | non trouvé | non trouvé | non trouvé | non trouvé | à vérifier |
| A6 | 2025 | smartglasses MR (HoloLens/vision pro contexte) | n/a | n/a | UX guidelines | co-design | n/a | élevée (acceptabilité) |
| A7 | 2024 | revue | n/a | n/a | n/a | n/a | n/a | moyenne (cadre macro) |
| A8 | ? | non trouvé | non trouvé | non trouvé | non trouvé | non trouvé | non trouvé | à vérifier |
| A9 | ? | non trouvé | non trouvé | non trouvé | non trouvé | non trouvé | non trouvé | à vérifier |
| A10 | 2025 | Apple Vision Pro | n/a (assistive XR) | n/a | XR | diary+co-design | n/a | élevée (profils) |
| B11 | 2023 | MCU | OD quantifié | caméra | n/a | bench | module | très élevée |
| B12 | 2025 | hors-sujet | hors-sujet | hors-sujet | hors-sujet | hors-sujet | hors-sujet | à corriger |
| B16 | 2024 | hors-sujet | hors-sujet | hors-sujet | hors-sujet | hors-sujet | hors-sujet | à corriger |
| B20 | 2024 | hors-sujet | hors-sujet | hors-sujet | hors-sujet | hors-sujet | hors-sujet | à corriger |
| C22 | 2024 | survey | n/a | event cams | n/a | n/a | n/a | élevée (option event) |
| C23 | 2020 | survey | n/a | event cams | n/a | n/a | n/a | très élevée (fondations) |
| D30 | 2020 | robot/sim | sémantique + carte | RGB/depth (sim) | n/a | benchmarks | modulaire | moyenne (concepts) |
| D32 | 2021 | robot/sim | aux tasks + exploration | RGB (sim) | n/a | benchmarks | moyenne | moyenne |
| D35 | 2024 | robot/sim | VER volumétrique | multi-vues | n/a | benchmarks | complexe | faible→moyenne (offload) |
| E39 | 2024 | survey voiture | multi-task joint | multi-capteurs | n/a | n/a | n/a | moyenne |

---

# 4) Conclusion transversale (gaps + positionnement mémoire) — basée uniquement sur les sources effectivement récupérées
Les sources accessibles convergent vers une même tension : **obtenir une perception utile en quasi temps réel** avec **budget énergie/latence** contraint, tout en maintenant **sécurité (confidentialité) et UX acceptable**. Les travaux A1/A3/A4 montrent trois stratégies complémentaires : (i) smartphone compagnon + scheduling (A1) [Source](https://www.mdpi.com/2079-9292/14/3/425), (ii) compute ultra-efficiente sur hardware spécialisé (A3) [Source](https://arxiv.org/abs/2311.01057), (iii) offload partiel + compression/fusion multimodale robuste (A4) [Source](https://www.nature.com/articles/s41467-025-58085-x). En parallèle, A6/A10 soulignent que sans co-design, contrôle utilisateur et réduction de surcharge (gestuelle, interface privée, stigma), l’adoption est fragile [Source](https://www.nature.com/articles/s41598-025-22253-2) [Source](https://arxiv.org/abs/2506.19210).  
Gap saillant (dans ce que j’ai pu lire) : **peu de propositions articulent explicitement une architecture “plateforme modulaire multi-modes”** (plugins, bus de messages, profils, OTA) tout en liant **métriques système** (E2E, énergie, robustesse) et **métriques utilisateur** (charge cognitive, acceptabilité). Ta contribution se positionne donc naturellement comme : **une architecture embarquée modulaire (hardware+software) orchestrée localement (bus type MQTT), multi-usage, profilée, extensible, et évaluée** sur latence/énergie/robustesse + UX, avec gestion explicite des modes et du offload.

---

## Réglages immédiats recommandés (actionnables) pour ton mémoire
1) Définir dès maintenant une **API de module** (entrées/sorties messages) + budget (latence/énergie) par module, inspiré des métriques système mises en avant dans A1/A3/A4. [A1](https://www.mdpi.com/2079-9292/14/3/425) [A3](https://arxiv.org/abs/2311.01057) [A4](https://www.nature.com/articles/s41467-025-58085-x)  
2) Spécifier un **mode dégradé always-on** (TinyML / détection simple) + mode “riche” (edge-hub RPi / smartphone / cloud) en s’appuyant sur l’écart A3↔A2. [A3](https://arxiv.org/abs/2311.01057) [A2](https://arxiv.org/abs/2503.16475)  
3) Formaliser un **cadre UX** : contrôle utilisateur, privacy-by-design, anti-surcharge (A6), et profils (CVI vs cécité vs mobilité réduite). [A6](https://www.nature.com/articles/s41598-025-22253-2) [A10](https://arxiv.org/abs/2506.19210)

---

## Dernière note (cruciale)
Si tu veux que cette revue devienne “insérable” avec **citations page/paragraph** et **8 rubriques complètes par article**, il faudra impérativement avoir accès aux **PDFs complets** (ou versions open access) des sources actuellement bloquées, et corriger les liens arXiv hors-sujet (B12/B16/B20/D34). Sans ça, une grande partie restera “non trouvé dans les sources”.

https://www.1nce.com/fr-fr/ressources/nouvelles/blog/mqtt-coap-lwm2m
