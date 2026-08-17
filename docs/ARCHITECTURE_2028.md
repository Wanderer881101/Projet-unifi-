# Architecture 2028 — Projet-unifi / Nexus

## But

Faire évoluer Projet-unifi vers une plateforme publique réellement exécutable, vérifiable et extensible sans sacrifier les acquis historiques de Nexus, Lagrosseclef ou des dépôts de distribution.

Le terme « 2028 » décrit ici une direction d'ingénierie : modularité forte, contrat de capacités, exécution asynchrone, dépendances optionnelles, politiques explicites, observabilité et reproductibilité. Il ne prétend pas qu'une technologie inexistante ou non vérifiée est déjà disponible.

## Invariants non négociables

1. **Conservation additive** — aucune source historique n'est remplacée silencieusement.
2. **Provenance** — chaque adaptation indique d'où vient le comportement qu'elle expose.
3. **Démarrage minimal** — le runtime public doit démarrer sans Docker, Kubernetes, cloud, Web3, TensorFlow ou autres piles optionnelles.
4. **Effets externes explicites** — une capacité pouvant agir hors du processus n'est pas autorisée implicitement.
5. **Dégradation contrôlée** — l'absence d'une intégration optionnelle ne doit pas rendre le noyau inutilisable.
6. **Vérifiabilité** — les capacités annoncées au public doivent être testables et classées par maturité.
7. **Reproductibilité** — les distributions doivent être reconstruites depuis les sources plutôt que traitées comme source de vérité.

## Couches

### 1. Runtime public

`projet_unifi.runtime.NexusRuntime` orchestre :

- cycle de vie explicite (`created` → `starting` → `running` → `stopping` → `stopped`);
- registre de capacités;
- politique d'autorisation;
- bus d'événements asynchrone;
- rapport de santé et compteurs d'exécution.

Cette couche ne dépend que de la bibliothèque standard Python.

### 2. Contrat de capacités

Une fonctionnalité publique est exposée sous un nom stable (`core.*`, `health.*`, `simulation.*`, etc.).

`projet_unifi.catalog` distingue quatre niveaux :

- `stable` : comportement public couvert par tests;
- `experimental` : utilisable mais susceptible d'évoluer;
- `conceptual` : spécification/objectif, pas une promesse d'exécution;
- `legacy` : comportement historique disponible via adaptation contrôlée.

Cette distinction empêche la documentation de confondre ambition et capacité démontrée.

### 3. Compatibilité historique

`projet_unifi.legacy` sonde les dépendances et sources historiques sans les importer. Cette séparation est importante car certains modules anciens déclenchent de la détection d'infrastructure au chargement.

Une intégration legacy future doit respecter le modèle suivant :

1. source originale préservée;
2. adaptateur séparé;
3. dépendances déclarées comme optionnelles;
4. activation explicite;
5. tests de compatibilité;
6. provenance documentée.

### 4. Événements et orchestration

Le bus d'événements fournit une file bornée, de la backpressure et un arrêt déterministe. Les futurs sous-systèmes Nexus peuvent communiquer par événements plutôt que par imports croisés obligatoires.

Cela permet de découpler progressivement le noyau historique monolithique sans le réécrire d'un bloc.

### 5. Politique et effets externes

Le moteur actuel autorise par défaut seulement les préfixes locaux jugés sûrs (`core`, `memory`, `analysis`, `simulation`, `health`).

Les futures capacités réseau, cloud, système, finance ou infrastructure devront être enregistrées explicitement et autorisées par politique. Le but est la maîtrise des effets de bord, pas la suppression des capacités historiques.

### 6. Interface publique

Le point d'entrée `projet-unifi` fournit une surface minimale automatisable :

```bash
projet-unifi health
projet-unifi capabilities
projet-unifi invoke core.echo --args '{"value":"bonjour"}'
```

Le format de sortie est JSON afin de pouvoir être consommé par humains, scripts, tests, services ou interfaces futures.

## Stratégie d'intégration des dépôts GitHub

Les dépôts `Nex-us-V`, `module`, `2-Nex-us-V` à `7-Nex-us-V` sont considérés comme sources/provenances spécialisées. Leur contenu ne doit pas être copié aveuglément dans le runtime public.

Ordre retenu :

1. inventorier et verrouiller la provenance;
2. valider les imports et dépendances;
3. isoler données et artefacts de build;
4. créer les adaptateurs minimaux;
5. ajouter tests et contrats de capacités;
6. seulement ensuite intégrer physiquement les sources nécessaires;
7. reconstruire les distributions à partir de cet état contrôlé.

## Qualité publique minimale avant `main`

Une fusion vers `main` exige au minimum :

- compilation Python réussie;
- tests du runtime et de compatibilité réussis;
- CLI fonctionnelle;
- package installable;
- aucune dépendance optionnelle requise au démarrage;
- documentation synchronisée avec l'état réel;
- aucun fichier historique supprimé;
- provenance des nouvelles adaptations documentée;
- revue de sécurité des capacités à effets externes.

## Évolution suivante

Les prochaines étapes prioritaires sont : adaptateurs read-only pour Nexus Core, configuration explicite des chemins de données, registre de plugins versionné, métriques structurées, snapshots de capacités, tests d'intégration avec sources historiques, puis interface/service public construit sur le même contrat de runtime.
