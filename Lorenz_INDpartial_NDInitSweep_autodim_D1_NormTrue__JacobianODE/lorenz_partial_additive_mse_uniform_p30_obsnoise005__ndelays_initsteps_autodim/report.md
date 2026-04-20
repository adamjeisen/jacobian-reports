# Sweep Analysis: `lorenz_partial_additive_mse_uniform_p30_obsnoise005__ndelays_initsteps_autodim`

**Project**: [Lorenz_INDpartial_NDInitSweep_autodim_D1_NormTrue__JacobianODE](https://wandb.ai/JacobianODE/Lorenz_INDpartial_NDInitSweep_autodim_D1_NormTrue__JacobianODE/groups/lorenz_partial_additive_mse_uniform_p30_obsnoise005__ndelays_initsteps_autodim)  
**Launched**: 2026-04-20T19:55:41Z  
**Completed**: 2026-04-20T22:01:43Z  
**Outcome**: `complete_with_failures`  
**Git**: `latent-JacobianODE` @ `6f807fc`  
**Expected runs**: 80

## Experiment Context

### `lorenz_partial_additive_mse_uniform_p30_obsnoise005__ndelays_initsteps_autodim`

**Description**

Lorenz partial additive coupling, uniform reconstruction loss,
obs_noise=0.05, prediction_steps=30, loop_closure_weight=0.
Sweeps delay_embedding_params.n_delays over
[5, 10, 15, ..., 100] (step 5, 20 values)
× jacobianODEint_kwargs.traj_init_steps over [15, 30]
= 40 runs.
n_target_dims is picked at data-load time as the smallest k such
that the first k PCs of the noisy training delay embeddings
explain ≥ model.n_target_var_threshold of the total variance.
final_perm_identity=true on the encoder guarantees that at init
z[..., :n_target_dims] == x[..., :n_target_dims] — independent of
permutation_seed.

**Hypothesis**

At obs_noise=0.05, small n_delays are noise-dominated in neighbor
scatter (per the amplification diagnostic), so PCA-auto should
pick a small n_target_dims there. As n_delays grows, more PCs
clear the threshold, and the encoder has enough input dims to
unfold the attractor. With traj_init_steps=30 (vs 15), the
encoder sees twice as much history at init, which should help
more at the high-noise setting than the low-noise one.

**Success criteria**

- All 40 runs train without divergence
- PCA-chosen n_target_dims grows with n_delays then saturates, with saturation value ≥ 3
- traj_init_steps=30 gives a larger val_loss improvement over 15 than at obs_noise=0.01 (noise-robustness)
- Best val traj_loss non-monotonic in n_delays with a clear optimum

## Results

**Swept axes** (9): `data.train_test_params.delay_embedding_params.n_delays`, `data.train_test_params.seq_length`, `model.encoder.n_input`, `model.n_target_dims`, `model.n_target_dims_pca_auto`, `model.n_target_dims_pca_cum_var`, `model.params.input_dim`, `model.params.output_dim`, `training.lightning.jacobianODEint_kwargs.traj_init_steps`

**Chosen run** (by `best_traj_loss`): `—` — traj_loss=—, MASE=—, R²=—, LC loss=—, epoch=None

### Integrity checks

⚠️ **Matched-run count mismatch**: expected 80 run_idx slots per the sentinel, matched 0 in wandb. The sweep may still be in progress, or some slots failed without producing wandb evidence.

⚠️ **5 wandb run(s) did not match any run_idx** (excluded from the per-run table). These are most likely orphans from preempt-cycle retries or rate-limit re-launches. IDs: `rozlkci9`, `eyfqgemc`, `l42rqc1g`, `hic5ynzw`, `rgca51q1`.

**Runs analyzed**: 0 (expected 80)

## Success-criteria verdicts (automated)

| Criterion | Verdict | Note |
|---|---|---|
| All 40 runs train without divergence | **Unknown** |  |
| PCA-chosen n_target_dims grows with n_delays then saturates, with saturation value ≥ 3 | **Unknown** |  |
| traj_init_steps=30 gives a larger val_loss improvement over 15 than at obs_noise=0.01 (noise-robustness) | **Unknown** |  |
| Best val traj_loss non-monotonic in n_delays with a clear optimum | **Unknown** |  |

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
No run_id provided — selecting best run from group 'lorenz_partial_additive_mse_uniform_p30_obsnoise005__ndelays_initsteps_autodim' ...
Found 6 total runs in JacobianODE/Lorenz_INDpartial_NDInitSweep_autodim_D1_NormTrue__JacobianODE (group=lorenz_partial_additive_mse_uniform_p30_obsnoise005__ndelays_initsteps_autodim)
All runs (state, loop_closure_weight, tangent_entropy_weight, kl_dyn_weight):
  rozlkci9: state=running, lc=0.0, te=0.0, kl_dyn=0.0
  eyfqgemc: state=running, lc=0.0, te=0.0, kl_dyn=0.0
  l42rqc1g: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  hic5ynzw: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  rgca51q1: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  f28hxmys: state=running, lc=0.0, te=0.0, kl_dyn=0.0

slurm_timeout_min not found in any run config — falling back to 180 min
  Including rozlkci9 (lc=0.0): use_all_runs=True (state=running)
  Including eyfqgemc (lc=0.0): use_all_runs=True (state=running)
  Including l42rqc1g (lc=0.0): use_all_runs=True (state=finished)
  Including hic5ynzw (lc=0.0): use_all_runs=True (state=finished)
  Including rgca51q1 (lc=0.0): use_all_runs=True (state=finished)
  Including f28hxmys (lc=0.0): use_all_runs=True (state=running)
Found 6 effectively-done sweep runs:
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=eyfqgemc
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=f28hxmys
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=hic5ynzw
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=l42rqc1g
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=rgca51q1
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=rozlkci9
  Dropping 1 run(s) with no checkpoint dir: ['f28hxmys']
n_dims=5, n_latent=5, n_dyn=2, dt=0.0150
  run=eyfqgemc: DiagnosticMetrics(one_step_mase=0.7904332280158997, loop_closure_loss=5.152933120727539, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.08754920959472656) (from W&B history)
  run=hic5ynzw: DiagnosticMetrics(one_step_mase=1.0403393507003784, loop_closure_loss=0.9549960494041443, fast_eigenvalue_fraction=0.3333333432674408, trajectory_val_loss=0.1392793208360672) (from W&B history)
  run=l42rqc1g: DiagnosticMetrics(one_step_mase=1.0393056869506836, loop_closure_loss=0.8822500705718994, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.2338985800743103) (from W&B history)
  run=rgca51q1: DiagnosticMetrics(one_step_mase=1.364698052406311, loop_closure_loss=4.962955474853516, fast_eigenvalue_fraction=0.2775000035762787, trajectory_val_loss=0.1578359156847) (from W&B history)
  run=rozlkci9: DiagnosticMetrics(one_step_mase=0.8035351037979126, loop_closure_loss=2.2053279876708984, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.12071456760168076) (from W&B history)

Ranking method:           best_traj_loss
Best run ID:              rozlkci9
Best loop_closure_weight: 0.0
Best tangent_entropy_weight: 0.0
Best kl_dyn_weight:       0.0
Best traj loss:           0.120715
Criteria applied: ['C1', 'C2', 'C3']
Surviving: 1 / 5
Auto-selected run_id: rozlkci9

======================================================================
PARETO FRONTIER RUNS (4 runs)
======================================================================
  Run ID               LC Loss   Traj Val Loss
  ------------  --------------  --------------
  l42rqc1g            0.882250        0.233899
  hic5ynzw            0.954996        0.139279
  rozlkci9            2.205328        0.120715 <-- selected
  eyfqgemc            5.152933        0.087549

======================================================================
RANKING METHOD COMPARISON (over 1 survivors)
======================================================================
  Method                  Run ID               LC Loss   Traj Val Loss
  ----------------------  ------------  --------------  --------------
  best_traj_loss          rozlkci9            2.205328        0.120715 <-- active
  pareto_knee             rozlkci9            2.205328        0.120715
  geo_rank                rozlkci9            2.205328        0.120715
  minimax_rank            rozlkci9            2.205328        0.120715
  geo_log_score           rozlkci9            2.205328        0.120715
  minimax_log_score       rozlkci9            2.205328        0.120715
======================================================================

Loading run rozlkci9 from JacobianODE/Lorenz_INDpartial_NDInitSweep_autodim_D1_NormTrue__JacobianODE ...
Train dataset shape: torch.Size([25322, 45, 5])
Validation dataset shape: torch.Size([8057, 45, 5])
Test dataset shape: torch.Size([3453, 45, 5])
Train trajectories dataset shape: torch.Size([22, 1196, 5])
Validation trajectories dataset shape: torch.Size([7, 1196, 5])
Test trajectories dataset shape: torch.Size([3, 1196, 5])
Loading checkpoint epoch=2-step=600.ckpt...
Computing reconstruction ...
Computing MASE ...
Teacher-forced MASE: 0.8083
Free-running MASE:   3.2063
Computing latent utilization ...
Entropy-based utilization: 0.999
Null subspace mean RMS: 8.363803e-02
Computing Lyapunov exponents ...
  Computing full-trajectory Lyapunov (3 test trajs, T=1196) ...
Predicted Lyapunov exponents (batch+burn-in, 128 windowed trajs):
  λ_1 = -4.5729 ± 1.4297
  λ_2 = -26.0730 ± 3.8024
Predicted Lyapunov exponents (full-length, 3 test trajs):
  λ_1 = -5.7019 ± 0.0116
  λ_2 = -23.5826 ± 0.1057
Empirical Lyapunov exponents (mean ± std):
  λ_1 = +0.4677 ± 0.0259
  λ_2 = -0.2173 ± 0.0549
  λ_3 = -13.9174 ± 0.0513
Mean KY dim (predicted): 0.000 ± 0.000
Mean KY dim (empirical): 2.018 ± 0.003
Mean KY dim (burn-in):   0.000 ± 0.000
Computing prediction windows ...
Windows: 117 — nMSE min=0.0398, median=0.4346, mean=0.8083, max=4.4706
Computing long-trajectory free-running rollouts ...
Computing encoder/decoder Jacobians ...
encoder_jacobian: (128, 5, 5)
decoder_jacobian: (128, 5, 5)
Computing amplification loss ...
Amplification loss — True state: 0.006862
Amplification loss — Latent:     0.006789
```

</details>
