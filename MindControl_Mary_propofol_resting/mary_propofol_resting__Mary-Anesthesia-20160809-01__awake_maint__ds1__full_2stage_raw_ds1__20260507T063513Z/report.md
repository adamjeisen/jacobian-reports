# mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__full_2stage_raw_ds1__20260507T063513Z

- wandb group: [mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__full_2stage_raw_ds1__20260507T063513Z](https://wandb.ai/JacobianODE/MindControl_Mary_propofol_resting/groups/mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__full_2stage_raw_ds1__20260507T063513Z)
- chosen cell: **`pre_pca_var_threshold_0.9__prediction_steps_50`** (val/one_step_mase = 1.1891)
- cells reported: 6

**Description**: ds=1 (1000 Hz raw), n_delays=5, awake + maintenance dose. Two-stage PCA: per-area PCA reduction BEFORE delay-embed at threshold ∈ {0.99, 0.95, 0.90}, then JacobianODE autodim PCA at 0.99 on the delay-embedded reduced obs. RAW (no LPF). 6 cells over prediction_steps × pre_pca_var_threshold.

**Hypothesis**

```
Two-stage PCA arm. The first stage controls how much per-area
raw variance is kept (lower threshold = aggressive compression);
the second stage always picks a tight 0.99 of the reduced+delay-
embedded variance. Compared to single-stage, this should yield
similar dynamic-dim totals at the 0.99 first-stage but much
smaller totals at 0.90, with potentially better gradient flow
because the encoder doesn't see redundant raw channels.
```

**Success criteria** (manual review until automated):

- [ ] All 6 cells finish within the 3-hour SLURM cap.
- [ ] val/one_step_mase finite for all cells.
- [ ] At pre_pca=0.99 the dynamic dim approximately matches the single-stage 0.99 case (consistency check).

## Run picking

![run-picking heatmap](figures/run_picking__heatmap.png)

Chose `pre_pca_var_threshold_0.9__prediction_steps_50` (val/one_step_mase = 1.1891). `val/one_step_mase < 1` would mean beating persistence (predicting `x_{t+1} ≈ x_t`); on 1 kHz LFP the persistence baseline is hard to beat per-step even when 30-step R² is high.

## Chosen run trajectory prediction

`pre_pca_var_threshold_0.9__prediction_steps_50` cell params: `{'pre_pca_var_threshold': 0.9, 'prediction_steps': 50}`

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
| `pre_pca_var_threshold_0.95__prediction_steps_30` | 5 | ? | 2.4171 | 1.3841 | — | 50.0000 |
| `pre_pca_var_threshold_0.95__prediction_steps_50` | 5 | ? | 3.8738 | 1.3340 | — | 44.0000 |
| `pre_pca_var_threshold_0.99__prediction_steps_30` | 5 | ? | 0.9679 | 1.8436 | — | 33.0000 |
| `pre_pca_var_threshold_0.99__prediction_steps_50` | 5 | ? | 1.5485 | 1.7887 | — | 30.0000 |
| `pre_pca_var_threshold_0.9__prediction_steps_30` | 5 | ? | 4.3557 | 1.2300 | — | 53.0000 |
| `pre_pca_var_threshold_0.9__prediction_steps_50` | 5 | ? | 7.0410 | 1.1891 | — | 47.0000 |