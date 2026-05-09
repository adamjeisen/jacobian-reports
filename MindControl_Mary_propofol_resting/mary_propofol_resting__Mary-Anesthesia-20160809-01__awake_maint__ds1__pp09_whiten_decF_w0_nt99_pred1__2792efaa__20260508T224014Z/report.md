# mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__pp09_whiten_decF_w0_nt99_pred1__2792efaa__20260508T224014Z

- wandb group: [mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__pp09_whiten_decF_w0_nt99_pred1__2792efaa__20260508T224014Z](https://wandb.ai/JacobianODE/MindControl_Mary_propofol_resting/groups/mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__pp09_whiten_decF_w0_nt99_pred1__2792efaa__20260508T224014Z)
- chosen cell: **`delay_spacing_1__n_delays_15`** (val/one_step_mase = 1.2179)
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

![run-picking heatmap](figures/run_picking__heatmap.png)

Chose `delay_spacing_1__n_delays_15` (val/one_step_mase = 1.2179). `val/one_step_mase < 1` would mean beating persistence (predicting `x_{t+1} ≈ x_t`); on 1 kHz LFP the persistence baseline is hard to beat per-step even when 30-step R² is high.

## Chosen run trajectory prediction

`delay_spacing_1__n_delays_15` cell params: `{'delay_spacing': 1, 'n_delays': 15}`

![chosen trajectory](figures/chosen_trajectory.png)

Solid = ground-truth, dashed = autoregressive rollout (`alpha_TF=0`). Top: latent space (top-6 dims). Bottom: observation space (top-3 LFP channels). Vertical line marks burn-in / start-of-rollout boundary.

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
| `delay_spacing_10__n_delays_1` | 1 | ? | 0.1831 | 1.3417 | — | 42.0000 |
| `delay_spacing_10__n_delays_10` | 10 | ? | 0.0550 | 1.6392 | — | 23.0000 |
| `delay_spacing_10__n_delays_15` | 15 | ? | 0.0552 | 1.6620 | — | 29.0000 |
| `delay_spacing_10__n_delays_20` | 20 | ? | 0.0511 | 1.7309 | — | 24.0000 |
| `delay_spacing_10__n_delays_25` | 25 | ? | 0.0542 | 1.7892 | — | 20.0000 |
| `delay_spacing_10__n_delays_30` | 30 | ? | 0.0547 | 1.8582 | — | 20.0000 |
| `delay_spacing_10__n_delays_5` | 5 | ? | 0.0595 | 1.4855 | — | 23.0000 |
| `delay_spacing_1__n_delays_1` | 1 | ? | 0.1831 | 1.3417 | — | 42.0000 |
| `delay_spacing_1__n_delays_10` | 10 | ? | 0.0340 | 1.2466 | — | 75.0000 |
| `delay_spacing_1__n_delays_15` | 15 | ? | 0.0298 | 1.2179 | — | 57.0000 |
| `delay_spacing_1__n_delays_20` | 20 | ? | 0.0255 | 1.3233 | — | 69.0000 |
| `delay_spacing_1__n_delays_25` | 25 | ? | 0.0261 | 1.3953 | — | 51.0000 |
| `delay_spacing_1__n_delays_30` | 30 | ? | 0.0267 | 1.5036 | — | 49.0000 |
| `delay_spacing_1__n_delays_5` | 5 | ? | 0.0624 | 1.4146 | — | 66.0000 |
| `delay_spacing_5__n_delays_1` | 1 | ? | 0.1831 | 1.3417 | — | 42.0000 |
| `delay_spacing_5__n_delays_10` | 10 | ? | 0.0254 | 1.3683 | — | 30.0000 |
| `delay_spacing_5__n_delays_15` | 15 | ? | 0.0211 | 1.3786 | — | 35.0000 |
| `delay_spacing_5__n_delays_20` | 20 | ? | 0.0187 | 1.4793 | — | 23.0000 |
| `delay_spacing_5__n_delays_25` | 25 | ? | 0.0173 | 1.4924 | — | 39.0000 |
| `delay_spacing_5__n_delays_30` | 30 | ? | 0.0165 | 1.5505 | — | 29.0000 |
| `delay_spacing_5__n_delays_5` | 5 | ? | 0.0386 | 1.2960 | — | 25.0000 |