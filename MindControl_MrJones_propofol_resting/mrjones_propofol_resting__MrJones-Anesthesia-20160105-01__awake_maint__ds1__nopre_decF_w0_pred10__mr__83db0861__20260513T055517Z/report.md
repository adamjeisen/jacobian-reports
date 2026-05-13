# mrjones_propofol_resting__MrJones-Anesthesia-20160105-01__awake_maint__ds1__nopre_decF_w0_pred10__mr__83db0861__20260513T055517Z

- wandb group: [mrjones_propofol_resting__MrJones-Anesthesia-20160105-01__awake_maint__ds1__nopre_decF_w0_pred10__mr__83db0861__20260513T055517Z](https://wandb.ai/JacobianODE/MindControl_MrJones_propofol_resting/groups/mrjones_propofol_resting__MrJones-Anesthesia-20160105-01__awake_maint__ds1__nopre_decF_w0_pred10__mr__83db0861__20260513T055517Z)
- chosen cell: **`n_delays_10__n_target_var_threshold_0.99`** (trajectory val_loss (min over history) = 0.0594)
- cells reported: 14

**Description**: 14 cells on MrJones-Anesthesia-20160105-01 (chosen as a sample MrJones propofol session; out of 11 available). Grid: n_delays ∈ {1, 5, 10, 15, 20, 25, 30}, n_target_var_threshold ∈ {0.99, 0.95}. delay_spacing fixed at 1 (no ds=5/10 this time). Other knobs match the prior Mary nopre+pred10 baseline: pre_pca_per_area=false, decoded_only_pred_loss=False, encoder_warmup_epochs=0, batch_size=16, prediction_steps=10, seq_length=25, lp=80 Hz, awake + maintenance dose, lc=0, obs_noise_scale=0. With migrate_to=mit_normal_gpu so the heavier cells move to mit_normal_gpu when the QOS budget allows.

**Hypothesis**

```
The ndelays × nt sweet-spot for the JacobianODE on Mary propofol
LFP was nd≈5–15 at nt=0.99 and nd≈10–20 at nt=0.95. We expect a
similar pattern on MrJones — that is, the optimum n_delays should
shift with nt and depend modestly on the recording, but the broad
shape (concave w.r.t. n_delays) should hold across subjects.
```

**Success criteria** (manual review until automated):

- [ ] All 14 cells run within the 6-hour SLURM cap (or TIMEOUT).
- [ ] val/one_step_mase finite for all cells.
- [ ] At least one (nt, n_delays) cell strictly beats the (nt, n_delays=1) baseline on best trajectory val_loss for both nt values.

## Run picking

![sweep overview](figures/sweep_overview.png)

Four panels: C1 (one-step MASE — uses `val/decoder_corrected_one_step_mase` per cell when available; threshold = 1 = decoded persistence baseline), C2 (loop closure — plots `LC / sqrt(n_dyn)` against y=1 when each cell carries its own `n_dyn`, otherwise raw LC vs the shared sqrt(n_dyn) line), C3 (fast eigenvalue fraction), trajectory val loss (min over training history). Bars are color-coded green = passes all selection criteria, red = excluded by some criterion, gold = the selected best run.

![sweep pareto](figures/sweep_pareto.png)

Pareto front in (loop closure loss, trajectory val loss) space. Gold star = the selected run.

**Chosen run** (by `best_traj_loss`): `n_delays_10__n_target_var_threshold_0.99` (trajectory val_loss (min over history) = 0.0594). Hard criteria applied after relaxation: C1, C3. Survivors / candidates: 11/14.

### Per-run results

| run_name | `n_delays` | `n_target_var_threshold` | best_traj_loss | MASE | dec_corr_MASE | LC loss | n_dyn | fast_eig_frac |
|---|---|---|---|---|---|---|---|---|
| `n_delays_10__n_target_var_threshold_0.99` | 10 | 0.99 | 0.05938 | 2.0384 | 0.9442 | 755.672 | 176 | 0.0000 |
| `n_delays_5__n_target_var_threshold_0.99` | 5 | 0.99 | 0.06121 | 2.0245 | 0.9766 | 572.772 | 140 | 0.0000 |
| `n_delays_15__n_target_var_threshold_0.99` | 15 | 0.99 | 0.06407 | 2.0734 | 0.9414 | 1214.387 | 216 | 0.0000 |
| `n_delays_20__n_target_var_threshold_0.99` | 20 | 0.99 | 0.06446 | 2.1023 | 0.9408 | 1650.504 | 256 | 0.0000 |
| `n_delays_30__n_target_var_threshold_0.99` | 30 | 0.99 | 0.06860 | 2.7364 | 0.9636 | 950.118 | 337 | 0.0000 |
| `n_delays_25__n_target_var_threshold_0.99` | 25 | 0.99 | 0.06935 | 2.3583 | 0.9525 | 1328.563 | 296 | 0.0000 |
| `n_delays_30__n_target_var_threshold_0.95` | 30 | 0.95 | 0.07815 | 4.2767 | 0.9916 | 1723.795 | 78 | 0.0000 |
| `n_delays_20__n_target_var_threshold_0.95` | 20 | 0.95 | 0.08217 | 4.0996 | 0.9921 | 1143.405 | 62 | 0.0000 |
| `n_delays_10__n_target_var_threshold_0.95` | 10 | 0.95 | 0.08250 | 3.9871 | 0.9951 | 602.822 | 48 | 0.0000 |
| `n_delays_15__n_target_var_threshold_0.95` | 15 | 0.95 | 0.08389 | 4.0875 | 0.9945 | 792.050 | 56 | 0.0000 |
| `n_delays_5__n_target_var_threshold_0.95` | 5 | 0.95 | 0.08675 | 3.9647 | 1.0052 | 305.384 | 41 | 0.0000 |
| `n_delays_25__n_target_var_threshold_0.95` | 25 | 0.95 | 0.08793 | 4.2347 | 0.9921 | 1411.261 | 71 | 0.0000 |
| `n_delays_1__n_target_var_threshold_0.99` | 1 | 0.99 | 0.11252 | 2.1667 | 1.0416 | 852.262 | 120 | 0.0000 |
| `n_delays_1__n_target_var_threshold_0.95` | 1 | 0.95 | 0.13022 | 4.0723 | 1.0110 | 1643.868 | 35 | 0.0000 |

## Chosen run trajectory prediction

`n_delays_10__n_target_var_threshold_0.99` cell params: `{'n_delays': 10, 'n_target_var_threshold': 0.99}`

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
| `n_delays_10__n_target_var_threshold_0.95` | 10 | ? | 0.0828 | 3.9926 | — | 50.0000 |
| `n_delays_10__n_target_var_threshold_0.99` | 10 | ? | 0.0597 | 2.0099 | — | 41.0000 |
| `n_delays_15__n_target_var_threshold_0.95` | 15 | ? | 0.0840 | 4.0658 | — | 42.0000 |
| `n_delays_15__n_target_var_threshold_0.99` | 15 | ? | 0.0647 | 2.0503 | — | 36.0000 |
| `n_delays_1__n_target_var_threshold_0.95` | 1 | ? | 0.1327 | 4.0759 | — | 37.0000 |
| `n_delays_1__n_target_var_threshold_0.99` | 1 | ? | 0.1248 | 2.2103 | — | 34.0000 |
| `n_delays_20__n_target_var_threshold_0.95` | 20 | ? | 0.0822 | 4.0996 | — | 52.0000 |
| `n_delays_20__n_target_var_threshold_0.99` | 20 | ? | 0.0659 | 2.0737 | — | 39.0000 |
| `n_delays_25__n_target_var_threshold_0.95` | 25 | ? | 0.0879 | 4.2347 | — | 32.0000 |
| `n_delays_25__n_target_var_threshold_0.99` | 25 | ? | 0.0694 | 2.3583 | — | 24.0000 |
| `n_delays_30__n_target_var_threshold_0.95` | 30 | ? | 0.0801 | 4.2550 | — | 38.0000 |
| `n_delays_30__n_target_var_threshold_0.99` | 30 | ? | 0.0731 | 2.8337 | — | 18.0000 |
| `n_delays_5__n_target_var_threshold_0.95` | 5 | ? | 0.0875 | 3.9727 | — | 39.0000 |
| `n_delays_5__n_target_var_threshold_0.99` | 5 | ? | 0.0623 | 2.0303 | — | 44.0000 |