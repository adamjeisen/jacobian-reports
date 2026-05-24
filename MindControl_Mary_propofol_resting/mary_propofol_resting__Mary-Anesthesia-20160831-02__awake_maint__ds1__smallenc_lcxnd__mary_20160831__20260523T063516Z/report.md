# mary_propofol_resting__Mary-Anesthesia-20160831-02__awake_maint__ds1__smallenc_lcxnd__mary_20160831__20260523T063516Z

- wandb group: [mary_propofol_resting__Mary-Anesthesia-20160831-02__awake_maint__ds1__smallenc_lcxnd__mary_20160831__20260523T063516Z](https://wandb.ai/JacobianODE/MindControl_Mary_propofol_resting/groups/mary_propofol_resting__Mary-Anesthesia-20160831-02__awake_maint__ds1__smallenc_lcxnd__mary_20160831__20260523T063516Z)
- chosen cell: **`lc_lc1e-1__n_delays_15`** (trajectory val_loss (min over history) = 0.0294)
- cells reported: 28

**Description**: Small-encoder (hidden_dim=128, n_coupling_layers=8 ~= 4.4M) n_delays x loop_closure_weight grid on Mary-Anesthesia-20160831-02. Regular dynamics MLP [2048,2048,4096,4096]. n_delays in {5,10,15,20} x loop_closure_weight in {0,1e-6,1e-5,1e-4,1e-3,1e-2,1e-1} = 28 cells. nt=0.99, pred_steps=10. 6h SLURM cap, partition=ou_bcs_normal + qos=mit_amf_advanced_gpu, migrate_to=mit_normal_gpu.

**Hypothesis**

```
Under the small encoder, lc>0 progressively linearizes the learned Jacobians (low jac_temporal_cv) while a moderate lc minimizes trajectory val_loss. Replicate the Mary-0818 grid on Mary-Anesthesia-20160831-02 to test whether the (nd, lc) operating-point pattern is session-agnostic.
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

**Chosen run** (by `best_traj_loss`): `lc_lc1e-1__n_delays_15` (trajectory val_loss (min over history) = 0.0294). Hard criteria applied after relaxation: C1, C2, C3. Survivors / candidates: 19/28.

### Per-run results

| run_name | `n_delays` | `lc` | best_traj_loss | MASE | dec_corr_MASE | LC loss | n_dyn | fast_eig_frac |
|---|---|---|---|---|---|---|---|---|
| `lc_lc1e-1__n_delays_15` | 15 | — | 0.02944 | 3.0143 | 0.9787 | 0.000 | 96 | 0.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | — | 0.02954 | 2.9113 | 0.9682 | 0.098 | 96 | 0.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | — | 0.02977 | 2.7654 | 0.9691 | 0.290 | 85 | 0.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | — | 0.02990 | 2.8107 | 0.9756 | 0.002 | 85 | 0.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | — | 0.03002 | 2.7652 | 0.9691 | 5.705 | 85 | 0.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | — | 0.03048 | 2.8287 | 0.9757 | 0.000 | 85 | 0.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | — | 0.03067 | 2.9313 | 0.9703 | 2.244 | 96 | 0.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | — | 0.03071 | 2.7795 | 0.9898 | 1.646 | 74 | 0.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | — | 0.03093 | 2.9378 | 0.9711 | 0.027 | 96 | 0.0000 |
| `lc_lc1e-5__n_delays_20` | 20 | — | 0.03134 | 3.0695 | 0.9741 | 10.017 | 105 | 0.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | — | 0.03137 | 2.9234 | 0.9693 | 84.480 | 96 | 0.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | — | 0.03148 | 2.9670 | 0.9771 | 0.001 | 96 | 0.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | — | 0.03165 | 2.7593 | 0.9723 | 111.529 | 85 | 0.0000 |
| `lc_lc1e-4__n_delays_20` | 20 | — | 0.03187 | 3.0814 | 0.9750 | 0.107 | 105 | 0.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | — | 0.03206 | 2.8072 | 0.9766 | 0.007 | 85 | 0.0000 |
| `lc_lc0__n_delays_15` | 15 | — | 0.03243 | 2.9168 | 0.9708 | 1351.554 | 96 | 0.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | — | 0.03250 | 2.8209 | 0.9999 | 0.013 | 74 | 0.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | — | 0.03253 | 2.7456 | 0.9829 | 20.977 | 74 | 0.0000 |
| `lc_lc1e-2__n_delays_20` | 20 | — | 0.03254 | 3.1350 | 0.9774 | 0.001 | 105 | 0.0000 |
| `lc_lc1e-3__n_delays_20` | 20 | — | 0.03281 | 3.1323 | 0.9771 | 0.022 | 105 | 0.0000 |
| `lc_lc1e-1__n_delays_20` | 20 | — | 0.03289 | 3.1991 | 0.9801 | 0.000 | 105 | 0.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | — | 0.03297 | 2.7614 | 0.9866 | 0.018 | 74 | 0.0000 |
| `lc_lc1e-6__n_delays_20` | 20 | — | 0.03345 | 3.0933 | 0.9739 | 118.131 | 105 | 0.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | — | 0.03355 | 2.8316 | 1.0000 | 0.000 | 74 | 0.0000 |
| `lc_lc0__n_delays_5` | 5 | — | 0.03358 | 2.7564 | 0.9876 | 702.251 | 74 | 0.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | — | 0.03435 | 2.8635 | 1.0012 | 0.000 | 74 | 0.0000 |
| `lc_lc0__n_delays_10` | 10 | — | 0.03463 | 2.7419 | 0.9718 | 1899.522 | 85 | 0.0000 |
| `lc_lc0__n_delays_20` | 20 | — | 0.03612 | 3.2299 | 0.9751 | 756.646 | 105 | 0.0000 |

## Chosen run trajectory prediction

`lc_lc1e-1__n_delays_15` cell params: `{'lightning_kwargs': {'reconstruction_mode': 'uniform', 'loop_closure_weight': 0.1}, 'n_delays': 15}`

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
| `lc_lc0__n_delays_10` | 10 | ? | 0.0355 | 2.7281 | — | 75.0000 |
| `lc_lc0__n_delays_15` | 15 | ? | 0.0324 | 2.9168 | — | 55.0000 |
| `lc_lc0__n_delays_20` | 20 | ? | 0.0365 | 3.1713 | — | 41.0000 |
| `lc_lc0__n_delays_5` | 5 | ? | 0.0336 | 2.7564 | — | 49.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | ? | 0.0307 | 2.8385 | — | 87.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | ? | 0.0298 | 3.0178 | — | 85.0000 |
| `lc_lc1e-1__n_delays_20` | 20 | ? | 0.0329 | 3.1991 | — | 68.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | ? | 0.0344 | 2.8829 | — | 49.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | ? | 0.0302 | 2.8135 | — | 92.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | ? | 0.0316 | 2.9742 | — | 58.0000 |
| `lc_lc1e-2__n_delays_20` | 20 | ? | 0.0329 | 3.1309 | — | 67.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | ? | 0.0339 | 2.8534 | — | 49.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | ? | 0.0324 | 2.8177 | — | 62.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | ? | 0.0314 | 2.9277 | — | 58.0000 |
| `lc_lc1e-3__n_delays_20` | 20 | ? | 0.0329 | 3.1196 | — | 61.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | ? | 0.0330 | 2.8463 | — | 49.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | ? | 0.0300 | 2.7704 | — | 87.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | ? | 0.0296 | 2.9078 | — | 69.0000 |
| `lc_lc1e-4__n_delays_20` | 20 | ? | 0.0319 | 3.0814 | — | 68.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | ? | 0.0331 | 2.7881 | — | 43.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | ? | 0.0303 | 2.7702 | — | 88.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | ? | 0.0311 | 2.9208 | — | 58.0000 |
| `lc_lc1e-5__n_delays_20` | 20 | ? | 0.0317 | 3.0513 | — | 86.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | ? | 0.0308 | 2.7810 | — | 63.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | ? | 0.0320 | 2.7446 | — | 81.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | ? | 0.0322 | 2.9220 | — | 57.0000 |
| `lc_lc1e-6__n_delays_20` | 20 | ? | 0.0340 | 3.0691 | — | 60.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | ? | 0.0326 | 2.7743 | — | 49.0000 |