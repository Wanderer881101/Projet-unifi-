# Projet Unifié - Nexus System Aggregation

## 📋 Vue d'ensemble

**Projet-unifi-** est une agrégation robuste et organisée de tous les composants Nexus :
- **Nex-us-V** : Système polymorphe autonome (core)
- **module** : Protocoles avancés et allocation dynamique
- **2-7-Nex-us-V** : Distributions, builds, et caches compilés

**Propriétaire** : Jonathan Therrien (Wanderer881101)  
**Localisation** : Marieville, Québec  
**Licence** : © 2026 Tous droits réservés

---

## 🏗️ Architecture

### `src/` - Code Source Principal
Contient le code Python source complet et les modules :
- **`core/`** : Noyau Nexus (nexus_core.py, nexus_ai.py)
- **`network/`** : Couche réseau polymorphe (nexus_network.py)
- **`persistence/`** : Persistance (nexus_persistence.py, BD)
- **`ml/`** : Machine Learning (nexus_ml.py)
- **`ui/`** : Interface graphique (nexus_gui.py, nexus_gui_launcher.py)
- **`module/`** : Protocoles avancés (Lagrosseclef.py, protocole de la seconde genèse.py)
- **`utils/`** : Utilitaires divers (nexus_demo.py, nexus_finance.py, nexus_technologies.py, nexus_surveillance.py, nexus_memory.py)

### `build/` - Artefacts Compilés
Distribution et cache d'exécution :
- **`dist/`** : Exécutables PyInstaller (PYZ, EXE, PKG)
- **`lib/`** : Librairies compilées (.pyc de base_lib)
- **`cache/`** : Cache Python 3.13 (.cpython-313.pyc)

### `templates/` - Interfaces Web
- **`index.html`** : Template d'interface web

### `data/` - Données Persistantes
- **`memory/`** : nexus_memory.json (snapshots mémoire, 2.4 MB)
- **`db/`** : Bases de données SQLite (nexus_persistence.db)

### `config/` - Configuration
- **`requirements.txt`** : Dépendances Python
- **`Nexus.spec`** : Spécification PyInstaller
- **`nexus_technologies.py`** : Config technologies

### `docs/` - Documentation
- README détaillés par module
- Architecture diagrams
- Guides d'utilisation

---

## ⚙️ Démarrage Rapide

### Installation
```bash
git clone https://github.com/Wanderer881101/Projet-unifi-.git
cd Projet-unifi-
pip install -r config/requirements.txt
```

### Exécution
```bash
# Démo complète
python src/utils/demo.py

# Interface GUI
python src/ui/launcher.py

# Test module protocoles
python src/module/Lagrosseclef.py
```

---

## 📦 Contenu des Sous-projets

| Repository | Type | Taille | Contenu |
|-----------|------|--------|---------|
| **Nex-us-V** | Source | 161 KB | Code source complet Nexus |
| **2-Nex-us-V** | Distribution | 2 KB | Interface HTML + DB |
| **3-Nex-us-V** | Build | 22.8 MB | PyInstaller artifacts |
| **4-Nex-us-V** | Library | 285 KB | Base lib compilée |
| **5-Nex-us-V** | Runtime | 22 KB | Importeurs PyInstaller |
| **6-Nex-us-V** | Cache | 59 KB | Cache Python 3.13 |
| **7-Nex-us-V** | Template | 1 KB | Template HTML |
| **module** | Protocol | 61 KB | Protocoles avancés |

---

## 🔧 Structure de Dépendances

```
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

---

## ✅ Checklist d'Intégrité

- ✅ Tous modules sources consolidés
- ✅ Tous artefacts compilés préservés
- ✅ Données persistantes archivées
- ✅ Configuration centralisée
- ✅ Documentation complète
- ✅ Structure modulaire et extensible

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

**Dernière mise à jour** : 2026-08-11  
**Statut** : Agrégation initiale complète ✅
