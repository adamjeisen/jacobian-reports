# mary_propofol_resting__Mary-Anesthesia-20160912-02__awake_maint__ds1__nopre_decF_w0_nt99_pred10__mar__a0fc4ec7__20260516T033521Z

- wandb group: [mary_propofol_resting__Mary-Anesthesia-20160912-02__awake_maint__ds1__nopre_decF_w0_nt99_pred10__mar__a0fc4ec7__20260516T033521Z](https://wandb.ai/JacobianODE/MindControl_Mary_propofol_resting/groups/mary_propofol_resting__Mary-Anesthesia-20160912-02__awake_maint__ds1__nopre_decF_w0_nt99_pred10__mar__a0fc4ec7__20260516T033521Z)
- chosen cell: **`lc_lc1e-3__n_delays_10`** (trajectory val_loss (min over history) = 0.0577)
- cells reported: 21

**Description**: 21 cells: 3 n_delays × 7 loop_closure_weight at nt=0.99, ds=1, on Mary-Anesthesia-20160912-02. n_delays ∈ {5, 10, 15}. loop_closure_weight ∈ {0, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1}. obs_noise_scale=0. 6-hour SLURM cap, migrate_to=mit_normal_gpu. All other knobs match the Mary-20160809 + MrJones-20160105 LC × nd siblings.

**Hypothesis**

```
The Mary-20160809 + MrJones-20160105 LC × nd sweeps both showed the
LC sweet spot in 1e-3 to 1e-1 with a late-bloomer at lc=1e-1, nd=10.
Expect Mary-Anesthesia-20160912-02 to land in the same regime.
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

**Chosen run** (by `best_traj_loss`): `lc_lc1e-3__n_delays_10` (trajectory val_loss (min over history) = 0.0577). Hard criteria applied after relaxation: C1, C2, C3. Survivors / candidates: 13/21.

### Per-run results

| run_name | `n_delays` | `lc` | best_traj_loss | MASE | dec_corr_MASE | LC loss | n_dyn | fast_eig_frac |
|---|---|---|---|---|---|---|---|---|
| `lc_lc1e-3__n_delays_10` | 10 | — | 0.05765 | 1.9041 | 0.9280 | 0.004 | 144 | 0.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | — | 0.05788 | 1.9086 | 0.9301 | 0.656 | 144 | 0.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | — | 0.05802 | 1.9148 | 0.9337 | 0.000 | 144 | 0.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | — | 0.06070 | 1.9084 | 0.9297 | 8.812 | 144 | 0.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | — | 0.06099 | 1.9466 | 0.9455 | 0.000 | 144 | 0.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | — | 0.06125 | 1.8587 | 0.9322 | 1.389 | 119 | 0.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | — | 0.06131 | 1.8750 | 0.9388 | 0.000 | 119 | 0.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | — | 0.06175 | 1.9040 | 0.9283 | 69.693 | 144 | 0.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | — | 0.06217 | 1.8385 | 0.9080 | 20.717 | 169 | 0.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | — | 0.06340 | 1.8753 | 0.9425 | 0.006 | 119 | 0.0000 |
| `lc_lc0__n_delays_10` | 10 | — | 0.06353 | 1.9003 | 0.9293 | 370.356 | 144 | 0.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | — | 0.06373 | 1.8787 | 0.9451 | 0.000 | 119 | 0.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | — | 0.06497 | 1.8566 | 0.9380 | 15.691 | 119 | 0.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | — | 0.06707 | 1.8885 | 0.9133 | 0.008 | 169 | 0.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | — | 0.06735 | 1.8847 | 0.9120 | 0.135 | 169 | 0.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | — | 0.06785 | 1.8905 | 0.9142 | 0.001 | 169 | 0.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | — | 0.06845 | 1.9042 | 0.9203 | 0.000 | 169 | 0.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | — | 0.06883 | 1.8998 | 0.9108 | 55.082 | 169 | 0.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | — | 0.06950 | 1.8540 | 0.9399 | 33.324 | 119 | 0.0000 |
| `lc_lc0__n_delays_15` | 15 | — | 0.06969 | 1.8959 | 0.9099 | 284.448 | 169 | 0.0000 |
| `lc_lc0__n_delays_5` | 5 | — | 0.07025 | 1.8293 | 0.9295 | 122.462 | 119 | 0.0000 |

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
| `lc_lc0__n_delays_10` | 10 | ? | 0.0652 | 1.8994 | — | 53.0000 |
| `lc_lc0__n_delays_15` | 15 | ? | 0.0716 | 1.8846 | — | 38.0000 |
| `lc_lc0__n_delays_5` | 5 | ? | 0.0711 | 1.8530 | — | 43.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | ? | 0.0617 | 1.9454 | — | 56.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | ? | 0.0685 | 1.9042 | — | 42.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | ? | 0.0613 | 1.8750 | — | 85.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | ? | 0.0588 | 1.9072 | — | 62.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | ? | 0.0679 | 1.8905 | — | 42.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | ? | 0.0644 | 1.8780 | — | 71.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | ? | 0.0577 | 1.9041 | — | 65.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | ? | 0.0671 | 1.8885 | — | 42.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | ? | 0.0640 | 1.8759 | — | 71.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | ? | 0.0584 | 1.9161 | — | 61.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | ? | 0.0674 | 1.8847 | — | 42.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | ? | 0.0613 | 1.8587 | — | 85.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | ? | 0.0611 | 1.9062 | — | 53.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | ? | 0.0641 | 1.8356 | — | 56.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | ? | 0.0657 | 1.8530 | — | 68.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | ? | 0.0627 | 1.9012 | — | 53.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | ? | 0.0715 | 1.8904 | — | 38.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | ? | 0.0705 | 1.8687 | — | 44.0000 |