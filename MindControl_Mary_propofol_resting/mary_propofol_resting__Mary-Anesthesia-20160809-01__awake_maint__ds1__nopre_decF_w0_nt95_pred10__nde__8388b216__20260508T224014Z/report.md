# mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__nopre_decF_w0_nt95_pred10__nde__8388b216__20260508T224014Z

- wandb group: [mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__nopre_decF_w0_nt95_pred10__nde__8388b216__20260508T224014Z](https://wandb.ai/JacobianODE/MindControl_Mary_propofol_resting/groups/mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__nopre_decF_w0_nt95_pred10__nde__8388b216__20260508T224014Z)
- chosen cell: **`delay_spacing_1__n_delays_10`** (trajectory val_loss (min over history) = 0.0943)
- cells reported: 21

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

**Chosen run** (by `best_traj_loss`): `delay_spacing_1__n_delays_10` (trajectory val_loss (min over history) = 0.0943). Hard criteria applied after relaxation: C3. Survivors / candidates: 21/21.

### Per-run results

| run_name | `n_delays` | `delay_spacing` | best_traj_loss | best_MASE | LC loss | fast_eig_frac |
|---|---|---|---|---|---|---|
| `delay_spacing_1__n_delays_10` | 10 | 1 | 0.09429 | 3.4356 | 251.758 | 0.0000 |
| `delay_spacing_1__n_delays_20` | 20 | 1 | 0.09713 | 3.5003 | 401.494 | 0.0000 |
| `delay_spacing_1__n_delays_15` | 15 | 1 | 0.09967 | 3.4448 | 428.865 | 0.0000 |
| `delay_spacing_1__n_delays_5` | 5 | 1 | 0.10726 | 3.4162 | 211.522 | 0.0000 |
| `delay_spacing_1__n_delays_30` | 30 | 1 | 0.10810 | 3.6501 | 784.851 | 0.0000 |
| `delay_spacing_5__n_delays_10` | 10 | 5 | 0.11196 | 3.4825 | 581.100 | 0.0000 |
| `delay_spacing_5__n_delays_5` | 5 | 5 | 0.11227 | 3.4354 | 363.540 | 0.0000 |
| `delay_spacing_5__n_delays_15` | 15 | 5 | 0.11422 | 3.6141 | 969.409 | 0.0000 |
| `delay_spacing_5__n_delays_20` | 20 | 5 | 0.11987 | 3.8020 | 906.812 | 0.0000 |
| `delay_spacing_5__n_delays_25` | 25 | 5 | 0.12076 | 4.0788 | 866.904 | 0.0000 |
| `delay_spacing_1__n_delays_25` | 25 | 1 | 0.12700 | 3.8646 | 441.991 | 0.0000 |
| `delay_spacing_10__n_delays_5` | 5 | 10 | 0.12945 | 3.5727 | 839.567 | 0.0000 |
| `delay_spacing_10__n_delays_15` | 15 | 10 | 0.14374 | 3.9181 | 2440.857 | 0.0000 |
| `delay_spacing_10__n_delays_10` | 10 | 10 | 0.14550 | 3.7463 | 1948.223 | 0.0000 |
| `delay_spacing_10__n_delays_20` | 20 | 10 | 0.14768 | 4.2546 | 2022.970 | 0.0000 |
| `delay_spacing_5__n_delays_30` | 30 | 5 | 0.15499 | 5.1606 | 768.585 | 0.0000 |
| `delay_spacing_10__n_delays_25` | 25 | 10 | 0.16018 | 4.8113 | 1484.732 | 0.0000 |
| `delay_spacing_10__n_delays_30` | 30 | 10 | 0.16248 | 5.1197 | 1131.442 | 0.0000 |
| `delay_spacing_1__n_delays_1` | 1 | 1 | 0.18384 | 3.5601 | 1111.883 | 0.0000 |
| `delay_spacing_5__n_delays_1` | 1 | 5 | 0.18384 | 3.5601 | 1111.883 | 0.0000 |
| `delay_spacing_10__n_delays_1` | 1 | 10 | 0.18384 | 3.5601 | 1111.883 | 0.0000 |

## Chosen run trajectory prediction

`delay_spacing_1__n_delays_10` cell params: `{'delay_spacing': 1, 'n_delays': 10}`

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
| `delay_spacing_10__n_delays_1` | 1 | ? | 0.1887 | 3.5847 | — | 47.0000 |
| `delay_spacing_10__n_delays_10` | 10 | ? | 0.1475 | 3.7430 | — | 39.0000 |
| `delay_spacing_10__n_delays_15` | 15 | ? | 0.1449 | 3.8822 | — | 31.0000 |
| `delay_spacing_10__n_delays_20` | 20 | ? | 0.1477 | 4.2546 | — | 22.0000 |
| `delay_spacing_10__n_delays_25` | 25 | ? | 0.1645 | 4.6670 | — | 16.0000 |
| `delay_spacing_10__n_delays_30` | 30 | ? | 0.1625 | 5.1197 | — | 12.0000 |
| `delay_spacing_10__n_delays_5` | 5 | ? | 0.1330 | 3.5399 | — | 64.0000 |
| `delay_spacing_1__n_delays_1` | 1 | ? | 0.1887 | 3.5847 | — | 47.0000 |
| `delay_spacing_1__n_delays_10` | 10 | ? | 0.0955 | 3.4345 | — | 59.0000 |
| `delay_spacing_1__n_delays_15` | 15 | ? | 0.1054 | 3.4633 | — | 43.0000 |
| `delay_spacing_1__n_delays_20` | 20 | ? | 0.1018 | 3.4977 | — | 46.0000 |
| `delay_spacing_1__n_delays_25` | 25 | ? | 0.1270 | 3.8646 | — | 9.0000 |
| `delay_spacing_1__n_delays_30` | 30 | ? | 0.1081 | 3.6501 | — | 28.0000 |
| `delay_spacing_1__n_delays_5` | 5 | ? | 0.1075 | 3.4139 | — | 27.0000 |
| `delay_spacing_5__n_delays_1` | 1 | ? | 0.1887 | 3.5847 | — | 47.0000 |
| `delay_spacing_5__n_delays_10` | 10 | ? | 0.1164 | 3.4537 | — | 54.0000 |
| `delay_spacing_5__n_delays_15` | 15 | ? | 0.1172 | 3.5878 | — | 38.0000 |
| `delay_spacing_5__n_delays_20` | 20 | ? | 0.1204 | 3.7918 | — | 25.0000 |
| `delay_spacing_5__n_delays_25` | 25 | ? | 0.1222 | 4.0008 | — | 20.0000 |
| `delay_spacing_5__n_delays_30` | 30 | ? | 0.1550 | 5.1606 | — | 7.0000 |
| `delay_spacing_5__n_delays_5` | 5 | ? | 0.1139 | 3.4326 | — | 54.0000 |