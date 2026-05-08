# mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__pilot16_decoded_only_x_pp__20260508T150521Z

- wandb group: [mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__pilot16_decoded_only_x_pp__20260508T150521Z](https://wandb.ai/JacobianODE/MindControl_Mary_propofol_resting/groups/mary_propofol_resting__Mary-Anesthesia-20160809-01__awake_maint__ds1__pilot16_decoded_only_x_pp__20260508T150521Z)
- chosen cell: **`arm_pp09_whiten_decF__base_combo_nt99_nd15_ds1`** (val/one_step_mase = 1.2124)
- cells reported: 16

**Description**: 16-cell OFAT mini-pilot. 8 base combos × 2 arms (pp=0.95+whiten with decoded_only_pred_loss=True; pp=0.9+whiten with decoded_only_pred_loss=False). Defaults: warmup=0, accum=1.

**Hypothesis**

```
Two single-factor flips against an implicit baseline of (pp=0.95
+whiten, decoded=False, warmup=0, accum=1):
- decoded_only_pred_loss=True under pp=0.95+whiten: the new loss
  cancels the obs-space reconstruction floor in the gradient to f.
- pp=0.9+whiten under decoded=False: tighter first-stage compression
  with whitening; baseline trajectory loss otherwise.
```

**Success criteria** (manual review until automated):

- [ ] All 16 cells finish within the 3-hour SLURM cap (or TIMEOUT, which counts as success-equivalent for reporting).
- [ ] val/one_step_mase + val/dynamics_only_one_step_mase finite for all.
- [ ] val/trajectory_pred_loss_obs and val/trajectory_pred_loss_decoded both logged side-by-side every val epoch (decoder-vs-decoded comparison works regardless of which target the loss was trained on).

## Run picking

![run-picking heatmap](figures/run_picking__heatmap.png)

Chose `arm_pp09_whiten_decF__base_combo_nt99_nd15_ds1` (val/one_step_mase = 1.2124). `val/one_step_mase < 1` would mean beating persistence (predicting `x_{t+1} ≈ x_t`); on 1 kHz LFP the persistence baseline is hard to beat per-step even when 30-step R² is high.

## Chosen run trajectory prediction

`arm_pp09_whiten_decF__base_combo_nt99_nd15_ds1` cell params: `{'pre_pca_per_area': True, 'pre_pca_var_threshold': 0.9, 'whiten_after_pre_pca': True, 'decoded_only_pred_loss': False, 'n_target_var_threshold': 0.99, 'n_delays': 15, 'delay_spacing': 1}`

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
| `arm_pp095_whiten_decT__base_combo_nt95_nd15_ds10` | 15 | ? | 0.1146 | 3.5597 | — | 11.0000 |
| `arm_pp095_whiten_decT__base_combo_nt95_nd15_ds5` | 15 | ? | 0.1329 | 3.3205 | — | 22.0000 |
| `arm_pp095_whiten_decT__base_combo_nt95_nd5_ds10` | 5 | ? | 0.1538 | 3.2762 | — | 30.0000 |
| `arm_pp095_whiten_decT__base_combo_nt95_nd5_ds5` | 5 | ? | 0.2305 | 2.9791 | — | 32.0000 |
| `arm_pp095_whiten_decT__base_combo_nt99_nd15_ds1` | 15 | ? | 0.3064 | 1.6418 | — | 30.0000 |
| `arm_pp095_whiten_decT__base_combo_nt99_nd15_ds5` | 15 | ? | 0.1637 | 1.6362 | — | 11.0000 |
| `arm_pp095_whiten_decT__base_combo_nt99_nd5_ds1` | 5 | ? | 0.3323 | 1.5150 | — | 34.0000 |
| `arm_pp095_whiten_decT__base_combo_nt99_nd5_ds5` | 5 | ? | 0.2196 | 1.5724 | — | 28.0000 |
| `arm_pp09_whiten_decF__base_combo_nt95_nd15_ds10` | 15 | ? | 0.1245 | 3.2645 | — | 22.0000 |
| `arm_pp09_whiten_decF__base_combo_nt95_nd15_ds5` | 15 | ? | 0.1348 | 3.0241 | — | 31.0000 |
| `arm_pp09_whiten_decF__base_combo_nt95_nd5_ds10` | 5 | ? | 0.1979 | 3.0196 | — | 36.0000 |
| `arm_pp09_whiten_decF__base_combo_nt95_nd5_ds5` | 5 | ? | 0.2525 | 2.6832 | — | 38.0000 |
| `arm_pp09_whiten_decF__base_combo_nt99_nd15_ds1` | 15 | ? | 0.2871 | 1.2124 | — | 36.0000 |
| `arm_pp09_whiten_decF__base_combo_nt99_nd15_ds5` | 15 | ? | 0.1028 | 1.4153 | — | 23.0000 |
| `arm_pp09_whiten_decF__base_combo_nt99_nd5_ds1` | 5 | ? | 0.3787 | 1.3440 | — | 40.0000 |
| `arm_pp09_whiten_decF__base_combo_nt99_nd5_ds5` | 5 | ? | 0.2325 | 1.2873 | — | 36.0000 |