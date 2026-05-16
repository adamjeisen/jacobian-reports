# mary_propofol_resting__Mary-Anesthesia-20160902-02__awake_maint__ds1__nopre_decF_w0_nt99_pred10__mar__bc0b9228__20260516T033519Z

- wandb group: [mary_propofol_resting__Mary-Anesthesia-20160902-02__awake_maint__ds1__nopre_decF_w0_nt99_pred10__mar__bc0b9228__20260516T033519Z](https://wandb.ai/JacobianODE/MindControl_Mary_propofol_resting/groups/mary_propofol_resting__Mary-Anesthesia-20160902-02__awake_maint__ds1__nopre_decF_w0_nt99_pred10__mar__bc0b9228__20260516T033519Z)
- chosen cell: **`lc_lc1e-4__n_delays_10`** (trajectory val_loss (min over history) = 0.0695)
- cells reported: 21

**Description**: 21 cells: 3 n_delays × 7 loop_closure_weight at nt=0.99, ds=1, on Mary-Anesthesia-20160902-02. n_delays ∈ {5, 10, 15}. loop_closure_weight ∈ {0, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1}. obs_noise_scale=0. 6-hour SLURM cap, migrate_to=mit_normal_gpu. All other knobs match the Mary-20160809 + MrJones-20160105 LC × nd siblings.

**Hypothesis**

```
The Mary-20160809 + MrJones-20160105 LC × nd sweeps both showed the
LC sweet spot in 1e-3 to 1e-1 with a late-bloomer at lc=1e-1, nd=10.
Expect Mary-Anesthesia-20160902-02 to land in the same regime.
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

**Chosen run** (by `best_traj_loss`): `lc_lc1e-4__n_delays_10` (trajectory val_loss (min over history) = 0.0695). Hard criteria applied after relaxation: C1, C2, C3. Survivors / candidates: 12/21.

### Per-run results

| run_name | `n_delays` | `lc` | best_traj_loss | MASE | dec_corr_MASE | LC loss | n_dyn | fast_eig_frac |
|---|---|---|---|---|---|---|---|---|
| `lc_lc1e-4__n_delays_10` | 10 | — | 0.06949 | 1.8899 | 0.9179 | 2.027 | 135 | 0.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | — | 0.06968 | 1.9000 | 0.9213 | 0.012 | 135 | 0.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | — | 0.07053 | 1.9003 | 0.9256 | 0.000 | 135 | 0.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | — | 0.07167 | 1.9309 | 0.9441 | 0.000 | 110 | 0.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | — | 0.07177 | 1.9060 | 0.9336 | 0.022 | 110 | 0.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | — | 0.07190 | 1.9069 | 0.9352 | 0.000 | 110 | 0.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | — | 0.07232 | 1.8847 | 0.9247 | 2.551 | 110 | 0.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | — | 0.07292 | 1.8567 | 0.9104 | 46.414 | 135 | 0.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | — | 0.07459 | 1.8547 | 0.9224 | 30.859 | 110 | 0.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | — | 0.07687 | 1.8132 | 0.9109 | 74.354 | 110 | 0.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | — | 0.07692 | 1.8667 | 0.9093 | 195.120 | 135 | 0.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | — | 0.07727 | 1.8885 | 0.9071 | 0.841 | 161 | 0.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | — | 0.07739 | 1.8699 | 0.9038 | 34.736 | 161 | 0.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | — | 0.07756 | 1.8979 | 0.9094 | 0.008 | 161 | 0.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | — | 0.07911 | 1.8932 | 0.9150 | 0.000 | 161 | 0.0000 |
| `lc_lc0__n_delays_5` | 5 | — | 0.08012 | 1.8060 | 0.9113 | 599.542 | 110 | 0.0000 |
| `lc_lc0__n_delays_10` | 10 | — | 0.08303 | 1.8581 | 0.9090 | 1437.531 | 135 | 0.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | — | 0.08602 | 1.9128 | 0.9081 | 0.000 | 161 | 0.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | — | 0.08622 | 1.9161 | 0.9066 | 70.164 | 161 | 0.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | — | 0.08718 | 1.9131 | 0.9088 | 0.000 | 135 | 0.0000 |
| `lc_lc0__n_delays_15` | 15 | — | 0.08862 | 1.8379 | 0.9000 | 2104.601 | 161 | 0.0000 |

## Chosen run trajectory prediction

`lc_lc1e-4__n_delays_10` cell params: `{'lightning_kwargs': {'reconstruction_mode': 'uniform', 'loop_closure_weight': 0.0001}, 'n_delays': 10}`

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
| `lc_lc0__n_delays_10` | 10 | ? | 0.0871 | 1.8277 | — | 52.0000 |
| `lc_lc0__n_delays_15` | 15 | ? | 0.0886 | 1.8379 | — | 43.0000 |
| `lc_lc0__n_delays_5` | 5 | ? | 0.0831 | 1.8329 | — | 37.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | ? | 0.0725 | 1.9103 | — | 83.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | ? | 0.0791 | 1.8932 | — | 43.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | ? | 0.0730 | 1.9308 | — | 60.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | ? | 0.0875 | 1.9046 | — | 27.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | ? | 0.0919 | 1.9617 | — | 31.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | ? | 0.0731 | 1.9036 | — | 60.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | ? | 0.0711 | 1.9088 | — | 62.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | ? | 0.0788 | 1.9011 | — | 44.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | ? | 0.0726 | 1.9059 | — | 59.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | ? | 0.0708 | 1.8953 | — | 59.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | ? | 0.0773 | 1.8885 | — | 43.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | ? | 0.0723 | 1.8847 | — | 56.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | ? | 0.0758 | 1.8599 | — | 61.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | ? | 0.0785 | 1.8699 | — | 44.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | ? | 0.0755 | 1.8498 | — | 56.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | ? | 0.0823 | 1.8441 | — | 52.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | ? | 0.0887 | 1.9241 | — | 31.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | ? | 0.0795 | 1.8415 | — | 37.0000 |