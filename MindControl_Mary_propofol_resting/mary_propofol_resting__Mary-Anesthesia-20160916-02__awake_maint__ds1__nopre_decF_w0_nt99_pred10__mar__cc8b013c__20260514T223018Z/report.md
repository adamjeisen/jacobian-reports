# mary_propofol_resting__Mary-Anesthesia-20160916-02__awake_maint__ds1__nopre_decF_w0_nt99_pred10__mar__cc8b013c__20260514T223018Z

- wandb group: [mary_propofol_resting__Mary-Anesthesia-20160916-02__awake_maint__ds1__nopre_decF_w0_nt99_pred10__mar__cc8b013c__20260514T223018Z](https://wandb.ai/JacobianODE/MindControl_Mary_propofol_resting/groups/mary_propofol_resting__Mary-Anesthesia-20160916-02__awake_maint__ds1__nopre_decF_w0_nt99_pred10__mar__cc8b013c__20260514T223018Z)
- chosen cell: **`lc_lc1e-3__n_delays_5`** (trajectory val_loss (min over history) = 0.0570)
- cells reported: 21

**Description**: 21 cells: 3 n_delays × 7 loop_closure_weight at nt=0.99, ds=1, on Mary-Anesthesia-20160916-02. n_delays ∈ {5, 10, 15}. loop_closure_weight ∈ {0, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1}. obs_noise_scale=0. 6-hour SLURM cap, migrate_to=mit_normal_gpu. All other knobs match the Mary-20160809 + MrJones-20160105 LC × nd siblings.

**Hypothesis**

```
The Mary-20160809 + MrJones-20160105 LC × nd sweeps both showed the
LC sweet spot in 1e-3 to 1e-1 with a late-bloomer at lc=1e-1, nd=10.
Expect Mary-Anesthesia-20160916-02 to land in the same regime.
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

**Chosen run** (by `best_traj_loss`): `lc_lc1e-3__n_delays_5` (trajectory val_loss (min over history) = 0.0570). Hard criteria applied after relaxation: C1, C2, C3. Survivors / candidates: 15/21.

### Per-run results

| run_name | `n_delays` | `lc` | best_traj_loss | MASE | dec_corr_MASE | LC loss | n_dyn | fast_eig_frac |
|---|---|---|---|---|---|---|---|---|
| `lc_lc1e-3__n_delays_5` | 5 | — | 0.05697 | 1.8575 | 0.9397 | 0.005 | 110 | 0.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | — | 0.05717 | 1.8474 | 0.9369 | 0.403 | 110 | 0.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | — | 0.05728 | 1.8402 | 0.9342 | 7.787 | 110 | 0.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | — | 0.05729 | 1.8566 | 0.9384 | 0.000 | 110 | 0.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | — | 0.05751 | 1.8116 | 0.9177 | 11.284 | 133 | 0.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | — | 0.05754 | 1.8500 | 0.9377 | 0.000 | 110 | 0.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | — | 0.05813 | 1.8353 | 0.9343 | 38.854 | 110 | 0.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | — | 0.06101 | 1.8505 | 0.9259 | 0.347 | 133 | 0.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | — | 0.06129 | 1.8422 | 0.9238 | 44.598 | 133 | 0.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | — | 0.06136 | 1.8534 | 0.9266 | 0.006 | 133 | 0.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | — | 0.06142 | 1.8610 | 0.9304 | 0.003 | 133 | 0.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | — | 0.06172 | 1.8643 | 0.9330 | 0.000 | 133 | 0.0000 |
| `lc_lc0__n_delays_5` | 5 | — | 0.06223 | 1.8283 | 0.9358 | 75.083 | 110 | 0.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | — | 0.06283 | 1.8307 | 0.9086 | 0.010 | 155 | 0.0000 |
| `lc_lc0__n_delays_10` | 10 | — | 0.06519 | 1.8373 | 0.9247 | 134.890 | 133 | 0.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | — | 0.06643 | 1.8494 | 0.9080 | 46.626 | 155 | 0.0000 |
| `lc_lc0__n_delays_15` | 15 | — | 0.06766 | 1.8490 | 0.9086 | 190.040 | 155 | 0.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | — | 0.06777 | 1.8700 | 0.9083 | 3.453 | 155 | 0.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | — | 0.06797 | 1.8793 | 0.9110 | 0.152 | 155 | 0.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | — | 0.06897 | 1.8870 | 0.9112 | 0.000 | 155 | 0.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | — | 0.06921 | 1.8865 | 0.9138 | 0.000 | 155 | 0.0000 |

## Chosen run trajectory prediction

`lc_lc1e-3__n_delays_5` cell params: `{'lightning_kwargs': {'reconstruction_mode': 'uniform', 'loop_closure_weight': 0.001}, 'n_delays': 5}`

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
| `lc_lc0__n_delays_10` | 10 | ? | 0.0658 | 1.8517 | — | 47.0000 |
| `lc_lc0__n_delays_15` | 15 | ? | 0.0685 | 1.8812 | — | 41.0000 |
| `lc_lc0__n_delays_5` | 5 | ? | 0.0631 | 1.8535 | — | 49.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | ? | 0.0632 | 1.8663 | — | 55.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | ? | 0.0697 | 1.8874 | — | 41.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | ? | 0.0584 | 1.8558 | — | 66.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | ? | 0.0628 | 1.8644 | — | 54.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | ? | 0.0691 | 1.8854 | — | 41.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | ? | 0.0581 | 1.8445 | — | 66.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | ? | 0.0622 | 1.8481 | — | 55.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | ? | 0.0639 | 1.8329 | — | 59.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | ? | 0.0579 | 1.8448 | — | 66.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | ? | 0.0621 | 1.8450 | — | 55.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | ? | 0.0680 | 1.8793 | — | 41.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | ? | 0.0575 | 1.8422 | — | 66.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | ? | 0.0582 | 1.8108 | — | 80.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | ? | 0.0678 | 1.8763 | — | 41.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | ? | 0.0575 | 1.8373 | — | 66.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | ? | 0.0616 | 1.8395 | — | 54.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | ? | 0.0687 | 1.8545 | — | 43.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | ? | 0.0582 | 1.8310 | — | 66.0000 |