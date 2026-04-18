# Sweep Analysis: `lorenz_partial_100d_7lat_additive_mse__klnull_sweep_v2`

**Project**: [Lorenz_INDpartial_N100_D1_NormTrue_T7__JacobianODE](https://wandb.ai/JacobianODE/Lorenz_INDpartial_N100_D1_NormTrue_T7__JacobianODE/groups/lorenz_partial_100d_7lat_additive_mse__klnull_sweep_v2)  
**Launched**: 2026-04-16T02:05:11Z  
**Completed**: 2026-04-16T06:55:12Z  
**Outcome**: `complete_clean`  
**Git**: `latent-JacobianODE` @ `1010983`  
**Expected runs**: 6

## Experiment Context

### `lorenz_partial_100d_7lat_additive_mse_klnull_sweep`

**Description**

Same as lorenz_partial_100d_7lat_additive_mse except
loop_closure_weight is FIXED at 1e-3 (best LC from the LC sweep)
and kl_null_weight is SWEPT over {0, 1e-4, 1e-3, 1e-2, 1e-1, 1}.
Every other knob identical. obs_noise_scale=0, reconstruction_mode
= most_recent, prediction_steps=10, seq_length=25.

**Hypothesis**

With z_null unpenalised, the encoder dumps trajectory history into
z_null and the Jacobian MLP spreads contraction across the 7
z_dyn axes (λ_min ≈ −6 instead of empirical ~−14). A positive
kl_null_weight should force information into z_dyn, tighten the
attractor manifold in z_dyn, and concentrate contraction into
a single axis whose λ moves toward empirical. Risk: too-large
kl_null suppresses z_null below what the decoder needs to
reconstruct observations — recon_loss explodes, trajectory
fidelity collapses. Expecting a U-shape in spectrum MSE vs
kl_null with a sweet spot somewhere in 1e-3 .. 1e-1.

**Success criteria**

- At the best kl_null, λ_min moves noticeably more negative than −6
- Σλ_i (volume-contraction rate) moves from −20 toward empirical ~−14
- val/trajectory_r2 at best kl_null within a few % of the 0-kl_null baseline
- Clear U-shape (or monotone direction) across the 6 kl_null values

## Results

**Swept axes** (1): `training.lightning.kl_null_weight`

**Chosen run** (by `best_traj_loss`): `jhg9x3lq` — traj_loss=0.00000, MASE=0.0253, R²=1.0000, LC loss=0.001, epoch=198.0

Swept-axis values at chosen run: `training.lightning.kl_null_weight`=0

**Runs analyzed**: 6 (expected 6)

### Per-run results

| run_idx | run_id | `training.lightning.kl_null_weight` | best_traj_loss | best_MASE | R² | LC loss | epoch |
|---|---|---|---|---|---|---|---|
| 0 | `jhg9x3lq` | 0 | 0.00000 | 0.0253 | 1.0000 | 0.001 | 198.0 |
| 2 | `88th62np` | 0.001 | 0.00000 | 0.0260 | 1.0000 | 0.001 | 198.0 |
| 4 | `gx6lmk6g` | 0.1 | 0.00000 | 0.0279 | 1.0000 | 0.001 | 198.0 |
| 5 | `6y24w9yt` | 1 | 0.00000 | 0.0316 | 1.0000 | 0.001 | 183.0 |
| 3 | `nklisi77` | 0.01 | 0.00000 | 0.0318 | 1.0000 | 0.001 | 195.0 |
| 1 | `kuhiqael` | 1.0e-04 | 0.00000 | 0.0479 | 1.0000 | 0.002 | 140.0 |

## Success-criteria verdicts (automated)

| Criterion | Verdict | Note |
|---|---|---|
| At the best kl_null, λ_min moves noticeably more negative than −6 | **Unknown** |  |
| Σλ_i (volume-contraction rate) moves from −20 toward empirical ~−14 | **Unknown** |  |
| val/trajectory_r2 at best kl_null within a few % of the 0-kl_null baseline | **Unknown** |  |
| Clear U-shape (or monotone direction) across the 6 kl_null values | **Unknown** |  |

_Automated verdicts use simple numeric-threshold parsing and may mis-classify qualitative criteria. The Discussion section below takes precedence._

## Figures

### sweep_overview

![sweep_overview](figures/sweep_overview.png)

### sweep_pareto

![sweep_pareto](figures/sweep_pareto.png)

### reconstruction

![reconstruction](figures/reconstruction.png)

### prediction_windows

![prediction_windows](figures/prediction_windows.png)

### long_trajectory

![long_trajectory](figures/long_trajectory.png)

### mase

![mase](figures/mase.png)

### latent_utilization

![latent_utilization](figures/latent_utilization.png)

### lyapunov

![lyapunov](figures/lyapunov.png)

### kaplan_yorke

![kaplan_yorke](figures/kaplan_yorke.png)

### per_run_lyapunov

![per_run_lyapunov](figures/per_run_lyapunov.png)

### per_run_lyapunov_vs_true

![per_run_lyapunov_vs_true](figures/per_run_lyapunov_vs_true.png)

### per_run_lyapunov_relerr

![per_run_lyapunov_relerr](figures/per_run_lyapunov_relerr.png)

### lyapunov_spectrum_mse_vs_val_loss

![lyapunov_spectrum_mse_vs_val_loss](figures/lyapunov_spectrum_mse_vs_val_loss.png)

### encoder_decoder_jacobians

![encoder_decoder_jacobians](figures/encoder_decoder_jacobians.png)

### amplification

![amplification](figures/amplification.png)

### kaplan_yorke_pca

![kaplan_yorke_pca](figures/kaplan_yorke_pca.png)

### prediction_detail_latent

![prediction_detail_latent](figures/prediction_detail_latent.png)

### prediction_detail_obs

![prediction_detail_obs](figures/prediction_detail_obs.png)

## Discussion

<!--
This section is intentionally left as a placeholder. A human reviewer
or Claude Code agent should fill it in based on the tables and figures
above, explicitly addressing each success criterion and comparing the
outcome to the stated hypothesis. Write the Discussion to
`discussion.md` in this directory and re-run `render_report`.
-->

_(to be written)_

## `run_analytics` stdout

<details><summary>Click to expand — full diagnostic output from <code>run_analytics</code></summary>

```
No run_id provided — selecting best run from group 'lorenz_partial_100d_7lat_additive_mse__klnull_sweep_v2' ...
Found 6 total runs in JacobianODE/Lorenz_INDpartial_N100_D1_NormTrue_T7__JacobianODE (group=lorenz_partial_100d_7lat_additive_mse__klnull_sweep_v2)
All runs (state, loop_closure_weight, tangent_entropy_weight, kl_dyn_weight):
  jhg9x3lq: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  kuhiqael: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  88th62np: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  nklisi77: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  gx6lmk6g: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  6y24w9yt: state=finished, lc=0.001, te=0.0, kl_dyn=0.0

slurm_timeout_min not found in any run config — falling back to 180 min
  Including jhg9x3lq (lc=0.001): use_all_runs=True (state=finished)
  Including kuhiqael (lc=0.001): use_all_runs=True (state=finished)
  Including 88th62np (lc=0.001): use_all_runs=True (state=finished)
  Including nklisi77 (lc=0.001): use_all_runs=True (state=finished)
  Including gx6lmk6g (lc=0.001): use_all_runs=True (state=finished)
  Including 6y24w9yt (lc=0.001): use_all_runs=True (state=finished)
Found 6 effectively-done sweep runs:
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=6y24w9yt
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=88th62np
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=gx6lmk6g
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=jhg9x3lq
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=kuhiqael
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=nklisi77
n_dims=100, n_latent=100, n_dyn=7, dt=0.0150
  run=6y24w9yt: DiagnosticMetrics(one_step_mase=0.0217712614685297, loop_closure_loss=0.0010781779419630766, fast_eigenvalue_fraction=0.0, trajectory_val_loss=3.1880242659099167e-06) (from cache, n_batches=100)
  run=88th62np: DiagnosticMetrics(one_step_mase=0.01953170634806156, loop_closure_loss=0.0010061676148325205, fast_eigenvalue_fraction=0.0, trajectory_val_loss=1.9812912341876654e-06) (from cache, n_batches=100)
  run=gx6lmk6g: DiagnosticMetrics(one_step_mase=0.018431490287184715, loop_closure_loss=0.001141534186899662, fast_eigenvalue_fraction=0.0, trajectory_val_loss=2.8873889732494717e-06) (from cache, n_batches=100)
  run=jhg9x3lq: DiagnosticMetrics(one_step_mase=0.01906902901828289, loop_closure_loss=0.0010725540341809392, fast_eigenvalue_fraction=0.0, trajectory_val_loss=1.8616602801557747e-06) (from cache, n_batches=100)
  run=kuhiqael: DiagnosticMetrics(one_step_mase=0.03152746707201004, loop_closure_loss=0.001629306934773922, fast_eigenvalue_fraction=0.0, trajectory_val_loss=4.002294190286193e-06) (from cache, n_batches=100)
  run=nklisi77: DiagnosticMetrics(one_step_mase=0.01955581083893776, loop_closure_loss=0.001203253399580717, fast_eigenvalue_fraction=0.0, trajectory_val_loss=3.2548061881243484e-06) (from cache, n_batches=100)

Ranking method:           best_traj_loss
Best run ID:              jhg9x3lq
Best loop_closure_weight: 0.001
Best tangent_entropy_weight: 0.0
Best kl_dyn_weight:       0.0
Best traj loss:           0.000002
Criteria applied: ['C1', 'C2', 'C3']
Surviving: 6 / 6
Auto-selected run_id: jhg9x3lq

======================================================================
PARETO FRONTIER RUNS (2 runs)
======================================================================
  Run ID               LC Loss   Traj Val Loss
  ------------  --------------  --------------
  88th62np            0.001006        0.000002
  jhg9x3lq            0.001073        0.000002 <-- selected

======================================================================
RANKING METHOD COMPARISON (over 6 survivors)
======================================================================
  Method                  Run ID               LC Loss   Traj Val Loss
  ----------------------  ------------  --------------  --------------
  best_traj_loss          jhg9x3lq            0.001073        0.000002 <-- active
  pareto_knee             88th62np            0.001006        0.000002
  geo_rank                88th62np            0.001006        0.000002
  minimax_rank            88th62np            0.001006        0.000002
  geo_log_score           88th62np            0.001006        0.000002
  minimax_log_score       88th62np            0.001006        0.000002
======================================================================

Loading run jhg9x3lq from JacobianODE/Lorenz_INDpartial_N100_D1_NormTrue_T7__JacobianODE ...
Train dataset shape: torch.Size([23672, 25, 100])
Validation dataset shape: torch.Size([7532, 25, 100])
Test dataset shape: torch.Size([3228, 25, 100])
Train trajectories dataset shape: torch.Size([22, 1101, 100])
Validation trajectories dataset shape: torch.Size([7, 1101, 100])
Test trajectories dataset shape: torch.Size([3, 1101, 100])
Loading checkpoint epoch=198-step=39800.ckpt...
Computing reconstruction ...
Computing MASE ...
Teacher-forced MASE: 0.0194
Free-running MASE:   0.0244
Computing latent utilization ...
Entropy-based utilization: 0.888
Null subspace mean RMS: 9.550717e-01
Computing Lyapunov exponents ...
  Computing full-trajectory Lyapunov (3 test trajs, T=1101) ...
Predicted Lyapunov exponents (batch+burn-in, 128 windowed trajs):
  λ_1 = +0.5159 ± 0.6785
  λ_2 = -0.5155 ± 0.3068
  λ_3 = -2.4080 ± 0.2719
  λ_4 = -2.9829 ± 0.2272
  λ_5 = -3.5357 ± 0.2471
  λ_6 = -4.5047 ± 0.2960
  λ_7 = -6.3818 ± 0.4127
Predicted Lyapunov exponents (full-length, 3 test trajs):
  λ_1 = +0.3009 ± 0.0503
  λ_2 = +0.0134 ± 0.0262
  λ_3 = -2.6481 ± 0.0260
  λ_4 = -3.1583 ± 0.0200
  λ_5 = -4.0222 ± 0.0390
  λ_6 = -4.4452 ± 0.0240
  λ_7 = -6.3321 ± 0.0457
Empirical Lyapunov exponents (mean ± std):
  λ_1 = +0.2716 ± 0.0605
  λ_2 = -0.1016 ± 0.0797
  λ_3 = -13.8370 ± 0.0514
Mean KY dim (predicted): 2.119 ± 0.008
Mean KY dim (empirical): 2.012 ± 0.003
Mean KY dim (burn-in):   1.332 ± 1.005
Computing prediction windows ...
Windows: 324 — nMSE min=0.0000, median=0.0000, mean=0.0000, max=0.0005
Computing long trajectory prediction ...
Computing encoder/decoder Jacobians ...
encoder_jacobian: (128, 100, 100)
decoder_jacobian: (128, 100, 100)
Computing amplification loss ...
Amplification loss — True state: 0.000055
Amplification loss — Latent:     0.000049
```

</details>
