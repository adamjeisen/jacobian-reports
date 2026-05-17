# mrjones_propofol_resting__MrJones-Anesthesia-20160125-01__awake_maint__ds1__nopre_decF_w0_nt99_pred1__8b8858a0__20260516T033521Z

- wandb group: [mrjones_propofol_resting__MrJones-Anesthesia-20160125-01__awake_maint__ds1__nopre_decF_w0_nt99_pred1__8b8858a0__20260516T033521Z](https://wandb.ai/JacobianODE/MindControl_MrJones_propofol_resting/groups/mrjones_propofol_resting__MrJones-Anesthesia-20160125-01__awake_maint__ds1__nopre_decF_w0_nt99_pred1__8b8858a0__20260516T033521Z)
- chosen cell: **`lc_lc1e-4__n_delays_10`** (trajectory val_loss (min over history) = 0.0440)
- cells reported: 21

**Description**: 21 cells: 3 n_delays × 7 loop_closure_weight at nt=0.99, ds=1, on MrJones-Anesthesia-20160125-01. n_delays ∈ {5, 10, 15}. loop_closure_weight ∈ {0, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1}. obs_noise_scale=0. 6-hour SLURM cap, migrate_to=mit_normal_gpu. All other knobs match the Mary-20160809 + MrJones-20160105 LC × nd siblings.

**Hypothesis**

```
The Mary-20160809 + MrJones-20160105 LC × nd sweeps both showed the
LC sweet spot in 1e-3 to 1e-1 with a late-bloomer at lc=1e-1, nd=10.
Expect MrJones-Anesthesia-20160125-01 to land in the same regime.
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

**Chosen run** (by `best_traj_loss`): `lc_lc1e-4__n_delays_10` (trajectory val_loss (min over history) = 0.0440). Hard criteria applied after relaxation: C1, C2, C3. Survivors / candidates: 12/21.

### Per-run results

| run_name | `n_delays` | `lc` | best_traj_loss | MASE | dec_corr_MASE | LC loss | n_dyn | fast_eig_frac |
|---|---|---|---|---|---|---|---|---|
| `lc_lc1e-4__n_delays_10` | 10 | — | 0.04404 | 2.1062 | 0.9523 | 0.884 | 164 | 0.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | — | 0.04499 | 2.1176 | 0.9540 | 0.000 | 164 | 0.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | — | 0.04552 | 2.1242 | 0.9526 | 18.588 | 164 | 0.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | — | 0.04568 | 2.1219 | 0.9544 | 0.006 | 164 | 0.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | — | 0.04590 | 2.1268 | 0.9564 | 0.001 | 164 | 0.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | — | 0.04613 | 2.1761 | 0.9924 | 1.245 | 133 | 0.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | — | 0.04623 | 2.1814 | 0.9944 | 0.000 | 133 | 0.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | — | 0.04627 | 2.1814 | 0.9930 | 0.006 | 133 | 0.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | — | 0.04694 | 2.1375 | 0.9812 | 32.556 | 133 | 0.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | — | 0.04717 | 2.1035 | 0.9475 | 175.971 | 164 | 0.0000 |
| `lc_lc0__n_delays_10` | 10 | — | 0.05070 | 2.0779 | 0.9493 | 863.785 | 164 | 0.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | — | 0.05108 | 2.1347 | 0.9486 | 0.001 | 196 | 0.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | — | 0.05122 | 2.1494 | 0.9959 | 124.323 | 133 | 0.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | — | 0.05177 | 2.1656 | 0.9491 | 0.983 | 196 | 0.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | — | 0.05210 | 2.1696 | 0.9500 | 0.024 | 196 | 0.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | — | 0.05309 | 2.1722 | 0.9525 | 0.000 | 196 | 0.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | — | 0.05334 | 2.1490 | 0.9460 | 24.362 | 196 | 0.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | — | 0.05446 | 2.1450 | 0.9453 | 175.377 | 196 | 0.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | — | 0.05492 | 2.0443 | 0.9567 | 0.000 | 133 | 0.0000 |
| `lc_lc0__n_delays_5` | 5 | — | 0.05580 | 2.0442 | 0.9562 | 252.305 | 133 | 0.0000 |
| `lc_lc0__n_delays_15` | 15 | — | 0.05675 | 2.1370 | 0.9472 | 819.780 | 196 | 0.0000 |

## Chosen run trajectory prediction

`lc_lc1e-4__n_delays_10` cell params: `{'lightning_kwargs': {'reconstruction_mode': 'uniform', 'loop_closure_weight': 0.0001}, 'n_delays': 10}`

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
| `lc_lc0__n_delays_10` | 10 | ? | 0.0516 | 2.0774 | — | 64.0000 |
| `lc_lc0__n_delays_15` | 15 | ? | 0.0567 | 2.1370 | — | 47.0000 |
| `lc_lc0__n_delays_5` | 5 | ? | 0.0565 | 2.0765 | — | 32.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | ? | 0.0450 | 2.1176 | — | 63.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | ? | 0.0531 | 2.1722 | — | 47.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | ? | 0.0557 | 2.1327 | — | 33.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | ? | 0.0461 | 2.1275 | — | 57.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | ? | 0.0512 | 2.1458 | — | 57.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | ? | 0.0469 | 2.1866 | — | 72.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | ? | 0.0459 | 2.1240 | — | 57.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | ? | 0.0521 | 2.1696 | — | 47.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | ? | 0.0469 | 2.1833 | — | 72.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | ? | 0.0441 | 2.1148 | — | 64.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | ? | 0.0518 | 2.1656 | — | 47.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | ? | 0.0467 | 2.1773 | — | 72.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | ? | 0.0456 | 2.1179 | — | 57.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | ? | 0.0537 | 2.1592 | — | 46.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | ? | 0.0469 | 2.1375 | — | 76.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | ? | 0.0478 | 2.1078 | — | 57.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | ? | 0.0549 | 2.1480 | — | 46.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | ? | 0.0520 | 2.1574 | — | 51.0000 |