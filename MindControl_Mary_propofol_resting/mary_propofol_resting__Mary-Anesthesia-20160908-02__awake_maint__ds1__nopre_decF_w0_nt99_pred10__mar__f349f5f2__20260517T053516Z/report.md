# mary_propofol_resting__Mary-Anesthesia-20160908-02__awake_maint__ds1__nopre_decF_w0_nt99_pred10__mar__f349f5f2__20260517T053516Z

- wandb group: [mary_propofol_resting__Mary-Anesthesia-20160908-02__awake_maint__ds1__nopre_decF_w0_nt99_pred10__mar__f349f5f2__20260517T053516Z](https://wandb.ai/JacobianODE/MindControl_Mary_propofol_resting/groups/mary_propofol_resting__Mary-Anesthesia-20160908-02__awake_maint__ds1__nopre_decF_w0_nt99_pred10__mar__f349f5f2__20260517T053516Z)
- chosen cell: **`lc_lc1e-2__n_delays_5`** (trajectory val_loss (min over history) = 0.0534)
- cells reported: 21

**Description**: 21 cells: 3 n_delays × 7 loop_closure_weight at nt=0.99, ds=1, on Mary-Anesthesia-20160908-02. n_delays ∈ {5, 10, 15}. loop_closure_weight ∈ {0, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1}. obs_noise_scale=0. 6-hour SLURM cap, migrate_to=mit_normal_gpu. All other knobs match the Mary-20160809 + MrJones-20160105 LC × nd siblings.

**Hypothesis**

```
The Mary-20160809 + MrJones-20160105 LC × nd sweeps both showed the
LC sweet spot in 1e-3 to 1e-1 with a late-bloomer at lc=1e-1, nd=10.
Expect Mary-Anesthesia-20160908-02 to land in the same regime.
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

**Chosen run** (by `best_traj_loss`): `lc_lc1e-2__n_delays_5` (trajectory val_loss (min over history) = 0.0534). Hard criteria applied after relaxation: C1, C2, C3. Survivors / candidates: 15/21.

### Per-run results

| run_name | `n_delays` | `lc` | best_traj_loss | MASE | dec_corr_MASE | LC loss | n_dyn | fast_eig_frac |
|---|---|---|---|---|---|---|---|---|
| `lc_lc1e-2__n_delays_5` | 5 | — | 0.05344 | 1.8826 | 0.9236 | 0.001 | 128 | 0.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | — | 0.05388 | 1.8907 | 0.9287 | 0.000 | 128 | 0.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | — | 0.05455 | 1.8861 | 0.9244 | 1.797 | 128 | 0.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | — | 0.05462 | 1.8915 | 0.9211 | 0.018 | 152 | 0.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | — | 0.05496 | 1.8919 | 0.9223 | 0.001 | 152 | 0.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | — | 0.05516 | 1.8989 | 0.9236 | 1.250 | 152 | 0.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | — | 0.05656 | 1.9367 | 0.9193 | 0.015 | 175 | 0.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | — | 0.05772 | 1.9385 | 0.9171 | 10.215 | 175 | 0.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | — | 0.05972 | 1.9491 | 0.9159 | 0.339 | 175 | 0.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | — | 0.06019 | 1.9085 | 0.9305 | 9.735 | 152 | 0.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | — | 0.06032 | 1.9268 | 0.9394 | 0.000 | 152 | 0.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | — | 0.06119 | 1.9613 | 0.9221 | 0.000 | 175 | 0.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | — | 0.06135 | 1.9058 | 0.9299 | 60.248 | 152 | 0.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | — | 0.06188 | 1.9692 | 0.9184 | 48.436 | 175 | 0.0000 |
| `lc_lc0__n_delays_15` | 15 | — | 0.06202 | 1.9680 | 0.9181 | 193.767 | 175 | 0.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | — | 0.06225 | 1.8711 | 0.9284 | 0.008 | 128 | 0.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | — | 0.06227 | 1.9916 | 0.9229 | 0.000 | 175 | 0.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | — | 0.06268 | 1.8659 | 0.9264 | 4.140 | 128 | 0.0000 |
| `lc_lc0__n_delays_10` | 10 | — | 0.06300 | 1.9075 | 0.9269 | 276.440 | 152 | 0.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | — | 0.06346 | 1.8796 | 0.9283 | 32.184 | 128 | 0.0000 |
| `lc_lc0__n_delays_5` | 5 | — | 0.06472 | 1.8720 | 0.9300 | 214.459 | 128 | 0.0000 |

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
| `lc_lc0__n_delays_10` | 10 | ? | 0.0634 | 1.9010 | — | 60.0000 |
| `lc_lc0__n_delays_15` | 15 | ? | 0.0653 | 1.9549 | — | 41.0000 |
| `lc_lc0__n_delays_5` | 5 | ? | 0.0667 | 1.9009 | — | 46.0000 |
| `lc_lc1e-1__n_delays_10` | 10 | ? | 0.0603 | 1.9268 | — | 60.0000 |
| `lc_lc1e-1__n_delays_15` | 15 | ? | 0.0612 | 1.9613 | — | 42.0000 |
| `lc_lc1e-1__n_delays_5` | 5 | ? | 0.0546 | 1.8881 | — | 89.0000 |
| `lc_lc1e-2__n_delays_10` | 10 | ? | 0.0560 | 1.8962 | — | 83.0000 |
| `lc_lc1e-2__n_delays_15` | 15 | ? | 0.0627 | 1.9688 | — | 40.0000 |
| `lc_lc1e-2__n_delays_5` | 5 | ? | 0.0544 | 1.8882 | — | 92.0000 |
| `lc_lc1e-3__n_delays_10` | 10 | ? | 0.0546 | 1.8915 | — | 82.0000 |
| `lc_lc1e-3__n_delays_15` | 15 | ? | 0.0570 | 1.9448 | — | 54.0000 |
| `lc_lc1e-3__n_delays_5` | 5 | ? | 0.0637 | 1.9112 | — | 46.0000 |
| `lc_lc1e-4__n_delays_10` | 10 | ? | 0.0573 | 1.8974 | — | 76.0000 |
| `lc_lc1e-4__n_delays_15` | 15 | ? | 0.0597 | 1.9491 | — | 42.0000 |
| `lc_lc1e-4__n_delays_5` | 5 | ? | 0.0558 | 1.8862 | — | 92.0000 |
| `lc_lc1e-5__n_delays_10` | 10 | ? | 0.0613 | 1.9146 | — | 59.0000 |
| `lc_lc1e-5__n_delays_15` | 15 | ? | 0.0596 | 1.9311 | — | 50.0000 |
| `lc_lc1e-5__n_delays_5` | 5 | ? | 0.0644 | 1.9040 | — | 46.0000 |
| `lc_lc1e-6__n_delays_10` | 10 | ? | 0.0615 | 1.9052 | — | 60.0000 |
| `lc_lc1e-6__n_delays_15` | 15 | ? | 0.0644 | 1.9510 | — | 41.0000 |
| `lc_lc1e-6__n_delays_5` | 5 | ? | 0.0653 | 1.9030 | — | 46.0000 |