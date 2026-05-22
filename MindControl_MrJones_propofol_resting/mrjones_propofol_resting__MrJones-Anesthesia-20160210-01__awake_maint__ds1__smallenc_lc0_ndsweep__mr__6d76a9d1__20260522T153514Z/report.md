# mrjones_propofol_resting__MrJones-Anesthesia-20160210-01__awake_maint__ds1__smallenc_lc0_ndsweep__mr__6d76a9d1__20260522T153514Z

- wandb group: [mrjones_propofol_resting__MrJones-Anesthesia-20160210-01__awake_maint__ds1__smallenc_lc0_ndsweep__mr__6d76a9d1__20260522T153514Z](https://wandb.ai/JacobianODE/MindControl_MrJones_propofol_resting/groups/mrjones_propofol_resting__MrJones-Anesthesia-20160210-01__awake_maint__ds1__smallenc_lc0_ndsweep__mr__6d76a9d1__20260522T153514Z)
- chosen cell: **`n_delays_10`** (trajectory val_loss (min over history) = 0.0477)
- cells reported: 7

**Description**: Small-encoder (hidden_dim=128, n_coupling_layers=8 ≈ 4.4M, ~21× smaller than the production 93M encoder) n_delays scout at loop_closure_weight=0, on MrJones-Anesthesia-20160210-01. Regular dynamics MLP [2048,2048,4096,4096]. n_delays ∈ {1, 5, 10, 15, 20, 25, 30}, nt=0.99, pred_steps=10. 3h SLURM cap, migrate_to mit_normal_gpu.

**Hypothesis**

```
With the oversized 93M encoder this session chose n_delays=15 and was the
one neural model with non-trivial (mild) Jacobian state-dependence
(jac_temporal_cv~0.05-0.12). Under the 21× smaller encoder + lc=0, sweeping
n_delays tests whether the chosen delay window shifts and whether the
nonlinearity strengthens — paired with the Mary-0818 small-encoder scout.
```

**Success criteria** (manual review until automated):

- [ ] All 7 cells run to early-stopping or the 3h cap.
- [ ] val/one_step_mase finite for all cells.
- [ ] Identify the best-trajectory-loss n_delays under the small encoder and compare to the big-encoder choice (n_delays=15).

## Run picking

![sweep overview](figures/sweep_overview.png)

Four panels: C1 (one-step MASE — uses `val/decoder_corrected_one_step_mase` per cell when available; threshold = 1 = decoded persistence baseline), C2 (loop closure — plots `LC / sqrt(n_dyn)` against y=1 when each cell carries its own `n_dyn`, otherwise raw LC vs the shared sqrt(n_dyn) line), C3 (fast eigenvalue fraction), trajectory val loss (min over training history). Bars are color-coded green = passes all selection criteria, red = excluded by some criterion, gold = the selected best run.

![sweep pareto](figures/sweep_pareto.png)

Pareto front in (loop closure loss, trajectory val loss) space. Gold star = the selected run.

**Chosen run** (by `best_traj_loss`): `n_delays_10` (trajectory val_loss (min over history) = 0.0477). Hard criteria applied after relaxation: C1, C3. Survivors / candidates: 6/7.

### Per-run results

| run_name | `n_delays` | best_traj_loss | MASE | dec_corr_MASE | LC loss | n_dyn | fast_eig_frac |
|---|---|---|---|---|---|---|---|
| `n_delays_10` | 10 | 0.04773 | 2.7657 | 0.9773 | 2270.397 | 139 | 0.0000 |
| `n_delays_15` | 15 | 0.04972 | 3.1355 | 0.9800 | 2349.327 | 166 | 0.0000 |
| `n_delays_5` | 5 | 0.05079 | 2.5516 | 0.9744 | 2498.526 | 113 | 0.0000 |
| `n_delays_20` | 20 | 0.05152 | 3.4620 | 0.9830 | 1729.916 | 192 | 0.0000 |
| `n_delays_25` | 25 | 0.05233 | 3.9638 | 0.9883 | 909.007 | 218 | 0.0000 |
| `n_delays_30` | 30 | 0.05630 | 4.1764 | 0.9893 | 989.543 | 245 | 0.0000 |
| `n_delays_1` | 1 | 0.08751 | 2.5886 | 1.0362 | 3128.398 | 100 | 0.0000 |

## Chosen run trajectory prediction

`n_delays_10` cell params: `{'n_delays': 10}`

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
| `n_delays_1` | 1 | ? | 0.0917 | 2.5658 | — | 31.0000 |
| `n_delays_10` | 10 | ? | 0.0482 | 2.7405 | — | 48.0000 |
| `n_delays_15` | 15 | ? | 0.0506 | 3.0616 | — | 36.0000 |
| `n_delays_20` | 20 | ? | 0.0515 | 3.4620 | — | 31.0000 |
| `n_delays_25` | 25 | ? | 0.0528 | 3.9767 | — | 24.0000 |
| `n_delays_30` | 30 | ? | 0.0563 | 4.1764 | — | 18.0000 |
| `n_delays_5` | 5 | ? | 0.0523 | 2.5310 | — | 39.0000 |