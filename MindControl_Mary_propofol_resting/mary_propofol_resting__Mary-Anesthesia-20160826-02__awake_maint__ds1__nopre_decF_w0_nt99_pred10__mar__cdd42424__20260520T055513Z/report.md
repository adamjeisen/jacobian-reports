# mary_propofol_resting__Mary-Anesthesia-20160826-02__awake_maint__ds1__nopre_decF_w0_nt99_pred10__mar__cdd42424__20260520T055513Z

- wandb group: [mary_propofol_resting__Mary-Anesthesia-20160826-02__awake_maint__ds1__nopre_decF_w0_nt99_pred10__mar__cdd42424__20260520T055513Z](https://wandb.ai/JacobianODE/MindControl_Mary_propofol_resting/groups/mary_propofol_resting__Mary-Anesthesia-20160826-02__awake_maint__ds1__nopre_decF_w0_nt99_pred10__mar__cdd42424__20260520T055513Z)
- chosen cell: **`lc_lc1e-3__n_delays_10`** (trajectory val_loss (min over history) = 0.0573)
- cells reported: 21

**Description**: 21 cells: 3 n_delays × 7 loop_closure_weight at nt=0.99, ds=1, on Mary-Anesthesia-20160826-02. n_delays ∈ {5, 10, 15}. loop_closure_weight ∈ {0, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1}. obs_noise_scale=0. 6-hour SLURM cap, migrate_to=mit_normal_gpu. All other knobs match the Mary-20160809 + MrJones-20160105 LC × nd siblings.

**Hypothesis**

```
The Mary-20160809 + MrJones-20160105 LC × nd sweeps both showed the
LC sweet spot in 1e-3 to 1e-1 with a late-bloomer at lc=1e-1, nd=10.
Expect Mary-Anesthesia-20160826-02 to land in the same regime.
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

**Chosen run** (by `best_traj_loss`): `lc_lc1e-3__n_delays_10` (trajectory val_loss (min over history) = 0.0573). Hard criteria applied after relaxation: C1, C2, C3. Survivors / candidates: 13/21.

### Per-run results

| run_name | `n_delays` | `lc` | best_traj_loss | MASE | dec_corr_MASE | LC loss | n_dyn | fast_eig_frac |
|---|---|---|---|---|---|---|---|---|
| `lc_lc1e-3__n_delays_10` | 10 | — | 0.05731 | 2.1770 | 0.9406 | 0.004 | 129 | 0.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | — | 0.05734 | 2.1954 | 0.9624 | 0.000 | 109 | 0.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | — | 0.05783 | 2.1789 | 0.9413 | 0.000 | 129 | 0.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | — | 0.05808 | 2.1533 | 0.9478 | 0.005 | 109 | 0.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | — | 0.05816 | 2.1481 | 0.9460 | 0.190 | 109 | 0.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | — | 0.05821 | 2.1907 | 0.9423 | 0.000 | 129 | 0.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | — | 0.05828 | 2.1618 | 0.9518 | 0.000 | 109 | 0.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | — | 0.05868 | 2.1637 | 0.9371 | 17.016 | 129 | 0.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | — | 0.05892 | 2.1386 | 0.9426 | 7.722 | 109 | 0.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | — | 0.05898 | 2.1888 | 0.9341 | 0.005 | 149 | 0.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | — | 0.05913 | 2.1688 | 0.9327 | 0.002 | 149 | 0.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | — | 0.05948 | 2.1876 | 0.9326 | 0.116 | 149 | 0.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | — | 0.06002 | 2.1794 | 0.9314 | 15.147 | 149 | 0.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | — | 0.06030 | 2.1942 | 0.9366 | 0.000 | 149 | 0.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | — | 0.06091 | 2.1041 | 0.9362 | 69.320 | 109 | 0.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | — | 0.06200 | 2.1681 | 0.9345 | 137.831 | 129 | 0.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | — | 0.06292 | 2.1609 | 0.9277 | 260.595 | 149 | 0.0000 |
| `lc_lc0__n_delays_5` | 5 | — | 0.06353 | 2.1005 | 0.9364 | 606.826 | 109 | 0.0000 |
| `lc_lc0__n_delays_15` | 15 | — | 0.06642 | 2.2272 | 0.9301 | 848.620 | 149 | 0.0000 |
| `lc_lc0__n_delays_10` | 10 | — | 0.06676 | 2.1626 | 0.9315 | 824.375 | 129 | 0.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | — | 0.07414 | 2.1997 | 0.9310 | 0.067 | 129 | 0.0000 |

## Chosen run trajectory prediction

`lc_lc1e-3__n_delays_10` cell params: `{'lightning_kwargs': {'reconstruction_mode': 'uniform', 'loop_closure_weight': 0.001}, 'n_delays': 10}`

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
| `lc_lc0__n_delays_10` | 10 | ? | 0.0707 | 2.1143 | — | 54.0000 |
| `lc_lc0__n_delays_15` | 15 | ? | 0.0679 | 2.1588 | — | 41.0000 |
| `lc_lc0__n_delays_5` | 5 | ? | 0.0650 | 2.1161 | — | 37.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | ? | 0.0592 | 2.1972 | — | 53.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | ? | 0.0603 | 2.1942 | — | 41.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | ? | 0.0574 | 2.2136 | — | 49.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | ? | 0.0587 | 2.1826 | — | 53.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | ? | 0.0592 | 2.1642 | — | 58.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | ? | 0.0591 | 2.1789 | — | 42.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | ? | 0.0581 | 2.1787 | — | 54.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | ? | 0.0590 | 2.1888 | — | 41.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | ? | 0.0588 | 2.1769 | — | 42.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | ? | 0.0741 | 2.1997 | — | 16.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | ? | 0.0595 | 2.1876 | — | 41.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | ? | 0.0589 | 2.1672 | — | 42.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | ? | 0.0595 | 2.1572 | — | 55.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | ? | 0.0600 | 2.1794 | — | 41.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | ? | 0.0589 | 2.1386 | — | 37.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | ? | 0.0640 | 2.1304 | — | 57.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | ? | 0.0642 | 2.1472 | — | 49.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | ? | 0.0612 | 2.1193 | — | 37.0000 |