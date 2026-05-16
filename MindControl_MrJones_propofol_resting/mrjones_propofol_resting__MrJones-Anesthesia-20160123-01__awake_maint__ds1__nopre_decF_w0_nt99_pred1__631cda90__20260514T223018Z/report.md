# mrjones_propofol_resting__MrJones-Anesthesia-20160123-01__awake_maint__ds1__nopre_decF_w0_nt99_pred1__631cda90__20260514T223018Z

- wandb group: [mrjones_propofol_resting__MrJones-Anesthesia-20160123-01__awake_maint__ds1__nopre_decF_w0_nt99_pred1__631cda90__20260514T223018Z](https://wandb.ai/JacobianODE/MindControl_MrJones_propofol_resting/groups/mrjones_propofol_resting__MrJones-Anesthesia-20160123-01__awake_maint__ds1__nopre_decF_w0_nt99_pred1__631cda90__20260514T223018Z)
- chosen cell: **`lc_lc1e-5__n_delays_10`** (trajectory val_loss (min over history) = 0.0370)
- cells reported: 21

**Description**: 21 cells: 3 n_delays × 7 loop_closure_weight at nt=0.99, ds=1, on MrJones-Anesthesia-20160123-01. n_delays ∈ {5, 10, 15}. loop_closure_weight ∈ {0, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1}. obs_noise_scale=0. 6-hour SLURM cap, migrate_to=mit_normal_gpu. All other knobs match the Mary-20160809 + MrJones-20160105 LC × nd siblings.

**Hypothesis**

```
The Mary-20160809 + MrJones-20160105 LC × nd sweeps both showed the
LC sweet spot in 1e-3 to 1e-1 with a late-bloomer at lc=1e-1, nd=10.
Expect MrJones-Anesthesia-20160123-01 to land in the same regime.
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

**Chosen run** (by `best_traj_loss`): `lc_lc1e-5__n_delays_10` (trajectory val_loss (min over history) = 0.0370). Hard criteria applied after relaxation: C1, C2, C3. Survivors / candidates: 15/21.

### Per-run results

| run_name | `n_delays` | `lc` | best_traj_loss | MASE | dec_corr_MASE | LC loss | n_dyn | fast_eig_frac |
|---|---|---|---|---|---|---|---|---|
| `lc_lc1e-5__n_delays_10` | 10 | — | 0.03703 | 2.3992 | 0.9613 | 7.573 | 133 | 0.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | — | 0.03889 | 2.4278 | 0.9665 | 0.215 | 133 | 0.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | — | 0.03898 | 2.4306 | 0.9670 | 0.003 | 133 | 0.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | — | 0.03909 | 2.4331 | 0.9672 | 0.000 | 133 | 0.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | — | 0.03912 | 2.4122 | 0.9649 | 38.239 | 133 | 0.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | — | 0.03922 | 2.4335 | 0.9676 | 0.000 | 133 | 0.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | — | 0.04003 | 2.4664 | 0.9625 | 8.066 | 157 | 0.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | — | 0.04034 | 2.4733 | 0.9640 | 0.001 | 157 | 0.0000 |
| `lc_lc0__n_delays_10` | 10 | — | 0.04075 | 2.4201 | 0.9652 | 142.509 | 133 | 0.0000 |
| `lc_lc0__n_delays_5` | 5 | — | 0.04281 | 2.3800 | 0.9941 | 109.281 | 109 | 0.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | — | 0.04318 | 2.4914 | 0.9616 | 47.719 | 157 | 0.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | — | 0.04352 | 2.4944 | 0.9623 | 0.095 | 157 | 0.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | — | 0.04365 | 2.5030 | 0.9608 | 0.000 | 157 | 0.0000 |
| `lc_lc0__n_delays_15` | 15 | — | 0.04370 | 2.4949 | 0.9614 | 209.874 | 157 | 0.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | — | 0.04396 | 2.4972 | 0.9637 | 0.001 | 157 | 0.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | — | 0.04455 | 2.3857 | 0.9927 | 2.202 | 109 | 0.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | — | 0.04479 | 2.3756 | 0.9902 | 22.124 | 109 | 0.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | — | 0.04501 | 2.3732 | 0.9855 | 0.052 | 109 | 0.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | — | 0.04517 | 2.3811 | 0.9873 | 0.000 | 109 | 0.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | — | 0.04542 | 2.3890 | 0.9869 | 0.001 | 109 | 0.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | — | 0.04550 | 2.3887 | 0.9899 | 0.000 | 109 | 0.0000 |

## Chosen run trajectory prediction

`lc_lc1e-5__n_delays_10` cell params: `{'lightning_kwargs': {'reconstruction_mode': 'uniform', 'loop_closure_weight': 1e-05}, 'n_delays': 10}`

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
| `lc_lc0__n_delays_10` | 10 | ? | 0.0407 | 2.4201 | — | 56.0000 |
| `lc_lc0__n_delays_15` | 15 | ? | 0.0437 | 2.4949 | — | 44.0000 |
| `lc_lc0__n_delays_5` | 5 | ? | 0.0429 | 2.3923 | — | 58.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | ? | 0.0392 | 2.4335 | — | 65.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | ? | 0.0436 | 2.5030 | — | 48.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | ? | 0.0455 | 2.3887 | — | 42.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | ? | 0.0398 | 2.4327 | — | 64.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | ? | 0.0405 | 2.4708 | — | 63.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | ? | 0.0452 | 2.3811 | — | 42.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | ? | 0.0397 | 2.4304 | — | 64.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | ? | 0.0446 | 2.5137 | — | 47.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | ? | 0.0454 | 2.3890 | — | 41.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | ? | 0.0396 | 2.4281 | — | 64.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | ? | 0.0440 | 2.5116 | — | 47.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | ? | 0.0450 | 2.3732 | — | 42.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | ? | 0.0370 | 2.3992 | — | 83.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | ? | 0.0405 | 2.4619 | — | 63.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | ? | 0.0448 | 2.3709 | — | 45.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | ? | 0.0391 | 2.4180 | — | 65.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | ? | 0.0432 | 2.4914 | — | 45.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | ? | 0.0448 | 2.3668 | — | 45.0000 |