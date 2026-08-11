# Structure Détaillée - Projet Unifié

## Hiérarchie Complète

```
Projet-unifi-/
│
├── 📄 README.md                    # Guide maître (vue d'ensemble)
├── 📄 STRUCTURE.md                 # Ce fichier (architecture détaillée)
├── 📄 MANIFEST.md                  # Inventaire complet
├── 📄 INTEGRATION.md               # Guide d'intégration
├── 📄 .gitignore                   # Configuration Git robuste
│
├── 📁 src/                         # CODE SOURCE PRINCIPAL (Nex-us-V)
│   │
│   ├── 📁 core/                    # Noyau système
│   │   ├── __init__.py
│   │   ├── nexus_core.py           # Moteur principal (20.9 KB)
│   │   ├── nexus_ai.py             # IA autonome (7.4 KB)
│   │   ├── nexus_memory.py         # Gestion mémoire (3.3 KB)
│   │   └── README_core.md
│   │
│   ├── 📁 network/                 # Couche réseau polymorphe
│   │   ├── __init__.py
│   │   ├── nexus_network.py        # Transport multi-proto (9.9 KB)
│   │   └── README_network.md
│   │
│   ├── 📁 persistence/             # Stockage & persistance
│   │   ├── __init__.py
│   │   ├── nexus_persistence.py    # Gestion BD (2.6 KB)
│   │   └── README_persistence.md
│   │
│   ├── 📁 ml/                      # Machine Learning
│   │   ├── __init__.py
│   │   ├── nexus_ml.py             # Prédiction (2.0 KB)
│   │   └── README_ml.md
│   │
│   ├── 📁 ui/                      # Interface utilisateur
│   │   ├── __init__.py
│   │   ├── nexus_gui.py            # GUI Tkinter (3.2 KB)
│   │   ├── nexus_gui_launcher.py   # Lanceur GUI (484 B)
│   │   └── README_ui.md
│   │
│   ├── 📁 module/                  # PROTOCOLES AVANCÉS (depuis 'module' repo)
│   │   ├── __init__.py
│   │   ├── Lagrosseclef.py         # Clé maître / allocation (217 KB)
│   │   ├── protocole_seconde_genese.py # Protocoles avancés (18 KB)
│   │   └── README_protocols.md
│   │
│   ├── 📁 utils/                   # Utilitaires & démos
│   │   ├── __init__.py
│   │   ├── nexus_demo.py           # Démo complète (3.4 KB)
│   │   ├── nexus_finance.py        # Analyse financière (12.5 KB)
│   │   ├── nexus_technologies.py   # Tech integration (6.3 KB)
│   │   ├── nexus_surveillance.py   # Surveillance (7.0 KB)
│   │   └── README_utils.md
│   │
│   └── README.md                   # Index modules src/
│
├── 📁 build/                       # ARTEFACTS COMPILÉS (2-7-Nex-us-V)
│   │
│   ├── 📁 dist/                    # Distribution PyInstaller (3-Nex-us-V)
│   │   ├── Analysis-00.toc         # Analysis metadata (716 KB)
│   │   ├── EXE-00.toc              # Executable metadata (173 KB)
│   │   ├── PKG-00.toc              # Package metadata (172 KB)
│   │   ├── PYZ-00.pyz              # Archive Python (22.9 MB)
│   │   ├── PYZ-00.toc              # Archive metadata (521 KB)
│   │   ├── xref-Nexus.html         # Cross-reference (4.7 MB)
│   │   ├── warn-Nexus.txt          # Warnings log (73 KB)
│   │   └── README_dist.md
│   │
│   ├── 📁 lib/                     # Base library compilée (4-Nex-us-V)
│   │   ├── _collections_abc.pyc
│   │   ├── _weakrefset.pyc
│   │   ├── abc.pyc
│   │   ├── codecs.pyc
│   │   ├── [... 20+ autres .pyc ...]
│   │   └── README_lib.md
│   │
│   ├── 📁 cache/                   # Python 3.13 cache (6-Nex-us-V)
│   │   ├── nexus_ai.cpython-313.pyc
│   │   ├── nexus_core.cpython-313.pyc
│   │   ├── nexus_finance.cpython-313.pyc
│   │   ├── nexus_gui.cpython-313.pyc
│   │   ├── nexus_memory.cpython-313.pyc
│   │   ├── nexus_ml.cpython-313.pyc
│   │   ├── nexus_network.cpython-313.pyc
│   │   ├── nexus_persistence.cpython-313.pyc
│   │   ├── nexus_surveillance.cpython-313.pyc
│   │   ├── nexus_technologies.cpython-313.pyc
│   │   ├── nexus_web_interface.cpython-313.pyc
│   │   └── README_cache.md
│   │
│   ├── 📁 runtime/                 # PyInstaller runtime (5-Nex-us-V)
│   │   ├── pyimod01_archive.pyc
│   │   ├── pyimod02_importers.pyc
│   │   ├── pyimod03_ctypes.pyc
│   │   ├── pyimod04_pywin32.pyc
│   │   ├── struct.pyc
│   │   └── README_runtime.md
│   │
│   └── README.md                   # Index artefacts build/
│
├── 📁 templates/                   # INTERFACES WEB (2-Nex-us-V, 7-Nex-us-V)
│   ├── index.html                  # Interface Web principale (2.8 KB)
│   └── README_templates.md
│
├── 📁 data/                        # DONNÉES PERSISTANTES
│   │
│   ├── 📁 memory/                  # Snapshots mémoire
│   │   ├── nexus_memory.json       # Mémoire système (2.4 MB)
│   │   └── README_memory.md
│   │
│   ├── 📁 db/                      # Bases de données
│   │   ├── nexus_persistence.db    # SQLite (20 KB)
│   │   └── README_db.md
│   │
│   └── README.md                   # Index données data/
│
├── 📁 config/                      # CONFIGURATION & SPEC
│   ├── requirements.txt            # Dépendances Python
│   ├── Nexus.spec                  # Spec PyInstaller
│   ├── setup.py                    # Setup distributable
│   └── README_config.md
│
├── 📁 docs/                        # DOCUMENTATION COMPLÈTE
│   ├── ARCHITECTURE.md             # Architecture système
│   ├── MODULES.md                  # Documentation modules
│   ├── API.md                      # Référence API
│   ├── PROTOCOLS.md                # Protocoles avancés
│   ├── USAGE.md                    # Guide d'utilisation
│   ├── DEPLOYMENT.md               # Déploiement
│   └── FAQ.md                      # Questions fréquentes
│
└── 📁 tests/                       # TESTS & VALIDATION (optionnel)
    ├── test_core.py
    ├── test_network.py
    └── README_tests.md
```

---

## Mapping Source → Unifié

### De `Nex-us-V` → `src/`
```
nexus_core.py          → src/core/
nexus_ai.py            → src/core/
nexus_memory.py        → src/core/
nexus_network.py       → src/network/
nexus_persistence.py   → src/persistence/
nexus_ml.py            → src/ml/
nexus_gui.py           → src/ui/
nexus_gui_launcher.py  → src/ui/
nexus_demo.py          → src/utils/
nexus_finance.py       → src/utils/
nexus_technologies.py  → src/utils/
nexus_surveillance.py  → src/utils/
requirements.txt       → config/
Nexus.spec             → config/
README_Nexus.md        → docs/README_NEXUS.md
```

### De `module` → `src/module/`
```
Lagrosseclef.py                    → src/module/
protocole de la seconde genèse.py  → src/module/protocole_seconde_genese.py
```

### De `2-Nex-us-V` → `templates/` + `data/db/`
```
index.html                         → templates/
nexus_persistence.db               → data/db/
```

### De `3-Nex-us-V` → `build/dist/`
```
Analysis-00.toc   → build/dist/
EXE-00.toc        → build/dist/
PKG-00.toc        → build/dist/
PYZ-00.pyz        → build/dist/
PYZ-00.toc        → build/dist/
xref-Nexus.html   → build/dist/
warn-Nexus.txt    → build/dist/
```

### De `4-Nex-us-V` → `build/lib/`
```
*.pyc files       → build/lib/
```

### De `5-Nex-us-V` → `build/runtime/`
```
pyimod*.pyc       → build/runtime/
struct.pyc        → build/runtime/
```

### De `6-Nex-us-V` → `build/cache/`
```
*.cpython-313.pyc → build/cache/
```

### De `7-Nex-us-V` → `templates/`
```
index.html        → templates/ (merged with 2-Nex-us-V)
```

### Données → `data/`
```
nexus_memory.json      → data/memory/
nexus_persistence.db   → data/db/
```

---

## Nomenclature & Conventions

### Python Modules
- Tous les modules utilisent l'importation absolue : `from src.core import ...`
- Chaque dossier contient un `__init__.py` pour packager Python
- Fichiers nommés en `snake_case`

### Fichiers de Config
- `*.spec` : PyInstaller specifications
- `*.txt` : Listes de dépendances (requirements)
- `*.py` : Scripts de setup

### Documentation
- `README.md` : Guide principal pour chaque dossier
- `*.md` : Documentation markdown structurée

### Données
- `.json` : Snapshots mémoire (texte, versionnable)
- `.db` : Bases de données SQLite (binaire, archivé)

---

## Propriété & Versionnage

**Propriétaire** : Jonathan Therrien (Wanderer881101)  
**Créé** : 2026-08-11  
**Version** : 1.0 (Agrégation initiale)  
**Licence** : © 2026 Tous droits réservés

---

**Note** : Cette structure maximise la clarté, maintenabilité et scalabilité tout en préservant l'intégrité de tous les artefacts originaux.
