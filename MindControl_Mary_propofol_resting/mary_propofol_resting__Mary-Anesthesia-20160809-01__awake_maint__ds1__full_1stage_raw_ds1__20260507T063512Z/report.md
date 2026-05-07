# mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__full_1stage_raw_ds1__20260507T063512Z

- wandb group: [mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__full_1stage_raw_ds1__20260507T063512Z](https://wandb.ai/JacobianODE/MindControl_Mary_propofol_resting/groups/mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__full_1stage_raw_ds1__20260507T063512Z)
- chosen cell: **`n_target_var_threshold_0.99__prediction_steps_30`** (val/one_step_mase = 1.3733)
- cells reported: 6

**Description**: ds=1 (1000 Hz raw), n_delays=5, awake + maintenance dose. Single- stage PCA autodim. RAW (no low-pass filtering). 6 cells over prediction_steps × n_target_var_threshold.

**Hypothesis**

```
Reference arm (no filter, single-stage PCA) for the 24-run sweep
that varies (filter ∈ {raw, LPF 100Hz}) × (prediction_steps ∈ {30, 50})
× (var threshold ∈ {.99, .95, .90}). Joint with the LPF 100 Hz
arm we'll see whether filtering helps at the high-threshold (raw-
spectrum-dependent) or low-threshold (variance-floor-dependent)
end of the autodim picks.
```

**Success criteria** (manual review until automated):

- [ ] All 6 cells finish within the 3-hour SLURM cap.
- [ ] val/one_step_mase finite for all cells.
- [ ] Higher prediction_steps degrades free-running r² but not the Jacobian/Lyapunov estimates.

## Run picking

![run-picking heatmap](figures/run_picking__heatmap.png)

Chose `n_target_var_threshold_0.99__prediction_steps_30` (val/one_step_mase = 1.3733). `val/one_step_mase < 1` would mean beating persistence (predicting `x_{t+1} ≈ x_t`); on 1 kHz LFP the persistence baseline is hard to beat per-step even when 30-step R² is high.

## Chosen run trajectory prediction

`n_target_var_threshold_0.99__prediction_steps_30` cell params: `{'n_target_var_threshold': 0.99, 'prediction_steps': 30}`

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
| `n_target_var_threshold_0.95__prediction_steps_30` | 5 | ? | 0.4142 | 2.4242 | — | 32.0000 |
| `n_target_var_threshold_0.95__prediction_steps_50` | 5 | ? | 0.6590 | 2.4317 | — | 29.0000 |
| `n_target_var_threshold_0.99__prediction_steps_30` | 5 | ? | 0.4897 | 1.3733 | — | 20.0000 |
| `n_target_var_threshold_0.99__prediction_steps_50` | 5 | ? | 0.7051 | 1.4043 | — | 17.0000 |
| `n_target_var_threshold_0.9__prediction_steps_30` | 5 | ? | 0.4560 | 3.1146 | — | 34.0000 |
| `n_target_var_threshold_0.9__prediction_steps_50` | 5 | ? | 0.7197 | 3.1289 | — | 31.0000 |