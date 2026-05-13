# mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__nopre_decF_w0_pred10__lc_x_nd_x_nt__20260512T052513Z

- wandb group: [mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__nopre_decF_w0_pred10__lc_x_nd_x_nt__20260512T052513Z](https://wandb.ai/JacobianODE/MindControl_Mary_propofol_resting/groups/mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__nopre_decF_w0_pred10__lc_x_nd_x_nt__20260512T052513Z)
- chosen cell: **`lc_lc1e-4__nt_nd_nt95_nd10`** (trajectory val_loss (min over history) = 0.0897)
- cells reported: 21

**Description**: 42 cells: 6 (n_target_var_threshold, n_delays) bundles × 7 loop_closure_weight values. nt99 uses n_delays ∈ {5, 10, 15}, nt95 uses {10, 15, 20} — top-3 per nt by trajectory val_loss from the prior nopre+pred10 ds×nd sweeps. loop_closure_weight ∈ {0, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1}. obs_noise_scale=0 (default; pilot showed >0 hurts). Other knobs match prior nopre+pred10 baseline: pre_pca_per_area=false, decoded_only_pred_loss=False, encoder_warmup_epochs=0, batch_size=16, delay_spacing=1, prediction_steps=10, seq_length=25, lp=80 Hz, awake + maintenance.

**Hypothesis**

```
Loop-closure regularization should improve the conservativity of
the learned Jacobian field, which the JacobianODE paper argues
improves Jacobian estimation accuracy. We expect a non-monotone
response curve in lc_weight: too low and the constraint is
inactive, too high and the encoder may sacrifice forecasting
accuracy for trivial conservativity. The sweet spot probably
differs per (nt, n_delays) — we want to identify it for the
eventual production training recipe.
```

**Success criteria** (manual review until automated):

- [ ] All 42 cells run within the 6-hour SLURM cap (or TIMEOUT).
- [ ] val/one_step_mase finite for all cells.
- [ ] For each (nt, n_delays) bundle, at least one lc_weight > 0 strictly beats lc_weight = 0 on best trajectory val_loss.

## Run picking

![sweep overview](figures/sweep_overview.png)

Four panels: C1 (one-step MASE — uses `val/decoder_corrected_one_step_mase` per cell when available; threshold = 1 = decoded persistence baseline), C2 (loop closure — plots `LC / sqrt(n_dyn)` against y=1 when each cell carries its own `n_dyn`, otherwise raw LC vs the shared sqrt(n_dyn) line), C3 (fast eigenvalue fraction), trajectory val loss (min over training history). Bars are color-coded green = passes all selection criteria, red = excluded by some criterion, gold = the selected best run.

![sweep pareto](figures/sweep_pareto.png)

Pareto front in (loop closure loss, trajectory val loss) space. Gold star = the selected run.

**Chosen run** (by `best_traj_loss`): `lc_lc1e-4__nt_nd_nt95_nd10` (trajectory val_loss (min over history) = 0.0897). Hard criteria applied after relaxation: C1, C2, C3. Survivors / candidates: 15/21.

### Per-run results

| run_name | `nt_nd` | `lc` | best_traj_loss | MASE | dec_corr_MASE | LC loss | n_dyn | fast_eig_frac |
|---|---|---|---|---|---|---|---|---|
| `lc_lc1e-4__nt_nd_nt95_nd10` | — | — | 0.08967 | 3.4270 | 0.9903 | 0.348 | 39 | 0.0000 |
| `lc_lc1e-2__nt_nd_nt95_nd10` | — | — | 0.09015 | 3.4506 | 0.9913 | 0.001 | 39 | 0.0000 |
| `lc_lc1e-6__nt_nd_nt95_nd10` | — | — | 0.09047 | 3.4250 | 0.9900 | 31.882 | 39 | 0.0000 |
| `lc_lc1e-3__nt_nd_nt95_nd10` | — | — | 0.09055 | 3.4533 | 0.9919 | 0.010 | 39 | 0.0000 |
| `lc_lc1e-1__nt_nd_nt95_nd10` | — | — | 0.09092 | 3.4516 | 0.9919 | 0.000 | 39 | 0.0000 |
| `lc_lc1e-5__nt_nd_nt95_nd10` | — | — | 0.09137 | 3.4422 | 0.9920 | 4.136 | 39 | 0.0000 |
| `lc_lc0__nt_nd_nt95_nd10` | — | — | 0.09475 | 3.4246 | 0.9917 | 246.427 | 39 | 0.0000 |
| `lc_lc1e-6__nt_nd_nt95_nd15` | — | — | 0.09577 | 3.4273 | 0.9832 | 48.471 | 43 | 0.0000 |
| `lc_lc1e-1__nt_nd_nt95_nd15` | — | — | 0.09638 | 3.4484 | 0.9877 | 0.000 | 43 | 0.0000 |
| `lc_lc1e-4__nt_nd_nt95_nd15` | — | — | 0.09787 | 3.4485 | 0.9836 | 0.324 | 43 | 0.0000 |
| `lc_lc1e-5__nt_nd_nt95_nd15` | — | — | 0.09889 | 3.4532 | 0.9832 | 4.992 | 43 | 0.0000 |
| `lc_lc1e-3__nt_nd_nt95_nd15` | — | — | 0.09911 | 3.4579 | 0.9840 | 0.005 | 43 | 0.0000 |
| `lc_lc0__nt_nd_nt95_nd15` | — | — | 0.09956 | 3.4456 | 0.9822 | 425.076 | 43 | 0.0000 |
| `lc_lc1e-2__nt_nd_nt95_nd15` | — | — | 0.10095 | 3.4767 | 0.9838 | 0.001 | 43 | 0.0000 |
| `lc_lc1e-5__nt_nd_nt95_nd20` | — | — | 0.10245 | 3.5420 | 0.9829 | 3.919 | 49 | 0.0000 |
| `lc_lc1e-6__nt_nd_nt95_nd20` | — | — | 0.10281 | 3.5342 | 0.9815 | 38.305 | 49 | 0.0000 |
| `lc_lc0__nt_nd_nt95_nd20` | — | — | 0.10310 | 3.5538 | 0.9829 | 372.199 | 49 | 0.0000 |
| `lc_lc1e-4__nt_nd_nt95_nd20` | — | — | 0.10317 | 3.5559 | 0.9807 | 0.115 | 49 | 0.0000 |
| `lc_lc1e-2__nt_nd_nt95_nd20` | — | — | 0.10527 | 3.5468 | 0.9848 | 0.000 | 49 | 0.0000 |
| `lc_lc1e-3__nt_nd_nt95_nd20` | — | — | 0.10528 | 3.5663 | 0.9808 | 0.039 | 49 | 0.0000 |
| `lc_lc1e-1__nt_nd_nt95_nd20` | — | — | 0.10535 | 3.5414 | 0.9844 | 0.000 | 49 | 0.0000 |

## Chosen run trajectory prediction

`lc_lc1e-4__nt_nd_nt95_nd10` cell params: `{'lightning_kwargs': {'reconstruction_mode': 'uniform', 'loop_closure_weight': 0.0001}, 'n_target_var_threshold': 0.95, 'n_delays': 10}`

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
| `lc_lc0__nt_nd_nt95_nd10` | 10 | ? | 0.0959 | 3.4265 | — | 55.0000 |
| `lc_lc0__nt_nd_nt95_nd15` | 15 | ? | 0.1049 | 3.4634 | — | 43.0000 |
| `lc_lc0__nt_nd_nt95_nd20` | 20 | ? | 0.1049 | 3.5382 | — | 36.0000 |
| `lc_lc1e-1__nt_nd_nt95_nd10` | 10 | ? | 0.0918 | 3.4356 | — | 65.0000 |
| `lc_lc1e-1__nt_nd_nt95_nd15` | 15 | ? | 0.0983 | 3.4601 | — | 67.0000 |
| `lc_lc1e-1__nt_nd_nt95_nd20` | 20 | ? | 0.1053 | 3.5414 | — | 34.0000 |
| `lc_lc1e-2__nt_nd_nt95_nd10` | 10 | ? | 0.0901 | 3.4506 | — | 58.0000 |
| `lc_lc1e-2__nt_nd_nt95_nd15` | 15 | ? | 0.1031 | 3.4871 | — | 46.0000 |
| `lc_lc1e-2__nt_nd_nt95_nd20` | 20 | ? | 0.1053 | 3.5468 | — | 34.0000 |
| `lc_lc1e-3__nt_nd_nt95_nd10` | 10 | ? | 0.0912 | 3.4379 | — | 66.0000 |
| `lc_lc1e-3__nt_nd_nt95_nd15` | 15 | ? | 0.1018 | 3.4688 | — | 46.0000 |
| `lc_lc1e-3__nt_nd_nt95_nd20` | 20 | ? | 0.1061 | 3.5659 | — | 32.0000 |
| `lc_lc1e-4__nt_nd_nt95_nd10` | 10 | ? | 0.0913 | 3.4324 | — | 71.0000 |
| `lc_lc1e-4__nt_nd_nt95_nd15` | 15 | ? | 0.1010 | 3.4489 | — | 48.0000 |
| `lc_lc1e-4__nt_nd_nt95_nd20` | 20 | ? | 0.1043 | 3.5389 | — | 33.0000 |
| `lc_lc1e-5__nt_nd_nt95_nd10` | 10 | ? | 0.0914 | 3.4422 | — | 58.0000 |
| `lc_lc1e-5__nt_nd_nt95_nd15` | 15 | ? | 0.1004 | 3.4533 | — | 45.0000 |
| `lc_lc1e-5__nt_nd_nt95_nd20` | 20 | ? | 0.1041 | 3.5268 | — | 34.0000 |
| `lc_lc1e-6__nt_nd_nt95_nd10` | 10 | ? | 0.0946 | 3.4148 | — | 86.0000 |
| `lc_lc1e-6__nt_nd_nt95_nd15` | 15 | ? | 0.0971 | 3.4342 | — | 65.0000 |
| `lc_lc1e-6__nt_nd_nt95_nd20` | 20 | ? | 0.1050 | 3.5263 | — | 34.0000 |