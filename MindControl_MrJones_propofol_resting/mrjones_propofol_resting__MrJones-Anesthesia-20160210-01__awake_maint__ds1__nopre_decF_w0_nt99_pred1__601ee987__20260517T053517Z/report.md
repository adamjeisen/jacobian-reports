# mrjones_propofol_resting__MrJones-Anesthesia-20160210-01__awake_maint__ds1__nopre_decF_w0_nt99_pred1__601ee987__20260517T053517Z

- wandb group: [mrjones_propofol_resting__MrJones-Anesthesia-20160210-01__awake_maint__ds1__nopre_decF_w0_nt99_pred1__601ee987__20260517T053517Z](https://wandb.ai/JacobianODE/MindControl_MrJones_propofol_resting/groups/mrjones_propofol_resting__MrJones-Anesthesia-20160210-01__awake_maint__ds1__nopre_decF_w0_nt99_pred1__601ee987__20260517T053517Z)
- chosen cell: **`lc_lc1e-5__n_delays_15`** (trajectory val_loss (min over history) = 0.0408)
- cells reported: 20

**Description**: 21 cells: 3 n_delays × 7 loop_closure_weight at nt=0.99, ds=1, on MrJones-Anesthesia-20160210-01. n_delays ∈ {5, 10, 15}. loop_closure_weight ∈ {0, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1}. obs_noise_scale=0. 6-hour SLURM cap, migrate_to=mit_normal_gpu. All other knobs match the Mary-20160809 + MrJones-20160105 LC × nd siblings.

**Hypothesis**

```
The Mary-20160809 + MrJones-20160105 LC × nd sweeps both showed the
LC sweet spot in 1e-3 to 1e-1 with a late-bloomer at lc=1e-1, nd=10.
Expect MrJones-Anesthesia-20160210-01 to land in the same regime.
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

**Chosen run** (by `best_traj_loss`): `lc_lc1e-5__n_delays_15` (trajectory val_loss (min over history) = 0.0408). Hard criteria applied after relaxation: C1, C2, C3. Survivors / candidates: 13/20.

### Per-run results

| run_name | `n_delays` | `lc` | best_traj_loss | MASE | dec_corr_MASE | LC loss | n_dyn | fast_eig_frac |
|---|---|---|---|---|---|---|---|---|
| `lc_lc1e-5__n_delays_15` | 15 | — | 0.04084 | 2.4411 | 0.9638 | 12.423 | 166 | 0.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | — | 0.04118 | 2.4760 | 0.9737 | 9.304 | 139 | 0.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | — | 0.04142 | 2.4897 | 0.9747 | 0.002 | 139 | 0.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | — | 0.04155 | 2.4861 | 0.9748 | 0.194 | 139 | 0.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | — | 0.04166 | 2.4822 | 0.9983 | 9.183 | 113 | 0.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | — | 0.04189 | 2.5161 | 1.0008 | 0.000 | 113 | 0.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | — | 0.04263 | 2.4782 | 0.9732 | 0.000 | 139 | 0.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | — | 0.04304 | 2.4571 | 0.9728 | 109.832 | 139 | 0.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | — | 0.04334 | 2.4994 | 0.9662 | 80.658 | 166 | 0.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | — | 0.04340 | 2.5078 | 0.9664 | 0.003 | 166 | 0.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | — | 0.04377 | 2.5084 | 0.9670 | 0.000 | 166 | 0.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | — | 0.04434 | 2.5135 | 0.9666 | 0.000 | 166 | 0.0000 |
| `lc_lc0__n_delays_15` | 15 | — | 0.04538 | 2.4700 | 0.9656 | 704.748 | 166 | 0.0000 |
| `lc_lc0__n_delays_10` | 10 | — | 0.04587 | 2.4557 | 0.9736 | 496.605 | 139 | 0.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | — | 0.04643 | 2.4478 | 0.9845 | 32.324 | 113 | 0.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | — | 0.04648 | 2.4612 | 0.9863 | 0.023 | 113 | 0.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | — | 0.04657 | 2.4612 | 0.9858 | 0.001 | 113 | 0.0000 |
| `lc_lc0__n_delays_5` | 5 | — | 0.04782 | 2.4337 | 0.9811 | 239.027 | 113 | 0.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | — | 0.04908 | 2.4126 | 0.9717 | 0.000 | 113 | 0.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | — | 0.05606 | 2.5338 | 0.9644 | 0.000 | 139 | 0.0000 |

## Chosen run trajectory prediction

`lc_lc1e-5__n_delays_15` cell params: `{'lightning_kwargs': {'reconstruction_mode': 'uniform', 'loop_closure_weight': 1e-05}, 'n_delays': 15}`

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
| `lc_lc0__n_delays_10` | 10 | ? | 0.0463 | 2.4610 | — | 54.0000 |
| `lc_lc0__n_delays_15` | 15 | ? | 0.0455 | 2.4746 | — | 46.0000 |
| `lc_lc0__n_delays_5` | 5 | ? | 0.0478 | 2.4466 | — | 34.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | ? | 0.0429 | 2.4893 | — | 51.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | ? | 0.0438 | 2.5084 | — | 45.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | ? | 0.0419 | 2.5161 | — | 60.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | ? | 0.0561 | 2.5338 | — | 17.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | ? | 0.0444 | 2.4997 | — | 44.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | ? | 0.0491 | 2.4126 | — | 28.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | ? | 0.0414 | 2.4897 | — | 57.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | ? | 0.0434 | 2.5078 | — | 45.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | ? | 0.0466 | 2.4612 | — | 34.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | ? | 0.0417 | 2.4982 | — | 56.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | ? | 0.0465 | 2.4612 | — | 34.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | ? | 0.0413 | 2.4716 | — | 59.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | ? | 0.0410 | 2.4421 | — | 60.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | ? | 0.0417 | 2.4889 | — | 60.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | ? | 0.0432 | 2.4549 | — | 59.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | ? | 0.0436 | 2.4908 | — | 46.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | ? | 0.0464 | 2.4478 | — | 34.0000 |