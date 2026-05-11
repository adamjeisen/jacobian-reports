# mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__nopre_decF_w0_nt99_pred10__nde__9637ce59__20260510T051512Z

- wandb group: [mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__nopre_decF_w0_nt99_pred10__nde__9637ce59__20260510T051512Z](https://wandb.ai/JacobianODE/MindControl_Mary_propofol_resting/groups/mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__nopre_decF_w0_nt99_pred10__nde__9637ce59__20260510T051512Z)
- chosen cell: **`delay_spacing_1__n_delays_5`** (trajectory val_loss (min over history) = 0.0635)
- cells reported: 16

**Description**: 7 × 3 = 21 cells over n_delays × delay_spacing. Defaults: encoder_warmup_epochs=0, decoded_only_pred_loss=False, pre_pca_per_area=false (no first-stage PCA), n_target_var_threshold=0.99, accumulate_grad_batches=1. Awake + maintenance dose, ds=1 (1000 Hz), lp=80 Hz.

**Hypothesis**

```
Wider/deeper temporal context (larger n_delays × delay_spacing)
should give the encoder more information per sample to disambiguate
the latent state, lowering one-step MASE — but only up to the point
where the autodim'd latent saturates the dynamics MLP's capacity
or the prediction horizon dominates the residual variance.
```

**Success criteria** (manual review until automated):

- [ ] All 21 cells run within the 6-hour SLURM cap (or TIMEOUT, which counts as success-equivalent for reporting).
- [ ] val/one_step_mase finite for all cells.
- [ ] At least one (n_delays, delay_spacing) combo strictly beats the n_delays=1, delay_spacing=1 baseline on val/one_step_mase.

## Run picking

![sweep overview](figures/sweep_overview.png)

Four panels: C1 (one-step MASE), C2 (loop closure loss), C3 (fast eigenvalue fraction), trajectory val loss (min over training history). Bars are color-coded green = passes all selection criteria, red = excluded by some criterion, gold = the selected best run.

![sweep pareto](figures/sweep_pareto.png)

Pareto front in (loop closure loss, trajectory val loss) space. Gold star = the selected run.

**Chosen run** (by `best_traj_loss`): `delay_spacing_1__n_delays_5` (trajectory val_loss (min over history) = 0.0635). Hard criteria applied after relaxation: C3. Survivors / candidates: 16/16.

### Per-run results

| run_name | `n_delays` | `delay_spacing` | best_traj_loss | best_MASE | LC loss | fast_eig_frac |
|---|---|---|---|---|---|---|
| `delay_spacing_1__n_delays_5` | 5 | 1 | 0.06346 | 1.8385 | 279.388 | 0.0000 |
| `delay_spacing_1__n_delays_10` | 10 | 1 | 0.06674 | 1.8432 | 176.754 | 0.0000 |
| `delay_spacing_1__n_delays_15` | 15 | 1 | 0.07645 | 1.8746 | 104.907 | 0.0000 |
| `delay_spacing_1__n_delays_20` | 20 | 1 | 0.08038 | 2.0695 | 177.868 | 0.0000 |
| `delay_spacing_1__n_delays_25` | 25 | 1 | 0.08710 | 2.2746 | 238.780 | 0.0000 |
| `delay_spacing_5__n_delays_5` | 5 | 5 | 0.09093 | 1.8140 | 414.022 | 0.0000 |
| `delay_spacing_1__n_delays_30` | 30 | 1 | 0.09509 | 2.5412 | 347.242 | 0.0000 |
| `delay_spacing_5__n_delays_10` | 10 | 5 | 0.10141 | 2.0161 | 350.880 | 0.0000 |
| `delay_spacing_5__n_delays_15` | 15 | 5 | 0.11598 | 2.5552 | 183.784 | 0.0000 |
| `delay_spacing_10__n_delays_5` | 5 | 10 | 0.11951 | 2.1043 | 1190.791 | 0.0000 |
| `delay_spacing_5__n_delays_20` | 20 | 5 | 0.13621 | 3.0277 | 161.957 | 0.0000 |
| `delay_spacing_10__n_delays_10` | 10 | 10 | 0.14646 | 2.6274 | 931.540 | 0.0000 |
| `delay_spacing_1__n_delays_1` | 1 | 1 | 0.16401 | 2.1252 | 574.773 | 0.0000 |
| `delay_spacing_5__n_delays_1` | 1 | 5 | 0.16401 | 2.1252 | 574.773 | 0.0000 |
| `delay_spacing_10__n_delays_1` | 1 | 10 | 0.16401 | 2.1252 | 574.773 | 0.0000 |
| `delay_spacing_10__n_delays_15` | 15 | 10 | 0.17575 | 3.4656 | 204.652 | 0.0000 |

## Chosen run trajectory prediction

`delay_spacing_1__n_delays_5` cell params: `{'delay_spacing': 1, 'n_delays': 5}`

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
| `delay_spacing_10__n_delays_1` | 1 | ? | 0.1739 | 2.1764 | — | 24.0000 |
| `delay_spacing_10__n_delays_10` | 10 | ? | 0.1465 | 2.6274 | — | 10.0000 |
| `delay_spacing_10__n_delays_15` | 15 | ? | 0.1774 | 3.1338 | — | 9.0000 |
| `delay_spacing_10__n_delays_5` | 5 | ? | 0.1201 | 2.1010 | — | 29.0000 |
| `delay_spacing_1__n_delays_1` | 1 | ? | 0.1739 | 2.1764 | — | 24.0000 |
| `delay_spacing_1__n_delays_10` | 10 | ? | 0.0667 | 1.8432 | — | 41.0000 |
| `delay_spacing_1__n_delays_15` | 15 | ? | 0.0769 | 1.8667 | — | 30.0000 |
| `delay_spacing_1__n_delays_20` | 20 | ? | 0.0805 | 2.0413 | — | 22.0000 |
| `delay_spacing_1__n_delays_25` | 25 | ? | 0.0883 | 2.2759 | — | 16.0000 |
| `delay_spacing_1__n_delays_30` | 30 | ? | 0.0951 | 2.5412 | — | 13.0000 |
| `delay_spacing_1__n_delays_5` | 5 | ? | 0.0636 | 1.8373 | — | 63.0000 |
| `delay_spacing_5__n_delays_1` | 1 | ? | 0.1739 | 2.1764 | — | 24.0000 |
| `delay_spacing_5__n_delays_10` | 10 | ? | 0.1014 | 2.0161 | — | 18.0000 |
| `delay_spacing_5__n_delays_15` | 15 | ? | 0.1263 | 2.5543 | — | 10.0000 |
| `delay_spacing_5__n_delays_20` | 20 | ? | 0.1398 | 3.0642 | — | 10.0000 |
| `delay_spacing_5__n_delays_5` | 5 | ? | 0.0924 | 1.8120 | — | 38.0000 |