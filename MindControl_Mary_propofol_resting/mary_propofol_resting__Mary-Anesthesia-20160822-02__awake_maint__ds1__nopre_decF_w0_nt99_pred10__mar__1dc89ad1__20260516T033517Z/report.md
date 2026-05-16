# mary_propofol_resting__Mary-Anesthesia-20160822-02__awake_maint__ds1__nopre_decF_w0_nt99_pred10__mar__1dc89ad1__20260516T033517Z

- wandb group: [mary_propofol_resting__Mary-Anesthesia-20160822-02__awake_maint__ds1__nopre_decF_w0_nt99_pred10__mar__1dc89ad1__20260516T033517Z](https://wandb.ai/JacobianODE/MindControl_Mary_propofol_resting/groups/mary_propofol_resting__Mary-Anesthesia-20160822-02__awake_maint__ds1__nopre_decF_w0_nt99_pred10__mar__1dc89ad1__20260516T033517Z)
- chosen cell: **`lc_lc1e-1__n_delays_5`** (trajectory val_loss (min over history) = 0.0458)
- cells reported: 21

**Description**: 21 cells: 3 n_delays × 7 loop_closure_weight at nt=0.99, ds=1, on Mary-Anesthesia-20160822-02. n_delays ∈ {5, 10, 15}. loop_closure_weight ∈ {0, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1}. obs_noise_scale=0. 6-hour SLURM cap, migrate_to=mit_normal_gpu. All other knobs match the Mary-20160809 + MrJones-20160105 LC × nd siblings.

**Hypothesis**

```
The Mary-20160809 + MrJones-20160105 LC × nd sweeps both showed the
LC sweet spot in 1e-3 to 1e-1 with a late-bloomer at lc=1e-1, nd=10.
Expect Mary-Anesthesia-20160822-02 to land in the same regime.
Variation across sessions in the precise LC peak + late-bloom epoch
is the whole point of running this on more sessions.
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

**Chosen run** (by `best_traj_loss`): `lc_lc1e-1__n_delays_5` (trajectory val_loss (min over history) = 0.0458). Hard criteria applied after relaxation: C1, C2, C3. Survivors / candidates: 15/21.

### Per-run results

| run_name | `n_delays` | `lc` | best_traj_loss | MASE | dec_corr_MASE | LC loss | n_dyn | fast_eig_frac |
|---|---|---|---|---|---|---|---|---|
| `lc_lc1e-1__n_delays_5` | 5 | — | 0.04577 | 2.1172 | 0.9467 | 0.000 | 97 | 0.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | — | 0.04638 | 2.1211 | 0.9479 | 0.000 | 97 | 0.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | — | 0.04747 | 2.1352 | 0.9434 | 0.001 | 116 | 0.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | — | 0.04781 | 2.1367 | 0.9439 | 0.000 | 116 | 0.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | — | 0.04798 | 2.0979 | 0.9416 | 1.645 | 97 | 0.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | — | 0.04807 | 2.1171 | 0.9406 | 0.759 | 116 | 0.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | — | 0.05241 | 2.0944 | 0.9382 | 132.694 | 116 | 0.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | — | 0.05293 | 2.0944 | 0.9543 | 62.739 | 97 | 0.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | — | 0.05306 | 2.1065 | 0.9518 | 0.002 | 97 | 0.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | — | 0.05323 | 2.1268 | 0.9377 | 0.004 | 116 | 0.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | — | 0.05349 | 2.1240 | 0.9366 | 4.413 | 116 | 0.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | — | 0.05392 | 2.1212 | 0.9368 | 0.000 | 135 | 0.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | — | 0.05443 | 2.1369 | 0.9329 | 7.914 | 135 | 0.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | — | 0.05499 | 2.1280 | 0.9326 | 0.010 | 135 | 0.0000 |
| `lc_lc0__n_delays_5` | 5 | — | 0.05548 | 2.0808 | 0.9511 | 520.445 | 97 | 0.0000 |
| `lc_lc0__n_delays_10` | 10 | — | 0.05581 | 2.1025 | 0.9369 | 623.679 | 116 | 0.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | — | 0.05624 | 2.1239 | 0.9343 | 0.070 | 135 | 0.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | — | 0.05672 | 2.0546 | 0.9304 | 1.311 | 97 | 0.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | — | 0.05703 | 2.1329 | 0.9367 | 0.000 | 135 | 0.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | — | 0.05760 | 2.1255 | 0.9304 | 104.507 | 135 | 0.0000 |
| `lc_lc0__n_delays_15` | 15 | — | 0.06065 | 2.1092 | 0.9299 | 1026.540 | 135 | 0.0000 |

## Chosen run trajectory prediction

`lc_lc1e-1__n_delays_5` cell params: `{'lightning_kwargs': {'reconstruction_mode': 'uniform', 'loop_closure_weight': 0.1}, 'n_delays': 5}`

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

### standard / k10

#### 7b → CPB

![7b → CPB (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__7b_to_CPB.png)

#### 7b → FEF

![7b → FEF (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__7b_to_FEF.png)

#### 7b → vlPFC

![7b → vlPFC (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__7b_to_vlPFC.png)

#### CPB → 7b

![CPB → 7b (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__CPB_to_7b.png)

#### CPB → FEF

![CPB → FEF (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__CPB_to_FEF.png)

#### CPB → vlPFC

![CPB → vlPFC (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__CPB_to_vlPFC.png)

#### FEF → 7b

![FEF → 7b (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__FEF_to_7b.png)

#### FEF → CPB

![FEF → CPB (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__FEF_to_CPB.png)

#### FEF → vlPFC

![FEF → vlPFC (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__FEF_to_vlPFC.png)

#### vlPFC → 7b

![vlPFC → 7b (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__vlPFC_to_7b.png)

#### vlPFC → CPB

![vlPFC → CPB (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__vlPFC_to_CPB.png)

#### vlPFC → FEF

![vlPFC → FEF (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__vlPFC_to_FEF.png)

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
| `lc_lc0__n_delays_10` | 10 | ? | 0.0579 | 2.0773 | — | 62.0000 |
| `lc_lc0__n_delays_15` | 15 | ? | 0.0609 | 2.0824 | — | 51.0000 |
| `lc_lc0__n_delays_5` | 5 | ? | 0.0576 | 2.0834 | — | 59.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | ? | 0.0482 | 2.1278 | — | 65.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | ? | 0.0560 | 2.1268 | — | 61.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | ? | 0.0462 | 2.1176 | — | 91.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | ? | 0.0475 | 2.1352 | — | 64.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | ? | 0.0570 | 2.1329 | — | 45.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | ? | 0.0470 | 2.1221 | — | 91.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | ? | 0.0547 | 2.1326 | — | 42.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | ? | 0.0557 | 2.1124 | — | 51.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | ? | 0.0545 | 2.1268 | — | 43.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | ? | 0.0484 | 2.1113 | — | 65.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | ? | 0.0562 | 2.1239 | — | 45.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | ? | 0.0484 | 2.1029 | — | 86.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | ? | 0.0551 | 2.1287 | — | 42.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | ? | 0.0552 | 2.1091 | — | 51.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | ? | 0.0574 | 2.0834 | — | 30.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | ? | 0.0530 | 2.0870 | — | 65.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | ? | 0.0577 | 2.1078 | — | 45.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | ? | 0.0542 | 2.0996 | — | 52.0000 |