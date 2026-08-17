# Provenance des composants — Projet-unifi-

Ce document distingue la structure annoncée par le manifeste de l'intégration effectivement matérialisée dans le dépôt.

## Règles

1. Un composant n'est considéré comme intégré que si sa présence dans `Projet-unifi-` est vérifiable.
2. Le dépôt source reste la source de vérité pour le code source historique.
3. Les artefacts `.pyc`, `.pyz`, caches et sorties PyInstaller sont des artefacts de build, pas des sources.
4. Les fichiers identiques provenant de plusieurs dépôts ne sont pas dupliqués sans justification.
5. Toute intégration conserve sa provenance et doit permettre de reconstruire les artefacts depuis les sources.
6. Une adaptation publique ne remplace jamais silencieusement un original historique : elle est ajoutée comme couche séparée et testable.

## Matrice initiale

| Source | Rôle prévu | Destination prévue | Nature | État |
|---|---|---|---|---|
| `Nex-us-V` | Nexus Core | couche d'adaptation / source préservée | source Python | vérifié, intégration physique à contrôler |
| `module` | protocoles/modules | couche d'adaptation / source préservée | source Python | vérifié, dépendances à normaliser |
| `2-Nex-us-V` | interface + persistance | `templates/`, `data/db/` | interface + donnée | à comparer |
| `3-Nex-us-V` | sortie PyInstaller | `build/dist/` | artefact | à préserver/reproduire |
| `4-Nex-us-V` | bibliothèques compilées | `build/lib/` | artefact | régénérable |
| `5-Nex-us-V` | runtime PyInstaller | `build/runtime/` | artefact | distribution |
| `6-Nex-us-V` | cache Python | `build/cache/` | artefact | régénérable |
| `7-Nex-us-V` | template web | `templates/` | interface | à comparer |

## État de la piste publique 2028

La branche `agent/nexus-2028-public` part de `agent/public-future-v2` et conserve son runtime asynchrone, son bus d'événements, son moteur de politiques et son registre de capacités. Elle réintroduit également les principes d'audit de `feature/complete-unified-integration` sans modifier `main`.

Le runtime public est volontairement découplé des dépendances lourdes historiques : il peut démarrer, exposer son état et exécuter les primitives locales sûres même si Docker, Kubernetes, TensorFlow, Web3, les clouds ou d'autres connecteurs historiques sont absents.

`pqc_module`, importé historiquement par `Lagrosseclef.py`, n'a pas été retrouvé dans les dépôts GitHub accessibles au moment de cette vérification. Il reste donc une dépendance manquante à retrouver, et n'est pas remplacé artificiellement.

## Historique

- 2026-08-13 : création de la matrice initiale sur `feature/complete-unified-integration`.
- 2026-08-17 : restauration et extension sur `agent/nexus-2028-public`, avec principe de compatibilité additive et absence de remplacement silencieux.
