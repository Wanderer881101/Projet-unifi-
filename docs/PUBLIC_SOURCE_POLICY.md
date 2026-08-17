# Politique de sources publiques

## Règle de publication

`Projet-unifi-` est un dépôt public. Toute implémentation, documentation ou adaptation publiée ici doit être dérivée exclusivement de sources elles-mêmes publiques et explicitement approuvées pour cette utilisation.

L'accès technique à un autre dépôt ne constitue jamais une autorisation de publication.

## Sources autorisées

La liste exécutable de référence est `projet_unifi.source_policy.PUBLIC_SOURCE_REPOSITORIES`.

Elle contient actuellement les dépôts publics suivants :

- `Wanderer881101/Projet-unifi-`
- `Wanderer881101/Nex-us-V`
- `Wanderer881101/module`
- `Wanderer881101/2-Nex-us-V`
- `Wanderer881101/3-Nex-us-V`
- `Wanderer881101/4-Nex-us-V`
- `Wanderer881101/5-Nex-us-V`
- `Wanderer881101/6-Nex-us-V`
- `Wanderer881101/7-Nex-us-V`
- `Wanderer881101/Book-1-Livre-1`

## Sources hors frontière

Tout dépôt absent de cette allowlist est hors frontière de publication, quelle que soit sa visibilité pour les outils de développement.

Il est interdit d'en publier :

- le code ou des fragments de code ;
- les noms de fichiers ou structures internes non déjà publics ;
- des descriptions suffisamment précises pour reconstruire une implémentation confidentielle ;
- des données, configurations, secrets ou artefacts ;
- une adaptation qui serait essentiellement une transposition d'un composant non public.

## Conception indépendante

Si une idée générale est nécessaire au projet public mais n'est pas disponible dans les sources autorisées, elle doit être conçue indépendamment à partir :

1. des exigences publiques du projet ;
2. de standards et technologies publics ;
3. des dépôts de l'allowlist ;
4. d'une implémentation nouvelle, documentée comme telle.

## Contrôle avant fusion

Toute PR publique doit pouvoir répondre oui aux questions suivantes :

1. Chaque comportement dérivé possède-t-il une provenance publique autorisée ou une conception indépendante identifiable ?
2. Le diff contient-il uniquement des informations publiables ?
3. Une personne ayant accès seulement aux dépôts publics pourrait-elle reproduire la justification technique du changement ?
4. Aucun dépôt hors allowlist n'est-il nécessaire pour expliquer le code publié ?

En cas de doute, le changement reste hors de `main` jusqu'à clarification.
