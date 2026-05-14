# mary_propofol_resting__Mary-Anesthesia-20160916-02__awake_maint__ds1__nopre_decF_w0_pred10__mary_201__a2c1b084__20260514T023018Z

- wandb group: [mary_propofol_resting__Mary-Anesthesia-20160916-02__awake_maint__ds1__nopre_decF_w0_pred10__mary_201__a2c1b084__20260514T023018Z](https://wandb.ai/JacobianODE/MindControl_Mary_propofol_resting/groups/mary_propofol_resting__Mary-Anesthesia-20160916-02__awake_maint__ds1__nopre_decF_w0_pred10__mary_201__a2c1b084__20260514T023018Z)
- chosen cell: **`n_delays_5`** (trajectory val_loss (min over history) = 0.0622)
- cells reported: 7

**Description**: 7 cells on Mary-Anesthesia-20160916-02 (end (10th of 10) — 2016-09-16, last Mary recording day). Grid: n_delays ∈ {1, 5, 10, 15, 20, 25, 30}, fixed nt=0.99, ds=1. Identical config to the other nd pilots. 6h SLURM cap with migrate_to=mit_normal_gpu.

**Hypothesis**

```
Same as the other nd pilots — expect top-3 nd at nt=0.99 to fall in
{5, 10, 15} (which is what Mary-20160809 + MrJones-20160105 both
show). If the sweet-spot drifts on a late-recording session, that's
important to know before committing to the LC×nd sweep on the rest.
```

**Success criteria** (manual review until automated):

- [ ] All 7 cells run within the 6-hour SLURM cap (or TIMEOUT).
- [ ] val/one_step_mase finite for all cells.
- [ ] Top-3 n_delays at nt=0.99 fall within {5, 10, 15, 20}.

## Run picking

![sweep overview](figures/sweep_overview.png)

Four panels: C1 (one-step MASE — uses `val/decoder_corrected_one_step_mase` per cell when available; threshold = 1 = decoded persistence baseline), C2 (loop closure — plots `LC / sqrt(n_dyn)` against y=1 when each cell carries its own `n_dyn`, otherwise raw LC vs the shared sqrt(n_dyn) line), C3 (fast eigenvalue fraction), trajectory val loss (min over training history). Bars are color-coded green = passes all selection criteria, red = excluded by some criterion, gold = the selected best run.

![sweep pareto](figures/sweep_pareto.png)

Pareto front in (loop closure loss, trajectory val loss) space. Gold star = the selected run.

**Chosen run** (by `best_traj_loss`): `n_delays_5` (trajectory val_loss (min over history) = 0.0622). Hard criteria applied after relaxation: C1, C3. Survivors / candidates: 6/7.

### Per-run results

| run_name | `n_delays` | best_traj_loss | MASE | dec_corr_MASE | LC loss | n_dyn | fast_eig_frac |
|---|---|---|---|---|---|---|---|
| `n_delays_5` | 5 | 0.06217 | 1.8283 | 0.9357 | 75.104 | 110 | 0.0000 |
| `n_delays_10` | 10 | 0.06519 | 1.8373 | 0.9247 | 134.890 | 133 | 0.0000 |
| `n_delays_15` | 15 | 0.06766 | 1.8490 | 0.9086 | 190.040 | 155 | 0.0000 |
| `n_delays_20` | 20 | 0.07225 | 2.0049 | 0.9196 | 184.698 | 177 | 0.0000 |
| `n_delays_25` | 25 | 0.07476 | 2.1473 | 0.9293 | 230.066 | 198 | 0.0000 |
| `n_delays_30` | 30 | 0.09023 | 2.3789 | 0.9465 | 220.364 | 221 | 0.0000 |
| `n_delays_1` | 1 | 0.14615 | 2.0519 | 1.0546 | 936.432 | 93 | 0.0000 |

## Chosen run trajectory prediction

`n_delays_5` cell params: `{'n_delays': 5}`

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
| `n_delays_1` | 1 | ? | 0.1475 | 2.0411 | — | 33.0000 |
| `n_delays_10` | 10 | ? | 0.0658 | 1.8517 | — | 47.0000 |
| `n_delays_15` | 15 | ? | 0.0677 | 1.8490 | — | 40.0000 |
| `n_delays_20` | 20 | ? | 0.0728 | 1.9827 | — | 28.0000 |
| `n_delays_25` | 25 | ? | 0.0748 | 2.1473 | — | 24.0000 |
| `n_delays_30` | 30 | ? | 0.0969 | 2.4283 | — | 18.0000 |
| `n_delays_5` | 5 | ? | 0.0631 | 1.8530 | — | 49.0000 |