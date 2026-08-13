# Audit des sources — Projet-unifi-

Date: 2026-08-13
Branche de travail: `feature/complete-unified-integration`

## Objectif

Vérifier les dépôts sources avant leur intégration physique afin de distinguer ce qui est exécutable tel quel, ce qui nécessite une adaptation, et ce qui relève d'artefacts ou de données persistantes.

## Nex-us-V

Le dépôt `Nex-us-V` contient bien le noyau annoncé : `nexus_core.py`, `nexus_ai.py`, `nexus_network.py`, `nexus_memory.py`, `nexus_persistence.py`, `nexus_ml.py`, `nexus_gui.py`, `nexus_gui_launcher.py`, `nexus_demo.py`, `nexus_finance.py`, `nexus_surveillance.py`, `nexus_technologies.py`, `nexus_web_interface.py`, ainsi que `requirements.txt`, `Nexus.spec`, une base SQLite et un snapshot mémoire JSON.

### Constat 1 — dépendances déclarées incomplètes

`nexus_finance.py` importe notamment `ccxt`, `web3` et `requests`, alors que le `requirements.txt` actuel ne les déclare pas. Une installation basée uniquement sur ce fichier peut donc échouer au premier import du noyau.

Action prévue : reconstruire la liste minimale des dépendances réelles à partir des imports du code avant de figer `config/requirements.txt`.

### Constat 2 — chemins de persistance relatifs

`nexus_memory.py` ouvre directement `nexus_memory.json` et `nexus_persistence.py` utilise par défaut `nexus_persistence.db` dans le répertoire courant. Après intégration dans une nouvelle arborescence, le comportement dépendrait donc du dossier depuis lequel le programme est lancé.

Action prévue : conserver les données originales, mais introduire ensuite une résolution de chemin explicite vers `data/memory/` et `data/db/`, configurable sans casser la compatibilité.

### Constat 3 — noyau monolithique au niveau des imports

`nexus_core.py` importe immédiatement réseau, mémoire, IA, finance, persistance, ML, technologies et surveillance. Une seule dépendance absente peut donc empêcher l'import du noyau complet, même lorsque la fonctionnalité concernée n'est pas utilisée.

Action prévue : tester d'abord l'import minimal et identifier les dépendances optionnelles avant tout refactor majeur.

## module

Le dépôt `module` contient actuellement deux fichiers :

- `Lagrosseclef.py`
- `protocole de la seconde genèse.py`

### Constat 4 — dépendance locale absente

`Lagrosseclef.py` importe `pqc_module`, mais aucun fichier ou package `pqc_module` n'est présent dans le dépôt `module` tel qu'il est actuellement publié.

Action prévue : rechercher sa provenance dans les autres dépôts avant de modifier cet import. Ne pas créer un faux module de remplacement sans retrouver la source originale.

### Constat 5 — dépendances externes lourdes

`Lagrosseclef.py` importe entre autres Docker, Kubernetes, gRPC, AWS (`boto3`), Google Cloud Storage, Azure Identity, TensorFlow, Prometheus, NumPy et scikit-learn. Le module tente aussi de détecter Docker et Kubernetes dès l'import.

Action prévue : classer ces dépendances en obligatoires et optionnelles, puis empêcher qu'une intégration du projet entier exige toutes les infrastructures externes au simple démarrage.

### Constat 6 — protocole Seconde Genèse non importable en l'état

La version stockée de `protocole de la seconde genèse.py` présente une structure qui n'est pas du Python exécutable en l'état : indentation perdue dans plusieurs blocs et définition `def **init**(...)` au lieu de `def __init__(...)`.

Action prévue : traiter ce fichier comme source historique à préserver. Créer ultérieurement une version normalisée dans l'arborescence unifiée seulement après comparaison avec les versions antérieures disponibles, plutôt que modifier silencieusement l'original.

## Ordre d'intégration retenu

1. Préserver les dépôts sources tels quels.
2. Établir les dépendances réellement utilisées par `Nex-us-V`.
3. Retrouver `pqc_module` et toute autre dépendance locale manquante.
4. Valider la syntaxe de chaque source Python destinée à être intégrée.
5. Intégrer le noyau dans une zone source cohérente.
6. Déplacer/configurer les chemins de données sans modifier leur contenu d'origine.
7. Ajouter des tests d'import et de démarrage minimal.
8. Intégrer les protocoles seulement après normalisation vérifiable.
9. Régénérer les artefacts PyInstaller depuis les sources plutôt que d'en faire la référence principale.

## Principe de conservation

Aucune correction structurelle ne doit effacer l'état historique des dépôts d'origine. Les adaptations destinées au projet unifié doivent être traçables, documentées et testables.
