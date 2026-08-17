# Projet Unifié - Nexus System Aggregation

## 🚀 Piste publique 2028

La branche `agent/nexus-2028-public` ajoute un **runtime public réellement exécutable** sans retirer l'architecture Nexus historique décrite plus bas. L'objectif est de faire converger progressivement les dépôts Nexus vers une plateforme modulaire, testable et publiable tout en conservant la provenance et les acquis existants.

### Ce qui est matériellement utilisable sur cette branche

- package Python `projet_unifi` sous `src/`;
- runtime asynchrone à cycle de vie explicite;
- registre de capacités;
- moteur de politique avec autorisation explicite des effets externes;
- bus d'événements avec backpressure;
- CLI JSON stable pour automatisation;
- catalogue de maturité (`stable`, `experimental`, `conceptual`, `legacy`);
- sondage non invasif des dépendances historiques;
- tests de non-régression et validation de structure;
- CI Python 3.11, 3.12 et 3.13;
- build wheel/sdist automatisé.

### Démarrage public actuel

```bash
python -m pip install -e .
projet-unifi health
projet-unifi capabilities
projet-unifi invoke core.echo --args '{"value":"bonjour"}'
```

Le runtime minimal n'exige pas Docker, Kubernetes, TensorFlow, Web3 ou les fournisseurs cloud pour démarrer. Ces piles restent des intégrations historiques/optionnelles à raccorder explicitement.

Voir `docs/ARCHITECTURE_2028.md`, `docs/PROVENANCE.md` et `docs/SOURCE_AUDIT.md` pour distinguer ce qui est présent, ce qui provient des dépôts historiques et ce qui reste à intégrer.

---

## 📋 Vue d'ensemble historique préservée

**Projet-unifi-** est une agrégation organisée des composants Nexus :
- **Nex-us-V** : Système polymorphe autonome (core)
- **module** : Protocoles avancés et allocation dynamique
- **2-7-Nex-us-V** : Distributions, builds, et caches compilés

**Propriétaire** : Jonathan Therrien (Wanderer881101)  
**Localisation** : Marieville, Québec  
**Licence** : © 2026 Tous droits réservés

> Les sections d'architecture historique ci-dessous sont conservées comme **cible d'intégration et provenance**. Leur présence dans ce document ne signifie plus qu'un chemin est physiquement matérialisé : `scripts/validate_structure.py` donne l'état vérifiable.

---

## 🏗️ Architecture historique / cible d'intégration

### `src/` - Code Source Principal
Architecture historique annoncée :
- **`core/`** : Noyau Nexus (nexus_core.py, nexus_ai.py)
- **`network/`** : Couche réseau polymorphe (nexus_network.py)
- **`persistence/`** : Persistance (nexus_persistence.py, BD)
- **`ml/`** : Machine Learning (nexus_ml.py)
- **`ui/`** : Interface graphique (nexus_gui.py, nexus_gui_launcher.py)
- **`module/`** : Protocoles avancés (Lagrosseclef.py, protocole de la seconde genèse.py)
- **`utils/`** : Utilitaires divers (nexus_demo.py, nexus_finance.py, nexus_technologies.py, nexus_surveillance.py, nexus_memory.py)

La piste publique actuelle ajoute parallèlement **`src/projet_unifi/`** comme couche moderne, additive et découplée.

### `build/` - Artefacts Compilés
Distribution et cache d'exécution historiques :
- **`dist/`** : Exécutables PyInstaller (PYZ, EXE, PKG)
- **`lib/`** : Librairies compilées (.pyc de base_lib)
- **`cache/`** : Cache Python 3.13 (.cpython-313.pyc)

### `templates/` - Interfaces Web
- **`index.html`** : Template d'interface web

### `data/` - Données Persistantes
- **`memory/`** : nexus_memory.json (snapshots mémoire)
- **`db/`** : Bases de données SQLite (nexus_persistence.db)

### `config/` - Configuration historique
- **`requirements.txt`** : Dépendances Python
- **`Nexus.spec`** : Spécification PyInstaller
- **`nexus_technologies.py`** : Config technologies

### `docs/` - Documentation
- documentation d'architecture et de provenance;
- audit des sources;
- workflows;
- contrat 2028.

---

## ⚙️ Intégration historique

Les commandes historiques suivantes restent la **cible** après matérialisation contrôlée des dépôts sources. Elles ne doivent pas être présentées comme disponibles tant que le validateur les marque `PENDING`.

```bash
# Cibles historiques après intégration physique
python src/utils/demo.py
python src/ui/launcher.py
python src/module/Lagrosseclef.py
```

Vérification :

```bash
python scripts/validate_structure.py
```

---

## 📦 Contenu des Sous-projets

| Repository | Type | Rôle historique |
|-----------|------|-----------------|
| **Nex-us-V** | Source | Code source Nexus |
| **2-Nex-us-V** | Distribution | Interface + persistance |
| **3-Nex-us-V** | Build | Artefacts PyInstaller |
| **4-Nex-us-V** | Library | Bibliothèques compilées |
| **5-Nex-us-V** | Runtime | Importeurs PyInstaller |
| **6-Nex-us-V** | Cache | Cache Python |
| **7-Nex-us-V** | Template | Template HTML |
| **module** | Protocol | Lagrosseclef et protocoles avancés |

---

## 🔧 Structure de Dépendances historique

```text
Lagrosseclef.py (module)
    ↓
nexus_core.py (allocation, gestion entités)
    ├── nexus_network.py (transport)
    ├── nexus_persistence.py (stockage)
    ├── nexus_memory.py (mémoire)
    ├── nexus_ai.py (IA autonome)
    ├── nexus_ml.py (prédiction)
    └── nexus_finance.py (analyse financière)
        ↓
nexus_gui.py + templates/ (interface)
    ↓
PyInstaller Build (build/)
```

La couche 2028 vise à découpler progressivement ces imports par capacités et adaptateurs sans retirer les fonctions historiques.

---

## ✅ Contrat d'intégrité

- ✅ sources historiques conservées dans leurs dépôts de provenance;
- ✅ runtime public ajouté de manière additive;
- ✅ capacités locales minimales exécutables sans infrastructure externe;
- ✅ provenance et audit documentés;
- ✅ dépendances manquantes signalées au lieu d'être inventées;
- ✅ tests et CI ajoutés;
- ⏳ intégration physique complète de toutes les sources historiques encore à valider;
- ⏳ données et artefacts historiques à matérialiser/reconstruire de manière reproductible;
- ⏳ adaptateurs Nexus Core / Lagrosseclef à compléter après validation des dépendances.

---

## 📞 Informations de Contact

**Développeur** : Jonathan Therrien  
**Alias** : Wanderer881101  
**Email** : (voir profil GitHub)  
**Région** : Marieville, Québec, Canada

---

## 📝 Licence & Propriété

Ce projet est © 2026 Jonathan Therrien. Tous droits réservés.  
Reproduction, distribution ou modification interdites sans autorisation explicite.

---

**Piste publique** : 2028 architecture track / alpha  
**Principe** : évolution additive, provenance vérifiable, aucune suppression silencieuse des acquis.
