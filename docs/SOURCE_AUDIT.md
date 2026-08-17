# Audit des sources — Projet-unifi-

Date initiale: 2026-08-13  
Révision: 2026-08-17  
Branche actuelle: `agent/nexus-2028-public`

## Objectif

Vérifier les dépôts sources avant leur intégration physique afin de distinguer ce qui est exécutable tel quel, ce qui nécessite une adaptation, et ce qui relève d'artefacts ou de données persistantes.

## Nex-us-V

Le dépôt `Nex-us-V` contient bien le noyau annoncé : `nexus_core.py`, `nexus_ai.py`, `nexus_network.py`, `nexus_memory.py`, `nexus_persistence.py`, `nexus_ml.py`, `nexus_gui.py`, `nexus_gui_launcher.py`, `nexus_demo.py`, `nexus_finance.py`, `nexus_surveillance.py`, `nexus_technologies.py`, ainsi que `requirements.txt`, `Nexus.spec`, une base SQLite et un snapshot mémoire JSON.

### Constat 1 — dépendances déclarées incomplètes

`nexus_finance.py` importe notamment `ccxt`, `web3` et `requests`, alors que le `requirements.txt` historique ne les déclare pas tous. Une installation basée uniquement sur ce fichier peut donc échouer au premier import du noyau.

Réponse 2028 : les dépendances historiques lourdes sont traitées comme intégrations optionnelles et peuvent être sondées sans les importer.

### Constat 2 — chemins de persistance relatifs

`nexus_memory.py` ouvre directement `nexus_memory.json` et `nexus_persistence.py` utilise par défaut `nexus_persistence.db` dans le répertoire courant. Après intégration dans une nouvelle arborescence, le comportement dépendrait donc du dossier depuis lequel le programme est lancé.

Règle : conserver les données originales et introduire une résolution de chemin explicite/configurable dans la couche publique, sans modifier silencieusement les originaux.

### Constat 3 — noyau monolithique au niveau des imports

`nexus_core.py` importe immédiatement plusieurs sous-systèmes. Une seule dépendance absente peut empêcher l'import du noyau complet, même lorsque la fonctionnalité concernée n'est pas utilisée.

Réponse 2028 : le runtime public est capability-oriented, démarre avec un socle minimal et n'active les intégrations externes qu'explicitement.

## module

Le dépôt `module` contient notamment :

- `Lagrosseclef.py`
- `protocole de la seconde genèse.py`

### Constat 4 — dépendance locale absente

`Lagrosseclef.py` importe `pqc_module`, mais aucune occurrence de `pqc_module` n'a été retrouvée dans les dépôts GitHub accessibles lors de l'audit du 2026-08-17.

Règle : ne pas créer un faux module de remplacement. Continuer la recherche de provenance et maintenir cette intégration comme indisponible tant que la source authentique n'est pas retrouvée.

### Constat 5 — dépendances externes lourdes

`Lagrosseclef.py` dépend de plusieurs piles d'infrastructure et de ML. Certaines peuvent effectuer de la détection d'environnement dès l'import.

Réponse 2028 : `projet_unifi.legacy.probe_dependencies()` utilise `importlib.util.find_spec` et évite d'importer ces bibliothèques au démarrage du runtime public.

### Constat 6 — protocole Seconde Genèse non importable en l'état historique audité

La version auditée de `protocole de la seconde genèse.py` contient des anomalies structurelles empêchant de la considérer comme module Python public prêt à l'emploi.

Règle : préserver le fichier historique; toute normalisation future doit être une adaptation distincte, comparée à d'autres versions disponibles et testée.

## Ordre d'intégration retenu

1. Préserver les dépôts et branches sources tels quels.
2. Garder le runtime public minimal indépendant des dépendances externes lourdes.
3. Cartographier les dépendances réelles et manquantes.
4. Valider syntaxe/import de chaque source destinée à l'intégration.
5. Ajouter des adaptateurs explicites plutôt que refactoriser silencieusement les originaux.
6. Rendre les chemins de données configurables.
7. Ajouter tests de démarrage, capacités, politiques et compatibilité.
8. Intégrer les protocoles seulement après normalisation vérifiable.
9. Régénérer les artefacts de build depuis les sources.
10. Marquer publiquement chaque capacité comme stable, expérimentale, conceptuelle ou legacy.

## Principe de conservation

Aucune correction structurelle ne doit effacer l'état historique des dépôts d'origine. Les adaptations destinées au projet unifié sont additives, traçables, documentées et testables.
