# mrjones_propofol_resting__MrJones-Anesthesia-20160113-01__awake_maint__ds1__nopre_decF_w0_nt99_pred1__ec36721a__20260516T033521Z

- wandb group: [mrjones_propofol_resting__MrJones-Anesthesia-20160113-01__awake_maint__ds1__nopre_decF_w0_nt99_pred1__ec36721a__20260516T033521Z](https://wandb.ai/JacobianODE/MindControl_MrJones_propofol_resting/groups/mrjones_propofol_resting__MrJones-Anesthesia-20160113-01__awake_maint__ds1__nopre_decF_w0_nt99_pred1__ec36721a__20260516T033521Z)
- chosen cell: **`lc_lc1e-3__n_delays_10`** (trajectory val_loss (min over history) = 0.0427)
- cells reported: 21

**Description**: 21 cells: 3 n_delays × 7 loop_closure_weight at nt=0.99, ds=1, on MrJones-Anesthesia-20160113-01. n_delays ∈ {5, 10, 15}. loop_closure_weight ∈ {0, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1}. obs_noise_scale=0. 6-hour SLURM cap, migrate_to=mit_normal_gpu. All other knobs match the Mary-20160809 + MrJones-20160105 LC × nd siblings.

**Hypothesis**

```
The Mary-20160809 + MrJones-20160105 LC × nd sweeps both showed the
LC sweet spot in 1e-3 to 1e-1 with a late-bloomer at lc=1e-1, nd=10.
Expect MrJones-Anesthesia-20160113-01 to land in the same regime.
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

**Chosen run** (by `best_traj_loss`): `lc_lc1e-3__n_delays_10` (trajectory val_loss (min over history) = 0.0427). Hard criteria applied after relaxation: C1, C2, C3. Survivors / candidates: 12/21.

### Per-run results

| run_name | `n_delays` | `lc` | best_traj_loss | MASE | dec_corr_MASE | LC loss | n_dyn | fast_eig_frac |
|---|---|---|---|---|---|---|---|---|
| `lc_lc1e-3__n_delays_10` | 10 | — | 0.04273 | 2.2063 | 0.9571 | 0.003 | 153 | 0.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | — | 0.04369 | 2.2029 | 0.9492 | 0.221 | 186 | 0.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | — | 0.04471 | 2.2136 | 0.9607 | 0.229 | 153 | 0.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | — | 0.04485 | 2.2255 | 0.9604 | 0.001 | 153 | 0.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | — | 0.04503 | 2.2058 | 0.9599 | 12.151 | 153 | 0.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | — | 0.04511 | 2.2037 | 0.9492 | 18.143 | 186 | 0.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | — | 0.04522 | 2.2274 | 0.9612 | 0.000 | 153 | 0.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | — | 0.04579 | 2.2277 | 0.9514 | 0.003 | 186 | 0.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | — | 0.04664 | 2.2778 | 1.0036 | 0.000 | 123 | 0.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | — | 0.04671 | 2.2486 | 0.9971 | 6.368 | 123 | 0.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | — | 0.04686 | 2.2857 | 1.0069 | 0.000 | 123 | 0.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | — | 0.04701 | 2.2572 | 0.9970 | 0.096 | 123 | 0.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | — | 0.04721 | 2.2610 | 0.9971 | 0.003 | 123 | 0.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | — | 0.04781 | 2.2234 | 0.9893 | 58.136 | 123 | 0.0000 |
| `lc_lc0__n_delays_10` | 10 | — | 0.04858 | 2.1882 | 0.9584 | 362.144 | 153 | 0.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | — | 0.04901 | 2.2109 | 0.9580 | 73.545 | 153 | 0.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | — | 0.04920 | 2.2534 | 0.9535 | 0.000 | 186 | 0.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | — | 0.04928 | 2.2414 | 0.9526 | 0.000 | 186 | 0.0000 |
| `lc_lc0__n_delays_5` | 5 | — | 0.04928 | 2.2346 | 0.9966 | 239.240 | 123 | 0.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | — | 0.04944 | 2.2356 | 0.9516 | 108.397 | 186 | 0.0000 |
| `lc_lc0__n_delays_15` | 15 | — | 0.05156 | 2.2263 | 0.9511 | 482.307 | 186 | 0.0000 |

## Chosen run trajectory prediction

`lc_lc1e-3__n_delays_10` cell params: `{'lightning_kwargs': {'reconstruction_mode': 'uniform', 'loop_closure_weight': 0.001}, 'n_delays': 10}`

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
| `lc_lc0__n_delays_10` | 10 | ? | 0.0487 | 2.1933 | — | 62.0000 |
| `lc_lc0__n_delays_15` | 15 | ? | 0.0519 | 2.2254 | — | 48.0000 |
| `lc_lc0__n_delays_5` | 5 | ? | 0.0493 | 2.2346 | — | 54.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | ? | 0.0452 | 2.2274 | — | 62.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | ? | 0.0493 | 2.2414 | — | 47.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | ? | 0.0471 | 2.2894 | — | 55.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | ? | 0.0449 | 2.2255 | — | 62.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | ? | 0.0492 | 2.2534 | — | 46.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | ? | 0.0468 | 2.2826 | — | 55.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | ? | 0.0427 | 2.2063 | — | 80.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | ? | 0.0469 | 2.2335 | — | 56.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | ? | 0.0472 | 2.2610 | — | 49.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | ? | 0.0449 | 2.2227 | — | 62.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | ? | 0.0445 | 2.1997 | — | 66.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | ? | 0.0470 | 2.2572 | — | 49.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | ? | 0.0458 | 2.2118 | — | 61.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | ? | 0.0451 | 2.2037 | — | 58.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | ? | 0.0467 | 2.2486 | — | 50.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | ? | 0.0490 | 2.2109 | — | 49.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | ? | 0.0495 | 2.2348 | — | 48.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | ? | 0.0478 | 2.2311 | — | 50.0000 |