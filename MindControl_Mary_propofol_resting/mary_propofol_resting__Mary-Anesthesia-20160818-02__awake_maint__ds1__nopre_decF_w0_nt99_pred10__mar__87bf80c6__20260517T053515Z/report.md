# mary_propofol_resting__Mary-Anesthesia-20160818-02__awake_maint__ds1__nopre_decF_w0_nt99_pred10__mar__87bf80c6__20260517T053515Z

- wandb group: [mary_propofol_resting__Mary-Anesthesia-20160818-02__awake_maint__ds1__nopre_decF_w0_nt99_pred10__mar__87bf80c6__20260517T053515Z](https://wandb.ai/JacobianODE/MindControl_Mary_propofol_resting/groups/mary_propofol_resting__Mary-Anesthesia-20160818-02__awake_maint__ds1__nopre_decF_w0_nt99_pred10__mar__87bf80c6__20260517T053515Z)
- chosen cell: **`lc_lc1e-2__n_delays_5`** (trajectory val_loss (min over history) = 0.0367)
- cells reported: 21

**Description**: 21 cells: 3 n_delays × 7 loop_closure_weight at nt=0.99, ds=1, on Mary-Anesthesia-20160818-02. n_delays ∈ {5, 10, 15}. loop_closure_weight ∈ {0, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1}. obs_noise_scale=0. 6-hour SLURM cap, migrate_to=mit_normal_gpu. All other knobs match the Mary-20160809 + MrJones-20160105 LC × nd siblings.

**Hypothesis**

```
The Mary-20160809 + MrJones-20160105 LC × nd sweeps both showed the
LC sweet spot in 1e-3 to 1e-1 with a late-bloomer at lc=1e-1, nd=10.
Expect Mary-Anesthesia-20160818-02 to land in the same regime.
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

**Chosen run** (by `best_traj_loss`): `lc_lc1e-2__n_delays_5` (trajectory val_loss (min over history) = 0.0367). Hard criteria applied after relaxation: C1, C2, C3. Survivors / candidates: 12/21.

### Per-run results

| run_name | `n_delays` | `lc` | best_traj_loss | MASE | dec_corr_MASE | LC loss | n_dyn | fast_eig_frac |
|---|---|---|---|---|---|---|---|---|
| `lc_lc1e-2__n_delays_5` | 5 | — | 0.03666 | 2.1900 | 0.9402 | 0.001 | 93 | 0.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | — | 0.03689 | 2.2044 | 0.9431 | 0.000 | 93 | 0.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | — | 0.03708 | 2.1767 | 0.9405 | 0.013 | 93 | 0.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | — | 0.03734 | 2.1819 | 0.9404 | 1.102 | 93 | 0.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | — | 0.03751 | 2.2001 | 0.9396 | 0.001 | 112 | 0.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | — | 0.03754 | 2.1683 | 0.9344 | 3.604 | 112 | 0.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | — | 0.03759 | 2.1705 | 0.9401 | 17.013 | 93 | 0.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | — | 0.03806 | 2.1819 | 0.9355 | 21.201 | 112 | 0.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | — | 0.03848 | 2.1700 | 0.9382 | 64.392 | 93 | 0.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | — | 0.03871 | 2.1904 | 0.9424 | 0.011 | 112 | 0.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | — | 0.03879 | 2.1718 | 0.9359 | 99.166 | 112 | 0.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | — | 0.03948 | 2.1979 | 0.9385 | 0.122 | 112 | 0.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | — | 0.04121 | 2.0818 | 0.9195 | 34.960 | 130 | 0.0000 |
| `lc_lc0__n_delays_10` | 10 | — | 0.04186 | 2.1743 | 0.9390 | 417.243 | 112 | 0.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | — | 0.04199 | 2.0843 | 0.9216 | 208.785 | 130 | 0.0000 |
| `lc_lc0__n_delays_15` | 15 | — | 0.04369 | 2.0810 | 0.9216 | 626.222 | 130 | 0.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | — | 0.04382 | 2.1305 | 0.9240 | 0.922 | 130 | 0.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | — | 0.04399 | 2.1290 | 0.9229 | 0.240 | 130 | 0.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | — | 0.04444 | 2.1367 | 0.9242 | 0.053 | 130 | 0.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | — | 0.04459 | 2.1320 | 0.9248 | 0.002 | 130 | 0.0000 |
| `lc_lc0__n_delays_5` | 5 | — | inf | inf | — | — | — | 1.0000 |

## Chosen run trajectory prediction

`lc_lc1e-2__n_delays_5` cell params: `{'lightning_kwargs': {'reconstruction_mode': 'uniform', 'loop_closure_weight': 0.01}, 'n_delays': 5}`

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
| `lc_lc0__n_delays_10` | 10 | ? | 0.0442 | 2.1708 | — | 87.0000 |
| `lc_lc0__n_delays_15` | 15 | ? | 0.0445 | 2.0742 | — | 63.0000 |
| `lc_lc0__n_delays_5` | 5 | ? | 0.0403 | 2.1591 | — | 76.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | ? | 0.0376 | 2.1889 | — | 86.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | ? | 0.0468 | 2.1460 | — | 46.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | ? | 0.0374 | 2.1987 | — | 85.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | ? | 0.0388 | 2.1903 | — | 62.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | ? | 0.0464 | 2.1396 | — | 46.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | ? | 0.0375 | 2.1844 | — | 85.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | ? | 0.0407 | 2.2014 | — | 63.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | ? | 0.0446 | 2.1259 | — | 47.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | ? | 0.0383 | 2.1824 | — | 76.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | ? | 0.0388 | 2.1763 | — | 81.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | ? | 0.0462 | 2.1351 | — | 46.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | ? | 0.0388 | 2.1864 | — | 76.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | ? | 0.0399 | 2.1773 | — | 85.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | ? | 0.0412 | 2.0818 | — | 63.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | ? | 0.0391 | 2.1779 | — | 76.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | ? | 0.0391 | 2.1632 | — | 80.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | ? | 0.0426 | 2.0799 | — | 63.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | ? | 0.0386 | 2.1723 | — | 83.0000 |