# Sweep Analysis: `lorenz_partial_additive_mse_uniform_p30_obsnoise001__ndelays_initsteps_autodim`

**Project**: [Lorenz_INDpartial_NDInitSweep_autodim_D1_NormTrue__JacobianODE](https://wandb.ai/JacobianODE/Lorenz_INDpartial_NDInitSweep_autodim_D1_NormTrue__JacobianODE/groups/lorenz_partial_additive_mse_uniform_p30_obsnoise001__ndelays_initsteps_autodim)  
**Launched**: 2026-04-20T19:55:11Z  
**Completed**: 2026-04-20T20:27:23Z  
**Outcome**: `complete_with_failures`  
**Git**: `latent-JacobianODE` @ `6f807fc`  
**Expected runs**: 80

## Experiment Context

### `lorenz_partial_additive_mse_uniform_p30_obsnoise001__ndelays_initsteps_autodim`

**Description**

Lorenz partial additive coupling, uniform reconstruction loss,
obs_noise=0.01, prediction_steps=30, loop_closure_weight=0.
Sweeps delay_embedding_params.n_delays over
[5, 10, 15, ..., 100] (step 5, 20 values)
× jacobianODEint_kwargs.traj_init_steps over [15, 30]
= 40 runs.
n_target_dims is picked at data-load time as the smallest k such
that the first k PCs of the noisy training delay embeddings explain
≥ model.n_target_var_threshold of the total variance.
final_perm_identity=true on the encoder guarantees that at init
z[..., :n_target_dims] == x[..., :n_target_dims] — the first
n_target_dims most-recent observations flow into z_dyn without
depending on permutation_seed.

**Hypothesis**

At a given obs_noise level, both n_delays and traj_init_steps
change how much state information is accumulated before the
dynamics model is asked to predict. The PCA-auto dim lets each
n_delays pick its own latent dimensionality, so that comparing
across n_delays is a fair comparison of "how much useful rank
is present" rather than "how well 3 fixed dims capture different
embeddings." With routing fixed, no n_delays will fail the
decoded[0]-disconnected-from-z_dyn failure mode we saw at seed=42
n_delays=30. We expect: (i) at higher traj_init_steps, every
n_delays achieves a better val_loss since the encoder has more
history to work with; (ii) a soft optimum in n_delays tracking
the point where PCA-auto n_target_dims stops growing.

**Success criteria**

- All 40 runs train without divergence (routing fix holds)
- PCA-chosen n_target_dims grows with n_delays then saturates
- Val traj_loss improves with traj_init_steps=30 over traj_init_steps=15 at most n_delays
- Best val traj_loss per (noise, init) has a non-monotonic optimum in n_delays

## Results

**Swept axes** (9): `data.train_test_params.delay_embedding_params.n_delays`, `data.train_test_params.seq_length`, `model.encoder.n_input`, `model.n_target_dims`, `model.n_target_dims_pca_auto`, `model.n_target_dims_pca_cum_var`, `model.params.input_dim`, `model.params.output_dim`, `training.lightning.jacobianODEint_kwargs.traj_init_steps`

**Chosen run** (by `best_traj_loss`): `—` — traj_loss=—, MASE=—, R²=—, LC loss=—, epoch=None

### Integrity checks

⚠️ **Matched-run count mismatch**: expected 80 run_idx slots per the sentinel, matched 0 in wandb. The sweep may still be in progress, or some slots failed without producing wandb evidence.

⚠️ **6 wandb run(s) did not match any run_idx** (excluded from the per-run table). These are most likely orphans from preempt-cycle retries or rate-limit re-launches. IDs: `vum47n54`, `9u7h6zjy`, `fhrst1rb`, `xr9flz8e`, `f93huri8`, `vblk9kz9`.

**Runs analyzed**: 0 (expected 80)

## Success-criteria verdicts (automated)

| Criterion | Verdict | Note |
|---|---|---|
| All 40 runs train without divergence (routing fix holds) | **Unknown** |  |
| PCA-chosen n_target_dims grows with n_delays then saturates | **Unknown** |  |
| Val traj_loss improves with traj_init_steps=30 over traj_init_steps=15 at most n_delays | **Unknown** |  |
| Best val traj_loss per (noise, init) has a non-monotonic optimum in n_delays | **Unknown** |  |

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
No run_id provided — selecting best run from group 'lorenz_partial_additive_mse_uniform_p30_obsnoise001__ndelays_initsteps_autodim' ...
Found 6 total runs in JacobianODE/Lorenz_INDpartial_NDInitSweep_autodim_D1_NormTrue__JacobianODE (group=lorenz_partial_additive_mse_uniform_p30_obsnoise001__ndelays_initsteps_autodim)
All runs (state, loop_closure_weight, tangent_entropy_weight, kl_dyn_weight):
  vum47n54: state=running, lc=0.0, te=0.0, kl_dyn=0.0
  9u7h6zjy: state=running, lc=0.0, te=0.0, kl_dyn=0.0
  fhrst1rb: state=running, lc=0.0, te=0.0, kl_dyn=0.0
  xr9flz8e: state=running, lc=0.0, te=0.0, kl_dyn=0.0
  f93huri8: state=running, lc=0.0, te=0.0, kl_dyn=0.0
  vblk9kz9: state=running, lc=0.0, te=0.0, kl_dyn=0.0

slurm_timeout_min not found in any run config — falling back to 180 min
  Including vum47n54 (lc=0.0): use_all_runs=True (state=running)
  Including 9u7h6zjy (lc=0.0): use_all_runs=True (state=running)
  Including fhrst1rb (lc=0.0): use_all_runs=True (state=running)
  Including xr9flz8e (lc=0.0): use_all_runs=True (state=running)
  Including f93huri8 (lc=0.0): use_all_runs=True (state=running)
  Including vblk9kz9 (lc=0.0): use_all_runs=True (state=running)
Found 6 effectively-done sweep runs:
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=9u7h6zjy
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=f93huri8
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=fhrst1rb
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=vblk9kz9
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=vum47n54
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=xr9flz8e
n_dims=5, n_latent=5, n_dyn=1, dt=0.0150
  run=9u7h6zjy: DiagnosticMetrics(one_step_mase=1.2581123113632202, loop_closure_loss=3.9132567053457024e-07, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.22783158719539642) (from W&B history)
  run=f93huri8: DiagnosticMetrics(one_step_mase=1.9041943550109863, loop_closure_loss=0.012637934647500515, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.02388305589556694) (from W&B history)
  run=fhrst1rb: DiagnosticMetrics(one_step_mase=1.8668575286865234, loop_closure_loss=0.019352059811353683, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.024262426421046257) (from W&B history)
  run=vblk9kz9: DiagnosticMetrics(one_step_mase=2.775660514831543, loop_closure_loss=0.047992728650569916, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.07126376032829285) (from W&B history)
  run=vum47n54: DiagnosticMetrics(one_step_mase=1.3777366876602173, loop_closure_loss=1.0135444566961027e-10, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.38192814588546753) (from W&B history)
  run=xr9flz8e: DiagnosticMetrics(one_step_mase=2.7965402603149414, loop_closure_loss=0.009711168706417084, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.07851911336183548) (from W&B history)

Ranking method:           best_traj_loss
Best run ID:              f93huri8
Best loop_closure_weight: 0.0
Best tangent_entropy_weight: 0.0
Best kl_dyn_weight:       0.0
Best traj loss:           0.023883
Criteria applied: ['C3']
Surviving: 6 / 6
Auto-selected run_id: f93huri8

======================================================================
PARETO FRONTIER RUNS (4 runs)
======================================================================
  Run ID               LC Loss   Traj Val Loss
  ------------  --------------  --------------
  vum47n54            0.000000        0.381928
  9u7h6zjy            0.000000        0.227832
  xr9flz8e            0.009711        0.078519
  f93huri8            0.012638        0.023883 <-- selected

======================================================================
RANKING METHOD COMPARISON (over 6 survivors)
======================================================================
  Method                  Run ID               LC Loss   Traj Val Loss
  ----------------------  ------------  --------------  --------------
  best_traj_loss          f93huri8            0.012638        0.023883 <-- active
  pareto_knee             xr9flz8e            0.009711        0.078519
  geo_rank                f93huri8            0.012638        0.023883
  minimax_rank            f93huri8            0.012638        0.023883
  geo_log_score           f93huri8            0.012638        0.023883
  minimax_log_score       9u7h6zjy            0.000000        0.227832
======================================================================

Loading run f93huri8 from JacobianODE/Lorenz_INDpartial_NDInitSweep_autodim_D1_NormTrue__JacobianODE ...
Train dataset shape: torch.Size([24882, 60, 10])
Validation dataset shape: torch.Size([7917, 60, 10])
Test dataset shape: torch.Size([3393, 60, 10])
Train trajectories dataset shape: torch.Size([22, 1191, 10])
Validation trajectories dataset shape: torch.Size([7, 1191, 10])
Test trajectories dataset shape: torch.Size([3, 1191, 10])
Loading checkpoint epoch=2-step=600.ckpt...
Computing reconstruction ...
Computing MASE ...
Teacher-forced MASE: 1.8848
Free-running MASE:   3.1168
Computing latent utilization ...
Entropy-based utilization: 0.987
Null subspace mean RMS: 1.291852e-01
Computing Lyapunov exponents ...
  Computing full-trajectory Lyapunov (3 test trajs, T=1191) ...
Predicted Lyapunov exponents (batch+burn-in, 128 windowed trajs):
  λ_1 = -0.3875 ± 0.2120
  λ_2 = -0.7434 ± 0.1403
Predicted Lyapunov exponents (full-length, 3 test trajs):
  λ_1 = +0.4684 ± 0.0202
  λ_2 = -1.8099 ± 0.0171
Empirical Lyapunov exponents (mean ± std):
  λ_1 = +0.3846 ± 0.0251
  λ_2 = -0.1716 ± 0.0444
  λ_3 = -13.8799 ± 0.0398
Mean KY dim (predicted): 1.259 ± 0.007
Mean KY dim (empirical): 2.015 ± 0.002
Mean KY dim (burn-in):   0.066 ± 0.279
Computing prediction windows ...
Windows: 114 — nMSE min=0.0067, median=0.0388, mean=0.1270, max=1.4669
Computing long-trajectory free-running rollouts ...
Computing encoder/decoder Jacobians ...
encoder_jacobian: (128, 10, 10)
decoder_jacobian: (128, 10, 10)
Computing amplification loss ...
Amplification loss — True state: 0.000342
Amplification loss — Latent:     0.000289
```

</details>
