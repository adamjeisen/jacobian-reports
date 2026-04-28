# Sweep Analysis: `wmtask_latent_additive_mse_p30_permidentity_dualckpt__lc_x_obsnoisescale_sweep__lrfix__stage_a`

**Project**: [WMTask_identity_encoder_verification](https://wandb.ai/JacobianODE/WMTask_identity_encoder_verification/groups/wmtask_latent_additive_mse_p30_permidentity_dualckpt__lc_x_obsnoisescale_sweep__lrfix__stage_a)  
**Launched**: 2026-04-28T20:00:18Z  
**Completed**: 2026-04-28T22:05:30Z  
**Outcome**: `complete_clean`  
**Git**: `latent-JacobianODE` @ `97053fe`  
**Expected runs**: 21

## Experiment Context

### `wmtask_latent_additive_mse_p30_permidentity_dualckpt__lc_x_obsnoisescale_sweep`

**Description**

WMTask fully-observed (N1=N2=64), latent JacobianODE with monolithic
additive coupling encoder, 128->128, final_perm_identity=true. 21-run
sweep over 7 LC × 3 obs_noise_scale. Split-mode loss. Dual checkpoint:
primary ES at patience=5, shadow-freeze at patience=2.

**Hypothesis**

Monolithic additive at this prediction horizon (p=30) shows the same
negative-Lyapunov suppression as DirectSum when trained for many epochs
(replication_v2 result). This sweep tests whether suppression is driven
by LC weight, obs_noise_scale, or develops uniformly across the
(LC, obs_noise) grid. Dual-ckpt isolates "ES patience caused it" from
a true late-training drift.

**Success criteria**

- All 21 cells train without divergence
- es2-best.ckpt and es5-best.ckpt both saved per cell
- Best val traj_loss (at either ckpt) within 2x of i73jwojr's 0.0105
- Lyapunov spectrum at es2-best vs es5-best directly comparable across LC × obs_noise

## Results

**Swept axes** (3): `data.postprocessing.generalized_variance`, `training.lightning.loop_closure_weight`, `training.lightning.obs_noise_scale`

**Chosen run** (by `best_traj_loss`): `1gm68s55` — traj_loss=0.00602, MASE=0.7526, R²=0.9931, LC loss=2.632, epoch=19.0

Swept-axis values at chosen run: `data.postprocessing.generalized_variance`=0.00954705 · `training.lightning.loop_closure_weight`=1.0e-05 · `training.lightning.obs_noise_scale`=0

**Runs analyzed**: 21 (expected 21)

### Per-run results

| run_idx | run_id | `data.postprocessing.generalized_variance` | `training.lightning.loop_closure_weight` | `training.lightning.obs_noise_scale` | best_traj_loss | best_MASE | R² | LC loss | epoch |
|---|---|---|---|---|---|---|---|---|---|
| 6 | `1gm68s55` | 0.00954705 | 1.0e-05 | 0 | 0.00602 | 0.7526 | 0.9931 | 2.632 | 19.0 |
| 3 | `usoqtjpp` | 0.00954705 | 1.0e-06 | 0 | 0.00623 | 0.7626 | 0.9929 | 6.267 | 18.0 |
| 2 | `oymqtr5n` | 0.00954705 | 0 | 0.05 | 0.00636 | 0.7649 | 0.9927 | 16.043 | 19.0 |
| 9 | `2ib1zx4c` | 0.00954705 | 1.0e-04 | 0 | 0.00642 | 0.7722 | 0.9926 | 0.635 | 19.0 |
| 0 | `64eey54d` | 0.00954705 | 0 | 0 | 0.00647 | 0.7742 | 0.9926 | 8.897 | 14.0 |
| 8 | `2pwhfrej` | 0.00954705 | 1.0e-05 | 0.05 | 0.00676 | 0.7876 | 0.9923 | 5.090 | 19.0 |
| 5 | `i0rcni41` | 0.00954705 | 1.0e-06 | 0.05 | 0.00686 | 0.7910 | 0.9922 | 11.835 | 19.0 |
| 11 | `gv65l6n9` | 0.00954705 | 1.0e-04 | 0.05 | 0.00701 | 0.8037 | 0.9920 | 1.233 | 19.0 |
| 12 | `tzakt7rh` | 0.00954705 | 0.001 | 0 | 0.00716 | 0.8112 | 0.9918 | 0.082 | 19.0 |
| 7 | `qur4r25e` | 0.00954705 | 1.0e-05 | 0.01 | 0.00760 | 0.8357 | 0.9913 | 4.087 | 17.0 |
| 4 | `rg7py753` | 0.00954705 | 1.0e-06 | 0.01 | 0.00796 | 0.8483 | 0.9909 | 7.768 | 10.0 |
| 1 | `tfj55paa` | 0.00954705 | 0 | 0.01 | 0.00801 | 0.8475 | 0.9908 | 12.020 | 15.0 |
| 10 | `i2yn5ska` | 0.00954705 | 1.0e-04 | 0.01 | 0.00816 | 0.8627 | 0.9906 | 0.877 | 17.0 |
| 15 | `305nurc0` | 0.00954705 | 0.01 | 0 | 0.00931 | 0.9083 | 0.9893 | 0.009 | 19.0 |
| 14 | `iav24a24` | 0.00954705 | 0.001 | 0.05 | 0.01109 | 0.9920 | 0.9873 | 0.234 | 17.0 |
| 13 | `qzq9nya8` | 0.00954705 | 0.001 | 0.01 | 0.01307 | 1.0837 | 0.9850 | 0.264 | 17.0 |
| 18 | `jq874isy` | 0.00954705 | 0.1 | 0 | 0.01335 | 1.0601 | 0.9847 | 0.001 | 19.0 |
| 17 | `32ih1qke` | 0.00954705 | 0.01 | 0.05 | 0.01773 | 1.2453 | 0.9797 | 0.059 | 19.0 |
| 20 | `9xyj2tyb` | 0.00954705 | 0.1 | 0.05 | 0.02228 | 1.3823 | 0.9745 | 0.003 | 19.0 |
| 16 | `ttcga8bb` | 0.00954705 | 0.01 | 0.01 | 0.02264 | 1.3991 | 0.9740 | 0.056 | 19.0 |
| 19 | `vjslj6vf` | 0.00954705 | 0.1 | 0.01 | 0.02451 | 1.4457 | 0.9719 | 0.005 | 19.0 |

### Best run per `obs_noise_scale`

| obs_noise_scale | Best LC weight | Best traj loss | MASE at best | R² | LC loss | epoch |
|---|---|---|---|---|---|---|
| 0.0 | 1.0e-05 | 0.00602 | 0.7526 | 0.9931 | 2.632 | 19.0 |
| 0.01 | 1.0e-05 | 0.00760 | 0.8357 | 0.9913 | 4.087 | 17.0 |
| 0.05 | 0.0e+00 | 0.00636 | 0.7649 | 0.9927 | 16.043 | 19.0 |

## Success-criteria verdicts (automated)

| Criterion | Verdict | Note |
|---|---|---|
| All 21 cells train without divergence | **Unknown** |  |
| es2-best.ckpt and es5-best.ckpt both saved per cell | **Unknown** |  |
| Best val traj_loss (at either ckpt) within 2x of i73jwojr's 0.0105 | **Unknown** |  |
| Lyapunov spectrum at es2-best vs es5-best directly comparable across LC × obs_noise | **Unknown** |  |

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

### tangent_spectrum

![tangent_spectrum](figures/tangent_spectrum.png)

### per_run_tangent_spectrum

![per_run_tangent_spectrum](figures/per_run_tangent_spectrum.png)

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
No run_id provided — selecting best run from group 'wmtask_latent_additive_mse_p30_permidentity_dualckpt__lc_x_obsnoisescale_sweep__lrfix__stage_a' ...
Found 21 total runs in JacobianODE/WMTask_identity_encoder_verification (group=wmtask_latent_additive_mse_p30_permidentity_dualckpt__lc_x_obsnoisescale_sweep__lrfix__stage_a)
All runs (state, loop_closure_weight, tangent_entropy_weight, kl_dyn_weight):
  gv65l6n9: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  i2yn5ska: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  1gm68s55: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  i0rcni41: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  2ib1zx4c: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  2pwhfrej: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  qur4r25e: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  tzakt7rh: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  rg7py753: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  305nurc0: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  qzq9nya8: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  iav24a24: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  32ih1qke: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  ttcga8bb: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  jq874isy: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  vjslj6vf: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  64eey54d: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  tfj55paa: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  9xyj2tyb: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  oymqtr5n: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  usoqtjpp: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0

slurm_timeout_min not found in any run config — falling back to 180 min
  Including gv65l6n9 (lc=0.0001): use_all_runs=True (state=finished)
  Including i2yn5ska (lc=0.0001): use_all_runs=True (state=finished)
  Including 1gm68s55 (lc=1e-05): use_all_runs=True (state=finished)
  Including i0rcni41 (lc=1e-06): use_all_runs=True (state=finished)
  Including 2ib1zx4c (lc=0.0001): use_all_runs=True (state=finished)
  Including 2pwhfrej (lc=1e-05): use_all_runs=True (state=finished)
  Including qur4r25e (lc=1e-05): use_all_runs=True (state=finished)
  Including tzakt7rh (lc=0.001): use_all_runs=True (state=finished)
  Including rg7py753 (lc=1e-06): use_all_runs=True (state=finished)
  Including 305nurc0 (lc=0.01): use_all_runs=True (state=finished)
  Including qzq9nya8 (lc=0.001): use_all_runs=True (state=finished)
  Including iav24a24 (lc=0.001): use_all_runs=True (state=finished)
  Including 32ih1qke (lc=0.01): use_all_runs=True (state=finished)
  Including ttcga8bb (lc=0.01): use_all_runs=True (state=finished)
  Including jq874isy (lc=0.1): use_all_runs=True (state=finished)
  Including vjslj6vf (lc=0.1): use_all_runs=True (state=finished)
  Including 64eey54d (lc=0.0): use_all_runs=True (state=finished)
  Including tfj55paa (lc=0.0): use_all_runs=True (state=finished)
  Including 9xyj2tyb (lc=0.1): use_all_runs=True (state=finished)
  Including oymqtr5n (lc=0.0): use_all_runs=True (state=finished)
  Including usoqtjpp (lc=1e-06): use_all_runs=True (state=finished)
Found 21 effectively-done sweep runs:
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=64eey54d
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=oymqtr5n
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=tfj55paa
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=i0rcni41
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=rg7py753
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=usoqtjpp
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=1gm68s55
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=2pwhfrej
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=qur4r25e
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=2ib1zx4c
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=gv65l6n9
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=i2yn5ska
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=iav24a24
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=qzq9nya8
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=tzakt7rh
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=305nurc0
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=32ih1qke
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=ttcga8bb
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=9xyj2tyb
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=jq874isy
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=vjslj6vf
loaded wmtask RNN model checkpoint 41
Loading cached wmtask hiddens from /orcd/data/ekmiller/001/eisenaj/ControlJacobians/WMTaskModels/WMSelectionTask__cue_time_0.1__response_time_0.25__enforce_fixation_False/BiologicalRNN__cue_time_0.1__learning_rate_0.0005__max_epochs_42__N1_64__N2_64__tau_0.05__dt_0.02__eig_lower_bound_0.1__init_mode_random/_jacobianode_cache/hiddens__all__epoch41__trials4096__seed42.pt
n_dims=128, n_latent=128, n_dyn=128, dt=0.0200
  run=64eey54d: DiagnosticMetrics(one_step_mase=0.6017956733703613, loop_closure_loss=8.897263526916504, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0064690192230045795) (from W&B history)
  run=oymqtr5n: DiagnosticMetrics(one_step_mase=0.5941788554191589, loop_closure_loss=16.043136596679688, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.006358050275593996) (from W&B history)
  run=tfj55paa: DiagnosticMetrics(one_step_mase=0.6108756065368652, loop_closure_loss=12.020463943481445, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.008005967363715172) (from W&B history)
  run=i0rcni41: DiagnosticMetrics(one_step_mase=0.5947271585464478, loop_closure_loss=11.834547996520996, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.006859329994767904) (from W&B history)
  run=rg7py753: DiagnosticMetrics(one_step_mase=0.6073485016822815, loop_closure_loss=7.767510890960693, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.007963992655277252) (from W&B history)
  run=usoqtjpp: DiagnosticMetrics(one_step_mase=0.6014305949211121, loop_closure_loss=6.266595840454102, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.006231546401977539) (from W&B history)
  run=1gm68s55: DiagnosticMetrics(one_step_mase=0.6029976606369019, loop_closure_loss=2.6324310302734375, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0060228388756513596) (from W&B history)
  run=2pwhfrej: DiagnosticMetrics(one_step_mase=0.5947934985160828, loop_closure_loss=5.090095043182373, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0067596822045743465) (from W&B history)
  run=qur4r25e: DiagnosticMetrics(one_step_mase=0.6116406917572021, loop_closure_loss=4.0867719650268555, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.007604192476719618) (from W&B history)
  run=2ib1zx4c: DiagnosticMetrics(one_step_mase=0.6046843528747559, loop_closure_loss=0.6353193521499634, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.006418250966817141) (from W&B history)
  run=gv65l6n9: DiagnosticMetrics(one_step_mase=0.5987222790718079, loop_closure_loss=1.2333767414093018, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.007005565334111452) (from W&B history)
  run=i2yn5ska: DiagnosticMetrics(one_step_mase=0.6170467138290405, loop_closure_loss=0.8773674964904785, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.008161334320902824) (from W&B history)
  run=iav24a24: DiagnosticMetrics(one_step_mase=0.6203426122665405, loop_closure_loss=0.23371930420398712, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.011090857908129692) (from W&B history)
  run=qzq9nya8: DiagnosticMetrics(one_step_mase=0.6349087357521057, loop_closure_loss=0.2637613117694855, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.013065677136182785) (from W&B history)
  run=tzakt7rh: DiagnosticMetrics(one_step_mase=0.6069064736366272, loop_closure_loss=0.08185486495494843, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0071599907241761684) (from W&B history)
  run=305nurc0: DiagnosticMetrics(one_step_mase=0.6137085556983948, loop_closure_loss=0.009318946860730648, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.009314497001469135) (from W&B history)
  run=32ih1qke: DiagnosticMetrics(one_step_mase=0.6376466155052185, loop_closure_loss=0.059059012681245804, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.017726611346006393) (from W&B history)
  run=ttcga8bb: DiagnosticMetrics(one_step_mase=0.6489613652229309, loop_closure_loss=0.05636737868189812, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.022636933252215385) (from W&B history)
  run=9xyj2tyb: DiagnosticMetrics(one_step_mase=0.6462177634239197, loop_closure_loss=0.0032358868047595024, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.02227659523487091) (from W&B history)
  run=jq874isy: DiagnosticMetrics(one_step_mase=0.6211221218109131, loop_closure_loss=0.0008295265724882483, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.013351824134588242) (from W&B history)
  run=vjslj6vf: DiagnosticMetrics(one_step_mase=0.6498464941978455, loop_closure_loss=0.0047307549975812435, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.024509182199835777) (from W&B history)

Ranking method:           best_traj_loss
Best run ID:              1gm68s55
Best loop_closure_weight: 1e-05
Best tangent_entropy_weight: 0.0
Best kl_dyn_weight:       0.0
Best traj loss:           0.006023
Criteria applied: ['C1', 'C2', 'C3']
Surviving: 18 / 21
Auto-selected run_id: 1gm68s55

======================================================================
PARETO FRONTIER RUNS (5 runs)
======================================================================
  Run ID               LC Loss   Traj Val Loss
  ------------  --------------  --------------
  jq874isy            0.000830        0.013352
  305nurc0            0.009319        0.009314
  tzakt7rh            0.081855        0.007160
  2ib1zx4c            0.635319        0.006418
  1gm68s55            2.632431        0.006023 <-- selected

======================================================================
RANKING METHOD COMPARISON (over 18 survivors)
======================================================================
  Method                  Run ID               LC Loss   Traj Val Loss
  ----------------------  ------------  --------------  --------------
  best_traj_loss          1gm68s55            2.632431        0.006023 <-- active
  pareto_knee             tzakt7rh            0.081855        0.007160
  geo_rank                1gm68s55            2.632431        0.006023
  minimax_rank            tzakt7rh            0.081855        0.007160
  geo_log_score           1gm68s55            2.632431        0.006023
  minimax_log_score       305nurc0            0.009319        0.009314
======================================================================

Loading run 1gm68s55 from JacobianODE/WMTask_identity_encoder_verification ...
loaded wmtask RNN model checkpoint 41
Loading cached wmtask hiddens from /orcd/data/ekmiller/001/eisenaj/ControlJacobians/WMTaskModels/WMSelectionTask__cue_time_0.1__response_time_0.25__enforce_fixation_False/BiologicalRNN__cue_time_0.1__learning_rate_0.0005__max_epochs_42__N1_64__N2_64__tau_0.05__dt_0.02__eig_lower_bound_0.1__init_mode_random/_jacobianode_cache/hiddens__all__epoch41__trials4096__seed42.pt
Loading checkpoint epoch=19-step=2500.ckpt...
Train dataset shape: torch.Size([11468, 45, 128])
Validation dataset shape: torch.Size([3280, 45, 128])
Test dataset shape: torch.Size([1636, 45, 128])
Train trajectories dataset shape: torch.Size([2867, 49, 128])
Validation trajectories dataset shape: torch.Size([820, 49, 128])
Test trajectories dataset shape: torch.Size([409, 49, 128])
Loading checkpoint epoch=19-step=2500.ckpt...
Computing reconstruction ...
Computing MASE ...
Teacher-forced MASE: 0.6049
Free-running MASE:   0.7483
Computing latent utilization ...
Entropy-based utilization: 0.894
Computing Lyapunov exponents ...
  Computing full-trajectory Lyapunov (409 test trajs, T=49) ...
Predicted Lyapunov exponents (batch+burn-in, 128 windowed trajs):
  λ_1 = -0.3156 ± 0.1289
  λ_2 = -0.4894 ± 0.1608
  λ_3 = -0.6130 ± 0.1305
  λ_4 = -0.9516 ± 0.1366
  λ_5 = -1.4111 ± 0.3679
  λ_6 = -1.6059 ± 0.3525
  λ_7 = -2.3875 ± 0.2692
  λ_8 = -2.5734 ± 0.2763
  λ_9 = -3.3313 ± 0.2089
  λ_10 = -3.6444 ± 0.1602
  λ_11 = -3.7425 ± 0.1600
  λ_12 = -3.8348 ± 0.1728
  λ_13 = -3.9147 ± 0.2043
  λ_14 = -4.0001 ± 0.2039
  λ_15 = -4.1076 ± 0.2159
  λ_16 = -4.2306 ± 0.1863
  λ_17 = -4.2938 ± 0.1757
  λ_18 = -4.3704 ± 0.1845
  λ_19 = -4.4503 ± 0.2021
  λ_20 = -4.5093 ± 0.2158
  λ_21 = -4.5511 ± 0.2288
  λ_22 = -4.5819 ± 0.2344
  λ_23 = -4.6101 ± 0.2324
  λ_24 = -4.6585 ± 0.2272
  λ_25 = -4.7232 ± 0.2153
  λ_26 = -4.7855 ± 0.2302
  λ_27 = -4.8350 ± 0.2384
  λ_28 = -4.8789 ± 0.2349
  λ_29 = -4.9154 ± 0.2403
  λ_30 = -4.9532 ± 0.2378
  λ_31 = -5.0140 ± 0.2379
  λ_32 = -5.0926 ± 0.2361
  λ_33 = -5.1706 ± 0.2460
  λ_34 = -5.2513 ± 0.2650
  λ_35 = -5.3497 ± 0.2610
  λ_36 = -5.4099 ± 0.2594
  λ_37 = -5.4586 ± 0.2687
  λ_38 = -5.4866 ± 0.2757
  λ_39 = -5.5358 ± 0.2975
  λ_40 = -5.5895 ± 0.3024
  λ_41 = -5.6365 ± 0.2981
  λ_42 = -5.6744 ± 0.2914
  λ_43 = -5.7146 ± 0.3084
  λ_44 = -5.7496 ± 0.3185
  λ_45 = -5.7874 ± 0.3274
  λ_46 = -5.8244 ± 0.3294
  λ_47 = -5.8671 ± 0.3381
  λ_48 = -5.8973 ± 0.3405
  λ_49 = -5.9348 ± 0.3486
  λ_50 = -6.0107 ± 0.3442
  λ_51 = -6.0569 ± 0.3456
  λ_52 = -6.1024 ± 0.3590
  λ_53 = -6.1472 ± 0.3596
  λ_54 = -6.1937 ± 0.3586
  λ_55 = -6.2411 ± 0.3587
  λ_56 = -6.3041 ± 0.3601
  λ_57 = -6.3626 ± 0.3584
  λ_58 = -6.4179 ± 0.3505
  λ_59 = -6.4614 ± 0.3592
  λ_60 = -6.5094 ± 0.3685
  λ_61 = -6.5595 ± 0.3667
  λ_62 = -6.6060 ± 0.3787
  λ_63 = -6.6497 ± 0.3822
  λ_64 = -6.7036 ± 0.3938
  λ_65 = -6.7567 ± 0.4018
  λ_66 = -6.8077 ± 0.3909
  λ_67 = -6.8694 ± 0.3881
  λ_68 = -6.9800 ± 0.3900
  λ_69 = -7.1229 ± 0.4122
  λ_70 = -7.2025 ± 0.4026
  λ_71 = -7.2581 ± 0.3986
  λ_72 = -7.3105 ± 0.4030
  λ_73 = -7.3627 ± 0.4056
  λ_74 = -7.4403 ± 0.4096
  λ_75 = -7.5842 ± 0.4346
  λ_76 = -7.6972 ± 0.4489
  λ_77 = -7.8395 ± 0.4806
  λ_78 = -7.9437 ± 0.4765
  λ_79 = -8.0973 ± 0.4755
  λ_80 = -8.2021 ± 0.4709
  λ_81 = -8.2882 ± 0.4541
  λ_82 = -8.3830 ± 0.4601
  λ_83 = -8.5043 ± 0.4778
  λ_84 = -8.6266 ± 0.4742
  λ_85 = -8.7283 ± 0.4908
  λ_86 = -8.8049 ± 0.5000
  λ_87 = -8.8588 ± 0.5010
  λ_88 = -8.9521 ± 0.5093
  λ_89 = -9.0428 ± 0.5345
  λ_90 = -9.1912 ± 0.5172
  λ_91 = -9.2845 ± 0.5234
  λ_92 = -9.3419 ± 0.5277
  λ_93 = -9.4224 ± 0.5378
  λ_94 = -9.7425 ± 0.5726
  λ_95 = -9.8788 ± 0.5982
  λ_96 = -10.0004 ± 0.5926
  λ_97 = -10.1136 ± 0.6063
  λ_98 = -10.2369 ± 0.6207
  λ_99 = -10.2951 ± 0.6155
  λ_100 = -10.4252 ± 0.6254
  λ_101 = -10.5333 ± 0.6527
  λ_102 = -10.7515 ± 0.6341
  λ_103 = -10.8737 ± 0.6122
  λ_104 = -11.0342 ± 0.6292
  λ_105 = -11.1552 ± 0.6499
  λ_106 = -11.2338 ± 0.6488
  λ_107 = -11.5100 ± 0.6965
  λ_108 = -11.7375 ± 0.6670
  λ_109 = -11.8841 ± 0.6799
  λ_110 = -11.9742 ± 0.6912
  λ_111 = -12.0458 ± 0.6846
  λ_112 = -12.1737 ± 0.7018
  λ_113 = -12.2982 ± 0.6981
  λ_114 = -12.5227 ± 0.7037
  λ_115 = -12.6655 ± 0.7220
  λ_116 = -12.7476 ± 0.7361
  λ_117 = -12.8260 ± 0.7640
  λ_118 = -12.9333 ± 0.7494
  λ_119 = -13.1042 ± 0.7450
  λ_120 = -13.2419 ± 0.7672
  λ_121 = -13.3420 ± 0.7749
  λ_122 = -13.5049 ± 0.7673
  λ_123 = -14.0508 ± 0.8290
  λ_124 = -14.4827 ± 0.8214
  λ_125 = -14.5494 ± 0.8229
  λ_126 = -15.0538 ± 0.8169
  λ_127 = -15.8795 ± 0.9602
  λ_128 = -16.0668 ± 0.9120
Predicted Lyapunov exponents (full-length, 409 test trajs):
  λ_1 = -1.3197 ± 0.3682
  λ_2 = -1.6049 ± 0.3590
  λ_3 = -2.2161 ± 0.3586
  λ_4 = -2.9552 ± 0.3022
  λ_5 = -3.3184 ± 0.1922
  λ_6 = -3.6147 ± 0.2538
  λ_7 = -3.9050 ± 0.2840
  λ_8 = -4.1213 ± 0.2868
  λ_9 = -4.3571 ± 0.3171
  λ_10 = -4.6665 ± 0.2547
  λ_11 = -4.9109 ± 0.1518
  λ_12 = -5.0626 ± 0.1502
  λ_13 = -5.1871 ± 0.2032
  λ_14 = -5.2931 ± 0.2266
  λ_15 = -5.4211 ± 0.2092
  λ_16 = -5.5392 ± 0.1770
  λ_17 = -5.6110 ± 0.1763
  λ_18 = -5.7110 ± 0.1820
  λ_19 = -5.8482 ± 0.1663
  λ_20 = -6.0135 ± 0.1576
  λ_21 = -6.1528 ± 0.1977
  λ_22 = -6.3002 ± 0.1969
  λ_23 = -6.4501 ± 0.1700
  λ_24 = -6.6063 ± 0.1834
  λ_25 = -6.6999 ± 0.2007
  λ_26 = -6.7881 ± 0.2026
  λ_27 = -6.8506 ± 0.2016
  λ_28 = -6.9120 ± 0.1902
  λ_29 = -6.9691 ± 0.1908
  λ_30 = -7.0709 ± 0.2135
  λ_31 = -7.1983 ± 0.2269
  λ_32 = -7.3112 ± 0.2352
  λ_33 = -7.4258 ± 0.2621
  λ_34 = -7.5383 ± 0.2818
  λ_35 = -7.6253 ± 0.2790
  λ_36 = -7.7116 ± 0.2553
  λ_37 = -7.7622 ± 0.2539
  λ_38 = -7.8033 ± 0.2498
  λ_39 = -7.8390 ± 0.2485
  λ_40 = -7.8790 ± 0.2428
  λ_41 = -7.9149 ± 0.2409
  λ_42 = -7.9519 ± 0.2349
  λ_43 = -7.9857 ± 0.2407
  λ_44 = -8.0183 ± 0.2459
  λ_45 = -8.0485 ± 0.2511
  λ_46 = -8.0762 ± 0.2555
  λ_47 = -8.1010 ± 0.2583
  λ_48 = -8.1338 ± 0.2641
  λ_49 = -8.1568 ± 0.2682
  λ_50 = -8.1935 ± 0.2756
  λ_51 = -8.2252 ± 0.2804
  λ_52 = -8.2650 ± 0.2933
  λ_53 = -8.3042 ± 0.2985
  λ_54 = -8.3398 ± 0.3015
  λ_55 = -8.3771 ± 0.3016
  λ_56 = -8.4135 ± 0.3028
  λ_57 = -8.4494 ± 0.3123
  λ_58 = -8.4944 ± 0.3146
  λ_59 = -8.5516 ± 0.3310
  λ_60 = -8.6017 ± 0.3255
  λ_61 = -8.6441 ± 0.3213
  λ_62 = -8.6845 ± 0.3203
  λ_63 = -8.7280 ± 0.3126
  λ_64 = -8.7731 ± 0.3078
  λ_65 = -8.8120 ± 0.3046
  λ_66 = -8.8507 ± 0.3043
  λ_67 = -8.8914 ± 0.3176
  λ_68 = -8.9255 ± 0.3219
  λ_69 = -8.9591 ± 0.3217
  λ_70 = -8.9956 ± 0.3197
  λ_71 = -9.0322 ± 0.3202
  λ_72 = -9.0750 ± 0.3295
  λ_73 = -9.1197 ± 0.3206
  λ_74 = -9.1526 ± 0.3202
  λ_75 = -9.1923 ± 0.3201
  λ_76 = -9.2344 ± 0.3192
  λ_77 = -9.2873 ± 0.3312
  λ_78 = -9.3408 ± 0.3453
  λ_79 = -9.4011 ± 0.3521
  λ_80 = -9.4690 ± 0.3745
  λ_81 = -9.5326 ± 0.3891
  λ_82 = -9.6006 ± 0.3985
  λ_83 = -9.6562 ± 0.3990
  λ_84 = -9.7175 ± 0.4001
  λ_85 = -9.7679 ± 0.3994
  λ_86 = -9.8154 ± 0.3953
  λ_87 = -9.8622 ± 0.4063
  λ_88 = -9.9111 ± 0.4022
  λ_89 = -9.9681 ± 0.4052
  λ_90 = -10.0197 ± 0.4041
  λ_91 = -10.0802 ± 0.4083
  λ_92 = -10.1633 ± 0.4357
  λ_93 = -10.2628 ± 0.4605
  λ_94 = -10.3452 ± 0.4852
  λ_95 = -10.4499 ± 0.4798
  λ_96 = -10.6081 ± 0.4582
  λ_97 = -10.7534 ± 0.4612
  λ_98 = -10.9253 ± 0.4694
  λ_99 = -11.0648 ± 0.4688
  λ_100 = -11.2119 ± 0.4817
  λ_101 = -11.3292 ± 0.4823
  λ_102 = -11.4460 ± 0.4960
  λ_103 = -11.5495 ± 0.5126
  λ_104 = -11.6820 ± 0.5265
  λ_105 = -11.8007 ± 0.5413
  λ_106 = -11.8975 ± 0.5428
  λ_107 = -12.0200 ± 0.5512
  λ_108 = -12.1484 ± 0.5410
  λ_109 = -12.2331 ± 0.5423
  λ_110 = -12.3815 ± 0.5789
  λ_111 = -12.4692 ± 0.5703
  λ_112 = -12.6264 ± 0.5565
  λ_113 = -12.7667 ± 0.5361
  λ_114 = -12.8674 ± 0.5239
  λ_115 = -12.9471 ± 0.5226
  λ_116 = -13.0393 ± 0.5618
  λ_117 = -13.1257 ± 0.5780
  λ_118 = -13.2378 ± 0.5704
  λ_119 = -13.3550 ± 0.6066
  λ_120 = -13.4945 ± 0.6316
  λ_121 = -13.6485 ± 0.6281
  λ_122 = -13.8711 ± 0.6236
  λ_123 = -14.3419 ± 0.6770
  λ_124 = -14.6888 ± 0.7662
  λ_125 = -14.8827 ± 0.7772
  λ_126 = -15.4474 ± 0.6986
  λ_127 = -15.7897 ± 0.6894
  λ_128 = -16.1365 ± 0.7115
Empirical Lyapunov exponents (mean ± std):
  λ_1 = -0.6836 ± 0.4470
  λ_2 = -1.2860 ± 0.4717
  λ_3 = -1.8796 ± 0.4983
  λ_4 = -2.5140 ± 0.3383
  λ_5 = -2.9329 ± 0.4143
  λ_6 = -3.2778 ± 0.5212
  λ_7 = -3.7948 ± 0.4446
  λ_8 = -4.2351 ± 0.4668
  λ_9 = -4.6672 ± 0.4583
  λ_10 = -5.0458 ± 0.4531
  λ_11 = -5.3534 ± 0.4185
  λ_12 = -5.7506 ± 0.4346
  λ_13 = -6.2355 ± 0.3491
  λ_14 = -6.7043 ± 0.5036
  λ_15 = -7.0414 ± 0.4554
  λ_16 = -7.3719 ± 0.4648
  λ_17 = -7.6725 ± 0.4415
  λ_18 = -7.9667 ± 0.4130
  λ_19 = -8.2155 ± 0.4290
  λ_20 = -8.4474 ± 0.4083
  λ_21 = -8.6400 ± 0.3667
  λ_22 = -8.8546 ± 0.3395
  λ_23 = -9.0471 ± 0.3366
  λ_24 = -9.3642 ± 0.2863
  λ_25 = -9.5403 ± 0.3009
  λ_26 = -9.7473 ± 0.3189
  λ_27 = -9.9780 ± 0.3514
  λ_28 = -10.2177 ± 0.4331
  λ_29 = -10.4760 ± 0.4197
  λ_30 = -10.6968 ± 0.4504
  λ_31 = -11.0538 ± 0.5425
  λ_32 = -11.3182 ± 0.5459
  λ_33 = -11.7806 ± 0.6071
  λ_34 = -12.3300 ± 0.5244
  λ_35 = -12.6464 ± 0.5369
  λ_36 = -13.0198 ± 0.6314
  λ_37 = -13.3795 ± 0.7073
  λ_38 = -13.7502 ± 0.7660
  λ_39 = -14.0682 ± 0.7579
  λ_40 = -14.3279 ± 0.7619
  λ_41 = -14.6206 ± 0.8778
  λ_42 = -15.0213 ± 0.8116
  λ_43 = -15.3487 ± 0.8488
  λ_44 = -15.7679 ± 0.8512
  λ_45 = -16.3535 ± 0.8105
  λ_46 = -17.2371 ± 0.8420
  λ_47 = -18.0172 ± 0.6551
  λ_48 = -18.7348 ± 0.4352
  λ_49 = -19.1920 ± 0.4388
  λ_50 = -19.6032 ± 0.3862
  λ_51 = -19.9849 ± 0.4171
  λ_52 = -20.2854 ± 0.3677
  λ_53 = -20.7129 ± 0.4088
  λ_54 = -21.2293 ± 0.4493
  λ_55 = -22.1518 ± 0.3711
  λ_56 = -22.5100 ± 0.3571
  λ_57 = -22.8264 ± 0.3133
  λ_58 = -23.1069 ± 0.3495
  λ_59 = -23.3589 ± 0.3337
  λ_60 = -23.6276 ± 0.2926
  λ_61 = -23.8603 ± 0.3155
  λ_62 = -24.0618 ± 0.3005
  λ_63 = -24.2152 ± 0.3129
  λ_64 = -24.3396 ± 0.3136
  λ_65 = -24.4895 ± 0.3210
  λ_66 = -24.6115 ± 0.3197
  λ_67 = -24.7359 ± 0.3269
  λ_68 = -24.8561 ± 0.3392
  λ_69 = -24.9753 ± 0.3426
  λ_70 = -25.1117 ± 0.3497
  λ_71 = -25.2226 ± 0.3734
  λ_72 = -25.3357 ± 0.4009
  λ_73 = -25.4353 ± 0.4172
  λ_74 = -25.5439 ± 0.4046
  λ_75 = -25.6332 ± 0.4116
  λ_76 = -25.7832 ± 0.4585
  λ_77 = -25.9142 ± 0.4799
  λ_78 = -26.0449 ± 0.4990
  λ_79 = -26.1810 ± 0.5037
  λ_80 = -26.3617 ± 0.4899
  λ_81 = -26.5171 ± 0.4864
  λ_82 = -26.6628 ± 0.4753
  λ_83 = -26.8617 ± 0.4795
  λ_84 = -27.0282 ± 0.5036
  λ_85 = -27.2607 ± 0.4846
  λ_86 = -27.4529 ± 0.4854
  λ_87 = -27.5733 ± 0.4725
  λ_88 = -27.7187 ± 0.4967
  λ_89 = -27.8617 ± 0.5003
  λ_90 = -27.9895 ± 0.4903
  λ_91 = -28.1274 ± 0.4923
  λ_92 = -28.2824 ± 0.4913
  λ_93 = -28.4072 ± 0.4914
  λ_94 = -28.5255 ± 0.4695
  λ_95 = -28.6477 ± 0.4521
  λ_96 = -28.7842 ± 0.4453
  λ_97 = -28.9001 ± 0.4403
  λ_98 = -29.0308 ± 0.4330
  λ_99 = -29.1511 ± 0.4295
  λ_100 = -29.2954 ± 0.4247
  λ_101 = -29.4503 ± 0.4217
  λ_102 = -29.5753 ± 0.4321
  λ_103 = -29.6956 ± 0.4539
  λ_104 = -29.8547 ± 0.4485
  λ_105 = -29.9992 ± 0.4490
  λ_106 = -30.1172 ± 0.4378
  λ_107 = -30.2615 ± 0.4426
  λ_108 = -30.4062 ± 0.3980
  λ_109 = -30.5554 ± 0.4003
  λ_110 = -30.7032 ± 0.3985
  λ_111 = -30.8743 ± 0.4228
  λ_112 = -31.0109 ± 0.4336
  λ_113 = -31.1492 ± 0.4292
  λ_114 = -31.3023 ± 0.3981
  λ_115 = -31.4396 ± 0.4097
  λ_116 = -31.5685 ± 0.3902
  λ_117 = -31.7302 ± 0.3526
  λ_118 = -31.8705 ± 0.3050
  λ_119 = -31.9948 ± 0.3040
  λ_120 = -32.0998 ± 0.2813
  λ_121 = -32.2401 ± 0.2718
  λ_122 = -32.3221 ± 0.2617
  λ_123 = -32.4282 ± 0.2531
  λ_124 = -32.5858 ± 0.2272
  λ_125 = -32.8296 ± 0.2629
  λ_126 = -33.0206 ± 0.2244
  λ_127 = -33.2132 ± 0.2160
  λ_128 = -33.4614 ± 0.3541
Mean KY dim (predicted): 0.000 ± 0.000
Mean KY dim (empirical): 0.042 ± 0.210
Mean KY dim (burn-in):   0.000 ± 0.000
Computing prediction windows ...
Windows: 3 — nMSE min=0.0126, median=0.0144, mean=0.0163, max=0.0219
Computing long-trajectory free-running rollouts ...
Computing encoder/decoder Jacobians ...
encoder_jacobian: (128, 128, 128)
decoder_jacobian: (128, 128, 128)
Computing amplification loss ...
Amplification loss — True state: 0.004748
Amplification loss — Latent:     0.005101
Computing tangent space spectrum ...
```

</details>
