# mrjones_propofol_resting__MrJones-Anesthesia-20160109-01__awake_maint__ds1__nopre_decF_w0_nt99_pred1__e49dffc4__20260517T053517Z

- wandb group: [mrjones_propofol_resting__MrJones-Anesthesia-20160109-01__awake_maint__ds1__nopre_decF_w0_nt99_pred1__e49dffc4__20260517T053517Z](https://wandb.ai/JacobianODE/MindControl_MrJones_propofol_resting/groups/mrjones_propofol_resting__MrJones-Anesthesia-20160109-01__awake_maint__ds1__nopre_decF_w0_nt99_pred1__e49dffc4__20260517T053517Z)
- chosen cell: **`lc_lc1e-2__n_delays_10`** (trajectory val_loss (min over history) = 0.0363)
- cells reported: 21

**Description**: 21 cells: 3 n_delays × 7 loop_closure_weight at nt=0.99, ds=1, on MrJones-Anesthesia-20160109-01. n_delays ∈ {5, 10, 15}. loop_closure_weight ∈ {0, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1}. obs_noise_scale=0. 6-hour SLURM cap, migrate_to=mit_normal_gpu. All other knobs match the Mary-20160809 + MrJones-20160105 LC × nd siblings.

**Hypothesis**

```
The Mary-20160809 + MrJones-20160105 LC × nd sweeps both showed the
LC sweet spot in 1e-3 to 1e-1 with a late-bloomer at lc=1e-1, nd=10.
Expect MrJones-Anesthesia-20160109-01 to land in the same regime.
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

**Chosen run** (by `best_traj_loss`): `lc_lc1e-2__n_delays_10` (trajectory val_loss (min over history) = 0.0363). Hard criteria applied after relaxation: C1, C2, C3. Survivors / candidates: 12/21.

### Per-run results

| run_name | `n_delays` | `lc` | best_traj_loss | MASE | dec_corr_MASE | LC loss | n_dyn | fast_eig_frac |
|---|---|---|---|---|---|---|---|---|
| `lc_lc1e-2__n_delays_10` | 10 | — | 0.03631 | 2.4327 | 0.9633 | 0.000 | 134 | 0.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | — | 0.03746 | 2.4357 | 0.9648 | 1.446 | 134 | 0.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | — | 0.03758 | 2.4425 | 0.9667 | 0.007 | 134 | 0.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | — | 0.03794 | 2.4183 | 0.9621 | 27.499 | 134 | 0.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | — | 0.03800 | 2.4510 | 0.9696 | 0.000 | 134 | 0.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | — | 0.03913 | 2.4273 | 0.9595 | 0.006 | 160 | 0.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | — | 0.04148 | 2.4341 | 0.9650 | 147.229 | 134 | 0.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | — | 0.04208 | 2.4178 | 0.9590 | 231.196 | 160 | 0.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | — | 0.04220 | 2.4656 | 0.9639 | 0.581 | 160 | 0.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | — | 0.04233 | 2.4645 | 0.9618 | 0.001 | 160 | 0.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | — | 0.04246 | 2.4626 | 0.9617 | 0.000 | 160 | 0.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | — | 0.04262 | 2.4558 | 0.9594 | 23.733 | 160 | 0.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | — | 0.04408 | 2.4438 | 0.9961 | 0.000 | 110 | 0.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | — | 0.04409 | 2.4354 | 0.9933 | 0.138 | 110 | 0.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | — | 0.04410 | 2.4350 | 0.9930 | 0.002 | 110 | 0.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | — | 0.04419 | 2.4486 | 1.0004 | 0.000 | 110 | 0.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | — | 0.04421 | 2.4266 | 0.9920 | 5.907 | 110 | 0.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | — | 0.04517 | 2.4039 | 0.9859 | 64.536 | 110 | 0.0000 |
| `lc_lc0__n_delays_10` | 10 | — | 0.04593 | 2.4675 | 0.9617 | 310.117 | 134 | 0.0000 |
| `lc_lc0__n_delays_15` | 15 | — | 0.04594 | 2.4555 | 0.9596 | 642.766 | 160 | 0.0000 |
| `lc_lc0__n_delays_5` | 5 | — | 0.05059 | 2.3483 | 0.9657 | 219.933 | 110 | 0.0000 |

## Chosen run trajectory prediction

`lc_lc1e-2__n_delays_10` cell params: `{'lightning_kwargs': {'reconstruction_mode': 'uniform', 'loop_closure_weight': 0.01}, 'n_delays': 10}`

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

### standard / k10

#### 7b → CPB

![7b → CPB (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__7b_to_CPB.png)

#### 7b → FEF

![7b → FEF (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__7b_to_FEF.png)

#### 7b → vlPFC

![7b → vlPFC (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__7b_to_vlPFC.png)

#### CPB → 7b

![CPB → 7b (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__CPB_to_7b.png)

#### CPB → FEF

![CPB → FEF (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__CPB_to_FEF.png)

#### CPB → vlPFC

![CPB → vlPFC (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__CPB_to_vlPFC.png)

#### FEF → 7b

![FEF → 7b (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__FEF_to_7b.png)

#### FEF → CPB

![FEF → CPB (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__FEF_to_CPB.png)

#### FEF → vlPFC

![FEF → vlPFC (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__FEF_to_vlPFC.png)

#### vlPFC → 7b

![vlPFC → 7b (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__vlPFC_to_7b.png)

#### vlPFC → CPB

![vlPFC → CPB (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__vlPFC_to_CPB.png)

#### vlPFC → FEF

![vlPFC → FEF (standard/k10)](figures/gramians_per_pair/gramian_pair__standard__k10__vlPFC_to_FEF.png)

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
| `lc_lc0__n_delays_10` | 10 | ? | 0.0459 | 2.4675 | — | 31.0000 |
| `lc_lc0__n_delays_15` | 15 | ? | 0.0470 | 2.4440 | — | 50.0000 |
| `lc_lc0__n_delays_5` | 5 | ? | 0.0513 | 2.3664 | — | 26.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | ? | 0.0380 | 2.4510 | — | 65.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | ? | 0.0425 | 2.4626 | — | 48.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | ? | 0.0442 | 2.4486 | — | 43.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | ? | 0.0363 | 2.4327 | — | 87.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | ? | 0.0431 | 2.4678 | — | 49.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | ? | 0.0441 | 2.4438 | — | 43.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | ? | 0.0378 | 2.4500 | — | 69.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | ? | 0.0391 | 2.4273 | — | 65.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | ? | 0.0441 | 2.4350 | — | 43.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | ? | 0.0375 | 2.4357 | — | 70.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | ? | 0.0422 | 2.4656 | — | 50.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | ? | 0.0441 | 2.4354 | — | 43.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | ? | 0.0381 | 2.4181 | — | 77.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | ? | 0.0428 | 2.4571 | — | 50.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | ? | 0.0442 | 2.4266 | — | 43.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | ? | 0.0415 | 2.4341 | — | 53.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | ? | 0.0427 | 2.3930 | — | 70.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | ? | 0.0453 | 2.4288 | — | 42.0000 |