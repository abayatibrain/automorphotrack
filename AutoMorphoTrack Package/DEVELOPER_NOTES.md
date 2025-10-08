# Developer Notes – AutoMorphoTrack

This document provides internal details for extending or maintaining the AutoMorphoTrack package.

---

## 🧩 Module Overview

| Module | Purpose | Key Outputs |
|---------|----------|--------------|
| utils.py | Shared utilities: saving, scaling, directory creation | Figures, videos, helper functions |
| detection.py | Organelle segmentation & outline drawing | PNG + MP4 |
| lyso_count.py | Per-frame lysosome counts | CSV + plot + video |
| morphology.py | E/P classification of mitochondria | CSV + labeled PNG + MP4 |
| shape_features.py | Extraction of morphological descriptors | CSV + KDE plots |
| shape_profiling.py | Combined shape comparison | CSV + violin plots |
| tracking.py | Cumulative trajectory plotting | CSV + MP4 + PNG |
| tracking_overlay.py | Tracks on real-intensity images | MP4 + PNG |
| motility.py | Velocity & displacement analysis | CSV + scatter/distribution plots |
| colocalization.py | Manders + Pearson overlap | CSV + MP4 + metrics plot |
| summary.py | Integrated cross-metric correlation | CSV + heatmap |

---

## ⚙️ Typical Directory Structure

```
Project/
├── Composite.tif
├── Detection_Outputs/
├── Lyso_Count_Outputs/
├── Morphology_Outputs/
├── Shape_Feature_Outputs/
├── Shape_Profiling_Outputs/
├── Tracking_Outputs/
├── TrackingOverlay_Outputs/
├── Motility_Outputs/
├── Colocalization_Outputs/
└── Summary_Outputs/
```

---

## 🧪 Testing

To test a module individually:

```python
from automorphotrack import morphology
morphology.classify_morphology("Composite.tif")
```

Run all modules sequentially in the example Jupyter notebook.

---

## 🧰 Build & Distribution

```bash
python setup.py sdist bdist_wheel
pip install dist/AutoMorphoTrack-1.0.0-py3-none-any.whl
```

---

## 📧 Maintainer

**Armin Bayati, Ph.D.**  
Harvard Medical School / Massachusetts General Hospital  
2025
