# mrjones_propofol_resting__MrJones-Anesthesia-20160105-01__awake_maint__ds1__nopre_decF_w0_nt99_pred1__0d7ad14d__20260514T123016Z

- wandb group: [mrjones_propofol_resting__MrJones-Anesthesia-20160105-01__awake_maint__ds1__nopre_decF_w0_nt99_pred1__0d7ad14d__20260514T123016Z](https://wandb.ai/JacobianODE/MindControl_MrJones_propofol_resting/groups/mrjones_propofol_resting__MrJones-Anesthesia-20160105-01__awake_maint__ds1__nopre_decF_w0_nt99_pred1__0d7ad14d__20260514T123016Z)
- chosen cell: **`lc_lc1e-1__n_delays_10`** (trajectory val_loss (min over history) = 0.0479)
- cells reported: 21

**Description**: 21 cells: 3 n_delays × 7 loop_closure_weight at nt=0.99, ds=1, on MrJones-Anesthesia-20160105-01. n_delays ∈ {5, 10, 15} = top-3 from the MrJones nd Stage-1 sweep at nt=0.99. loop_closure_weight ∈ {0, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1}. obs_noise_scale=0 (Mary pilot showed >0 hurts; reasonable to assume the same for MrJones). 6-hour SLURM cap, migrate_to=mit_normal_gpu. All other knobs match the Mary 21-cell sibling.

**Hypothesis**

```
The Mary-20160809 LC × nd nt99 sweep showed the LC sweet spot at
1e-3 to 1e-2 across all 3 n_delays. We expect the MrJones LC
sweet spot to fall in the same range, with the absolute best
n_delays plausibly differing (Mary preferred nd=5, MrJones Stage 1
preferred nd=10). If MrJones shows a wildly different LC optimum
that's important to know before scaling to remaining sessions.
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

**Chosen run** (by `best_traj_loss`): `lc_lc1e-1__n_delays_10` (trajectory val_loss (min over history) = 0.0479). Hard criteria applied after relaxation: C1, C2, C3. Survivors / candidates: 8/21.

### Per-run results

| run_name | `n_delays` | `lc` | best_traj_loss | MASE | dec_corr_MASE | LC loss | n_dyn | fast_eig_frac |
|---|---|---|---|---|---|---|---|---|
| `lc_lc1e-1__n_delays_10` | 10 | — | 0.04792 | 2.0431 | 0.9540 | 0.000 | 176 | 0.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | — | 0.04974 | 2.0474 | 0.9508 | 1.019 | 176 | 0.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | — | 0.04982 | 2.0497 | 0.9525 | 0.001 | 176 | 0.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | — | 0.04999 | 2.0554 | 0.9521 | 0.004 | 176 | 0.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | — | 0.05087 | 2.0436 | 0.9471 | 26.813 | 176 | 0.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | — | 0.05145 | 2.0409 | 0.9429 | 0.002 | 216 | 0.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | — | 0.05165 | 2.1293 | 1.0066 | 0.000 | 140 | 0.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | — | 0.05173 | 2.1279 | 1.0049 | 0.002 | 140 | 0.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | — | 0.05177 | 2.1184 | 1.0014 | 1.388 | 140 | 0.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | — | 0.05229 | 2.0318 | 0.9388 | 0.005 | 216 | 0.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | — | 0.05282 | 2.1434 | 1.0088 | 0.000 | 140 | 0.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | — | 0.05352 | 2.0306 | 0.9464 | 202.868 | 176 | 0.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | — | 0.05449 | 2.0686 | 0.9816 | 22.651 | 140 | 0.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | — | 0.05646 | 2.1031 | 0.9427 | 0.263 | 216 | 0.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | — | 0.05663 | 2.0965 | 0.9398 | 23.960 | 216 | 0.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | — | 0.05743 | 2.1150 | 0.9472 | 0.000 | 216 | 0.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | — | 0.05794 | 2.0376 | 0.9737 | 164.675 | 140 | 0.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | — | 0.05799 | 2.0346 | 0.9372 | 344.795 | 216 | 0.0000 |
| `lc_lc0__n_delays_5` | 5 | — | 0.06121 | 2.0245 | 0.9766 | 572.772 | 140 | 0.0000 |
| `lc_lc0__n_delays_15` | 15 | — | 0.06407 | 2.0734 | 0.9414 | 1214.387 | 216 | 0.0000 |
| `lc_lc0__n_delays_10` | 10 | — | 0.06547 | 2.0597 | 0.9353 | 299.535 | 176 | 0.0000 |

## Chosen run trajectory prediction

`lc_lc1e-1__n_delays_10` cell params: `{'lightning_kwargs': {'reconstruction_mode': 'uniform', 'loop_closure_weight': 0.1}, 'n_delays': 10}`

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
| `lc_lc0__n_delays_10` | 10 | ? | 0.0655 | 2.1234 | — | 20.0000 |
| `lc_lc0__n_delays_15` | 15 | ? | 0.0647 | 2.0503 | — | 36.0000 |
| `lc_lc0__n_delays_5` | 5 | ? | 0.0623 | 2.0303 | — | 44.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | ? | 0.0479 | 2.0431 | — | 72.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | ? | 0.0578 | 2.0858 | — | 42.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | ? | 0.0528 | 2.1434 | — | 52.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | ? | 0.0498 | 2.0497 | — | 56.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | ? | 0.0514 | 2.0409 | — | 52.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | ? | 0.0531 | 2.1407 | — | 57.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | ? | 0.0502 | 2.0553 | — | 55.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | ? | 0.0523 | 2.0318 | — | 51.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | ? | 0.0533 | 2.1446 | — | 57.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | ? | 0.0499 | 2.0536 | — | 54.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | ? | 0.0565 | 2.1031 | — | 41.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | ? | 0.0534 | 2.1292 | — | 57.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | ? | 0.0510 | 2.0252 | — | 53.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | ? | 0.0570 | 2.0514 | — | 42.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | ? | 0.0545 | 2.0686 | — | 45.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | ? | 0.0544 | 2.0052 | — | 53.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | ? | 0.0592 | 2.0295 | — | 45.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | ? | 0.0583 | 2.0405 | — | 43.0000 |