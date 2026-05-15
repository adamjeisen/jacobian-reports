# mary_propofol_resting__Mary-Anesthesia-20160831-02__awake_maint__ds1__nopre_decF_w0_nt99_pred10__mar__b7882f2d__20260514T223016Z

- wandb group: [mary_propofol_resting__Mary-Anesthesia-20160831-02__awake_maint__ds1__nopre_decF_w0_nt99_pred10__mar__b7882f2d__20260514T223016Z](https://wandb.ai/JacobianODE/MindControl_Mary_propofol_resting/groups/mary_propofol_resting__Mary-Anesthesia-20160831-02__awake_maint__ds1__nopre_decF_w0_nt99_pred10__mar__b7882f2d__20260514T223016Z)
- chosen cell: **`lc_lc1e-2__n_delays_15`** (trajectory val_loss (min over history) = 0.0294)
- cells reported: 21

**Description**: 21 cells: 3 n_delays × 7 loop_closure_weight at nt=0.99, ds=1, on Mary-Anesthesia-20160831-02. n_delays ∈ {5, 10, 15}. loop_closure_weight ∈ {0, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1}. obs_noise_scale=0. 6-hour SLURM cap, migrate_to=mit_normal_gpu. All other knobs match the Mary-20160809 + MrJones-20160105 LC × nd siblings.

**Hypothesis**

```
The Mary-20160809 + MrJones-20160105 LC × nd sweeps both showed the
LC sweet spot in 1e-3 to 1e-1 with a late-bloomer at lc=1e-1, nd=10.
Expect Mary-Anesthesia-20160831-02 to land in the same regime.
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

**Chosen run** (by `best_traj_loss`): `lc_lc1e-2__n_delays_15` (trajectory val_loss (min over history) = 0.0294). Hard criteria applied after relaxation: C1, C2, C3. Survivors / candidates: 15/21.

### Per-run results

| run_name | `n_delays` | `lc` | best_traj_loss | MASE | dec_corr_MASE | LC loss | n_dyn | fast_eig_frac |
|---|---|---|---|---|---|---|---|---|
| `lc_lc1e-2__n_delays_15` | 15 | — | 0.02941 | 2.6688 | 0.9608 | 0.000 | 96 | 0.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | — | 0.02967 | 2.6524 | 0.9593 | 36.182 | 96 | 0.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | — | 0.03024 | 2.6904 | 0.9755 | 35.811 | 74 | 0.0000 |
| `lc_lc0__n_delays_15` | 15 | — | 0.03059 | 2.6440 | 0.9580 | 340.163 | 96 | 0.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | — | 0.03091 | 2.7313 | 0.9950 | 0.002 | 74 | 0.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | — | 0.03125 | 2.6560 | 0.9724 | 2.064 | 85 | 0.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | — | 0.03128 | 2.6679 | 0.9751 | 0.001 | 85 | 0.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | — | 0.03132 | 2.7440 | 0.9983 | 0.001 | 74 | 0.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | — | 0.03156 | 2.6745 | 0.9737 | 21.739 | 85 | 0.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | — | 0.03157 | 2.6696 | 0.9743 | 0.000 | 85 | 0.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | — | 0.03169 | 2.7094 | 0.9643 | 0.020 | 96 | 0.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | — | 0.03200 | 2.7017 | 0.9626 | 1.338 | 96 | 0.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | — | 0.03257 | 2.6997 | 0.9610 | 0.005 | 96 | 0.0000 |
| `lc_lc0__n_delays_10` | 10 | — | 0.03263 | 2.6458 | 0.9693 | 319.208 | 85 | 0.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | — | 0.03279 | 2.6804 | 0.9719 | 0.000 | 85 | 0.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | — | 0.03357 | 2.7330 | 0.9648 | 0.000 | 96 | 0.0000 |
| `lc_lc0__n_delays_5` | 5 | — | 0.03364 | 2.6722 | 0.9748 | 113.076 | 74 | 0.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | — | 0.03369 | 2.7150 | 0.9873 | 0.000 | 74 | 0.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | — | 0.03400 | 2.6660 | 0.9751 | 0.007 | 74 | 0.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | — | 0.03416 | 2.6615 | 0.9727 | 0.340 | 74 | 0.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | — | 0.03695 | 2.7215 | 0.9653 | 0.015 | 85 | 0.0000 |

## Chosen run trajectory prediction

`lc_lc1e-2__n_delays_15` cell params: `{'lightning_kwargs': {'reconstruction_mode': 'uniform', 'loop_closure_weight': 0.01}, 'n_delays': 15}`

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
| `lc_lc0__n_delays_10` | 10 | ? | 0.0332 | 2.6447 | — | 65.0000 |
| `lc_lc0__n_delays_15` | 15 | ? | 0.0311 | 2.6387 | — | 68.0000 |
| `lc_lc0__n_delays_5` | 5 | ? | 0.0339 | 2.6972 | — | 45.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | ? | 0.0328 | 2.6804 | — | 54.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | ? | 0.0336 | 2.7330 | — | 43.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | ? | 0.0339 | 2.7510 | — | 46.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | ? | 0.0316 | 2.6696 | — | 58.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | ? | 0.0303 | 2.6681 | — | 67.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | ? | 0.0316 | 2.7356 | — | 60.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | ? | 0.0313 | 2.6679 | — | 58.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | ? | 0.0335 | 2.7041 | — | 45.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | ? | 0.0314 | 2.7294 | — | 60.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | ? | 0.0376 | 2.6913 | — | 32.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | ? | 0.0332 | 2.6963 | — | 45.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | ? | 0.0347 | 2.6747 | — | 38.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | ? | 0.0313 | 2.6560 | — | 58.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | ? | 0.0337 | 2.6982 | — | 45.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | ? | 0.0349 | 2.6741 | — | 38.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | ? | 0.0322 | 2.6654 | — | 63.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | ? | 0.0297 | 2.6524 | — | 66.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | ? | 0.0304 | 2.6850 | — | 95.0000 |