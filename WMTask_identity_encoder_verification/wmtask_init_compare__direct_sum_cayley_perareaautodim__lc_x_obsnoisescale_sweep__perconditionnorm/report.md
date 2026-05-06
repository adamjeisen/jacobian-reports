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

### gramians_overlay_k20

![gramians_overlay_k20](figures/gramians_overlay_k20.png)

### gramians_metric_overlay_k20

![gramians_metric_overlay_k20](figures/gramians_metric_overlay_k20.png)

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
  run=iz44k2nk: DiagnosticMetrics(one_step_mase=0.5969197750091553, loop_closure_loss=21.36981964111328, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005127726122736931) (from cache, n_batches=100)
  run=qgocet1h: DiagnosticMetrics(one_step_mase=0.5969600677490234, loop_closure_loss=19.969823837280273, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004911379422992468) (from cache, n_batches=100)
  run=x7i3g4gi: DiagnosticMetrics(one_step_mase=0.5961401462554932, loop_closure_loss=20.709047317504883, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.00506466394290328) (from cache, n_batches=100)
  run=33ip4oe8: DiagnosticMetrics(one_step_mase=0.5945682525634766, loop_closure_loss=14.434311866760254, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005033677909523249) (from cache, n_batches=100)
  run=75p7jyz8: DiagnosticMetrics(one_step_mase=0.5943389534950256, loop_closure_loss=13.870006561279297, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004903852473944426) (from cache, n_batches=100)
  run=drdbjo4e: DiagnosticMetrics(one_step_mase=0.5968809723854065, loop_closure_loss=15.334417343139648, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005073728039860725) (from cache, n_batches=100)
  run=7vi6tjz5: DiagnosticMetrics(one_step_mase=0.5937438607215881, loop_closure_loss=5.215959548950195, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004858900792896748) (from cache, n_batches=100)
  run=ca15pojg: DiagnosticMetrics(one_step_mase=0.5947051644325256, loop_closure_loss=5.927053451538086, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005017589777708054) (from cache, n_batches=100)
  run=kc35bjna: DiagnosticMetrics(one_step_mase=0.595614492893219, loop_closure_loss=5.664689540863037, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0051010968163609505) (from cache, n_batches=100)
  run=0sy0ro0a: DiagnosticMetrics(one_step_mase=0.5948210954666138, loop_closure_loss=1.4588721990585327, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.00514299375936389) (from cache, n_batches=100)
  run=60rccaw9: DiagnosticMetrics(one_step_mase=0.6116471886634827, loop_closure_loss=1.1194342374801636, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.006201017647981644) (from cache, n_batches=100)
  run=pzefu97k: DiagnosticMetrics(one_step_mase=0.5960590243339539, loop_closure_loss=1.1617023944854736, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0052101933397352695) (from cache, n_batches=100)
  run=2elb7ude: DiagnosticMetrics(one_step_mase=0.5942543745040894, loop_closure_loss=0.3706282079219818, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.00539412721991539) (from cache, n_batches=100)
  run=ocdj4wic: DiagnosticMetrics(one_step_mase=0.5989025831222534, loop_closure_loss=0.33876949548721313, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005760048050433397) (from cache, n_batches=100)
  run=yd4s93ma: DiagnosticMetrics(one_step_mase=0.5934380292892456, loop_closure_loss=0.2959526479244232, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005204958841204643) (from cache, n_batches=100)
  run=0icv7fzu: DiagnosticMetrics(one_step_mase=0.6120094060897827, loop_closure_loss=0.06836685538291931, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.007593028713017702) (from cache, n_batches=100)
  run=c2zsfvm3: DiagnosticMetrics(one_step_mase=0.8272522687911987, loop_closure_loss=0.6058242321014404, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.023672649636864662) (from cache, n_batches=100)
  run=wzyu7fxr: DiagnosticMetrics(one_step_mase=0.8479897975921631, loop_closure_loss=0.6829243302345276, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.026836449280381203) (from cache, n_batches=100)
  run=fadz4xfr: DiagnosticMetrics(one_step_mase=0.9144480228424072, loop_closure_loss=0.04995812103152275, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.030060097575187683) (from cache, n_batches=100)
  run=xhtv61pp: DiagnosticMetrics(one_step_mase=0.919941246509552, loop_closure_loss=0.05522070825099945, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.030138961970806122) (from cache, n_batches=100)
  run=yn5vn5yo: DiagnosticMetrics(one_step_mase=0.6504870653152466, loop_closure_loss=0.009629915468394756, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.01192634180188179) (from cache, n_batches=100)

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
Computing prediction windows ...
Windows: 3 — nMSE min=0.9790, median=1.2828, mean=1.1844, max=1.2915
Skipping 'encoder_decoder_jacobians' for conditioned model: vmap+jacrev OOMs on DirectSum + condition (TODO: rewrite without vmap or wait for index_copy_ batching rule).
Skipping 'tangent_spectrum' for conditioned model: compute_tangent_spectrum needs c plumbing through _encoder_jacobian_at's vmap+jacrev (TODO).
Computing gramians_overlay ...
  shapes: test_trajs=(818, 49, 128), test_trajs_full=(818, 49, 128); delay_offset=0 (= n_delays - 1)
  GT obs_blocks (raw 128-dim): [slice(0, 64, None), slice(64, 128, None)]
  c=[-1.0] vis→cog  reach (pred log_tr / gt log_tr): 0.461 / 0.659  [B*T=784, n_windows=1]
  c=[-1.0] cog→vis  reach (pred log_tr / gt log_tr): -0.030 / 0.413  [B*T=784, n_windows=1]
  c=[1.0] vis→cog  reach (pred log_tr / gt log_tr): 4.429 / 5.344  [B*T=784, n_windows=1]
  c=[1.0] cog→vis  reach (pred log_tr / gt log_tr): 2.753 / 3.104  [B*T=784, n_windows=1]
Computing gramians_metric_overlay ...
  shapes: test_trajs=(818, 49, 128), test_trajs_full=(818, 49, 128); delay_offset=0 (= n_delays - 1)
  GT obs_blocks (raw 128-dim): [slice(0, 64, None), slice(64, 128, None)]
  c=[-1.0] vis→cog  reach (pred log_tr / gt log_tr): 0.711 / 0.659  [B*T=784, n_windows=1]
  c=[-1.0] cog→vis  reach (pred log_tr / gt log_tr): 0.153 / 0.413  [B*T=784, n_windows=1]
  c=[1.0] vis→cog  reach (pred log_tr / gt log_tr): 4.689 / 5.344  [B*T=784, n_windows=1]
  c=[1.0] cog→vis  reach (pred log_tr / gt log_tr): 3.040 / 3.104  [B*T=784, n_windows=1]
Computing gramians_overlay_k20 ...
  shapes: test_trajs=(818, 49, 128), test_trajs_full=(818, 49, 128); delay_offset=0 (= n_delays - 1)
  GT obs_blocks (raw 128-dim): [slice(0, 64, None), slice(64, 128, None)]
  c=[-1.0] vis→cog  reach (pred log_tr / gt log_tr): 0.017 / 0.362  [B*T=640, n_windows=2]
  c=[-1.0] cog→vis  reach (pred log_tr / gt log_tr): -0.340 / 0.232  [B*T=640, n_windows=2]
  c=[1.0] vis→cog  reach (pred log_tr / gt log_tr): 4.151 / 4.940  [B*T=640, n_windows=2]
  c=[1.0] cog→vis  reach (pred log_tr / gt log_tr): 2.397 / 2.468  [B*T=640, n_windows=2]
Computing gramians_metric_overlay_k20 ...
  shapes: test_trajs=(818, 49, 128), test_trajs_full=(818, 49, 128); delay_offset=0 (= n_delays - 1)
  GT obs_blocks (raw 128-dim): [slice(0, 64, None), slice(64, 128, None)]
  c=[-1.0] vis→cog  reach (pred log_tr / gt log_tr): 0.265 / 0.362  [B*T=640, n_windows=2]
  c=[-1.0] cog→vis  reach (pred log_tr / gt log_tr): -0.156 / 0.232  [B*T=640, n_windows=2]
  c=[1.0] vis→cog  reach (pred log_tr / gt log_tr): 4.409 / 4.940  [B*T=640, n_windows=2]
  c=[1.0] cog→vis  reach (pred log_tr / gt log_tr): 2.683 / 2.468  [B*T=640, n_windows=2]


--- backfill 2026-05-06T00:46:33Z sections=['prediction_detail', 'encoder_decoder_jacobians', 'tangent_spectrum', 'gramians_overlay', 'gramians_metric_overlay', 'gramians_overlay_k20', 'gramians_metric_overlay_k20'] ---
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
  run=iz44k2nk: DiagnosticMetrics(one_step_mase=0.5969197750091553, loop_closure_loss=21.36981964111328, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005127726122736931) (from cache, n_batches=100)
  run=qgocet1h: DiagnosticMetrics(one_step_mase=0.5969600677490234, loop_closure_loss=19.969823837280273, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004911379422992468) (from cache, n_batches=100)
  run=x7i3g4gi: DiagnosticMetrics(one_step_mase=0.5961401462554932, loop_closure_loss=20.709047317504883, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.00506466394290328) (from cache, n_batches=100)
  run=33ip4oe8: DiagnosticMetrics(one_step_mase=0.5945682525634766, loop_closure_loss=14.434311866760254, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005033677909523249) (from cache, n_batches=100)
  run=75p7jyz8: DiagnosticMetrics(one_step_mase=0.5943389534950256, loop_closure_loss=13.870006561279297, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004903852473944426) (from cache, n_batches=100)
  run=drdbjo4e: DiagnosticMetrics(one_step_mase=0.5968809723854065, loop_closure_loss=15.334417343139648, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005073728039860725) (from cache, n_batches=100)
  run=7vi6tjz5: DiagnosticMetrics(one_step_mase=0.5937438607215881, loop_closure_loss=5.215959548950195, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004858900792896748) (from cache, n_batches=100)
  run=ca15pojg: DiagnosticMetrics(one_step_mase=0.5947051644325256, loop_closure_loss=5.927053451538086, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005017589777708054) (from cache, n_batches=100)
  run=kc35bjna: DiagnosticMetrics(one_step_mase=0.595614492893219, loop_closure_loss=5.664689540863037, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0051010968163609505) (from cache, n_batches=100)
  run=0sy0ro0a: DiagnosticMetrics(one_step_mase=0.5948210954666138, loop_closure_loss=1.4588721990585327, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.00514299375936389) (from cache, n_batches=100)
  run=60rccaw9: DiagnosticMetrics(one_step_mase=0.6116471886634827, loop_closure_loss=1.1194342374801636, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.006201017647981644) (from cache, n_batches=100)
  run=pzefu97k: DiagnosticMetrics(one_step_mase=0.5960590243339539, loop_closure_loss=1.1617023944854736, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0052101933397352695) (from cache, n_batches=100)
  run=2elb7ude: DiagnosticMetrics(one_step_mase=0.5942543745040894, loop_closure_loss=0.3706282079219818, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.00539412721991539) (from cache, n_batches=100)
  run=ocdj4wic: DiagnosticMetrics(one_step_mase=0.5989025831222534, loop_closure_loss=0.33876949548721313, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005760048050433397) (from cache, n_batches=100)
  run=yd4s93ma: DiagnosticMetrics(one_step_mase=0.5934380292892456, loop_closure_loss=0.2959526479244232, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005204958841204643) (from cache, n_batches=100)
  run=0icv7fzu: DiagnosticMetrics(one_step_mase=0.6120094060897827, loop_closure_loss=0.06836685538291931, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.007593028713017702) (from cache, n_batches=100)
  run=c2zsfvm3: DiagnosticMetrics(one_step_mase=0.8272522687911987, loop_closure_loss=0.6058242321014404, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.023672649636864662) (from cache, n_batches=100)
  run=wzyu7fxr: DiagnosticMetrics(one_step_mase=0.8479897975921631, loop_closure_loss=0.6829243302345276, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.026836449280381203) (from cache, n_batches=100)
  run=fadz4xfr: DiagnosticMetrics(one_step_mase=0.9144480228424072, loop_closure_loss=0.04995812103152275, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.030060097575187683) (from cache, n_batches=100)
  run=xhtv61pp: DiagnosticMetrics(one_step_mase=0.919941246509552, loop_closure_loss=0.05522070825099945, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.030138961970806122) (from cache, n_batches=100)
  run=yn5vn5yo: DiagnosticMetrics(one_step_mase=0.6504870653152466, loop_closure_loss=0.009629915468394756, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.01192634180188179) (from cache, n_batches=100)

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
Computing prediction windows ...
Windows: 3 — nMSE min=0.9790, median=1.2828, mean=1.1844, max=1.2915
Skipping 'encoder_decoder_jacobians' for conditioned model: vmap+jacrev OOMs on DirectSum + condition (TODO: rewrite without vmap or wait for index_copy_ batching rule).
Skipping 'tangent_spectrum' for conditioned model: compute_tangent_spectrum needs c plumbing through _encoder_jacobian_at's vmap+jacrev (TODO).
Computing gramians_overlay ...
  shapes: test_trajs=(818, 49, 128), test_trajs_full=(818, 49, 128); delay_offset=0 (= n_delays - 1)
  GT obs_blocks (raw 128-dim): [slice(0, 64, None), slice(64, 128, None)]
  c=[-1.0] vis→cog  reach (pred log_tr / gt log_tr): 0.461 / 0.659  [B*T=784, n_windows=1]
  c=[-1.0] cog→vis  reach (pred log_tr / gt log_tr): -0.030 / 0.413  [B*T=784, n_windows=1]
  c=[1.0] vis→cog  reach (pred log_tr / gt log_tr): 4.429 / 5.344  [B*T=784, n_windows=1]
  c=[1.0] cog→vis  reach (pred log_tr / gt log_tr): 2.753 / 3.104  [B*T=784, n_windows=1]
Computing gramians_metric_overlay ...
  shapes: test_trajs=(818, 49, 128), test_trajs_full=(818, 49, 128); delay_offset=0 (= n_delays - 1)
  GT obs_blocks (raw 128-dim): [slice(0, 64, None), slice(64, 128, None)]
  c=[-1.0] vis→cog  reach (pred log_tr / gt log_tr): 0.711 / 0.659  [B*T=784, n_windows=1]
  c=[-1.0] cog→vis  reach (pred log_tr / gt log_tr): 0.153 / 0.413  [B*T=784, n_windows=1]
  c=[1.0] vis→cog  reach (pred log_tr / gt log_tr): 4.689 / 5.344  [B*T=784, n_windows=1]
  c=[1.0] cog→vis  reach (pred log_tr / gt log_tr): 3.040 / 3.104  [B*T=784, n_windows=1]
Computing gramians_overlay_k20 ...
  shapes: test_trajs=(818, 49, 128), test_trajs_full=(818, 49, 128); delay_offset=0 (= n_delays - 1)
  GT obs_blocks (raw 128-dim): [slice(0, 64, None), slice(64, 128, None)]
  c=[-1.0] vis→cog  reach (pred log_tr / gt log_tr): 0.017 / 0.362  [B*T=640, n_windows=2]
  c=[-1.0] cog→vis  reach (pred log_tr / gt log_tr): -0.340 / 0.232  [B*T=640, n_windows=2]
  c=[1.0] vis→cog  reach (pred log_tr / gt log_tr): 4.151 / 4.940  [B*T=640, n_windows=2]
  c=[1.0] cog→vis  reach (pred log_tr / gt log_tr): 2.397 / 2.468  [B*T=640, n_windows=2]
Computing gramians_metric_overlay_k20 ...
  shapes: test_trajs=(818, 49, 128), test_trajs_full=(818, 49, 128); delay_offset=0 (= n_delays - 1)
  GT obs_blocks (raw 128-dim): [slice(0, 64, None), slice(64, 128, None)]
  c=[-1.0] vis→cog  reach (pred log_tr / gt log_tr): 0.265 / 0.362  [B*T=640, n_windows=2]
  c=[-1.0] cog→vis  reach (pred log_tr / gt log_tr): -0.156 / 0.232  [B*T=640, n_windows=2]
  c=[1.0] vis→cog  reach (pred log_tr / gt log_tr): 4.409 / 4.940  [B*T=640, n_windows=2]
  c=[1.0] cog→vis  reach (pred log_tr / gt log_tr): 2.683 / 2.468  [B*T=640, n_windows=2]
```

</details>
