# mrjones_propofol_resting__MrJones-Anesthesia-20160206-01__awake_maint__ds1__nopre_decF_w0_nt99_pred1__4393de4c__20260516T033522Z

- wandb group: [mrjones_propofol_resting__MrJones-Anesthesia-20160206-01__awake_maint__ds1__nopre_decF_w0_nt99_pred1__4393de4c__20260516T033522Z](https://wandb.ai/JacobianODE/MindControl_MrJones_propofol_resting/groups/mrjones_propofol_resting__MrJones-Anesthesia-20160206-01__awake_maint__ds1__nopre_decF_w0_nt99_pred1__4393de4c__20260516T033522Z)
- chosen cell: **`lc_lc1e-1__n_delays_5`** (trajectory val_loss (min over history) = 0.0379)
- cells reported: 21

**Description**: 21 cells: 3 n_delays × 7 loop_closure_weight at nt=0.99, ds=1, on MrJones-Anesthesia-20160206-01. n_delays ∈ {5, 10, 15}. loop_closure_weight ∈ {0, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1}. obs_noise_scale=0. 6-hour SLURM cap, migrate_to=mit_normal_gpu. All other knobs match the Mary-20160809 + MrJones-20160105 LC × nd siblings.

**Hypothesis**

```
The Mary-20160809 + MrJones-20160105 LC × nd sweeps both showed the
LC sweet spot in 1e-3 to 1e-1 with a late-bloomer at lc=1e-1, nd=10.
Expect MrJones-Anesthesia-20160206-01 to land in the same regime.
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

**Chosen run** (by `best_traj_loss`): `lc_lc1e-1__n_delays_5` (trajectory val_loss (min over history) = 0.0379). Hard criteria applied after relaxation: C1, C2, C3. Survivors / candidates: 13/21.

### Per-run results

| run_name | `n_delays` | `lc` | best_traj_loss | MASE | dec_corr_MASE | LC loss | n_dyn | fast_eig_frac |
|---|---|---|---|---|---|---|---|---|
| `lc_lc1e-1__n_delays_5` | 5 | — | 0.03794 | 2.5323 | 0.9949 | 0.000 | 120 | 0.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | — | 0.03844 | 2.5388 | 0.9958 | 0.003 | 120 | 0.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | — | 0.03846 | 2.5336 | 0.9946 | 0.589 | 120 | 0.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | — | 0.03847 | 2.5425 | 0.9967 | 0.000 | 120 | 0.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | — | 0.03898 | 2.5121 | 0.9924 | 15.391 | 120 | 0.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | — | 0.04079 | 2.4945 | 0.9920 | 105.467 | 120 | 0.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | — | 0.04135 | 2.4678 | 0.9694 | 0.004 | 147 | 0.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | — | 0.04147 | 2.4765 | 0.9713 | 0.000 | 147 | 0.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | — | 0.04174 | 2.4601 | 0.9688 | 15.655 | 147 | 0.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | — | 0.04179 | 2.4701 | 0.9703 | 0.000 | 147 | 0.0000 |
| `lc_lc0__n_delays_5` | 5 | — | 0.04205 | 2.4847 | 0.9915 | 276.644 | 120 | 0.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | — | 0.04235 | 2.4675 | 0.9691 | 0.427 | 147 | 0.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | — | 0.04239 | 2.4564 | 0.9626 | 180.105 | 175 | 0.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | — | 0.04362 | 2.5171 | 0.9634 | 9.865 | 175 | 0.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | — | 0.04369 | 2.5245 | 0.9644 | 0.231 | 175 | 0.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | — | 0.04386 | 2.5275 | 0.9649 | 0.004 | 175 | 0.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | — | 0.04410 | 2.4566 | 0.9667 | 113.681 | 147 | 0.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | — | 0.04418 | 2.5247 | 0.9645 | 0.000 | 175 | 0.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | — | 0.04418 | 2.5280 | 0.9648 | 0.000 | 175 | 0.0000 |
| `lc_lc0__n_delays_15` | 15 | — | 0.04626 | 2.4915 | 0.9634 | 688.372 | 175 | 0.0000 |
| `lc_lc0__n_delays_10` | 10 | — | 0.04691 | 2.4728 | 0.9681 | 391.117 | 147 | 0.0000 |

## Chosen run trajectory prediction

`lc_lc1e-1__n_delays_5` cell params: `{'lightning_kwargs': {'reconstruction_mode': 'uniform', 'loop_closure_weight': 0.1}, 'n_delays': 5}`

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

#### 7b → 7b

![7b → 7b (standard/full)](figures/gramians_per_pair/gramian_pair__standard__full__7b_to_7b.png)

#### 7b → CPB

![7b → CPB (standard/full)](figures/gramians_per_pair/gramian_pair__standard__full__7b_to_CPB.png)

#### 7b → FEF

![7b → FEF (standard/full)](figures/gramians_per_pair/gramian_pair__standard__full__7b_to_FEF.png)

#### 7b → vlPFC

![7b → vlPFC (standard/full)](figures/gramians_per_pair/gramian_pair__standard__full__7b_to_vlPFC.png)

#### CPB → 7b

![CPB → 7b (standard/full)](figures/gramians_per_pair/gramian_pair__standard__full__CPB_to_7b.png)

#### CPB → CPB

![CPB → CPB (standard/full)](figures/gramians_per_pair/gramian_pair__standard__full__CPB_to_CPB.png)

#### CPB → FEF

![CPB → FEF (standard/full)](figures/gramians_per_pair/gramian_pair__standard__full__CPB_to_FEF.png)

#### CPB → vlPFC

![CPB → vlPFC (standard/full)](figures/gramians_per_pair/gramian_pair__standard__full__CPB_to_vlPFC.png)

#### FEF → 7b

![FEF → 7b (standard/full)](figures/gramians_per_pair/gramian_pair__standard__full__FEF_to_7b.png)

#### FEF → CPB

![FEF → CPB (standard/full)](figures/gramians_per_pair/gramian_pair__standard__full__FEF_to_CPB.png)

#### FEF → FEF

![FEF → FEF (standard/full)](figures/gramians_per_pair/gramian_pair__standard__full__FEF_to_FEF.png)

#### FEF → vlPFC

![FEF → vlPFC (standard/full)](figures/gramians_per_pair/gramian_pair__standard__full__FEF_to_vlPFC.png)

#### vlPFC → 7b

![vlPFC → 7b (standard/full)](figures/gramians_per_pair/gramian_pair__standard__full__vlPFC_to_7b.png)

#### vlPFC → CPB

![vlPFC → CPB (standard/full)](figures/gramians_per_pair/gramian_pair__standard__full__vlPFC_to_CPB.png)

#### vlPFC → FEF

![vlPFC → FEF (standard/full)](figures/gramians_per_pair/gramian_pair__standard__full__vlPFC_to_FEF.png)

#### vlPFC → vlPFC

![vlPFC → vlPFC (standard/full)](figures/gramians_per_pair/gramian_pair__standard__full__vlPFC_to_vlPFC.png)

### standard / k10

#### 7b → 7b

![7b → 7b (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__7b_to_7b.png)

#### 7b → CPB

![7b → CPB (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__7b_to_CPB.png)

#### 7b → FEF

![7b → FEF (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__7b_to_FEF.png)

#### 7b → vlPFC

![7b → vlPFC (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__7b_to_vlPFC.png)

#### CPB → 7b

![CPB → 7b (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__CPB_to_7b.png)

#### CPB → CPB

![CPB → CPB (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__CPB_to_CPB.png)

#### CPB → FEF

![CPB → FEF (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__CPB_to_FEF.png)

#### CPB → vlPFC

![CPB → vlPFC (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__CPB_to_vlPFC.png)

#### FEF → 7b

![FEF → 7b (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__FEF_to_7b.png)

#### FEF → CPB

![FEF → CPB (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__FEF_to_CPB.png)

#### FEF → FEF

![FEF → FEF (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__FEF_to_FEF.png)

#### FEF → vlPFC

![FEF → vlPFC (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__FEF_to_vlPFC.png)

#### vlPFC → 7b

![vlPFC → 7b (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__vlPFC_to_7b.png)

#### vlPFC → CPB

![vlPFC → CPB (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__vlPFC_to_CPB.png)

#### vlPFC → FEF

![vlPFC → FEF (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__vlPFC_to_FEF.png)

#### vlPFC → vlPFC

![vlPFC → vlPFC (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__vlPFC_to_vlPFC.png)

### standard / k20

#### 7b → 7b

![7b → 7b (standard/k20)](figures/gramians_per_pair/gramian_pair__standard__k20__7b_to_7b.png)

#### 7b → CPB

![7b → CPB (standard/k20)](figures/gramians_per_pair/gramian_pair__standard__k20__7b_to_CPB.png)

#### 7b → FEF

![7b → FEF (standard/k20)](figures/gramians_per_pair/gramian_pair__standard__k20__7b_to_FEF.png)

#### 7b → vlPFC

![7b → vlPFC (standard/k20)](figures/gramians_per_pair/gramian_pair__standard__k20__7b_to_vlPFC.png)

#### CPB → 7b

![CPB → 7b (standard/k20)](figures/gramians_per_pair/gramian_pair__standard__k20__CPB_to_7b.png)

#### CPB → CPB

![CPB → CPB (standard/k20)](figures/gramians_per_pair/gramian_pair__standard__k20__CPB_to_CPB.png)

#### CPB → FEF

![CPB → FEF (standard/k20)](figures/gramians_per_pair/gramian_pair__standard__k20__CPB_to_FEF.png)

#### CPB → vlPFC

![CPB → vlPFC (standard/k20)](figures/gramians_per_pair/gramian_pair__standard__k20__CPB_to_vlPFC.png)

#### FEF → 7b

![FEF → 7b (standard/k20)](figures/gramians_per_pair/gramian_pair__standard__k20__FEF_to_7b.png)

#### FEF → CPB

![FEF → CPB (standard/k20)](figures/gramians_per_pair/gramian_pair__standard__k20__FEF_to_CPB.png)

#### FEF → FEF

![FEF → FEF (standard/k20)](figures/gramians_per_pair/gramian_pair__standard__k20__FEF_to_FEF.png)

#### FEF → vlPFC

![FEF → vlPFC (standard/k20)](figures/gramians_per_pair/gramian_pair__standard__k20__FEF_to_vlPFC.png)

#### vlPFC → 7b

![vlPFC → 7b (standard/k20)](figures/gramians_per_pair/gramian_pair__standard__k20__vlPFC_to_7b.png)

#### vlPFC → CPB

![vlPFC → CPB (standard/k20)](figures/gramians_per_pair/gramian_pair__standard__k20__vlPFC_to_CPB.png)

#### vlPFC → FEF

![vlPFC → FEF (standard/k20)](figures/gramians_per_pair/gramian_pair__standard__k20__vlPFC_to_FEF.png)

#### vlPFC → vlPFC

![vlPFC → vlPFC (standard/k20)](figures/gramians_per_pair/gramian_pair__standard__k20__vlPFC_to_vlPFC.png)

## Per-cell summary metrics

| run | n_delays | encoder_warmup | mean val loss | val/one_step_mase | val/total_loss | epoch |
|---|---|---|---|---|---|---|
| `lc_lc0__n_delays_10` | 10 | ? | 0.0472 | 2.4620 | — | 42.0000 |
| `lc_lc0__n_delays_15` | 15 | ? | 0.0463 | 2.4915 | — | 45.0000 |
| `lc_lc0__n_delays_5` | 5 | ? | 0.0423 | 2.4994 | — | 54.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | ? | 0.0418 | 2.4701 | — | 62.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | ? | 0.0442 | 2.5247 | — | 45.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | ? | 0.0379 | 2.5323 | — | 74.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | ? | 0.0417 | 2.4728 | — | 61.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | ? | 0.0442 | 2.5280 | — | 45.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | ? | 0.0385 | 2.5425 | — | 66.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | ? | 0.0413 | 2.4678 | — | 59.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | ? | 0.0439 | 2.5275 | — | 45.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | ? | 0.0384 | 2.5388 | — | 66.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | ? | 0.0423 | 2.4675 | — | 53.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | ? | 0.0437 | 2.5245 | — | 45.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | ? | 0.0385 | 2.5336 | — | 66.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | ? | 0.0420 | 2.4523 | — | 62.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | ? | 0.0436 | 2.4989 | — | 46.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | ? | 0.0390 | 2.5185 | — | 66.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | ? | 0.0441 | 2.4566 | — | 51.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | ? | 0.0424 | 2.4564 | — | 60.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | ? | 0.0408 | 2.4921 | — | 63.0000 |