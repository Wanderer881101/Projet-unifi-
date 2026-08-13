# Provenance des composants — Projet-unifi-

Ce document distingue la structure annoncée par le manifeste de l'intégration effectivement matérialisée dans le dépôt.

## Règles

1. Un composant n'est considéré comme intégré que si sa présence dans `Projet-unifi-` est vérifiable.
2. Le dépôt source reste la source de vérité pour le code source.
3. Les artefacts `.pyc`, `.pyz`, caches et sorties PyInstaller sont des artefacts de build, pas des sources.
4. Les fichiers identiques provenant de plusieurs dépôts ne sont pas dupliqués sans justification.
5. Toute intégration doit conserver la provenance du dépôt et permettre de reconstruire l'artefact depuis les sources.

## Matrice initiale

| Source | Rôle prévu | Destination prévue | Nature | État à vérifier |
|---|---|---|---|---|
| `Nex-us-V` | Nexus Core | `src/nexus-core/` | source Python | à intégrer/tester |
| `module` | protocoles/modules | `src/module/` | source Python | à intégrer/tester |
| `2-Nex-us-V` | interface + persistance | `templates/`, `data/db/` | interface + donnée | à comparer |
| `3-Nex-us-V` | sortie PyInstaller | `build/dist/` | artefact | à préserver/reproduire |
| `4-Nex-us-V` | bibliothèques compilées | `build/lib/` | artefact | régénérable |
| `5-Nex-us-V` | runtime PyInstaller | `build/runtime/` | artefact | distribution |
| `6-Nex-us-V` | cache Python | `build/cache/` | artefact | régénérable |
| `7-Nex-us-V` | template web | `templates/` | interface | à comparer |

## Point de contrôle

Le `MANIFEST.md` décrit une architecture cible beaucoup plus complète que le contenu actuellement matérialisé dans le dépôt. Cette matrice sert donc de contrat d'audit : chaque ligne devra être confirmée par une vérification du dépôt source et de la destination avant d'être marquée comme intégrée.

## Historique

- 2026-08-13 : création de cette matrice lors de l'audit d'intégration.
