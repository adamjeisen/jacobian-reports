# mrjones_propofol_resting__MrJones-Anesthesia-20160301-01__awake_maint__ds1__nopre_decF_w0_nt99_pred1__f781b761__20260514T223018Z

- wandb group: [mrjones_propofol_resting__MrJones-Anesthesia-20160301-01__awake_maint__ds1__nopre_decF_w0_nt99_pred1__f781b761__20260514T223018Z](https://wandb.ai/JacobianODE/MindControl_MrJones_propofol_resting/groups/mrjones_propofol_resting__MrJones-Anesthesia-20160301-01__awake_maint__ds1__nopre_decF_w0_nt99_pred1__f781b761__20260514T223018Z)
- chosen cell: **`lc_lc1e-1__n_delays_5`** (trajectory val_loss (min over history) = 0.0428)
- cells reported: 21

**Description**: 21 cells: 3 n_delays × 7 loop_closure_weight at nt=0.99, ds=1, on MrJones-Anesthesia-20160301-01. n_delays ∈ {5, 10, 15}. loop_closure_weight ∈ {0, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1}. obs_noise_scale=0. 6-hour SLURM cap, migrate_to=mit_normal_gpu. All other knobs match the Mary-20160809 + MrJones-20160105 LC × nd siblings.

**Hypothesis**

```
The Mary-20160809 + MrJones-20160105 LC × nd sweeps both showed the
LC sweet spot in 1e-3 to 1e-1 with a late-bloomer at lc=1e-1, nd=10.
Expect MrJones-Anesthesia-20160301-01 to land in the same regime.
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

**Chosen run** (by `best_traj_loss`): `lc_lc1e-1__n_delays_5` (trajectory val_loss (min over history) = 0.0428). Hard criteria applied after relaxation: C1, C2, C3. Survivors / candidates: 12/21.

### Per-run results

| run_name | `n_delays` | `lc` | best_traj_loss | MASE | dec_corr_MASE | LC loss | n_dyn | fast_eig_frac |
|---|---|---|---|---|---|---|---|---|
| `lc_lc1e-1__n_delays_5` | 5 | — | 0.04281 | 2.2202 | 0.9945 | 0.000 | 128 | 0.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | — | 0.04525 | 2.1898 | 0.9510 | 0.269 | 186 | 0.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | — | 0.04562 | 2.1966 | 0.9545 | 0.000 | 186 | 0.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | — | 0.04634 | 2.1882 | 0.9598 | 0.322 | 155 | 0.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | — | 0.04636 | 2.2342 | 1.0125 | 0.000 | 128 | 0.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | — | 0.04639 | 2.2315 | 1.0108 | 0.001 | 128 | 0.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | — | 0.04674 | 2.1929 | 0.9608 | 0.001 | 155 | 0.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | — | 0.04718 | 2.2053 | 1.0029 | 0.111 | 128 | 0.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | — | 0.04774 | 2.1980 | 0.9609 | 0.002 | 155 | 0.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | — | 0.04776 | 2.2080 | 0.9517 | 0.001 | 186 | 0.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | — | 0.04784 | 2.2051 | 0.9641 | 0.000 | 155 | 0.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | — | 0.04790 | 2.2084 | 0.9501 | 0.007 | 186 | 0.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | — | 0.04821 | 2.2191 | 0.9528 | 7.348 | 186 | 0.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | — | 0.04831 | 2.1941 | 0.9585 | 12.372 | 155 | 0.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | — | 0.04869 | 2.1914 | 0.9490 | 137.864 | 186 | 0.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | — | 0.04882 | 2.1658 | 0.9906 | 2.489 | 128 | 0.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | — | 0.04951 | 2.1415 | 0.9795 | 31.087 | 128 | 0.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | — | 0.04960 | 2.1732 | 0.9597 | 95.012 | 155 | 0.0000 |
| `lc_lc0__n_delays_15` | 15 | — | 0.05076 | 2.1845 | 0.9499 | 634.096 | 186 | 0.0000 |
| `lc_lc0__n_delays_5` | 5 | — | 0.05076 | 2.1467 | 0.9860 | 199.934 | 128 | 0.0000 |
| `lc_lc0__n_delays_10` | 10 | — | 0.05362 | 2.1902 | 0.9587 | 338.329 | 155 | 0.0000 |

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
| `lc_lc0__n_delays_10` | 10 | ? | 0.0540 | 2.1983 | — | 43.0000 |
| `lc_lc0__n_delays_15` | 15 | ? | 0.0513 | 2.1799 | — | 53.0000 |
| `lc_lc0__n_delays_5` | 5 | ? | 0.0508 | 2.1593 | — | 39.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | ? | 0.0478 | 2.2051 | — | 61.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | ? | 0.0456 | 2.1966 | — | 58.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | ? | 0.0429 | 2.2161 | — | 78.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | ? | 0.0467 | 2.1929 | — | 62.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | ? | 0.0478 | 2.2080 | — | 48.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | ? | 0.0464 | 2.2342 | — | 49.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | ? | 0.0477 | 2.1980 | — | 60.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | ? | 0.0479 | 2.2084 | — | 48.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | ? | 0.0464 | 2.2315 | — | 49.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | ? | 0.0466 | 2.1882 | — | 67.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | ? | 0.0458 | 2.1870 | — | 59.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | ? | 0.0475 | 2.2290 | — | 45.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | ? | 0.0485 | 2.1996 | — | 59.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | ? | 0.0488 | 2.2075 | — | 47.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | ? | 0.0491 | 2.1759 | — | 39.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | ? | 0.0501 | 2.1871 | — | 59.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | ? | 0.0487 | 2.1914 | — | 48.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | ? | 0.0498 | 2.1678 | — | 39.0000 |