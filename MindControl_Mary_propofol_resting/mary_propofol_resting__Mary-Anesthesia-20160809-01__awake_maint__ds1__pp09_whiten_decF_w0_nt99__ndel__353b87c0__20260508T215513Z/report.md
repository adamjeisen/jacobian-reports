# mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__pp09_whiten_decF_w0_nt99__ndel__353b87c0__20260508T215513Z

- wandb group: [mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__pp09_whiten_decF_w0_nt99__ndel__353b87c0__20260508T215513Z](https://wandb.ai/JacobianODE/MindControl_Mary_propofol_resting/groups/mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__pp09_whiten_decF_w0_nt99__ndel__353b87c0__20260508T215513Z)
- chosen cell: **`delay_spacing_5__n_delays_25`** (trajectory val_loss (min over history) = 0.0700)
- cells reported: 21

**Description**: 7 × 3 = 21 cells over n_delays × delay_spacing. Defaults: encoder_warmup_epochs=0, decoded_only_pred_loss=False, pre_pca_per_area=true at threshold 0.9 with whitening, n_target_var_threshold=0.99, accumulate_grad_batches=1. Awake + maintenance dose, ds=1 (1000 Hz), lp=80 Hz.

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

**Chosen run** (by `best_traj_loss`): `delay_spacing_5__n_delays_25` (trajectory val_loss (min over history) = 0.0700). Hard criteria applied after relaxation: C3. Survivors / candidates: 21/21.

### Per-run results

| run_name | `n_delays` | `delay_spacing` | best_traj_loss | best_MASE | LC loss | fast_eig_frac |
|---|---|---|---|---|---|---|
| `delay_spacing_5__n_delays_25` | 25 | 5 | 0.06996 | 1.4756 | 463.497 | 0.0000 |
| `delay_spacing_5__n_delays_20` | 20 | 5 | 0.07397 | 1.4389 | 365.463 | 0.0000 |
| `delay_spacing_5__n_delays_30` | 30 | 5 | 0.07801 | 1.5289 | 190.486 | 0.0000 |
| `delay_spacing_5__n_delays_15` | 15 | 5 | 0.08601 | 1.3939 | 366.608 | 0.0000 |
| `delay_spacing_10__n_delays_20` | 20 | 10 | 0.09497 | 1.6979 | 859.128 | 0.0000 |
| `delay_spacing_10__n_delays_15` | 15 | 10 | 0.09543 | 1.6397 | 1172.650 | 0.0000 |
| `delay_spacing_10__n_delays_10` | 10 | 10 | 0.10895 | 1.6052 | 1572.137 | 0.0000 |
| `delay_spacing_10__n_delays_25` | 25 | 10 | 0.11472 | 1.7334 | 643.443 | 0.0000 |
| `delay_spacing_5__n_delays_10` | 10 | 5 | 0.12188 | 1.3528 | 406.763 | 0.0000 |
| `delay_spacing_10__n_delays_30` | 30 | 10 | 0.13568 | 1.8281 | 440.807 | 0.0000 |
| `delay_spacing_1__n_delays_25` | 25 | 1 | 0.17756 | 1.7343 | 76.114 | 0.0000 |
| `delay_spacing_1__n_delays_15` | 15 | 1 | 0.18582 | 1.5112 | 36.237 | 0.0000 |
| `delay_spacing_1__n_delays_20` | 20 | 1 | 0.18785 | 1.5308 | 86.663 | 0.0000 |
| `delay_spacing_1__n_delays_30` | 30 | 1 | 0.19792 | 1.7491 | 98.861 | 0.0000 |
| `delay_spacing_10__n_delays_5` | 5 | 10 | 0.19956 | 1.4405 | 673.659 | 0.0000 |
| `delay_spacing_5__n_delays_5` | 5 | 5 | 0.20194 | 1.3006 | 348.790 | 0.0000 |
| `delay_spacing_1__n_delays_10` | 10 | 1 | 0.21597 | 1.5819 | 34.279 | 0.0000 |
| `delay_spacing_1__n_delays_5` | 5 | 1 | 0.26046 | 1.8429 | 119.015 | 0.0000 |
| `delay_spacing_1__n_delays_1` | 1 | 1 | 0.50314 | 1.5380 | 94709.961 | 0.0000 |
| `delay_spacing_5__n_delays_1` | 1 | 5 | 0.50314 | 1.5380 | 94709.961 | 0.0000 |
| `delay_spacing_10__n_delays_1` | 1 | 10 | 1.05731 | 1.2399 | 336.840 | 0.0000 |

## Chosen run trajectory prediction

`delay_spacing_5__n_delays_25` cell params: `{'delay_spacing': 5, 'n_delays': 25}`

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
| `delay_spacing_10__n_delays_1` | 1 | ? | 1.0573 | 1.2399 | — | 0.0000 |
| `delay_spacing_10__n_delays_10` | 10 | ? | 0.1092 | 1.6058 | — | 45.0000 |
| `delay_spacing_10__n_delays_15` | 15 | ? | 0.0958 | 1.6398 | — | 33.0000 |
| `delay_spacing_10__n_delays_20` | 20 | ? | 0.0950 | 1.6979 | — | 21.0000 |
| `delay_spacing_10__n_delays_25` | 25 | ? | 0.1147 | 1.7334 | — | 16.0000 |
| `delay_spacing_10__n_delays_30` | 30 | ? | 0.1357 | 1.8281 | — | 12.0000 |
| `delay_spacing_10__n_delays_5` | 5 | ? | 0.1996 | 1.4405 | — | 19.0000 |
| `delay_spacing_1__n_delays_1` | 1 | ? | 0.5229 | 1.5390 | — | 83.0000 |
| `delay_spacing_1__n_delays_10` | 10 | ? | 0.2169 | 1.6064 | — | 77.0000 |
| `delay_spacing_1__n_delays_15` | 15 | ? | 0.1862 | 1.5464 | — | 76.0000 |
| `delay_spacing_1__n_delays_20` | 20 | ? | 0.1878 | 1.5308 | — | 71.0000 |
| `delay_spacing_1__n_delays_25` | 25 | ? | 0.1776 | 1.7343 | — | 61.0000 |
| `delay_spacing_1__n_delays_30` | 30 | ? | 0.1985 | 1.7600 | — | 66.0000 |
| `delay_spacing_1__n_delays_5` | 5 | ? | 0.2605 | 1.8429 | — | 82.0000 |
| `delay_spacing_5__n_delays_1` | 1 | ? | 0.5229 | 1.5390 | — | 83.0000 |
| `delay_spacing_5__n_delays_10` | 10 | ? | 0.1221 | 1.3572 | — | 52.0000 |
| `delay_spacing_5__n_delays_15` | 15 | ? | 0.0863 | 1.3942 | — | 48.0000 |
| `delay_spacing_5__n_delays_20` | 20 | ? | 0.0753 | 1.4429 | — | 60.0000 |
| `delay_spacing_5__n_delays_25` | 25 | ? | 0.0718 | 1.4753 | — | 59.0000 |
| `delay_spacing_5__n_delays_30` | 30 | ? | 0.0780 | 1.5289 | — | 25.0000 |
| `delay_spacing_5__n_delays_5` | 5 | ? | 0.2055 | 1.3027 | — | 58.0000 |