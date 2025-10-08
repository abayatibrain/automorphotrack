# AutoMorphoTrack

**AutoMorphoTrack** is a modular image-analysis pipeline for automated detection, morphology classification, shape profiling, motility tracking, and colocalization analysis of mitochondria and lysosomes in multichannel fluorescence microscopy data.

Developed by **Armin Bayati, Ph.D.**

---

## 🧬 Overview

AutoMorphoTrack processes time-lapse `.tif` stacks (typically two-channel: mitochondria + lysosomes) and generates publication-ready visual and quantitative outputs at every step.

**Pipeline stages:**

1. **Detection** – Organelle segmentation and outline visualization  
2. **Lysosomal Counting** – Per-frame lysosome counts and plots  
3. **Morphology Classification** – Elongated vs. punctate mitochondria  
4. **Shape Feature Extraction** – Circularity, solidity, aspect ratio, orientation  
5. **Shape Profiling** – Combined violin plots of mitochondrial and lysosomal metrics  
6. **Tracking** – Cumulative organelle trajectories (mitochondria, lysosomes, composite)  
7. **Tracking Overlay** – Tracks drawn on real-intensity images  
8. **Motility Analysis** – Velocity and displacement distributions + scatter plots  
9. **Colocalization** – Bright-blue overlap visualization with Manders and Pearson coefficients  
10. **Integrated Summary** – Correlation matrix across all extracted metrics  

---

## 📁 Installation

```bash
pip install automorphotrack
```

Or clone directly:

```bash
git clone https://github.com/abayatibrain/AutoMorphoTrack.git
cd AutoMorphoTrack
pip install -e .
```

---

## 🚀 Basic Usage

```python
from automorphotrack import *

tif_path = "Composite.tif"

detect_organelles(tif_path)
count_lysosomes_per_frame(tif_path)
classify_morphology(tif_path)
analyze_shape_features(tif_path)
profile_shape_data()
track_organelles(tif_path)
track_overlay(tif_path)
analyze_motility()
analyze_colocalization(tif_path)
summarize_integrated_data()
```

---

## 📦 Outputs

| Step | Output Type | Example Files |
|------|--------------|---------------|
| Detection | PNG + MP4 | `Mito_Frame0.png`, `Mitochondria_Detection.mp4` |
| Lysosome Count | PNG + CSV + MP4 | `Lyso_Count_Plot.png`, `Lysosome_Counts.csv` |
| Morphology | PNG + MP4 + CSV | `Morphology_Frame0_Labeled.png`, `Morphology_Labeled.mp4` |
| Shape Features | PNG + CSV | `Shape_Distributions.png`, `Mito_ShapeMetrics.csv` |
| Shape Profiling | PNG + CSV | `Shape_ViolinPlots.png`, `Combined_ShapeData.csv` |
| Tracking | PNG + MP4 + CSV | `Cumulative_Mito.png`, `Mito_Tracks.csv` |
| Tracking Overlay | PNG + MP4 | `Cumulative_Composite.png`, `Composite_CumulativeTracks.mp4` |
| Motility | PNG + CSV | `Motility_Distributions.png`, `Motility_Scatter.png` |
| Colocalization | PNG + MP4 + CSV | `Colocalization_Frame0.png`, `Colocalization.csv` |
| Summary | PNG + CSV | `Integrated_CorrelationMatrix.png`, `Integrated_Merged_Data.csv` |

---

## 🔧 Dependencies

- Python ≥ 3.9  
- numpy, pandas, matplotlib, seaborn, opencv-python, scikit-image, scipy, tifffile

---

## 🧩 Citation

If you use this pipeline in your work, please cite:

> **Bayati, A. et al.** AutoMorphoTrack: Automated Organelle Tracking and Morphometric Profiling Toolkit (2025)
