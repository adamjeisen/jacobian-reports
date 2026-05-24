# mary_propofol_resting__Mary-Anesthesia-20160826-02__awake_maint__ds1__smallenc_lcxnd__mary_20160826__20260523T063515Z

- wandb group: [mary_propofol_resting__Mary-Anesthesia-20160826-02__awake_maint__ds1__smallenc_lcxnd__mary_20160826__20260523T063515Z](https://wandb.ai/JacobianODE/MindControl_Mary_propofol_resting/groups/mary_propofol_resting__Mary-Anesthesia-20160826-02__awake_maint__ds1__smallenc_lcxnd__mary_20160826__20260523T063515Z)
- chosen cell: **`lc_lc1e-3__n_delays_5`** (trajectory val_loss (min over history) = 0.0530)
- cells reported: 28

**Description**: Small-encoder (hidden_dim=128, n_coupling_layers=8 ~= 4.4M) n_delays x loop_closure_weight grid on Mary-Anesthesia-20160826-02. Regular dynamics MLP [2048,2048,4096,4096]. n_delays in {5,10,15,20} x loop_closure_weight in {0,1e-6,1e-5,1e-4,1e-3,1e-2,1e-1} = 28 cells. nt=0.99, pred_steps=10. 6h SLURM cap, partition=ou_bcs_normal + qos=mit_amf_advanced_gpu, migrate_to=mit_normal_gpu.

**Hypothesis**

```
Under the small encoder, lc>0 progressively linearizes the learned Jacobians (low jac_temporal_cv) while a moderate lc minimizes trajectory val_loss. Replicate the Mary-0818 grid on Mary-Anesthesia-20160826-02 to test whether the (nd, lc) operating-point pattern is session-agnostic.
```

**Success criteria** (manual review until automated):

- [ ] All 28 cells run to early-stopping or the 6h cap.
- [ ] val/one_step_mase finite for all cells.
- [ ] Locate the (nd, lc) operating point that minimizes trajectory val_loss and characterize jac_temporal_cv across the grid.

## Run picking

![sweep overview](figures/sweep_overview.png)

Four panels: C1 (one-step MASE — uses `val/decoder_corrected_one_step_mase` per cell when available; threshold = 1 = decoded persistence baseline), C2 (loop closure — plots `LC / sqrt(n_dyn)` against y=1 when each cell carries its own `n_dyn`, otherwise raw LC vs the shared sqrt(n_dyn) line), C3 (fast eigenvalue fraction), trajectory val loss (min over training history). Bars are color-coded green = passes all selection criteria, red = excluded by some criterion, gold = the selected best run.

![sweep pareto](figures/sweep_pareto.png)

Pareto front in (loop closure loss, trajectory val loss) space. Gold star = the selected run.

**Chosen run** (by `best_traj_loss`): `lc_lc1e-3__n_delays_5` (trajectory val_loss (min over history) = 0.0530). Hard criteria applied after relaxation: C1, C2, C3. Survivors / candidates: 17/28.

### Per-run results

| run_name | `n_delays` | `lc` | best_traj_loss | MASE | dec_corr_MASE | LC loss | n_dyn | fast_eig_frac |
|---|---|---|---|---|---|---|---|---|
| `lc_lc1e-3__n_delays_5` | 5 | — | 0.05297 | 2.2565 | 0.9492 | 0.034 | 109 | 0.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | — | 0.05316 | 2.2821 | 0.9595 | 0.005 | 109 | 0.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | — | 0.05405 | 2.2350 | 0.9486 | 1.916 | 109 | 0.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | — | 0.05513 | 2.3257 | 0.9749 | 0.000 | 109 | 0.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | — | 0.05573 | 2.4301 | 0.9525 | 2.895 | 129 | 0.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | — | 0.05649 | 2.5778 | 0.9534 | 0.025 | 149 | 0.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | — | 0.05696 | 2.5338 | 0.9507 | 3.235 | 149 | 0.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | — | 0.05726 | 2.4917 | 0.9614 | 0.000 | 129 | 0.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | — | 0.05754 | 2.4489 | 0.9564 | 0.019 | 129 | 0.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | — | 0.05783 | 2.6020 | 0.9571 | 0.007 | 149 | 0.0000 |
| `lc_lc1e-4__n_delays_20` | 20 | — | 0.05792 | 2.7767 | 0.9600 | 2.384 | 169 | 0.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | — | 0.05862 | 2.3860 | 0.9473 | 63.098 | 129 | 0.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | — | 0.05903 | 2.4597 | 0.9591 | 0.003 | 129 | 0.0000 |
| `lc_lc1e-3__n_delays_20` | 20 | — | 0.05930 | 2.7984 | 0.9632 | 0.089 | 169 | 0.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | — | 0.05961 | 2.6674 | 0.9657 | 0.000 | 149 | 0.0000 |
| `lc_lc1e-1__n_delays_20` | 20 | — | 0.05996 | 2.8943 | 0.9693 | 0.000 | 169 | 0.0000 |
| `lc_lc1e-5__n_delays_20` | 20 | — | 0.06071 | 2.7205 | 0.9566 | 80.273 | 169 | 0.0000 |
| `lc_lc1e-2__n_delays_20` | 20 | — | 0.06073 | 2.8176 | 0.9650 | 0.003 | 169 | 0.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | — | 0.06083 | 2.5288 | 0.9486 | 52.376 | 149 | 0.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | — | 0.06145 | 2.2226 | 0.9394 | 8.162 | 109 | 0.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | — | 0.06438 | 2.2135 | 0.9348 | 169.911 | 109 | 0.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | — | 0.06518 | 2.3954 | 0.9462 | 358.094 | 129 | 0.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | — | 0.06596 | 2.6775 | 0.9542 | 276.603 | 149 | 0.0000 |
| `lc_lc1e-6__n_delays_20` | 20 | — | 0.06701 | 2.7797 | 0.9571 | 462.579 | 169 | 0.0000 |
| `lc_lc0__n_delays_5` | 5 | — | 0.06992 | 2.2523 | 0.9357 | 2239.978 | 109 | 0.0000 |
| `lc_lc0__n_delays_10` | 10 | — | 0.07154 | 2.5733 | 0.9549 | 2903.260 | 129 | 0.0000 |
| `lc_lc0__n_delays_20` | 20 | — | 0.07331 | 2.8340 | 0.9581 | 5889.288 | 169 | 0.0000 |
| `lc_lc0__n_delays_15` | 15 | — | 0.07428 | 2.7919 | 0.9572 | 3316.317 | 149 | 0.0000 |

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
| `lc_lc0__n_delays_10` | 10 | ? | 0.0751 | 2.4289 | — | 32.0000 |
| `lc_lc0__n_delays_15` | 15 | ? | 0.0768 | 2.6017 | — | 33.0000 |
| `lc_lc0__n_delays_20` | 20 | ? | 0.0760 | 2.7312 | — | 42.0000 |
| `lc_lc0__n_delays_5` | 5 | ? | 0.0730 | 2.2122 | — | 27.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | ? | 0.0592 | 2.4954 | — | 83.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | ? | 0.0635 | 2.6546 | — | 77.0000 |
| `lc_lc1e-1__n_delays_20` | 20 | ? | 0.0603 | 2.8861 | — | 56.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | ? | 0.0551 | 2.3257 | — | 57.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | ? | 0.0596 | 2.4536 | — | 52.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | ? | 0.0607 | 2.5947 | — | 77.0000 |
| `lc_lc1e-2__n_delays_20` | 20 | ? | 0.0607 | 2.8176 | — | 56.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | ? | 0.0535 | 2.2796 | — | 68.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | ? | 0.0575 | 2.4489 | — | 55.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | ? | 0.0595 | 2.5739 | — | 77.0000 |
| `lc_lc1e-3__n_delays_20` | 20 | ? | 0.0596 | 2.7862 | — | 57.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | ? | 0.0548 | 2.2589 | — | 72.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | ? | 0.0568 | 2.4269 | — | 71.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | ? | 0.0596 | 2.5277 | — | 77.0000 |
| `lc_lc1e-4__n_delays_20` | 20 | ? | 0.0579 | 2.7767 | — | 57.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | ? | 0.0545 | 2.2434 | — | 58.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | ? | 0.0613 | 2.3600 | — | 71.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | ? | 0.0618 | 2.5035 | — | 58.0000 |
| `lc_lc1e-5__n_delays_20` | 20 | ? | 0.0619 | 2.7244 | — | 58.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | ? | 0.0615 | 2.2182 | — | 31.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | ? | 0.0673 | 2.2910 | — | 58.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | ? | 0.0684 | 2.5977 | — | 36.0000 |
| `lc_lc1e-6__n_delays_20` | 20 | ? | 0.0694 | 2.6776 | — | 51.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | ? | 0.0648 | 2.2101 | — | 29.0000 |