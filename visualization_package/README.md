# Visualization package – fruit decay-stage systematic review

## Folders
- `figures/` – fig1–fig7 as used in the manuscript (PNG, 200 dpi). Fig 6 = QUADAS-2 stacked bars (% Low/Unclear/High per domain).
- `data/` – the numbers behind each figure (`fig2_…`, `fig3_…`, `fig4_…`, `fig5_…`, `fig6_…`, `fig7_…` CSV), per-study QUADAS-2 ratings with rationale (`quadas2_per_study.csv`), included/excluded study lists, and `summary_statistics.json` (all statistics quoted in the text).
- `tables/` – Table 3.6 (QUADAS-2 per study) as CSV, the manuscript tables exported as CSV, and the supplementary workbook.
- `code/` – `data.py` (verified per-study data model, 41 included / 19 excluded), `stats.py` (counts, Wilson CIs, Spearman, Kruskal–Wallis, Mann–Whitney, QUADAS-2 overall rule, Δ), `figs.py` (all figures), `export_data.py` (CSV export).

## Run
`sh run_all.sh` (pip install -r requirements.txt first). Figures are rewritten to `figures/`, CSVs to `data/`.

## Conventions
- QUADAS-2 overall: High if any of D1–D4 is High; Low only if all four Low; otherwise Unclear. Applicability A1–A3 reported separately.
- Best accuracy = highest top-1 accuracy on held-out, unperturbed data (mAP, pixel accuracy, R² excluded); n = 31.
- Δ = in-distribution minus shifted accuracy (percentage points); 6 values from 3 studies, not pooled.
- Wilson 95% CIs for proportions; two-sided tests, α = 0.05, no multiplicity adjustment.
- Colours: palette slots 2a78d6 / eb6834 / 1baf7a (Low = green, Unclear = grey, High = orange).
