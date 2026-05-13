# mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__nopre_decF_w0_pred10__lc_x_nd_x_nt__20260512T052513Z

- wandb group: [mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__nopre_decF_w0_pred10__lc_x_nd_x_nt__20260512T052513Z](https://wandb.ai/JacobianODE/MindControl_Mary_propofol_resting/groups/mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__nopre_decF_w0_pred10__lc_x_nd_x_nt__20260512T052513Z)
- chosen cell: **`lc_lc1e-3__nt_nd_nt99_nd5`** (trajectory val_loss (min over history) = 0.0576)
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

Four panels: C1 (one-step MASE), C2 (loop closure loss), C3 (fast eigenvalue fraction), trajectory val loss (min over training history). Bars are color-coded green = passes all selection criteria, red = excluded by some criterion, gold = the selected best run.

![sweep pareto](figures/sweep_pareto.png)

Pareto front in (loop closure loss, trajectory val loss) space. Gold star = the selected run.

**Chosen run** (by `best_traj_loss`): `lc_lc1e-3__nt_nd_nt99_nd5` (trajectory val_loss (min over history) = 0.0576). Hard criteria applied after relaxation: C1, C2, C3. Survivors / candidates: 15/21.

### Per-run results

| run_name | `nt_nd` | `lc` | best_traj_loss | best_MASE | LC loss | fast_eig_frac |
|---|---|---|---|---|---|---|
| `lc_lc1e-3__nt_nd_nt99_nd5` | — | — | 0.05757 | 1.8429 | 0.013 | 0.0000 |
| `lc_lc1e-2__nt_nd_nt99_nd5` | — | — | 0.05761 | 1.8479 | 0.000 | 0.0000 |
| `lc_lc1e-4__nt_nd_nt99_nd5` | — | — | 0.05887 | 1.8428 | 0.632 | 0.0000 |
| `lc_lc1e-1__nt_nd_nt99_nd10` | — | — | 0.05911 | 1.8611 | 0.000 | 0.0000 |
| `lc_lc1e-5__nt_nd_nt99_nd5` | — | — | 0.06009 | 1.8321 | 11.186 | 0.0000 |
| `lc_lc1e-6__nt_nd_nt99_nd5` | — | — | 0.06144 | 1.8320 | 81.862 | 0.0000 |
| `lc_lc1e-3__nt_nd_nt99_nd10` | — | — | 0.06203 | 1.8515 | 0.006 | 0.0000 |
| `lc_lc1e-2__nt_nd_nt99_nd10` | — | — | 0.06217 | 1.8528 | 0.001 | 0.0000 |
| `lc_lc1e-6__nt_nd_nt99_nd10` | — | — | 0.06329 | 1.8404 | 84.213 | 0.0000 |
| `lc_lc0__nt_nd_nt99_nd5` | — | — | 0.06469 | 1.8311 | 164.997 | 0.0000 |
| `lc_lc0__nt_nd_nt99_nd10` | — | — | 0.06499 | 1.8437 | 221.792 | 0.0000 |
| `lc_lc1e-4__nt_nd_nt99_nd10` | — | — | 0.06526 | 1.8529 | 0.264 | 0.0000 |
| `lc_lc1e-5__nt_nd_nt99_nd10` | — | — | 0.06603 | 1.8507 | 6.188 | 0.0000 |
| `lc_lc1e-4__nt_nd_nt99_nd15` | — | — | 0.06635 | 1.8202 | 0.645 | 0.0000 |
| `lc_lc1e-1__nt_nd_nt99_nd15` | — | — | 0.06718 | 1.8286 | 0.000 | 0.0000 |
| `lc_lc1e-1__nt_nd_nt99_nd5` | — | — | 0.06892 | 1.8283 | 0.000 | 0.0000 |
| `lc_lc1e-6__nt_nd_nt99_nd15` | — | — | 0.07064 | 1.8487 | 69.910 | 0.0000 |
| `lc_lc1e-5__nt_nd_nt99_nd15` | — | — | 0.07100 | 1.8417 | 3.696 | 0.0000 |
| `lc_lc1e-3__nt_nd_nt99_nd15` | — | — | 0.07107 | 1.8509 | 0.011 | 0.0000 |
| `lc_lc0__nt_nd_nt99_nd15` | — | — | 0.07190 | 1.8435 | 213.973 | 0.0000 |
| `lc_lc1e-2__nt_nd_nt99_nd15` | — | — | 0.07246 | 1.8518 | 0.000 | 0.0000 |

## Chosen run trajectory prediction

`lc_lc1e-3__nt_nd_nt99_nd5` cell params: `{'lightning_kwargs': {'reconstruction_mode': 'uniform', 'loop_closure_weight': 0.001}, 'n_target_var_threshold': 0.99, 'n_delays': 5}`

![chosen trajectory](figures/chosen_trajectory.png)

Solid = ground-truth, dashed = autoregressive rollout (`alpha_TF=0`). Left: latent space, projected onto top-3 PCs of rollout-window ground-truth latent. Right: observation space, projected onto top-3 PCs of rollout-window ground-truth obs. Color = PC index (`PC1=C0, PC2=C1, PC3=C2`). Vertical line = burn-in / start-of-rollout.

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
| `lc_lc0__nt_nd_nt99_nd10` | 10 | ? | 0.0676 | 1.8511 | — | 49.0000 |
| `lc_lc0__nt_nd_nt99_nd15` | 15 | ? | 0.0732 | 1.8695 | — | 38.0000 |
| `lc_lc0__nt_nd_nt99_nd5` | 5 | ? | 0.0657 | 1.8360 | — | 44.0000 |
| `lc_lc1e-1__nt_nd_nt99_nd10` | 10 | ? | 0.0595 | 1.8622 | — | 77.0000 |
| `lc_lc1e-1__nt_nd_nt99_nd15` | 15 | ? | 0.0672 | 1.8286 | — | 53.0000 |
| `lc_lc1e-1__nt_nd_nt99_nd5` | 5 | ? | 0.0689 | 1.8283 | — | 32.0000 |
| `lc_lc1e-2__nt_nd_nt99_nd10` | 10 | ? | 0.0653 | 1.8796 | — | 52.0000 |
| `lc_lc1e-2__nt_nd_nt99_nd15` | 15 | ? | 0.0726 | 1.8605 | — | 40.0000 |
| `lc_lc1e-2__nt_nd_nt99_nd5` | 5 | ? | 0.0576 | 1.8479 | — | 74.0000 |
| `lc_lc1e-3__nt_nd_nt99_nd10` | 10 | ? | 0.0656 | 1.8774 | — | 52.0000 |
| `lc_lc1e-3__nt_nd_nt99_nd15` | 15 | ? | 0.0720 | 1.8632 | — | 42.0000 |
| `lc_lc1e-3__nt_nd_nt99_nd5` | 5 | ? | 0.0576 | 1.8429 | — | 74.0000 |
| `lc_lc1e-4__nt_nd_nt99_nd10` | 10 | ? | 0.0653 | 1.8685 | — | 44.0000 |
| `lc_lc1e-4__nt_nd_nt99_nd15` | 15 | ? | 0.0663 | 1.8202 | — | 55.0000 |
| `lc_lc1e-4__nt_nd_nt99_nd5` | 5 | ? | 0.0605 | 1.8455 | — | 71.0000 |
| `lc_lc1e-5__nt_nd_nt99_nd10` | 10 | ? | 0.0700 | 1.8809 | — | 45.0000 |
| `lc_lc1e-5__nt_nd_nt99_nd15` | 15 | ? | 0.0710 | 1.8442 | — | 40.0000 |
| `lc_lc1e-5__nt_nd_nt99_nd5` | 5 | ? | 0.0617 | 1.8332 | — | 71.0000 |
| `lc_lc1e-6__nt_nd_nt99_nd10` | 10 | ? | 0.0634 | 1.8454 | — | 58.0000 |
| `lc_lc1e-6__nt_nd_nt99_nd15` | 15 | ? | 0.0713 | 1.8471 | — | 42.0000 |
| `lc_lc1e-6__nt_nd_nt99_nd5` | 5 | ? | 0.0629 | 1.8280 | — | 71.0000 |