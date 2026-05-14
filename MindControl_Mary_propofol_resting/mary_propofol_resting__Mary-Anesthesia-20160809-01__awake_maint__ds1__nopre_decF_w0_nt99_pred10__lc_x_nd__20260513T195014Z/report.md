# mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__nopre_decF_w0_nt99_pred10__lc_x_nd__20260513T195014Z

- wandb group: [mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__nopre_decF_w0_nt99_pred10__lc_x_nd__20260513T195014Z](https://wandb.ai/JacobianODE/MindControl_Mary_propofol_resting/groups/mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__nopre_decF_w0_nt99_pred10__lc_x_nd__20260513T195014Z)
- chosen cell: **`lc_lc1e-4__n_delays_5`** (trajectory val_loss (min over history) = 0.0575)
- cells reported: 21

**Description**: 21 cells: 3 n_delays × 7 loop_closure_weight at nt=0.99, ds=1. n_delays ∈ {5, 10, 15} = top-3 from the prior nopre+pred10 ds×nd sweep at nt=0.99. loop_closure_weight ∈ {0, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1}. obs_noise_scale=0 (pilot showed >0 hurts). 6-hour SLURM cap, migrate_to=mit_normal_gpu so PENDING cells auto-move when the QOS budget allows. Other knobs match the prior nopre+pred10 baseline: pre_pca_per_area=false, decoded_only_pred_loss=False, encoder_warmup_epochs=0, batch_size=16, prediction_steps=10, seq_length=25, lp=80 Hz, awake + maintenance.

**Hypothesis**

```
Re-running the nt99 slice of the 42-cell lc×nd×nt sweep with a
longer SLURM cap + auto-migration is expected to (a) push training
past 50–60 epochs for all cells (the prior 6h cap was binding —
median epoch reached = 52) and (b) sharpen the LC sweet spot. We
expect 1e-3 to 1e-2 to remain the best LC range at nd=5,10 (it was
in the prior sweep), and lc=1e-1, nd=10 to confirm as a real
late-blooming peak (it was 4th-best by tv_final at the cap).
```

**Success criteria** (manual review until automated):

- [ ] All 21 cells run within the 6-hour SLURM cap (or TIMEOUT).
- [ ] val/one_step_mase finite for all cells.
- [ ] For each n_delays, at least one lc_weight > 0 strictly beats lc_weight = 0 on best trajectory val_loss.

## Run picking

![sweep overview](figures/sweep_overview.png)

Four panels: C1 (one-step MASE — uses `val/decoder_corrected_one_step_mase` per cell when available; threshold = 1 = decoded persistence baseline), C2 (loop closure — plots `LC / sqrt(n_dyn)` against y=1 when each cell carries its own `n_dyn`, otherwise raw LC vs the shared sqrt(n_dyn) line), C3 (fast eigenvalue fraction), trajectory val loss (min over training history). Bars are color-coded green = passes all selection criteria, red = excluded by some criterion, gold = the selected best run.

![sweep pareto](figures/sweep_pareto.png)

Pareto front in (loop closure loss, trajectory val loss) space. Gold star = the selected run.

**Chosen run** (by `best_traj_loss`): `lc_lc1e-4__n_delays_5` (trajectory val_loss (min over history) = 0.0575). Hard criteria applied after relaxation: C1, C2, C3. Survivors / candidates: 14/21.

### Per-run results

| run_name | `n_delays` | `lc` | best_traj_loss | MASE | dec_corr_MASE | LC loss | n_dyn | fast_eig_frac |
|---|---|---|---|---|---|---|---|---|
| `lc_lc1e-4__n_delays_5` | 5 | — | 0.05750 | 1.8387 | 0.9238 | 0.825 | 115 | 0.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | — | 0.05778 | 1.8480 | 0.9265 | 0.000 | 115 | 0.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | — | 0.05855 | 1.8556 | 0.9311 | 0.000 | 115 | 0.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | — | 0.05868 | 1.8405 | 0.9128 | 0.001 | 141 | 0.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | — | 0.05893 | 1.8445 | 0.9267 | 0.009 | 115 | 0.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | — | 0.06009 | 1.8321 | 0.9241 | 11.186 | 115 | 0.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | — | 0.06168 | 1.8329 | 0.9245 | 86.470 | 115 | 0.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | — | 0.06203 | 1.8515 | 0.9165 | 0.006 | 141 | 0.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | — | 0.06341 | 1.8687 | 0.9245 | 0.000 | 141 | 0.0000 |
| `lc_lc0__n_delays_5` | 5 | — | 0.06350 | 1.8379 | 0.9318 | 281.942 | 115 | 0.0000 |
| `lc_lc0__n_delays_10` | 10 | — | 0.06380 | 1.8271 | 0.9129 | 418.986 | 141 | 0.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | — | 0.06522 | 1.8525 | 0.9152 | 0.267 | 141 | 0.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | — | 0.06541 | 1.8611 | 0.9172 | 57.758 | 141 | 0.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | — | 0.06603 | 1.8507 | 0.9155 | 6.188 | 141 | 0.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | — | 0.06622 | 1.8226 | 0.9082 | 0.012 | 165 | 0.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | — | 0.07095 | 1.8450 | 0.9048 | 0.109 | 165 | 0.0000 |
| `lc_lc0__n_delays_15` | 15 | — | 0.07146 | 1.8416 | 0.9028 | 278.924 | 165 | 0.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | — | 0.07214 | 1.8535 | 0.9038 | 3.085 | 165 | 0.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | — | 0.07246 | 1.8518 | 0.9068 | 0.000 | 165 | 0.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | — | 0.07290 | 1.8491 | 0.9047 | 41.797 | 165 | 0.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | — | 0.07329 | 1.8620 | 0.9078 | 0.000 | 165 | 0.0000 |

## Chosen run trajectory prediction

`lc_lc1e-4__n_delays_5` cell params: `{'lightning_kwargs': {'reconstruction_mode': 'uniform', 'loop_closure_weight': 0.0001}, 'n_delays': 5}`

![chosen trajectory](figures/chosen_trajectory.png)

One row per condition. Window = the model's native training convention: `traj_init_steps` teacher-forced steps followed by `prediction_steps` autoregressive (alpha_TF=0) steps. Solid = ground-truth, dashed = autoregressive rollout. Left: latent space, projected onto top-3 PCs of rollout-window ground-truth latent. Right: observation space, projected onto top-3 PCs of rollout-window ground-truth obs. Color = PC index (`PC1=C0, PC2=C1, PC3=C2`). Vertical line = end of teacher forcing / start of autoregressive rollout.

## Chosen run Lyapunov spectrum (per condition)

![chosen lyap](figures/chosen_lyapunov.png)

Bars = mean ± std across the chosen-cell's trajectories within each condition. No empirical / GT comparison — for neural data we only have model-predicted exponents.

## Per-cell Lyapunov spectra

![per-cell lyap](figures/per_cell_lyapunov.png)

Each subplot is one cell's per-condition Lyapunov spectrum (mean across that cell's trajectories). Watch for monotone trends as `n_delays` increases and for any cell where the conditions cleanly separate.

## Chosen run cross-area block gramians (per pair)

For each ordered (source → target) area pair, we compute the reach / ctrl / obs gramians of the chosen run's predicted Jacobian's cross-area blocks. Bars show `log_trace` (top row) and `log_min_eig` (bottom row — the LOG of the SMALLEST eigenvalue, i.e. the bottleneck-dim energy) per condition, with SEM error bars across the cell's trajectories. Pure model side — no GT since neural data lacks a ground-truth dynamical model. `metric` mode is currently identical to `standard` (encoder-Jacobian B_factor / C_factor not yet plugged in).

### standard / full

#### 7b → CPB

![7b → CPB (standard/full)](figures/gramians_per_pair/gramian_pair__standard__full__7b_to_CPB.png)

#### 7b → FEF

![7b → FEF (standard/full)](figures/gramians_per_pair/gramian_pair__standard__full__7b_to_FEF.png)

#### 7b → vlPFC

![7b → vlPFC (standard/full)](figures/gramians_per_pair/gramian_pair__standard__full__7b_to_vlPFC.png)

#### CPB → 7b

![CPB → 7b (standard/full)](figures/gramians_per_pair/gramian_pair__standard__full__CPB_to_7b.png)

#### CPB → FEF

![CPB → FEF (standard/full)](figures/gramians_per_pair/gramian_pair__standard__full__CPB_to_FEF.png)

#### CPB → vlPFC

![CPB → vlPFC (standard/full)](figures/gramians_per_pair/gramian_pair__standard__full__CPB_to_vlPFC.png)

#### FEF → 7b

![FEF → 7b (standard/full)](figures/gramians_per_pair/gramian_pair__standard__full__FEF_to_7b.png)

#### FEF → CPB

![FEF → CPB (standard/full)](figures/gramians_per_pair/gramian_pair__standard__full__FEF_to_CPB.png)

#### FEF → vlPFC

![FEF → vlPFC (standard/full)](figures/gramians_per_pair/gramian_pair__standard__full__FEF_to_vlPFC.png)

#### vlPFC → 7b

![vlPFC → 7b (standard/full)](figures/gramians_per_pair/gramian_pair__standard__full__vlPFC_to_7b.png)

#### vlPFC → CPB

![vlPFC → CPB (standard/full)](figures/gramians_per_pair/gramian_pair__standard__full__vlPFC_to_CPB.png)

#### vlPFC → FEF

![vlPFC → FEF (standard/full)](figures/gramians_per_pair/gramian_pair__standard__full__vlPFC_to_FEF.png)

### standard / k20

#### 7b → CPB

![7b → CPB (standard/k20)](figures/gramians_per_pair/gramian_pair__standard__k20__7b_to_CPB.png)

#### 7b → FEF

![7b → FEF (standard/k20)](figures/gramians_per_pair/gramian_pair__standard__k20__7b_to_FEF.png)

#### 7b → vlPFC

![7b → vlPFC (standard/k20)](figures/gramians_per_pair/gramian_pair__standard__k20__7b_to_vlPFC.png)

#### CPB → 7b

![CPB → 7b (standard/k20)](figures/gramians_per_pair/gramian_pair__standard__k20__CPB_to_7b.png)

#### CPB → FEF

![CPB → FEF (standard/k20)](figures/gramians_per_pair/gramian_pair__standard__k20__CPB_to_FEF.png)

#### CPB → vlPFC

![CPB → vlPFC (standard/k20)](figures/gramians_per_pair/gramian_pair__standard__k20__CPB_to_vlPFC.png)

#### FEF → 7b

![FEF → 7b (standard/k20)](figures/gramians_per_pair/gramian_pair__standard__k20__FEF_to_7b.png)

#### FEF → CPB

![FEF → CPB (standard/k20)](figures/gramians_per_pair/gramian_pair__standard__k20__FEF_to_CPB.png)

#### FEF → vlPFC

![FEF → vlPFC (standard/k20)](figures/gramians_per_pair/gramian_pair__standard__k20__FEF_to_vlPFC.png)

#### vlPFC → 7b

![vlPFC → 7b (standard/k20)](figures/gramians_per_pair/gramian_pair__standard__k20__vlPFC_to_7b.png)

#### vlPFC → CPB

![vlPFC → CPB (standard/k20)](figures/gramians_per_pair/gramian_pair__standard__k20__vlPFC_to_CPB.png)

#### vlPFC → FEF

![vlPFC → FEF (standard/k20)](figures/gramians_per_pair/gramian_pair__standard__k20__vlPFC_to_FEF.png)

## Per-cell summary metrics

| run | n_delays | encoder_warmup | mean val loss | val/one_step_mase | val/total_loss | epoch |
|---|---|---|---|---|---|---|
| `lc_lc0__n_delays_10` | 10 | ? | 0.0638 | 1.8271 | — | 72.0000 |
| `lc_lc0__n_delays_15` | 15 | ? | 0.0721 | 1.8557 | — | 42.0000 |
| `lc_lc0__n_delays_5` | 5 | ? | 0.0642 | 1.8287 | — | 68.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | ? | 0.0634 | 1.8687 | — | 48.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | ? | 0.0757 | 1.8678 | — | 36.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | ? | 0.0585 | 1.8556 | — | 72.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | ? | 0.0599 | 1.8434 | — | 76.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | ? | 0.0735 | 1.8556 | — | 39.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | ? | 0.0578 | 1.8480 | — | 73.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | ? | 0.0650 | 1.8722 | — | 51.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | ? | 0.0664 | 1.8197 | — | 55.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | ? | 0.0598 | 1.8529 | — | 67.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | ? | 0.0654 | 1.8680 | — | 44.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | ? | 0.0719 | 1.8458 | — | 39.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | ? | 0.0581 | 1.8424 | — | 77.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | ? | 0.0700 | 1.8809 | — | 45.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | ? | 0.0721 | 1.8535 | — | 35.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | ? | 0.0612 | 1.8358 | — | 67.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | ? | 0.0654 | 1.8611 | — | 47.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | ? | 0.0730 | 1.8559 | — | 36.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | ? | 0.0631 | 1.8291 | — | 71.0000 |