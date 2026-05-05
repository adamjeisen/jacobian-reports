# Sweep Analysis: `wmtask_init_compare__direct_sum_cayley_perareaautodim__lc_x_obsnoisescale_sweep__perconditionnorm`

**Project**: [WMTask_identity_encoder_verification](https://wandb.ai/JacobianODE/WMTask_identity_encoder_verification/groups/wmtask_init_compare__direct_sum_cayley_perareaautodim__lc_x_obsnoisescale_sweep__perconditionnorm)  
**Launched**: 2026-05-04T17:45:17Z  
**Completed**: 2026-05-04T23:50:24Z  
**Outcome**: `complete_clean`  
**Git**: `latent-JacobianODE` @ `7d3a182`  
**Expected runs**: 21

## Experiment Context

### `wmtask_init_compare_perconditionnorm`

**Description**

WMTask fully-observed (N1=N2=64), DirectSum coupling encoder with
per-area PCA-autodim, additive coupling + Cayley orthogonal mixers +
near-identity init, TF-coupled LR. Combined dataloader pools
trajectories from random-init and end-of-training checkpoints of the
same BiologicalRNN; condition_dim=1 with values {-1: init, +1: final}
threaded through encoder conditioners + dynamics MLP. Per-condition
normalization (each source gets its own grand-mean centering and
noise-scale calibration). Single-stage; sweep over loop_closure
weight + obs_noise_scale.

**Hypothesis**

The init-vs-final pair is the maximum-contrast within-system
comparison available — randomly-initialized weights vs trained
weights. If a conditioned JacobianODE can capture the dynamical
difference between these two extremes, the framework works at the
"easy" end. Per-condition normalization removes scale confound (init
activations may have systematically different magnitude than final
activations).

**Success criteria**

- All cells train without divergence (no NaN train loss)
- Per-source mu/sigma logged in config and visible in wandb
- Empirical Lyapunov spectrum at c=-1 (init) clearly differs from c=+1 (final) — unlike epoch_compare where they were nearly identical

## Results

**Swept axes** (8): `data.postprocessing.generalized_variance`, `data.postprocessing.mu`, `data.postprocessing.mu_per_source`, `data.postprocessing.sigma`, `data.postprocessing.sigma_per_source`, `model.n_target_dims_per_block_pca_cum_var`, `training.lightning.loop_closure_weight`, `training.lightning.obs_noise_scale`

**Chosen run** (by `best_traj_loss`): `7vi6tjz5` — traj_loss=0.00486, MASE=0.6909, R²=0.9941, LC loss=5.216, epoch=36.0

Swept-axis values at chosen run: `data.postprocessing.generalized_variance`=0.0198624 · `data.postprocessing.mu`=-0.00252023 · `data.postprocessing.mu_per_source`=[1.8099059910041237e-05, -0.005058568907196558] · `data.postprocessing.sigma`=0.481842 · `data.postprocessing.sigma_per_source`=[0.032797589644248414, 0.9308871126064868] · `model.n_target_dims_per_block_pca_cum_var`=[0.9910603877827018, 0.9910091959123422] · `training.lightning.loop_closure_weight`=1.0e-05 · `training.lightning.obs_noise_scale`=0

**Runs analyzed**: 21 (expected 21)

### Per-run results

| run_idx | run_id | `data.postprocessing.generalized_variance` | `data.postprocessing.mu` | `data.postprocessing.mu_per_source` | `data.postprocessing.sigma` | `data.postprocessing.sigma_per_source` | `model.n_target_dims_per_block_pca_cum_var` | `training.lightning.loop_closure_weight` | `training.lightning.obs_noise_scale` | best_traj_loss | best_MASE | R² | LC loss | epoch |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6 | `7vi6tjz5` | 0.0198624 | -0.00252023 | [1.8099059910041237e-05, -0.005058568907196558] | 0.481842 | [0.032797589644248414, 0.9308871126064868] | [0.9910603877827018, 0.9910091959123422] | 1.0e-05 | 0 | 0.00486 | 0.6909 | 0.9941 | 5.216 | 36.0 |
| 3 | `75p7jyz8` | 0.0198624 | -0.00252023 | [1.8099059910041237e-05, -0.005058568907196558] | 0.481842 | [0.032797589644248414, 0.9308871126064868] | [0.9910603877827018, 0.9910091959123422] | 1.0e-06 | 0 | 0.00490 | 0.6934 | 0.9940 | 13.870 | 35.0 |
| 0 | `qgocet1h` | 0.0198626 | -0.00252019 | [1.809667547217943e-05, -0.005058470008580706] | 0.481849 | [0.032797399902999645, 0.9309005828619008] | [0.991073378791082, 0.9909906471869928] | 0 | 0 | 0.00491 | 0.6976 | 0.9941 | 19.970 | 32.0 |
| 8 | `ca15pojg` | 0.0198624 | -0.00252023 | [1.8099059910041237e-05, -0.005058568907196558] | 0.481842 | [0.032797589644248414, 0.9308871126064868] | [0.9910603877827018, 0.9910091959123422] | 1.0e-05 | 0.05 | 0.00502 | 0.7001 | 0.9939 | 5.927 | 35.0 |
| 4 | `33ip4oe8` | 0.0198624 | -0.00252023 | [1.8099059910041237e-05, -0.005058568907196558] | 0.481842 | [0.032797589644248414, 0.9308871126064868] | [0.9910603877827018, 0.9910091959123422] | 1.0e-06 | 0.01 | 0.00503 | 0.7013 | 0.9938 | 14.434 | 36.0 |
| 2 | `x7i3g4gi` | 0.0198624 | -0.00252023 | [1.8099059910041237e-05, -0.005058568907196558] | 0.481842 | [0.032797589644248414, 0.9308871126064868] | [0.9910603877827018, 0.9910091959123422] | 0 | 0.05 | 0.00506 | 0.7038 | 0.9938 | 20.709 | 33.0 |
| 5 | `drdbjo4e` | 0.0198624 | -0.00252023 | [1.8099059910041237e-05, -0.005058568907196558] | 0.481842 | [0.032797589644248414, 0.9308871126064868] | [0.9910603877827018, 0.9910091959123422] | 1.0e-06 | 0.05 | 0.00507 | 0.7038 | 0.9938 | 15.334 | 31.0 |
| 7 | `kc35bjna` | 0.0198624 | -0.00252023 | [1.8099059910041237e-05, -0.005058568907196558] | 0.481842 | [0.032797589644248414, 0.9308871126064868] | [0.9910603877827018, 0.9910091959123422] | 1.0e-05 | 0.01 | 0.00510 | 0.7045 | 0.9938 | 5.665 | 33.0 |
| 1 | `iz44k2nk` | 0.0198624 | -0.00252023 | [1.8099059910041237e-05, -0.005058568907196558] | 0.481842 | [0.032797589644248414, 0.9308871126064868] | [0.9910603877827018, 0.9910091959123422] | 0 | 0.01 | 0.00513 | 0.7068 | 0.9937 | 21.370 | 31.0 |
| 11 | `0sy0ro0a` | 0.0198624 | -0.00252023 | [1.8099059910041237e-05, -0.005058568907196558] | 0.481842 | [0.032797589644248414, 0.9308871126064868] | [0.9910603877827018, 0.9910091959123422] | 1.0e-04 | 0.05 | 0.00514 | 0.7074 | 0.9937 | 1.459 | 35.0 |
| 12 | `yd4s93ma` | 0.0198624 | -0.00252023 | [1.8099059910041237e-05, -0.005058568907196558] | 0.481842 | [0.032797589644248414, 0.9308871126064868] | [0.9910603877827042, 0.991009195912342] | 0.001 | 0 | 0.00520 | 0.7109 | 0.9936 | 0.296 | 50.0 |
| 9 | `pzefu97k` | 0.0198624 | -0.00252023 | [1.8099059910041237e-05, -0.005058568907196558] | 0.481842 | [0.032797589644248414, 0.9308871126064868] | [0.9910603877827018, 0.9910091959123422] | 1.0e-04 | 0 | 0.00521 | 0.7107 | 0.9936 | 1.162 | 30.0 |
| 13 | `2elb7ude` | 0.0198624 | -0.00252023 | [1.8099059910041237e-05, -0.005058568907196558] | 0.481842 | [0.032797589644248414, 0.9308871126064868] | [0.9910603877827042, 0.991009195912342] | 0.001 | 0.01 | 0.00539 | 0.7217 | 0.9934 | 0.371 | 50.0 |
| 14 | `ocdj4wic` | 0.0198624 | -0.00252023 | [1.8099059910041237e-05, -0.005058568907196558] | 0.481842 | [0.032797589644248414, 0.9308871126064868] | [0.9910603877827018, 0.9910091959123422] | 0.001 | 0.05 | 0.00576 | 0.7417 | 0.9930 | 0.339 | 35.0 |
| 10 | `60rccaw9` | 0.0198624 | -0.00252023 | [1.8099059910041237e-05, -0.005058568907196558] | 0.481842 | [0.032797589644248414, 0.9308871126064868] | [0.9910603877827042, 0.991009195912342] | 1.0e-04 | 0.01 | 0.00620 | 0.7669 | 0.9924 | 1.119 | 18.0 |
| 15 | `0icv7fzu` | 0.0198624 | -0.00252023 | [1.8099059910041237e-05, -0.005058568907196558] | 0.481842 | [0.032797589644248414, 0.9308871126064868] | [0.9910603877827018, 0.9910091959123422] | 0.01 | 0 | 0.00759 | 0.8299 | 0.9907 | 0.068 | 31.0 |
| 18 | `yn5vn5yo` | 0.0198624 | -0.00252023 | [1.8099059910041237e-05, -0.005058568907196558] | 0.481842 | [0.032797589644248414, 0.9308871126064868] | [0.9910603877827018, 0.9910091959123422] | 0.1 | 0 | 0.01193 | 1.0152 | 0.9855 | 0.010 | 36.0 |
| 16 | `c2zsfvm3` | 0.0198624 | -0.00252023 | [1.8099059910041237e-05, -0.005058568907196558] | 0.481842 | [0.032797589644248414, 0.9308871126064868] | [0.9910603877827018, 0.9910091959123422] | 0.01 | 0.01 | 0.02367 | 1.4050 | 0.9711 | 0.606 | 36.0 |
| 17 | `wzyu7fxr` | 0.0198624 | -0.00252023 | [1.8099059910041237e-05, -0.005058568907196558] | 0.481842 | [0.032797589644248414, 0.9308871126064868] | [0.9910603877827018, 0.9910091959123422] | 0.01 | 0.05 | 0.02684 | 1.4892 | 0.9672 | 0.683 | 33.0 |
| 20 | `fadz4xfr` | 0.0198624 | -0.00252023 | [1.8099059910041237e-05, -0.005058568907196558] | 0.481842 | [0.032797589644248414, 0.9308871126064868] | [0.9910603877827018, 0.9910091959123422] | 0.1 | 0.05 | 0.03006 | 1.5973 | 0.9634 | 0.050 | 32.0 |
| 19 | `xhtv61pp` | 0.0198624 | -0.00252023 | [1.8099059910041237e-05, -0.005058568907196558] | 0.481842 | [0.032797589644248414, 0.9308871126064868] | [0.9910603877827018, 0.9910091959123422] | 0.1 | 0.01 | 0.03014 | 1.5941 | 0.9633 | 0.055 | 36.0 |

### Best run per `obs_noise_scale`

| obs_noise_scale | Best LC weight | Best traj loss | MASE at best | R² | LC loss | epoch |
|---|---|---|---|---|---|---|
| 0.0 | 1.0e-05 | 0.00486 | 0.6909 | 0.9941 | 5.216 | 36.0 |
| 0.01 | 1.0e-06 | 0.00503 | 0.7013 | 0.9938 | 14.434 | 36.0 |
| 0.05 | 1.0e-05 | 0.00502 | 0.7001 | 0.9939 | 5.927 | 35.0 |

## Success-criteria verdicts (automated)

| Criterion | Verdict | Note |
|---|---|---|
| All cells train without divergence (no NaN train loss) | **Unknown** |  |
| Per-source mu/sigma logged in config and visible in wandb | **Unknown** |  |
| Empirical Lyapunov spectrum at c=-1 (init) clearly differs from c=+1 (final) — unlike epoch_compare where they were nearly identical | **Unknown** |  |

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

### lyapunov_top10

![lyapunov_top10](figures/lyapunov_top10.png)

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

### amplification

![amplification](figures/amplification.png)

### kaplan_yorke_pca

![kaplan_yorke_pca](figures/kaplan_yorke_pca.png)

### prediction_detail_latent

![prediction_detail_latent](figures/prediction_detail_latent.png)

### prediction_detail_obs

![prediction_detail_obs](figures/prediction_detail_obs.png)

### gramians_overlay

![gramians_overlay](figures/gramians_overlay.png)

### gramians_metric_overlay

![gramians_metric_overlay](figures/gramians_metric_overlay.png)

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
No run_id provided — selecting best run from group 'wmtask_init_compare__direct_sum_cayley_perareaautodim__lc_x_obsnoisescale_sweep__perconditionnorm' ...
Found 21 total runs in JacobianODE/WMTask_identity_encoder_verification (group=wmtask_init_compare__direct_sum_cayley_perareaautodim__lc_x_obsnoisescale_sweep__perconditionnorm)
All runs (state, loop_closure_weight, tangent_entropy_weight, kl_dyn_weight):
  qgocet1h: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  33ip4oe8: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  x7i3g4gi: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  75p7jyz8: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  iz44k2nk: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  drdbjo4e: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  kc35bjna: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  7vi6tjz5: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  ca15pojg: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  pzefu97k: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  60rccaw9: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  0sy0ro0a: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  ocdj4wic: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  2elb7ude: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  yd4s93ma: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  0icv7fzu: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  wzyu7fxr: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  xhtv61pp: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  yn5vn5yo: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  c2zsfvm3: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  fadz4xfr: state=finished, lc=0.1, te=0.0, kl_dyn=0.0

slurm_timeout_min not found in any run config — falling back to 180 min
  Including qgocet1h (lc=0.0): use_all_runs=True (state=finished)
  Including 33ip4oe8 (lc=1e-06): use_all_runs=True (state=finished)
  Including x7i3g4gi (lc=0.0): use_all_runs=True (state=finished)
  Including 75p7jyz8 (lc=1e-06): use_all_runs=True (state=finished)
  Including iz44k2nk (lc=0.0): use_all_runs=True (state=finished)
  Including drdbjo4e (lc=1e-06): use_all_runs=True (state=finished)
  Including kc35bjna (lc=1e-05): use_all_runs=True (state=finished)
  Including 7vi6tjz5 (lc=1e-05): use_all_runs=True (state=finished)
  Including ca15pojg (lc=1e-05): use_all_runs=True (state=finished)
  Including pzefu97k (lc=0.0001): use_all_runs=True (state=finished)
  Including 60rccaw9 (lc=0.0001): use_all_runs=True (state=finished)
  Including 0sy0ro0a (lc=0.0001): use_all_runs=True (state=finished)
  Including ocdj4wic (lc=0.001): use_all_runs=True (state=finished)
  Including 2elb7ude (lc=0.001): use_all_runs=True (state=finished)
  Including yd4s93ma (lc=0.001): use_all_runs=True (state=finished)
  Including 0icv7fzu (lc=0.01): use_all_runs=True (state=finished)
  Including wzyu7fxr (lc=0.01): use_all_runs=True (state=finished)
  Including xhtv61pp (lc=0.1): use_all_runs=True (state=finished)
  Including yn5vn5yo (lc=0.1): use_all_runs=True (state=finished)
  Including c2zsfvm3 (lc=0.01): use_all_runs=True (state=finished)
  Including fadz4xfr (lc=0.1): use_all_runs=True (state=finished)
Found 21 effectively-done sweep runs:
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=iz44k2nk
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=qgocet1h
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=x7i3g4gi
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=33ip4oe8
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=75p7jyz8
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=drdbjo4e
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=7vi6tjz5
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=ca15pojg
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=kc35bjna
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=0sy0ro0a
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=60rccaw9
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=pzefu97k
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=2elb7ude
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=ocdj4wic
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=yd4s93ma
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=0icv7fzu
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=c2zsfvm3
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=wzyu7fxr
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=fadz4xfr
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=xhtv61pp
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=yn5vn5yo
Loading cached wmtask hiddens from /orcd/data/ekmiller/001/eisenaj/ControlJacobians/WMTaskModels/WMSelectionTask__cue_time_0.1__response_time_0.25__enforce_fixation_False/BiologicalRNN__cue_time_0.1__learning_rate_0.0005__max_epochs_42__N1_64__N2_64__tau_0.05__dt_0.02__eig_lower_bound_0.1__init_mode_random/_jacobianode_cache/hiddens__all__epochinit__trials4096__seed42.pt
loaded wmtask RNN model checkpoint 41
Loading cached wmtask hiddens from /orcd/data/ekmiller/001/eisenaj/ControlJacobians/WMTaskModels/WMSelectionTask__cue_time_0.1__response_time_0.25__enforce_fixation_False/BiologicalRNN__cue_time_0.1__learning_rate_0.0005__max_epochs_42__N1_64__N2_64__tau_0.05__dt_0.02__eig_lower_bound_0.1__init_mode_random/_jacobianode_cache/hiddens__all__epoch41__trials4096__seed42.pt
n_dims=128, n_latent=128, n_dyn=33, dt=0.0200
  run=iz44k2nk: DiagnosticMetrics(one_step_mase=0.5969197750091553, loop_closure_loss=21.36981964111328, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005127726122736931) (from W&B history)
  run=qgocet1h: DiagnosticMetrics(one_step_mase=0.5969600677490234, loop_closure_loss=19.969823837280273, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004911379422992468) (from W&B history)
  run=x7i3g4gi: DiagnosticMetrics(one_step_mase=0.5961401462554932, loop_closure_loss=20.709047317504883, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.00506466394290328) (from W&B history)
  run=33ip4oe8: DiagnosticMetrics(one_step_mase=0.5945682525634766, loop_closure_loss=14.434311866760254, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005033677909523249) (from W&B history)
  run=75p7jyz8: DiagnosticMetrics(one_step_mase=0.5943389534950256, loop_closure_loss=13.870006561279297, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004903852473944426) (from W&B history)
  run=drdbjo4e: DiagnosticMetrics(one_step_mase=0.5968809723854065, loop_closure_loss=15.334417343139648, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005073728039860725) (from W&B history)
  run=7vi6tjz5: DiagnosticMetrics(one_step_mase=0.5937438607215881, loop_closure_loss=5.215959548950195, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004858900792896748) (from W&B history)
  run=ca15pojg: DiagnosticMetrics(one_step_mase=0.5947051644325256, loop_closure_loss=5.927053451538086, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005017589777708054) (from W&B history)
  run=kc35bjna: DiagnosticMetrics(one_step_mase=0.595614492893219, loop_closure_loss=5.664689540863037, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0051010968163609505) (from W&B history)
  run=0sy0ro0a: DiagnosticMetrics(one_step_mase=0.5948210954666138, loop_closure_loss=1.4588721990585327, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.00514299375936389) (from W&B history)
  run=60rccaw9: DiagnosticMetrics(one_step_mase=0.6116471886634827, loop_closure_loss=1.1194342374801636, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.006201017647981644) (from W&B history)
  run=pzefu97k: DiagnosticMetrics(one_step_mase=0.5960590243339539, loop_closure_loss=1.1617023944854736, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0052101933397352695) (from W&B history)
  run=2elb7ude: DiagnosticMetrics(one_step_mase=0.5942543745040894, loop_closure_loss=0.3706282079219818, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.00539412721991539) (from W&B history)
  run=ocdj4wic: DiagnosticMetrics(one_step_mase=0.5989025831222534, loop_closure_loss=0.33876949548721313, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005760048050433397) (from W&B history)
  run=yd4s93ma: DiagnosticMetrics(one_step_mase=0.5934380292892456, loop_closure_loss=0.2959526479244232, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005204958841204643) (from W&B history)
  run=0icv7fzu: DiagnosticMetrics(one_step_mase=0.6120094060897827, loop_closure_loss=0.06836685538291931, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.007593028713017702) (from W&B history)
  run=c2zsfvm3: DiagnosticMetrics(one_step_mase=0.8272522687911987, loop_closure_loss=0.6058242321014404, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.023672649636864662) (from W&B history)
  run=wzyu7fxr: DiagnosticMetrics(one_step_mase=0.8479897975921631, loop_closure_loss=0.6829243302345276, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.026836449280381203) (from W&B history)
  run=fadz4xfr: DiagnosticMetrics(one_step_mase=0.9144480228424072, loop_closure_loss=0.04995812103152275, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.030060097575187683) (from W&B history)
  run=xhtv61pp: DiagnosticMetrics(one_step_mase=0.919941246509552, loop_closure_loss=0.05522070825099945, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.030138961970806122) (from W&B history)
  run=yn5vn5yo: DiagnosticMetrics(one_step_mase=0.6504870653152466, loop_closure_loss=0.009629915468394756, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.01192634180188179) (from W&B history)

Ranking method:           best_traj_loss
Best run ID:              7vi6tjz5
Best loop_closure_weight: 1e-05
Best tangent_entropy_weight: 0.0
Best kl_dyn_weight:       0.0
Best traj loss:           0.004859
Criteria applied: ['C1', 'C2', 'C3']
Surviving: 14 / 21
Auto-selected run_id: 7vi6tjz5

======================================================================
PARETO FRONTIER RUNS (5 runs)
======================================================================
  Run ID               LC Loss   Traj Val Loss
  ------------  --------------  --------------
  yn5vn5yo            0.009630        0.011926
  0icv7fzu            0.068367        0.007593
  yd4s93ma            0.295953        0.005205
  0sy0ro0a            1.458872        0.005143
  7vi6tjz5            5.215960        0.004859 <-- selected

======================================================================
RANKING METHOD COMPARISON (over 14 survivors)
======================================================================
  Method                  Run ID               LC Loss   Traj Val Loss
  ----------------------  ------------  --------------  --------------
  best_traj_loss          7vi6tjz5            5.215960        0.004859 <-- active
  pareto_knee             yd4s93ma            0.295953        0.005205
  geo_rank                yn5vn5yo            0.009630        0.011926
  minimax_rank            yd4s93ma            0.295953        0.005205
  geo_log_score           7vi6tjz5            5.215960        0.004859
  minimax_log_score       0icv7fzu            0.068367        0.007593
======================================================================

Loading run 7vi6tjz5 from JacobianODE/WMTask_identity_encoder_verification ...
Loading cached wmtask hiddens from /orcd/data/ekmiller/001/eisenaj/ControlJacobians/WMTaskModels/WMSelectionTask__cue_time_0.1__response_time_0.25__enforce_fixation_False/BiologicalRNN__cue_time_0.1__learning_rate_0.0005__max_epochs_42__N1_64__N2_64__tau_0.05__dt_0.02__eig_lower_bound_0.1__init_mode_random/_jacobianode_cache/hiddens__all__epochinit__trials4096__seed42.pt
loaded wmtask RNN model checkpoint 41
Loading cached wmtask hiddens from /orcd/data/ekmiller/001/eisenaj/ControlJacobians/WMTaskModels/WMSelectionTask__cue_time_0.1__response_time_0.25__enforce_fixation_False/BiologicalRNN__cue_time_0.1__learning_rate_0.0005__max_epochs_42__N1_64__N2_64__tau_0.05__dt_0.02__eig_lower_bound_0.1__init_mode_random/_jacobianode_cache/hiddens__all__epoch41__trials4096__seed42.pt
Loading checkpoint epoch=36-step=4625.ckpt...
Loading checkpoint epoch=36-step=4625.ckpt...
Computing reconstruction ...
Computing MASE ...
Teacher-forced MASE: 0.6319
Free-running MASE:   1.9135
Computing latent utilization ...
Entropy-based utilization: 0.903
Null subspace mean RMS: 6.498273e-02
Computing Lyapunov exponents ...
  Computing full-trajectory Lyapunov (818 test trajs, T=49) ...
Predicted Lyapunov exponents (batch+burn-in, 128 windowed trajs):
  λ_1 = -0.6817 ± 0.6533
  λ_2 = -1.2341 ± 0.2808
  λ_3 = -1.5454 ± 0.3066
  λ_4 = -1.7668 ± 0.4259
  λ_5 = -2.1647 ± 0.7288
  λ_6 = -2.2976 ± 0.8409
  λ_7 = -2.4400 ± 0.8891
  λ_8 = -2.5181 ± 0.9346
  λ_9 = -2.6053 ± 1.0062
  λ_10 = -2.7830 ± 0.9863
  λ_11 = -2.8588 ± 1.0585
  λ_12 = -2.9239 ± 1.1105
  λ_13 = -3.0078 ± 1.1519
  λ_14 = -3.0805 ± 1.2171
  λ_15 = -3.1671 ± 1.2506
  λ_16 = -3.2283 ± 1.2787
  λ_17 = -3.3099 ± 1.3385
  λ_18 = -3.3990 ± 1.4014
  λ_19 = -3.4617 ± 1.4508
  λ_20 = -3.6063 ± 1.4097
  λ_21 = -3.6705 ± 1.4671
  λ_22 = -3.8133 ± 1.4120
  λ_23 = -3.8989 ± 1.4032
  λ_24 = -4.0481 ± 1.3296
  λ_25 = -4.1127 ± 1.3586
  λ_26 = -4.1832 ± 1.3868
  λ_27 = -4.2630 ± 1.4186
  λ_28 = -4.5489 ± 1.3072
  λ_29 = -4.6721 ± 1.3186
  λ_30 = -4.7592 ± 1.3428
  λ_31 = -4.9393 ± 1.3566
  λ_32 = -5.1964 ± 1.3586
  λ_33 = -5.5402 ± 1.3130
Predicted Lyapunov exponents (full-length, 818 test trajs):
  λ_1 = -0.6817 ± 0.6533
  λ_2 = -1.2341 ± 0.2808
  λ_3 = -1.5454 ± 0.3066
  λ_4 = -1.7668 ± 0.4259
  λ_5 = -2.1647 ± 0.7288
  λ_6 = -2.2976 ± 0.8409
  λ_7 = -2.4400 ± 0.8891
  λ_8 = -2.5181 ± 0.9346
  λ_9 = -2.6053 ± 1.0062
  λ_10 = -2.7830 ± 0.9863
  λ_11 = -2.8588 ± 1.0585
  λ_12 = -2.9239 ± 1.1105
  λ_13 = -3.0078 ± 1.1519
  λ_14 = -3.0805 ± 1.2171
  λ_15 = -3.1671 ± 1.2506
  λ_16 = -3.2283 ± 1.2787
  λ_17 = -3.3099 ± 1.3385
  λ_18 = -3.3990 ± 1.4014
  λ_19 = -3.4617 ± 1.4508
  λ_20 = -3.6063 ± 1.4097
  λ_21 = -3.6705 ± 1.4671
  λ_22 = -3.8133 ± 1.4120
  λ_23 = -3.8989 ± 1.4032
  λ_24 = -4.0481 ± 1.3296
  λ_25 = -4.1127 ± 1.3586
  λ_26 = -4.1832 ± 1.3868
  λ_27 = -4.2630 ± 1.4186
  λ_28 = -4.5489 ± 1.3072
  λ_29 = -4.6721 ± 1.3186
  λ_30 = -4.7592 ± 1.3428
  λ_31 = -4.9393 ± 1.3566
  λ_32 = -5.1964 ± 1.3586
  λ_33 = -5.5402 ± 1.3130
Empirical Lyapunov exponents (mean ± std, all trajectories):
  λ_1 = -1.1792 ± 1.1190
  λ_2 = -1.4656 ± 0.9515
  λ_3 = -1.7931 ± 0.7364
  λ_4 = -2.1466 ± 0.4535
  λ_5 = -2.4430 ± 0.3807
  λ_6 = -2.6559 ± 0.3877
  λ_7 = -3.0228 ± 0.3257
  λ_8 = -3.3684 ± 0.2836
  λ_9 = -3.6626 ± 0.3270
  λ_10 = -3.8883 ± 0.4642
  λ_11 = -4.0673 ± 0.5582
  λ_12 = -4.4969 ± 0.6211
  λ_13 = -4.8524 ± 0.8048
  λ_14 = -5.2574 ± 0.8732
  λ_15 = -5.5204 ± 0.8870
  λ_16 = -5.8675 ± 0.8214
  λ_17 = -6.3471 ± 0.7414
  λ_18 = -6.5145 ± 0.8499
  λ_19 = -6.6754 ± 0.9315
  λ_20 = -6.7995 ± 0.9877
  λ_21 = -7.0082 ± 0.9556
  λ_22 = -7.1268 ± 1.0262
  λ_23 = -7.2705 ± 1.1235
  λ_24 = -7.4548 ± 1.2122
  λ_25 = -7.5659 ± 1.2707
  λ_26 = -7.7242 ± 1.2872
  λ_27 = -7.8978 ± 1.3182
  λ_28 = -8.0513 ± 1.3721
  λ_29 = -8.3507 ± 1.2997
  λ_30 = -8.7824 ± 1.1210
  λ_31 = -8.9658 ± 1.2366
  λ_32 = -9.1458 ± 1.3271
  λ_33 = -9.3745 ± 1.4872
  λ_34 = -9.7320 ± 1.7746
  λ_35 = -10.1154 ± 1.7243
  λ_36 = -10.3420 ± 1.8391
  λ_37 = -10.5401 ± 1.9714
  λ_38 = -10.7665 ± 2.0906
  λ_39 = -10.9310 ± 2.1658
  λ_40 = -11.8722 ± 1.5411
  λ_41 = -12.0081 ± 1.6343
  λ_42 = -12.6116 ± 1.3532
  λ_43 = -12.8786 ± 1.5341
  λ_44 = -13.9306 ± 1.0416
  λ_45 = -14.9140 ± 0.8029
  λ_46 = -15.7926 ± 0.8624
  λ_47 = -16.9225 ± 0.8161
  λ_48 = -18.0495 ± 0.4232
  λ_49 = -18.6935 ± 0.3773
  λ_50 = -19.2556 ± 0.2806
  λ_51 = -19.7508 ± 0.2508
  λ_52 = -20.1888 ± 0.2832
  λ_53 = -20.4692 ± 0.2686
  λ_54 = -21.1799 ± 0.3901
  λ_55 = -21.8665 ± 0.4471
  λ_56 = -22.4217 ± 0.3629
  λ_57 = -22.9242 ± 0.2314
  λ_58 = -23.2805 ± 0.2388
  λ_59 = -23.8713 ± 0.3841
  λ_60 = -24.0473 ± 0.3277
  λ_61 = -24.4570 ± 0.3410
  λ_62 = -24.6748 ± 0.2885
  λ_63 = -24.8263 ± 0.2505
  λ_64 = -25.0544 ± 0.2782
  λ_65 = -25.1689 ± 0.2398
  λ_66 = -25.3399 ± 0.2575
  λ_67 = -25.7386 ± 0.4818
  λ_68 = -26.0788 ± 0.6636
  λ_69 = -26.2179 ± 0.6724
  λ_70 = -26.2898 ± 0.6438
  λ_71 = -26.3522 ± 0.6207
  λ_72 = -26.4788 ± 0.6360
  λ_73 = -26.6727 ± 0.7120
  λ_74 = -26.8858 ± 0.7773
  λ_75 = -27.1707 ± 0.8684
  λ_76 = -27.2892 ± 0.8351
  λ_77 = -27.3689 ± 0.7947
  λ_78 = -27.4562 ± 0.7555
  λ_79 = -27.7218 ± 0.8136
  λ_80 = -28.0815 ± 0.9851
  λ_81 = -28.2232 ± 0.9688
  λ_82 = -28.3304 ± 0.9488
  λ_83 = -28.7719 ± 1.2249
  λ_84 = -28.9696 ± 1.2076
  λ_85 = -29.1010 ± 1.1737
  λ_86 = -29.2226 ± 1.1174
  λ_87 = -29.4063 ± 1.1424
  λ_88 = -29.5200 ± 1.1128
  λ_89 = -29.6903 ± 1.1375
  λ_90 = -29.8451 ± 1.1838
  λ_91 = -30.0167 ± 1.2222
  λ_92 = -30.1209 ± 1.1979
  λ_93 = -30.2440 ± 1.2231
  λ_94 = -30.4153 ± 1.2589
  λ_95 = -30.5249 ± 1.1820
  λ_96 = -30.6294 ± 1.1559
  λ_97 = -30.7479 ± 1.1384
  λ_98 = -31.0260 ± 1.2676
  λ_99 = -31.1506 ± 1.2685
  λ_100 = -31.2267 ± 1.2335
  λ_101 = -31.3068 ± 1.1875
  λ_102 = -31.4031 ± 1.1180
  λ_103 = -31.6534 ± 1.2544
  λ_104 = -31.8123 ± 1.2628
  λ_105 = -31.8967 ± 1.2089
  λ_106 = -31.9602 ± 1.1710
  λ_107 = -32.0324 ± 1.1156
  λ_108 = -32.2227 ± 1.1660
  λ_109 = -32.3439 ± 1.1514
  λ_110 = -32.4150 ± 1.0956
  λ_111 = -32.5919 ± 1.1148
  λ_112 = -32.7123 ± 1.1121
  λ_113 = -32.7820 ± 1.0752
  λ_114 = -32.8644 ± 1.0228
  λ_115 = -33.0267 ± 1.0589
  λ_116 = -33.1323 ± 1.0299
  λ_117 = -33.3630 ± 1.0855
  λ_118 = -33.4552 ± 1.0399
  λ_119 = -33.5489 ± 1.0496
  λ_120 = -33.7906 ± 1.1956
  λ_121 = -33.8602 ± 1.1592
  λ_122 = -34.0231 ± 1.2273
  λ_123 = -34.2578 ± 1.3301
  λ_124 = -34.5178 ± 1.4514
  λ_125 = -34.7694 ± 1.4713
  λ_126 = -34.8548 ± 1.4047
  λ_127 = -35.1170 ± 1.4727
  λ_128 = -35.3101 ± 1.4212
Empirical Lyapunov per condition:
  c=[-1.0]:
    λ_1 = -2.2594 ± 0.0331
    λ_2 = -2.3766 ± 0.0309
    λ_3 = -2.4512 ± 0.0347
    λ_4 = -2.5213 ± 0.0234
    λ_5 = -2.7046 ± 0.0362
    λ_6 = -2.8313 ± 0.0628
    λ_7 = -3.0986 ± 0.0589
    λ_8 = -3.2954 ± 0.0374
    λ_9 = -3.5067 ± 0.0206
    λ_10 = -3.5354 ± 0.0249
    λ_11 = -3.5831 ± 0.0401
    λ_12 = -3.9644 ± 0.0396
    λ_13 = -4.0837 ± 0.0369
    λ_14 = -4.4406 ± 0.0465
    λ_15 = -4.6935 ± 0.0397
    λ_16 = -5.1075 ± 0.0610
    λ_17 = -5.6505 ± 0.0333
    λ_18 = -5.7062 ± 0.0404
    λ_19 = -5.7798 ± 0.0270
    λ_20 = -5.8431 ± 0.0416
    λ_21 = -6.0868 ± 0.0303
    λ_22 = -6.1274 ± 0.0369
    λ_23 = -6.1713 ± 0.0392
    λ_24 = -6.2562 ± 0.0313
    λ_25 = -6.3101 ± 0.0421
    λ_26 = -6.4511 ± 0.0330
    λ_27 = -6.5950 ± 0.0278
    λ_28 = -6.7005 ± 0.0406
    λ_29 = -7.0737 ± 0.0650
    λ_30 = -7.6983 ± 0.0296
    λ_31 = -7.7828 ± 0.0324
    λ_32 = -7.8715 ± 0.0322
    λ_33 = -7.9392 ± 0.0346
    λ_34 = -7.9862 ± 0.0253
    λ_35 = -8.4290 ± 0.0369
    λ_36 = -8.5582 ± 0.0340
    λ_37 = -8.6232 ± 0.0435
    λ_38 = -8.7295 ± 0.0436
    λ_39 = -8.8257 ± 0.0351
    λ_40 = -10.4265 ± 0.0256
    λ_41 = -10.4639 ± 0.0327
    λ_42 = -11.3660 ± 0.0353
    λ_43 = -11.4444 ± 0.0382
    λ_44 = -12.9960 ± 0.0530
    λ_45 = -14.2059 ± 0.0424
    λ_46 = -15.0861 ± 0.0892
    λ_47 = -16.3269 ± 0.0809
    λ_48 = -17.7799 ± 0.0266
    λ_49 = -18.4960 ± 0.0373
    λ_50 = -19.1949 ± 0.0839
    λ_51 = -19.7689 ± 0.0587
    λ_52 = -20.3126 ± 0.0317
    λ_53 = -20.4890 ± 0.0718
    λ_54 = -21.4199 ± 0.0937
    λ_55 = -21.5800 ± 0.0784
    λ_56 = -22.1277 ± 0.0379
    λ_57 = -22.8243 ± 0.0440
    λ_58 = -23.2526 ± 0.1787
    λ_59 = -24.1890 ± 0.0402
    λ_60 = -24.3001 ± 0.0475
    λ_61 = -24.7415 ± 0.0835
    λ_62 = -24.8838 ± 0.0726
    λ_63 = -24.9849 ± 0.0420
    λ_64 = -25.2546 ± 0.0638
    λ_65 = -25.3311 ± 0.0480
    λ_66 = -25.5323 ± 0.0718
    λ_67 = -26.1820 ± 0.1085
    λ_68 = -26.7184 ± 0.0699
    λ_69 = -26.8658 ± 0.0282
    λ_70 = -26.9028 ± 0.0289
    λ_71 = -26.9386 ± 0.0320
    λ_72 = -27.0760 ± 0.0903
    λ_73 = -27.3500 ± 0.0545
    λ_74 = -27.6275 ± 0.0339
    λ_75 = -27.9929 ± 0.0331
    λ_76 = -28.0696 ± 0.0286
    λ_77 = -28.0993 ± 0.0290
    λ_78 = -28.1441 ± 0.0324
    λ_79 = -28.4763 ± 0.0394
    λ_80 = -29.0217 ± 0.0312
    λ_81 = -29.1504 ± 0.0321
    λ_82 = -29.2320 ± 0.0499
    λ_83 = -29.9550 ± 0.0285
    λ_84 = -30.1418 ± 0.0371
    λ_85 = -30.2364 ± 0.0333
    λ_86 = -30.2995 ± 0.0299
    λ_87 = -30.5094 ± 0.0350
    λ_88 = -30.5897 ± 0.0540
    λ_89 = -30.7774 ± 0.0495
    λ_90 = -30.9822 ± 0.0379
    λ_91 = -31.1951 ± 0.0253
    λ_92 = -31.2723 ± 0.0423
    λ_93 = -31.4245 ± 0.0343
    λ_94 = -31.6387 ± 0.0337
    λ_95 = -31.6687 ± 0.0294
    λ_96 = -31.7501 ± 0.0328
    λ_97 = -31.8500 ± 0.0293
    λ_98 = -32.2587 ± 0.0362
    λ_99 = -32.3834 ± 0.0294
    λ_100 = -32.4231 ± 0.0282
    λ_101 = -32.4576 ± 0.0208
    λ_102 = -32.4806 ± 0.0204
    λ_103 = -32.8699 ± 0.0277
    λ_104 = -33.0391 ± 0.0246
    λ_105 = -33.0652 ± 0.0243
    λ_106 = -33.0917 ± 0.0267
    λ_107 = -33.1107 ± 0.0282
    λ_108 = -33.3575 ± 0.0245
    λ_109 = -33.4683 ± 0.0206
    λ_110 = -33.4838 ± 0.0192
    λ_111 = -33.6733 ± 0.0280
    λ_112 = -33.7834 ± 0.0234
    λ_113 = -33.8097 ± 0.0195
    λ_114 = -33.8381 ± 0.0195
    λ_115 = -34.0408 ± 0.0320
    λ_116 = -34.1248 ± 0.0279
    λ_117 = -34.4236 ± 0.0451
    λ_118 = -34.4748 ± 0.0357
    λ_119 = -34.5763 ± 0.0295
    λ_120 = -34.9668 ± 0.0381
    λ_121 = -35.0001 ± 0.0306
    λ_122 = -35.2337 ± 0.0531
    λ_123 = -35.5756 ± 0.0468
    λ_124 = -35.9604 ± 0.0341
    λ_125 = -36.2271 ± 0.0399
    λ_126 = -36.2480 ± 0.0367
    λ_127 = -36.5812 ± 0.0296
    λ_128 = -36.7114 ± 0.0394
  c=[1.0]:
    λ_1 = -0.0990 ± 0.4089
    λ_2 = -0.5546 ± 0.3848
    λ_3 = -1.1349 ± 0.4651
    λ_4 = -1.7720 ± 0.3604
    λ_5 = -2.1813 ± 0.3894
    λ_6 = -2.4805 ± 0.4852
    λ_7 = -2.9471 ± 0.4443
    λ_8 = -3.4414 ± 0.3859
    λ_9 = -3.8185 ± 0.4061
    λ_10 = -4.2411 ± 0.4258
    λ_11 = -4.5516 ± 0.3900
    λ_12 = -5.0294 ± 0.4498
    λ_13 = -5.6211 ± 0.3332
    λ_14 = -6.0741 ± 0.4325
    λ_15 = -6.3473 ± 0.4504
    λ_16 = -6.6274 ± 0.4351
    λ_17 = -7.0436 ± 0.3563
    λ_18 = -7.3229 ± 0.3670
    λ_19 = -7.5709 ± 0.3588
    λ_20 = -7.7559 ± 0.3436
    λ_21 = -7.9297 ± 0.3543
    λ_22 = -8.1262 ± 0.3239
    λ_23 = -8.3697 ± 0.3218
    λ_24 = -8.6535 ± 0.2472
    λ_25 = -8.8217 ± 0.2647
    λ_26 = -8.9972 ± 0.2599
    λ_27 = -9.2005 ± 0.2764
    λ_28 = -9.4020 ± 0.3324
    λ_29 = -9.6276 ± 0.3299
    λ_30 = -9.8665 ± 0.3988
    λ_31 = -10.1489 ± 0.5050
    λ_32 = -10.4201 ± 0.5192
    λ_33 = -10.8098 ± 0.5454
    λ_34 = -11.4778 ± 0.4419
    λ_35 = -11.8018 ± 0.5006
    λ_36 = -12.1258 ± 0.6260
    λ_37 = -12.4569 ± 0.6431
    λ_38 = -12.8035 ± 0.6568
    λ_39 = -13.0363 ± 0.7113
    λ_40 = -13.3179 ± 0.7513
    λ_41 = -13.5523 ± 0.7528
    λ_42 = -13.8572 ± 0.7450
    λ_43 = -14.3129 ± 0.7664
    λ_44 = -14.8653 ± 0.6469
    λ_45 = -15.6221 ± 0.5327
    λ_46 = -16.4992 ± 0.6931
    λ_47 = -17.5181 ± 0.7847
    λ_48 = -18.3191 ± 0.4606
    λ_49 = -18.8911 ± 0.4533
    λ_50 = -19.3163 ± 0.3785
    λ_51 = -19.7328 ± 0.3491
    λ_52 = -20.0651 ± 0.3591
    λ_53 = -20.4494 ± 0.3722
    λ_54 = -20.9400 ± 0.4249
    λ_55 = -22.1529 ± 0.4793
    λ_56 = -22.7157 ± 0.2983
    λ_57 = -23.0241 ± 0.2920
    λ_58 = -23.3084 ± 0.2841
    λ_59 = -23.5536 ± 0.3024
    λ_60 = -23.7946 ± 0.2911
    λ_61 = -24.1726 ± 0.2524
    λ_62 = -24.4657 ± 0.2717
    λ_63 = -24.6678 ± 0.2712
    λ_64 = -24.8542 ± 0.2656
    λ_65 = -25.0067 ± 0.2452
    λ_66 = -25.1476 ± 0.2313
    λ_67 = -25.2951 ± 0.2427
    λ_68 = -25.4393 ± 0.2386
    λ_69 = -25.5700 ± 0.2508
    λ_70 = -25.6769 ± 0.2755
    λ_71 = -25.7658 ± 0.2847
    λ_72 = -25.8815 ± 0.2943
    λ_73 = -25.9955 ± 0.3042
    λ_74 = -26.1441 ± 0.3251
    λ_75 = -26.3485 ± 0.3921
    λ_76 = -26.5088 ± 0.4178
    λ_77 = -26.6384 ± 0.4405
    λ_78 = -26.7684 ± 0.4397
    λ_79 = -26.9673 ± 0.4273
    λ_80 = -27.1413 ± 0.4124
    λ_81 = -27.2959 ± 0.3932
    λ_82 = -27.4287 ± 0.4129
    λ_83 = -27.5887 ± 0.4441
    λ_84 = -27.7975 ± 0.4053
    λ_85 = -27.9656 ± 0.4154
    λ_86 = -28.1458 ± 0.4177
    λ_87 = -28.3033 ± 0.4156
    λ_88 = -28.4502 ± 0.4272
    λ_89 = -28.6031 ± 0.4677
    λ_90 = -28.7080 ± 0.4608
    λ_91 = -28.8384 ± 0.4547
    λ_92 = -28.9696 ± 0.4626
    λ_93 = -29.0635 ± 0.4475
    λ_94 = -29.1919 ± 0.4142
    λ_95 = -29.3812 ± 0.4168
    λ_96 = -29.5087 ± 0.3955
    λ_97 = -29.6459 ± 0.3990
    λ_98 = -29.7933 ± 0.4120
    λ_99 = -29.9178 ± 0.4175
    λ_100 = -30.0302 ± 0.4190
    λ_101 = -30.1561 ± 0.4101
    λ_102 = -30.3257 ± 0.4180
    λ_103 = -30.4369 ± 0.4278
    λ_104 = -30.5854 ± 0.4180
    λ_105 = -30.7281 ± 0.4336
    λ_106 = -30.8286 ± 0.4217
    λ_107 = -30.9540 ± 0.3998
    λ_108 = -31.0879 ± 0.3741
    λ_109 = -31.2196 ± 0.3461
    λ_110 = -31.3462 ± 0.3364
    λ_111 = -31.5105 ± 0.3783
    λ_112 = -31.6413 ± 0.4196
    λ_113 = -31.7543 ± 0.4440
    λ_114 = -31.8907 ± 0.4397
    λ_115 = -32.0127 ± 0.4271
    λ_116 = -32.1398 ± 0.3848
    λ_117 = -32.3023 ± 0.3196
    λ_118 = -32.4357 ± 0.2834
    λ_119 = -32.5216 ± 0.2981
    λ_120 = -32.6145 ± 0.2959
    λ_121 = -32.7202 ± 0.2911
    λ_122 = -32.8125 ± 0.2738
    λ_123 = -32.9400 ± 0.2430
    λ_124 = -33.0753 ± 0.2113
    λ_125 = -33.3118 ± 0.2706
    λ_126 = -33.4616 ± 0.2414
    λ_127 = -33.6528 ± 0.2089
    λ_128 = -33.9088 ± 0.3256
Mean KY dim (predicted): 0.271 ± 0.585
Mean KY dim (empirical): 0.405 ± 0.796
Mean KY dim (burn-in):   0.271 ± 0.585
Computing prediction windows ...
Windows: 3 — nMSE min=0.9790, median=1.2828, mean=1.1844, max=1.2915
Computing long-trajectory free-running rollouts ...
Skipping 'encoder_decoder_jacobians' for conditioned model: vmap+jacrev OOMs on DirectSum + condition (TODO: rewrite without vmap or wait for index_copy_ batching rule).
Computing amplification loss ...
Amplification loss — True state: 0.001991
Amplification loss — Latent:     0.002199
Skipping 'tangent_spectrum' for conditioned model: compute_tangent_spectrum needs c plumbing through _encoder_jacobian_at's vmap+jacrev (TODO).
Computing gramians_overlay ...
  c=[-1.0] vis→cog  reach (pred log_tr / gt log_tr): 0.461 / 0.659
  c=[-1.0] cog→vis  reach (pred log_tr / gt log_tr): -0.030 / 0.413
  c=[1.0] vis→cog  reach (pred log_tr / gt log_tr): 4.429 / 5.344
  c=[1.0] cog→vis  reach (pred log_tr / gt log_tr): 2.753 / 3.104
Computing gramians_metric_overlay ...
  c=[-1.0] vis→cog  reach (pred log_tr / gt log_tr): 0.711 / 0.659
  c=[-1.0] cog→vis  reach (pred log_tr / gt log_tr): 0.153 / 0.413
  c=[1.0] vis→cog  reach (pred log_tr / gt log_tr): 4.689 / 5.344
  c=[1.0] cog→vis  reach (pred log_tr / gt log_tr): 3.040 / 3.104
```

</details>
