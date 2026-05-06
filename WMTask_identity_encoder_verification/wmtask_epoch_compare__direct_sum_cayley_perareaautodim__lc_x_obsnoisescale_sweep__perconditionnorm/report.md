# Sweep Analysis: `wmtask_epoch_compare__direct_sum_cayley_perareaautodim__lc_x_obsnoisescale_sweep__perconditionnorm`

**Project**: [WMTask_identity_encoder_verification](https://wandb.ai/JacobianODE/WMTask_identity_encoder_verification/groups/wmtask_epoch_compare__direct_sum_cayley_perareaautodim__lc_x_obsnoisescale_sweep__perconditionnorm)  
**Launched**: 2026-05-04T06:45:29Z  
**Completed**: 2026-05-04T16:10:21Z  
**Outcome**: `complete_clean`  
**Git**: `latent-JacobianODE` @ `73d708b`  
**Expected runs**: 21

## Experiment Context

### `wmtask_epoch_compare_perconditionnorm`

**Description**

Same as wmtask_epoch_compare but with per-condition data normalization:
each source (epoch=1, epoch=final) is centered + noise-scaled
independently. Grand-mean centering (single scalar per source across
all dims/trials/timesteps), not per-dim.

**Hypothesis**

Per-condition normalization removes any cross-condition scale
confound (e.g. if epoch=1 activations are systematically larger or
smaller than final-epoch activations). The model then has to learn
the dynamical difference between conditions on its own, with
matched observable scales. If results match the cross-condition
normalization sweep, scale wasn't a confound; if not, it was.

**Success criteria**

- All cells train without divergence (no NaN train loss)
- Per-source mu/sigma logged in config and visible in wandb
- val/trajectory_loss within ~2x of cross-condition sweep at the matching cell (no big regression from per-condition scaling)

## Results

**Swept axes** (4): `data.postprocessing.generalized_variance`, `model.n_target_dims_per_block_pca_cum_var`, `training.lightning.loop_closure_weight`, `training.lightning.obs_noise_scale`

**Chosen run** (by `best_traj_loss`): `5fm9o2jn` — traj_loss=0.00484, MASE=0.6357, R²=0.9953, LC loss=13.246, epoch=42.0

Swept-axis values at chosen run: `data.postprocessing.generalized_variance`=0.012975 · `model.n_target_dims_per_block_pca_cum_var`=[0.9901708670591398, 0.9905536733923817] · `training.lightning.loop_closure_weight`=1.0e-06 · `training.lightning.obs_noise_scale`=0

**Runs analyzed**: 21 (expected 21)

### Per-run results

| run_idx | run_id | `data.postprocessing.generalized_variance` | `model.n_target_dims_per_block_pca_cum_var` | `training.lightning.loop_closure_weight` | `training.lightning.obs_noise_scale` | best_traj_loss | best_MASE | R² | LC loss | epoch |
|---|---|---|---|---|---|---|---|---|---|---|
| 3 | `5fm9o2jn` | 0.012975 | [0.9901708670591398, 0.9905536733923817] | 1.0e-06 | 0 | 0.00484 | 0.6357 | 0.9953 | 13.246 | 42.0 |
| 4 | `tiaoc90n` | 0.012975 | [0.9901708670591398, 0.9905536733923817] | 1.0e-06 | 0.01 | 0.00495 | 0.6415 | 0.9952 | 14.037 | 45.0 |
| 2 | `579j062v` | 0.012975 | [0.9901708670591398, 0.9905536733923817] | 0 | 0.05 | 0.00495 | 0.6405 | 0.9952 | 20.502 | 38.0 |
| 1 | `2uqoy8fk` | 0.012975 | [0.9901708670591398, 0.9905536733923817] | 0 | 0.01 | 0.00495 | 0.6416 | 0.9952 | 18.904 | 45.0 |
| 0 | `gtdbbxo1` | 0.012975 | [0.9901708670591388, 0.9905536733923824] | 0 | 0 | 0.00495 | 0.6418 | 0.9952 | 18.361 | 37.0 |
| 5 | `cmig5yy3` | 0.012975 | [0.9901708670591388, 0.9905536733923824] | 1.0e-06 | 0.05 | 0.00502 | 0.6441 | 0.9951 | 15.011 | 36.0 |
| 8 | `0b7akhye` | 0.012975 | [0.9901708670591388, 0.9905536733923824] | 1.0e-05 | 0.05 | 0.00503 | 0.6448 | 0.9951 | 6.555 | 36.0 |
| 6 | `9u8o402o` | 0.012975 | [0.9901708670591388, 0.9905536733923824] | 1.0e-05 | 0 | 0.00504 | 0.6466 | 0.9951 | 5.042 | 34.0 |
| 7 | `dabyt1p0` | 0.012975 | [0.9901708670591388, 0.9905536733923824] | 1.0e-05 | 0.01 | 0.00512 | 0.6504 | 0.9950 | 5.930 | 36.0 |
| 11 | `laanygdn` | 0.012975 | [0.9901708670591398, 0.9905536733923817] | 1.0e-04 | 0.05 | 0.00517 | 0.6526 | 0.9950 | 1.834 | 36.0 |
| 9 | `p0o3shoc` | 0.012975 | [0.9901708670591388, 0.9905536733923824] | 1.0e-04 | 0 | 0.00524 | 0.6578 | 0.9949 | 1.282 | 32.0 |
| 10 | `ab6ugre6` | 0.012975 | [0.9901708670591388, 0.9905536733923824] | 1.0e-04 | 0.01 | 0.00549 | 0.6714 | 0.9947 | 1.502 | 29.0 |
| 12 | `ke9qk7o3` | 0.012975 | [0.9901708670591398, 0.9905536733923817] | 0.001 | 0 | 0.00550 | 0.6731 | 0.9947 | 0.345 | 51.0 |
| 13 | `390es83s` | 0.012975 | [0.9901708670591398, 0.9905536733923817] | 0.001 | 0.01 | 0.00579 | 0.6891 | 0.9944 | 0.511 | 51.0 |
| 14 | `ozm7srj5` | 0.012975 | [0.9901708670591388, 0.9905536733923824] | 0.001 | 0.05 | 0.00613 | 0.7052 | 0.9940 | 0.457 | 34.0 |
| 15 | `e1valj5j` | 0.012975 | [0.9901708670591388, 0.9905536733923824] | 0.01 | 0 | 0.00847 | 0.8135 | 0.9918 | 0.058 | 34.0 |
| 18 | `sd091ug7` | 0.012975 | [0.9901708670591388, 0.9905536733923824] | 0.1 | 0 | 0.01432 | 1.0242 | 0.9861 | 0.005 | 33.0 |
| 17 | `u5uq8i65` | 0.012975 | [0.9901708670591388, 0.9905536733923824] | 0.01 | 0.05 | 0.01614 | 1.0939 | 0.9843 | 0.234 | 32.0 |
| 16 | `coduqz9d` | 0.012975 | [0.9901708670591388, 0.9905536733923824] | 0.01 | 0.01 | 0.01999 | 1.2320 | 0.9806 | 0.431 | 34.0 |
| 20 | `orhpwyg3` | 0.012975 | [0.9901708670591398, 0.9905536733923817] | 0.1 | 0.05 | 0.02283 | 1.2922 | 0.9778 | 0.047 | 53.0 |
| 19 | `vcyfh9lk` | 0.012975 | [0.9901708670591398, 0.9905536733923817] | 0.1 | 0.01 | 0.02621 | 1.3831 | 0.9746 | 0.057 | 53.0 |

### Best run per `obs_noise_scale`

| obs_noise_scale | Best LC weight | Best traj loss | MASE at best | R² | LC loss | epoch |
|---|---|---|---|---|---|---|
| 0.0 | 1.0e-06 | 0.00484 | 0.6357 | 0.9953 | 13.246 | 42.0 |
| 0.01 | 1.0e-06 | 0.00495 | 0.6415 | 0.9952 | 14.037 | 45.0 |
| 0.05 | 0.0e+00 | 0.00495 | 0.6405 | 0.9952 | 20.502 | 38.0 |

## Success-criteria verdicts (automated)

| Criterion | Verdict | Note |
|---|---|---|
| All cells train without divergence (no NaN train loss) | **Unknown** |  |
| Per-source mu/sigma logged in config and visible in wandb | **Unknown** |  |
| val/trajectory_loss within ~2x of cross-condition sweep at the matching cell (no big regression from per-condition scaling) | **Unknown** |  |

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
No run_id provided — selecting best run from group 'wmtask_epoch_compare__direct_sum_cayley_perareaautodim__lc_x_obsnoisescale_sweep__perconditionnorm' ...
Found 21 total runs in JacobianODE/WMTask_identity_encoder_verification (group=wmtask_epoch_compare__direct_sum_cayley_perareaautodim__lc_x_obsnoisescale_sweep__perconditionnorm)
All runs (state, loop_closure_weight, tangent_entropy_weight, kl_dyn_weight):
  gtdbbxo1: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  2uqoy8fk: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  579j062v: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  5fm9o2jn: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  cmig5yy3: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  tiaoc90n: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  0b7akhye: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  dabyt1p0: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  9u8o402o: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  p0o3shoc: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  ab6ugre6: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  laanygdn: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  ke9qk7o3: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  390es83s: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  ozm7srj5: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  coduqz9d: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  e1valj5j: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  u5uq8i65: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  sd091ug7: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  vcyfh9lk: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  orhpwyg3: state=finished, lc=0.1, te=0.0, kl_dyn=0.0

slurm_timeout_min not found in any run config — falling back to 180 min
  Including gtdbbxo1 (lc=0.0): use_all_runs=True (state=finished)
  Including 2uqoy8fk (lc=0.0): use_all_runs=True (state=finished)
  Including 579j062v (lc=0.0): use_all_runs=True (state=finished)
  Including 5fm9o2jn (lc=1e-06): use_all_runs=True (state=finished)
  Including cmig5yy3 (lc=1e-06): use_all_runs=True (state=finished)
  Including tiaoc90n (lc=1e-06): use_all_runs=True (state=finished)
  Including 0b7akhye (lc=1e-05): use_all_runs=True (state=finished)
  Including dabyt1p0 (lc=1e-05): use_all_runs=True (state=finished)
  Including 9u8o402o (lc=1e-05): use_all_runs=True (state=finished)
  Including p0o3shoc (lc=0.0001): use_all_runs=True (state=finished)
  Including ab6ugre6 (lc=0.0001): use_all_runs=True (state=finished)
  Including laanygdn (lc=0.0001): use_all_runs=True (state=finished)
  Including ke9qk7o3 (lc=0.001): use_all_runs=True (state=finished)
  Including 390es83s (lc=0.001): use_all_runs=True (state=finished)
  Including ozm7srj5 (lc=0.001): use_all_runs=True (state=finished)
  Including coduqz9d (lc=0.01): use_all_runs=True (state=finished)
  Including e1valj5j (lc=0.01): use_all_runs=True (state=finished)
  Including u5uq8i65 (lc=0.01): use_all_runs=True (state=finished)
  Including sd091ug7 (lc=0.1): use_all_runs=True (state=finished)
  Including vcyfh9lk (lc=0.1): use_all_runs=True (state=finished)
  Including orhpwyg3 (lc=0.1): use_all_runs=True (state=finished)
Found 21 effectively-done sweep runs:
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=2uqoy8fk
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=579j062v
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=gtdbbxo1
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=5fm9o2jn
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=cmig5yy3
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=tiaoc90n
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=0b7akhye
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=9u8o402o
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=dabyt1p0
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=ab6ugre6
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=laanygdn
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=p0o3shoc
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=390es83s
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=ke9qk7o3
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=ozm7srj5
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=coduqz9d
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=e1valj5j
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=u5uq8i65
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=orhpwyg3
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=sd091ug7
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=vcyfh9lk
loaded wmtask RNN model checkpoint 1
Loading cached wmtask hiddens from /orcd/data/ekmiller/001/eisenaj/ControlJacobians/WMTaskModels/WMSelectionTask__cue_time_0.1__response_time_0.25__enforce_fixation_False/BiologicalRNN__cue_time_0.1__learning_rate_0.0005__max_epochs_42__N1_64__N2_64__tau_0.05__dt_0.02__eig_lower_bound_0.1__init_mode_random/_jacobianode_cache/hiddens__all__epoch1__trials4096__seed42.pt
loaded wmtask RNN model checkpoint 41
Loading cached wmtask hiddens from /orcd/data/ekmiller/001/eisenaj/ControlJacobians/WMTaskModels/WMSelectionTask__cue_time_0.1__response_time_0.25__enforce_fixation_False/BiologicalRNN__cue_time_0.1__learning_rate_0.0005__max_epochs_42__N1_64__N2_64__tau_0.05__dt_0.02__eig_lower_bound_0.1__init_mode_random/_jacobianode_cache/hiddens__all__epoch41__trials4096__seed42.pt
n_dims=128, n_latent=128, n_dyn=34, dt=0.0200
  run=2uqoy8fk: DiagnosticMetrics(one_step_mase=0.5558187961578369, loop_closure_loss=18.903587341308594, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004950683563947678) (from cache, n_batches=100)
  run=579j062v: DiagnosticMetrics(one_step_mase=0.5559232831001282, loop_closure_loss=20.50197982788086, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004950535483658314) (from cache, n_batches=100)
  run=gtdbbxo1: DiagnosticMetrics(one_step_mase=0.5532814860343933, loop_closure_loss=18.360904693603516, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004951320122927427) (from cache, n_batches=100)
  run=5fm9o2jn: DiagnosticMetrics(one_step_mase=0.5522419810295105, loop_closure_loss=13.246111869812012, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.00484210392460227) (from cache, n_batches=100)
  run=cmig5yy3: DiagnosticMetrics(one_step_mase=0.5563136339187622, loop_closure_loss=15.011119842529297, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005018870811909437) (from cache, n_batches=100)
  run=tiaoc90n: DiagnosticMetrics(one_step_mase=0.555823802947998, loop_closure_loss=14.03726577758789, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004947544075548649) (from cache, n_batches=100)
  run=0b7akhye: DiagnosticMetrics(one_step_mase=0.5564490556716919, loop_closure_loss=6.554826736450195, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005029578693211079) (from cache, n_batches=100)
  run=9u8o402o: DiagnosticMetrics(one_step_mase=0.5540623068809509, loop_closure_loss=5.042276382446289, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005039408802986145) (from cache, n_batches=100)
  run=dabyt1p0: DiagnosticMetrics(one_step_mase=0.5573251843452454, loop_closure_loss=5.929609298706055, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005117913708090782) (from cache, n_batches=100)
  run=ab6ugre6: DiagnosticMetrics(one_step_mase=0.5603269338607788, loop_closure_loss=1.501705288887024, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005491080228239298) (from cache, n_batches=100)
  run=laanygdn: DiagnosticMetrics(one_step_mase=0.5573882460594177, loop_closure_loss=1.8341436386108398, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.00516900047659874) (from cache, n_batches=100)
  run=p0o3shoc: DiagnosticMetrics(one_step_mase=0.5552201271057129, loop_closure_loss=1.2823923826217651, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005241198465228081) (from cache, n_batches=100)
  run=390es83s: DiagnosticMetrics(one_step_mase=0.5621083974838257, loop_closure_loss=0.5111938714981079, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005792605224996805) (from cache, n_batches=100)
  run=ke9qk7o3: DiagnosticMetrics(one_step_mase=0.5546627044677734, loop_closure_loss=0.34494704008102417, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.00550009123980999) (from cache, n_batches=100)
  run=ozm7srj5: DiagnosticMetrics(one_step_mase=0.5648052096366882, loop_closure_loss=0.45738956332206726, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.006133679300546646) (from cache, n_batches=100)
  run=coduqz9d: DiagnosticMetrics(one_step_mase=0.7148721218109131, loop_closure_loss=0.4305470585823059, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.019992414861917496) (from cache, n_batches=100)
  run=e1valj5j: DiagnosticMetrics(one_step_mase=0.569633424282074, loop_closure_loss=0.05807286128401756, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.00847175344824791) (from cache, n_batches=100)
  run=u5uq8i65: DiagnosticMetrics(one_step_mase=0.6564177870750427, loop_closure_loss=0.2338138371706009, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.01613655313849449) (from cache, n_batches=100)
  run=orhpwyg3: DiagnosticMetrics(one_step_mase=0.7736932039260864, loop_closure_loss=0.0469277985394001, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.02282564342021942) (from cache, n_batches=100)
  run=sd091ug7: DiagnosticMetrics(one_step_mase=0.5886143445968628, loop_closure_loss=0.0048964242450892925, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.014319156296551228) (from cache, n_batches=100)
  run=vcyfh9lk: DiagnosticMetrics(one_step_mase=0.8123706579208374, loop_closure_loss=0.05695308744907379, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.026211142539978027) (from cache, n_batches=100)

Ranking method:           best_traj_loss
Best run ID:              9u8o402o
Best loop_closure_weight: 1e-05
Best tangent_entropy_weight: 0.0
Best kl_dyn_weight:       0.0
Best traj loss:           0.005039
Criteria applied: ['C1', 'C2', 'C3']
Surviving: 13 / 21
Auto-selected run_id: 9u8o402o

======================================================================
PARETO FRONTIER RUNS (8 runs)
======================================================================
  Run ID               LC Loss   Traj Val Loss
  ------------  --------------  --------------
  sd091ug7            0.004896        0.014319
  e1valj5j            0.058073        0.008472
  ke9qk7o3            0.344947        0.005500
  p0o3shoc            1.282392        0.005241
  laanygdn            1.834144        0.005169
  9u8o402o            5.042276        0.005039 <-- selected
  0b7akhye            6.554827        0.005030
  5fm9o2jn           13.246112        0.004842

======================================================================
RANKING METHOD COMPARISON (over 13 survivors)
======================================================================
  Method                  Run ID               LC Loss   Traj Val Loss
  ----------------------  ------------  --------------  --------------
  best_traj_loss          9u8o402o            5.042276        0.005039 <-- active
  pareto_knee             ke9qk7o3            0.344947        0.005500
  geo_rank                sd091ug7            0.004896        0.014319
  minimax_rank            ke9qk7o3            0.344947        0.005500
  geo_log_score           9u8o402o            5.042276        0.005039
  minimax_log_score       e1valj5j            0.058073        0.008472
======================================================================

Loading run 9u8o402o from JacobianODE/WMTask_identity_encoder_verification ...
loaded wmtask RNN model checkpoint 1
Loading cached wmtask hiddens from /orcd/data/ekmiller/001/eisenaj/ControlJacobians/WMTaskModels/WMSelectionTask__cue_time_0.1__response_time_0.25__enforce_fixation_False/BiologicalRNN__cue_time_0.1__learning_rate_0.0005__max_epochs_42__N1_64__N2_64__tau_0.05__dt_0.02__eig_lower_bound_0.1__init_mode_random/_jacobianode_cache/hiddens__all__epoch1__trials4096__seed42.pt
loaded wmtask RNN model checkpoint 41
Loading cached wmtask hiddens from /orcd/data/ekmiller/001/eisenaj/ControlJacobians/WMTaskModels/WMSelectionTask__cue_time_0.1__response_time_0.25__enforce_fixation_False/BiologicalRNN__cue_time_0.1__learning_rate_0.0005__max_epochs_42__N1_64__N2_64__tau_0.05__dt_0.02__eig_lower_bound_0.1__init_mode_random/_jacobianode_cache/hiddens__all__epoch41__trials4096__seed42.pt
Loading checkpoint epoch=34-step=4375.ckpt...
Loading checkpoint epoch=34-step=4375.ckpt...
Computing prediction windows ...
Windows: 3 — nMSE min=0.0705, median=0.0881, mean=0.0862, max=0.0998
Skipping 'encoder_decoder_jacobians' for conditioned model: vmap+jacrev OOMs on DirectSum + condition (TODO: rewrite without vmap or wait for index_copy_ batching rule).
Skipping 'tangent_spectrum' for conditioned model: compute_tangent_spectrum needs c plumbing through _encoder_jacobian_at's vmap+jacrev (TODO).
Computing gramians_overlay ...
  shapes: test_trajs=(818, 49, 128), test_trajs_full=(818, 49, 128); delay_offset=0 (= n_delays - 1)
  GT obs_blocks (raw 128-dim): [slice(0, 64, None), slice(64, 128, None)]
  c=[-1.0] vis→cog  reach (pred log_tr / gt log_tr): 4.329 / 3.569  [B*T=784, n_windows=1]
  c=[-1.0] cog→vis  reach (pred log_tr / gt log_tr): 1.707 / 1.526  [B*T=784, n_windows=1]
  c=[1.0] vis→cog  reach (pred log_tr / gt log_tr): 4.684 / 5.007  [B*T=784, n_windows=1]
  c=[1.0] cog→vis  reach (pred log_tr / gt log_tr): 2.440 / 2.796  [B*T=784, n_windows=1]
Computing gramians_metric_overlay ...
  shapes: test_trajs=(818, 49, 128), test_trajs_full=(818, 49, 128); delay_offset=0 (= n_delays - 1)
  GT obs_blocks (raw 128-dim): [slice(0, 64, None), slice(64, 128, None)]
  c=[-1.0] vis→cog  reach (pred log_tr / gt log_tr): 4.814 / 3.569  [B*T=784, n_windows=1]
  c=[-1.0] cog→vis  reach (pred log_tr / gt log_tr): 1.902 / 1.526  [B*T=784, n_windows=1]
  c=[1.0] vis→cog  reach (pred log_tr / gt log_tr): 5.129 / 5.007  [B*T=784, n_windows=1]
  c=[1.0] cog→vis  reach (pred log_tr / gt log_tr): 2.672 / 2.796  [B*T=784, n_windows=1]
Computing gramians_overlay_k20 ...
  shapes: test_trajs=(818, 49, 128), test_trajs_full=(818, 49, 128); delay_offset=0 (= n_delays - 1)
  GT obs_blocks (raw 128-dim): [slice(0, 64, None), slice(64, 128, None)]
  c=[-1.0] vis→cog  reach (pred log_tr / gt log_tr): 3.653 / 3.271  [B*T=640, n_windows=2]
  c=[-1.0] cog→vis  reach (pred log_tr / gt log_tr): 1.275 / 1.027  [B*T=640, n_windows=2]
  c=[1.0] vis→cog  reach (pred log_tr / gt log_tr): 4.523 / 4.754  [B*T=640, n_windows=2]
  c=[1.0] cog→vis  reach (pred log_tr / gt log_tr): 2.162 / 2.311  [B*T=640, n_windows=2]
Computing gramians_metric_overlay_k20 ...
  shapes: test_trajs=(818, 49, 128), test_trajs_full=(818, 49, 128); delay_offset=0 (= n_delays - 1)
  GT obs_blocks (raw 128-dim): [slice(0, 64, None), slice(64, 128, None)]
  c=[-1.0] vis→cog  reach (pred log_tr / gt log_tr): 4.114 / 3.271  [B*T=640, n_windows=2]
  c=[-1.0] cog→vis  reach (pred log_tr / gt log_tr): 1.464 / 1.027  [B*T=640, n_windows=2]
  c=[1.0] vis→cog  reach (pred log_tr / gt log_tr): 4.969 / 4.754  [B*T=640, n_windows=2]
  c=[1.0] cog→vis  reach (pred log_tr / gt log_tr): 2.385 / 2.311  [B*T=640, n_windows=2]


--- backfill 2026-05-06T00:45:35Z sections=['prediction_detail', 'encoder_decoder_jacobians', 'tangent_spectrum', 'gramians_overlay', 'gramians_metric_overlay', 'gramians_overlay_k20', 'gramians_metric_overlay_k20'] ---
No run_id provided — selecting best run from group 'wmtask_epoch_compare__direct_sum_cayley_perareaautodim__lc_x_obsnoisescale_sweep__perconditionnorm' ...
Found 21 total runs in JacobianODE/WMTask_identity_encoder_verification (group=wmtask_epoch_compare__direct_sum_cayley_perareaautodim__lc_x_obsnoisescale_sweep__perconditionnorm)
All runs (state, loop_closure_weight, tangent_entropy_weight, kl_dyn_weight):
  gtdbbxo1: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  2uqoy8fk: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  579j062v: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  5fm9o2jn: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  cmig5yy3: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  tiaoc90n: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  0b7akhye: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  dabyt1p0: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  9u8o402o: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  p0o3shoc: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  ab6ugre6: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  laanygdn: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  ke9qk7o3: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  390es83s: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  ozm7srj5: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  coduqz9d: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  e1valj5j: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  u5uq8i65: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  sd091ug7: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  vcyfh9lk: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  orhpwyg3: state=finished, lc=0.1, te=0.0, kl_dyn=0.0

slurm_timeout_min not found in any run config — falling back to 180 min
  Including gtdbbxo1 (lc=0.0): use_all_runs=True (state=finished)
  Including 2uqoy8fk (lc=0.0): use_all_runs=True (state=finished)
  Including 579j062v (lc=0.0): use_all_runs=True (state=finished)
  Including 5fm9o2jn (lc=1e-06): use_all_runs=True (state=finished)
  Including cmig5yy3 (lc=1e-06): use_all_runs=True (state=finished)
  Including tiaoc90n (lc=1e-06): use_all_runs=True (state=finished)
  Including 0b7akhye (lc=1e-05): use_all_runs=True (state=finished)
  Including dabyt1p0 (lc=1e-05): use_all_runs=True (state=finished)
  Including 9u8o402o (lc=1e-05): use_all_runs=True (state=finished)
  Including p0o3shoc (lc=0.0001): use_all_runs=True (state=finished)
  Including ab6ugre6 (lc=0.0001): use_all_runs=True (state=finished)
  Including laanygdn (lc=0.0001): use_all_runs=True (state=finished)
  Including ke9qk7o3 (lc=0.001): use_all_runs=True (state=finished)
  Including 390es83s (lc=0.001): use_all_runs=True (state=finished)
  Including ozm7srj5 (lc=0.001): use_all_runs=True (state=finished)
  Including coduqz9d (lc=0.01): use_all_runs=True (state=finished)
  Including e1valj5j (lc=0.01): use_all_runs=True (state=finished)
  Including u5uq8i65 (lc=0.01): use_all_runs=True (state=finished)
  Including sd091ug7 (lc=0.1): use_all_runs=True (state=finished)
  Including vcyfh9lk (lc=0.1): use_all_runs=True (state=finished)
  Including orhpwyg3 (lc=0.1): use_all_runs=True (state=finished)
Found 21 effectively-done sweep runs:
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=2uqoy8fk
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=579j062v
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=gtdbbxo1
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=5fm9o2jn
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=cmig5yy3
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=tiaoc90n
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=0b7akhye
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=9u8o402o
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=dabyt1p0
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=ab6ugre6
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=laanygdn
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=p0o3shoc
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=390es83s
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=ke9qk7o3
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=ozm7srj5
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=coduqz9d
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=e1valj5j
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=u5uq8i65
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=orhpwyg3
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=sd091ug7
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=vcyfh9lk
loaded wmtask RNN model checkpoint 1
Loading cached wmtask hiddens from /orcd/data/ekmiller/001/eisenaj/ControlJacobians/WMTaskModels/WMSelectionTask__cue_time_0.1__response_time_0.25__enforce_fixation_False/BiologicalRNN__cue_time_0.1__learning_rate_0.0005__max_epochs_42__N1_64__N2_64__tau_0.05__dt_0.02__eig_lower_bound_0.1__init_mode_random/_jacobianode_cache/hiddens__all__epoch1__trials4096__seed42.pt
loaded wmtask RNN model checkpoint 41
Loading cached wmtask hiddens from /orcd/data/ekmiller/001/eisenaj/ControlJacobians/WMTaskModels/WMSelectionTask__cue_time_0.1__response_time_0.25__enforce_fixation_False/BiologicalRNN__cue_time_0.1__learning_rate_0.0005__max_epochs_42__N1_64__N2_64__tau_0.05__dt_0.02__eig_lower_bound_0.1__init_mode_random/_jacobianode_cache/hiddens__all__epoch41__trials4096__seed42.pt
n_dims=128, n_latent=128, n_dyn=34, dt=0.0200
  run=2uqoy8fk: DiagnosticMetrics(one_step_mase=0.5558187961578369, loop_closure_loss=18.903587341308594, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004950683563947678) (from cache, n_batches=100)
  run=579j062v: DiagnosticMetrics(one_step_mase=0.5559232831001282, loop_closure_loss=20.50197982788086, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004950535483658314) (from cache, n_batches=100)
  run=gtdbbxo1: DiagnosticMetrics(one_step_mase=0.5532814860343933, loop_closure_loss=18.360904693603516, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004951320122927427) (from cache, n_batches=100)
  run=5fm9o2jn: DiagnosticMetrics(one_step_mase=0.5522419810295105, loop_closure_loss=13.246111869812012, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.00484210392460227) (from cache, n_batches=100)
  run=cmig5yy3: DiagnosticMetrics(one_step_mase=0.5563136339187622, loop_closure_loss=15.011119842529297, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005018870811909437) (from cache, n_batches=100)
  run=tiaoc90n: DiagnosticMetrics(one_step_mase=0.555823802947998, loop_closure_loss=14.03726577758789, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004947544075548649) (from cache, n_batches=100)
  run=0b7akhye: DiagnosticMetrics(one_step_mase=0.5564490556716919, loop_closure_loss=6.554826736450195, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005029578693211079) (from cache, n_batches=100)
  run=9u8o402o: DiagnosticMetrics(one_step_mase=0.5540623068809509, loop_closure_loss=5.042276382446289, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005039408802986145) (from cache, n_batches=100)
  run=dabyt1p0: DiagnosticMetrics(one_step_mase=0.5573251843452454, loop_closure_loss=5.929609298706055, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005117913708090782) (from cache, n_batches=100)
  run=ab6ugre6: DiagnosticMetrics(one_step_mase=0.5603269338607788, loop_closure_loss=1.501705288887024, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005491080228239298) (from cache, n_batches=100)
  run=laanygdn: DiagnosticMetrics(one_step_mase=0.5573882460594177, loop_closure_loss=1.8341436386108398, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.00516900047659874) (from cache, n_batches=100)
  run=p0o3shoc: DiagnosticMetrics(one_step_mase=0.5552201271057129, loop_closure_loss=1.2823923826217651, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005241198465228081) (from cache, n_batches=100)
  run=390es83s: DiagnosticMetrics(one_step_mase=0.5621083974838257, loop_closure_loss=0.5111938714981079, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005792605224996805) (from cache, n_batches=100)
  run=ke9qk7o3: DiagnosticMetrics(one_step_mase=0.5546627044677734, loop_closure_loss=0.34494704008102417, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.00550009123980999) (from cache, n_batches=100)
  run=ozm7srj5: DiagnosticMetrics(one_step_mase=0.5648052096366882, loop_closure_loss=0.45738956332206726, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.006133679300546646) (from cache, n_batches=100)
  run=coduqz9d: DiagnosticMetrics(one_step_mase=0.7148721218109131, loop_closure_loss=0.4305470585823059, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.019992414861917496) (from cache, n_batches=100)
  run=e1valj5j: DiagnosticMetrics(one_step_mase=0.569633424282074, loop_closure_loss=0.05807286128401756, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.00847175344824791) (from cache, n_batches=100)
  run=u5uq8i65: DiagnosticMetrics(one_step_mase=0.6564177870750427, loop_closure_loss=0.2338138371706009, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.01613655313849449) (from cache, n_batches=100)
  run=orhpwyg3: DiagnosticMetrics(one_step_mase=0.7736932039260864, loop_closure_loss=0.0469277985394001, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.02282564342021942) (from cache, n_batches=100)
  run=sd091ug7: DiagnosticMetrics(one_step_mase=0.5886143445968628, loop_closure_loss=0.0048964242450892925, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.014319156296551228) (from cache, n_batches=100)
  run=vcyfh9lk: DiagnosticMetrics(one_step_mase=0.8123706579208374, loop_closure_loss=0.05695308744907379, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.026211142539978027) (from cache, n_batches=100)

Ranking method:           best_traj_loss
Best run ID:              9u8o402o
Best loop_closure_weight: 1e-05
Best tangent_entropy_weight: 0.0
Best kl_dyn_weight:       0.0
Best traj loss:           0.005039
Criteria applied: ['C1', 'C2', 'C3']
Surviving: 13 / 21
Auto-selected run_id: 9u8o402o

======================================================================
PARETO FRONTIER RUNS (8 runs)
======================================================================
  Run ID               LC Loss   Traj Val Loss
  ------------  --------------  --------------
  sd091ug7            0.004896        0.014319
  e1valj5j            0.058073        0.008472
  ke9qk7o3            0.344947        0.005500
  p0o3shoc            1.282392        0.005241
  laanygdn            1.834144        0.005169
  9u8o402o            5.042276        0.005039 <-- selected
  0b7akhye            6.554827        0.005030
  5fm9o2jn           13.246112        0.004842

======================================================================
RANKING METHOD COMPARISON (over 13 survivors)
======================================================================
  Method                  Run ID               LC Loss   Traj Val Loss
  ----------------------  ------------  --------------  --------------
  best_traj_loss          9u8o402o            5.042276        0.005039 <-- active
  pareto_knee             ke9qk7o3            0.344947        0.005500
  geo_rank                sd091ug7            0.004896        0.014319
  minimax_rank            ke9qk7o3            0.344947        0.005500
  geo_log_score           9u8o402o            5.042276        0.005039
  minimax_log_score       e1valj5j            0.058073        0.008472
======================================================================

Loading run 9u8o402o from JacobianODE/WMTask_identity_encoder_verification ...
loaded wmtask RNN model checkpoint 1
Loading cached wmtask hiddens from /orcd/data/ekmiller/001/eisenaj/ControlJacobians/WMTaskModels/WMSelectionTask__cue_time_0.1__response_time_0.25__enforce_fixation_False/BiologicalRNN__cue_time_0.1__learning_rate_0.0005__max_epochs_42__N1_64__N2_64__tau_0.05__dt_0.02__eig_lower_bound_0.1__init_mode_random/_jacobianode_cache/hiddens__all__epoch1__trials4096__seed42.pt
loaded wmtask RNN model checkpoint 41
Loading cached wmtask hiddens from /orcd/data/ekmiller/001/eisenaj/ControlJacobians/WMTaskModels/WMSelectionTask__cue_time_0.1__response_time_0.25__enforce_fixation_False/BiologicalRNN__cue_time_0.1__learning_rate_0.0005__max_epochs_42__N1_64__N2_64__tau_0.05__dt_0.02__eig_lower_bound_0.1__init_mode_random/_jacobianode_cache/hiddens__all__epoch41__trials4096__seed42.pt
Loading checkpoint epoch=34-step=4375.ckpt...
Loading checkpoint epoch=34-step=4375.ckpt...
Computing prediction windows ...
Windows: 3 — nMSE min=0.0705, median=0.0881, mean=0.0862, max=0.0998
Skipping 'encoder_decoder_jacobians' for conditioned model: vmap+jacrev OOMs on DirectSum + condition (TODO: rewrite without vmap or wait for index_copy_ batching rule).
Skipping 'tangent_spectrum' for conditioned model: compute_tangent_spectrum needs c plumbing through _encoder_jacobian_at's vmap+jacrev (TODO).
Computing gramians_overlay ...
  shapes: test_trajs=(818, 49, 128), test_trajs_full=(818, 49, 128); delay_offset=0 (= n_delays - 1)
  GT obs_blocks (raw 128-dim): [slice(0, 64, None), slice(64, 128, None)]
  c=[-1.0] vis→cog  reach (pred log_tr / gt log_tr): 4.329 / 3.569  [B*T=784, n_windows=1]
  c=[-1.0] cog→vis  reach (pred log_tr / gt log_tr): 1.707 / 1.526  [B*T=784, n_windows=1]
  c=[1.0] vis→cog  reach (pred log_tr / gt log_tr): 4.684 / 5.007  [B*T=784, n_windows=1]
  c=[1.0] cog→vis  reach (pred log_tr / gt log_tr): 2.440 / 2.796  [B*T=784, n_windows=1]
Computing gramians_metric_overlay ...
  shapes: test_trajs=(818, 49, 128), test_trajs_full=(818, 49, 128); delay_offset=0 (= n_delays - 1)
  GT obs_blocks (raw 128-dim): [slice(0, 64, None), slice(64, 128, None)]
  c=[-1.0] vis→cog  reach (pred log_tr / gt log_tr): 4.814 / 3.569  [B*T=784, n_windows=1]
  c=[-1.0] cog→vis  reach (pred log_tr / gt log_tr): 1.902 / 1.526  [B*T=784, n_windows=1]
  c=[1.0] vis→cog  reach (pred log_tr / gt log_tr): 5.129 / 5.007  [B*T=784, n_windows=1]
  c=[1.0] cog→vis  reach (pred log_tr / gt log_tr): 2.672 / 2.796  [B*T=784, n_windows=1]
Computing gramians_overlay_k20 ...
  shapes: test_trajs=(818, 49, 128), test_trajs_full=(818, 49, 128); delay_offset=0 (= n_delays - 1)
  GT obs_blocks (raw 128-dim): [slice(0, 64, None), slice(64, 128, None)]
  c=[-1.0] vis→cog  reach (pred log_tr / gt log_tr): 3.653 / 3.271  [B*T=640, n_windows=2]
  c=[-1.0] cog→vis  reach (pred log_tr / gt log_tr): 1.275 / 1.027  [B*T=640, n_windows=2]
  c=[1.0] vis→cog  reach (pred log_tr / gt log_tr): 4.523 / 4.754  [B*T=640, n_windows=2]
  c=[1.0] cog→vis  reach (pred log_tr / gt log_tr): 2.162 / 2.311  [B*T=640, n_windows=2]
Computing gramians_metric_overlay_k20 ...
  shapes: test_trajs=(818, 49, 128), test_trajs_full=(818, 49, 128); delay_offset=0 (= n_delays - 1)
  GT obs_blocks (raw 128-dim): [slice(0, 64, None), slice(64, 128, None)]
  c=[-1.0] vis→cog  reach (pred log_tr / gt log_tr): 4.114 / 3.271  [B*T=640, n_windows=2]
  c=[-1.0] cog→vis  reach (pred log_tr / gt log_tr): 1.464 / 1.027  [B*T=640, n_windows=2]
  c=[1.0] vis→cog  reach (pred log_tr / gt log_tr): 4.969 / 4.754  [B*T=640, n_windows=2]
  c=[1.0] cog→vis  reach (pred log_tr / gt log_tr): 2.385 / 2.311  [B*T=640, n_windows=2]
```

</details>
