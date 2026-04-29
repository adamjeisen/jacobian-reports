# Sweep Analysis: `wmtask_latent_additive_p30_nearid_tf__lc_x_obsnoisescale_sweep_20260429T163244Z__stage_b_v2`

**Project**: [WMTask_identity_encoder_verification](https://wandb.ai/JacobianODE/WMTask_identity_encoder_verification/groups/wmtask_latent_additive_p30_nearid_tf__lc_x_obsnoisescale_sweep_20260429T163244Z__stage_b_v2)  
**Launched**: 2026-04-29T20:15:18Z  
**Completed**: 2026-04-29T23:10:28Z  
**Outcome**: `complete_clean`  
**Git**: `latent-JacobianODE` @ `547e96e`  
**Expected runs**: 10

## Experiment Context

### `wmtask_latent_additive_p30_nearid_tf__lc_x_obsnoisescale_sweep`

**Description**

WMTask fully-observed (N1=N2=64), latent JacobianODE, monolithic
CouplingEncoder (additive coupling, 8 layers, hidden_dim=128),
near_identity_std=1e-3, final_perm_identity=true. 21-cell sweep
over 7 LC x 3 obs_noise_scale. TF-coupled LR schedule (k_scale=1):
LR follows teacher-forcing alpha annealing instead of an arbitrary
cosine_T_max. Two-stage protocol with dual-checkpoint (primary ES
patience=5, shadow-freeze patience=2).

**Hypothesis**

The TF-coupled LR schedule auto-adapts the high-LR-then-low-LR shape
that orig (1266f49) accidentally got right via cosine_T_max=20. Mean
effective LR over the high-LR phase ~5e-5 (matches orig's 5.35e-5)
without an arbitrary epoch-count hyperparameter; the schedule just
follows the model's actual Jacobian-stability progression. Combined
with near-identity init (gradient flow on conditioner hidden layers
from step 1, vs strict zero-init's one-step block), this is the
"principled" fully-clean recipe to validate against orig and against
Lorenz 3->3.

**Success criteria**

- All 21 cells train without divergence
- es2-best.ckpt and es5-best.ckpt both saved per cell
- Best val traj_loss within ~10% of orig __stage_a's 0.00494
- Lyapunov spectrum NOT compressed in Stage B vs Stage A
- Result shape is consistent with the matched Lorenz 3->3 sweep (init effect, LC dependence)

## Results

**Swept axes** (4): `data.postprocessing.generalized_variance`, `training.ckpt_path`, `training.lightning.loop_closure_weight`, `training.lightning.obs_noise_scale`

**Chosen run** (by `best_traj_loss`): `slpqn0gt` — traj_loss=0.00406, MASE=0.6301, R²=0.9953, LC loss=26.886, epoch=56.0

Swept-axis values at chosen run: `data.postprocessing.generalized_variance`=0.00954705 · `training.ckpt_path`=/orcd/data/ekmiller/001/eisenaj/JacobianODE/sweeps/two_stage_ckpts/wmtask_latent_additive_p30_nearid_tf__lc_x_obsnoisescale_sweep_20260429T163244Z__stage_a/b2b02557d16c691e/last.ckpt · `training.lightning.loop_closure_weight`=0 · `training.lightning.obs_noise_scale`=0.05

**Runs analyzed**: 10 (expected 10)

### Per-run results

| run_idx | run_id | `data.postprocessing.generalized_variance` | `training.ckpt_path` | `training.lightning.loop_closure_weight` | `training.lightning.obs_noise_scale` | best_traj_loss | best_MASE | R² | LC loss | epoch |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | `slpqn0gt` | 0.00954705 | /orcd/data/ekmiller/001/eisenaj/JacobianODE/sweeps/two_stage_ckpts/wmtask_latent_additive_p30_nearid_tf__lc_x_obsnoisescale_sweep_20260429T163244Z__stage_a/b2b02557d16c691e/last.ckpt | 0 | 0.05 | 0.00406 | 0.6301 | 0.9953 | 26.886 | 56.0 |
| 5 | `wrpnn427` | 0.00954705 | /orcd/data/ekmiller/001/eisenaj/JacobianODE/sweeps/two_stage_ckpts/wmtask_latent_additive_p30_nearid_tf__lc_x_obsnoisescale_sweep_20260429T163244Z__stage_a/e2d851cdaeb66b9f/last.ckpt | 1.0e-05 | 0.05 | 0.00411 | 0.6335 | 0.9953 | 8.038 | 51.0 |
| 3 | `xbofsisv` | 0.00954705 | /orcd/data/ekmiller/001/eisenaj/JacobianODE/sweeps/two_stage_ckpts/wmtask_latent_additive_p30_nearid_tf__lc_x_obsnoisescale_sweep_20260429T163244Z__stage_a/f9a20657e9f3ccd2/last.ckpt | 1.0e-06 | 0 | 0.00436 | 0.6507 | 0.9950 | 9.980 | 45.0 |
| 2 | `a45zk5sh` | 0.00954705 | /orcd/data/ekmiller/001/eisenaj/JacobianODE/sweeps/two_stage_ckpts/wmtask_latent_additive_p30_nearid_tf__lc_x_obsnoisescale_sweep_20260429T163244Z__stage_a/a08083641f8d8494/last.ckpt | 0 | 0 | 0.00437 | 0.6512 | 0.9950 | 14.050 | 45.0 |
| 4 | `fsnytm0o` | 0.00954705 | /orcd/data/ekmiller/001/eisenaj/JacobianODE/sweeps/two_stage_ckpts/wmtask_latent_additive_p30_nearid_tf__lc_x_obsnoisescale_sweep_20260429T163244Z__stage_a/d7a3ea34a2d5401c/last.ckpt | 1.0e-05 | 0 | 0.00439 | 0.6525 | 0.9950 | 4.224 | 45.0 |
| 6 | `ees17qgj` | 0.00954705 | /orcd/data/ekmiller/001/eisenaj/JacobianODE/sweeps/two_stage_ckpts/wmtask_latent_additive_p30_nearid_tf__lc_x_obsnoisescale_sweep_20260429T163244Z__stage_a/a4e7a36e10c4eac1/last.ckpt | 1.0e-04 | 0 | 0.00458 | 0.6646 | 0.9947 | 1.108 | 48.0 |
| 9 | `bgl6aks1` | 0.00954705 | /orcd/data/ekmiller/001/eisenaj/JacobianODE/sweeps/two_stage_ckpts/wmtask_latent_additive_p30_nearid_tf__lc_x_obsnoisescale_sweep_20260429T163244Z__stage_a/54426b7f2a8f1f3a/last.ckpt | 0 | 0.01 | 0.00459 | 0.6666 | 0.9947 | 18.452 | 45.0 |
| 1 | `sgqoux4c` | 0.00954705 | /orcd/data/ekmiller/001/eisenaj/JacobianODE/sweeps/two_stage_ckpts/wmtask_latent_additive_p30_nearid_tf__lc_x_obsnoisescale_sweep_20260429T163244Z__stage_a/536feb1e214ff933/last.ckpt | 1.0e-06 | 0.05 | 0.00459 | 0.6631 | 0.9947 | 15.847 | 28.0 |
| 8 | `0b5de702` | 0.00954705 | /orcd/data/ekmiller/001/eisenaj/JacobianODE/sweeps/two_stage_ckpts/wmtask_latent_additive_p30_nearid_tf__lc_x_obsnoisescale_sweep_20260429T163244Z__stage_a/a0d0954aa2aebc4e/last.ckpt | 1.0e-06 | 0.01 | 0.00460 | 0.6671 | 0.9947 | 13.521 | 45.0 |
| 7 | `grvw9w8o` | 0.00954705 | /orcd/data/ekmiller/001/eisenaj/JacobianODE/sweeps/two_stage_ckpts/wmtask_latent_additive_p30_nearid_tf__lc_x_obsnoisescale_sweep_20260429T163244Z__stage_a/a421f95ba66ac4b7/last.ckpt | 1.0e-05 | 0.01 | 0.00464 | 0.6706 | 0.9947 | 6.610 | 45.0 |

### Best run per `obs_noise_scale`

| obs_noise_scale | Best LC weight | Best traj loss | MASE at best | R² | LC loss | epoch |
|---|---|---|---|---|---|---|
| 0.0 | 1.0e-06 | 0.00436 | 0.6507 | 0.9950 | 9.980 | 45.0 |
| 0.01 | 0.0e+00 | 0.00459 | 0.6666 | 0.9947 | 18.452 | 45.0 |
| 0.05 | 0.0e+00 | 0.00406 | 0.6301 | 0.9953 | 26.886 | 56.0 |

## Success-criteria verdicts (automated)

| Criterion | Verdict | Note |
|---|---|---|
| All 21 cells train without divergence | **Unknown** |  |
| es2-best.ckpt and es5-best.ckpt both saved per cell | **Unknown** |  |
| Best val traj_loss within ~10% of orig __stage_a's 0.00494 | **Unknown** |  |
| Lyapunov spectrum NOT compressed in Stage B vs Stage A | **Unknown** |  |
| Result shape is consistent with the matched Lorenz 3->3 sweep (init effect, LC dependence) | **Unknown** |  |

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
No run_id provided — selecting best run from group 'wmtask_latent_additive_p30_nearid_tf__lc_x_obsnoisescale_sweep_20260429T163244Z__stage_b_v2' ...
Found 10 total runs in JacobianODE/WMTask_identity_encoder_verification (group=wmtask_latent_additive_p30_nearid_tf__lc_x_obsnoisescale_sweep_20260429T163244Z__stage_b_v2)
All runs (state, loop_closure_weight, tangent_entropy_weight, kl_dyn_weight):
  fsnytm0o: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  wrpnn427: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  sgqoux4c: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  a45zk5sh: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  ees17qgj: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  xbofsisv: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  grvw9w8o: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  0b5de702: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  bgl6aks1: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  slpqn0gt: state=finished, lc=0.0, te=0.0, kl_dyn=0.0

slurm_timeout_min not found in any run config — falling back to 180 min
  Including fsnytm0o (lc=1e-05): use_all_runs=True (state=finished)
  Including wrpnn427 (lc=1e-05): use_all_runs=True (state=finished)
  Including sgqoux4c (lc=1e-06): use_all_runs=True (state=finished)
  Including a45zk5sh (lc=0.0): use_all_runs=True (state=finished)
  Including ees17qgj (lc=0.0001): use_all_runs=True (state=finished)
  Including xbofsisv (lc=1e-06): use_all_runs=True (state=finished)
  Including grvw9w8o (lc=1e-05): use_all_runs=True (state=finished)
  Including 0b5de702 (lc=1e-06): use_all_runs=True (state=finished)
  Including bgl6aks1 (lc=0.0): use_all_runs=True (state=finished)
  Including slpqn0gt (lc=0.0): use_all_runs=True (state=finished)
Found 10 effectively-done sweep runs:
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=a45zk5sh
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=bgl6aks1
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=slpqn0gt
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=0b5de702
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=sgqoux4c
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=xbofsisv
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=fsnytm0o
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=grvw9w8o
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=wrpnn427
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=ees17qgj
loaded wmtask RNN model checkpoint 41
Loading cached wmtask hiddens from /orcd/data/ekmiller/001/eisenaj/ControlJacobians/WMTaskModels/WMSelectionTask__cue_time_0.1__response_time_0.25__enforce_fixation_False/BiologicalRNN__cue_time_0.1__learning_rate_0.0005__max_epochs_42__N1_64__N2_64__tau_0.05__dt_0.02__eig_lower_bound_0.1__init_mode_random/_jacobianode_cache/hiddens__all__epoch41__trials4096__seed42.pt
n_dims=128, n_latent=128, n_dyn=128, dt=0.0200
  run=a45zk5sh: DiagnosticMetrics(one_step_mase=0.583189845085144, loop_closure_loss=14.049751281738281, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004369640722870827) (from W&B history)
  run=bgl6aks1: DiagnosticMetrics(one_step_mase=0.5902959704399109, loop_closure_loss=18.451641082763672, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004592176526784897) (from W&B history)
  run=slpqn0gt: DiagnosticMetrics(one_step_mase=0.5655663013458252, loop_closure_loss=26.886211395263672, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004060692153871059) (from W&B history)
  run=0b5de702: DiagnosticMetrics(one_step_mase=0.5905017256736755, loop_closure_loss=13.521018028259277, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004598299972712994) (from W&B history)
  run=sgqoux4c: DiagnosticMetrics(one_step_mase=0.5696651935577393, loop_closure_loss=15.846663475036621, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004594835918396711) (from W&B history)
  run=xbofsisv: DiagnosticMetrics(one_step_mase=0.5831796526908875, loop_closure_loss=9.980290412902832, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004361877217888832) (from W&B history)
  run=fsnytm0o: DiagnosticMetrics(one_step_mase=0.5839802026748657, loop_closure_loss=4.223639965057373, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004388238303363323) (from W&B history)
  run=grvw9w8o: DiagnosticMetrics(one_step_mase=0.5922072529792786, loop_closure_loss=6.61032772064209, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004642031621187925) (from W&B history)
  run=wrpnn427: DiagnosticMetrics(one_step_mase=0.5678009390830994, loop_closure_loss=8.038137435913086, fast_eigenvalue_fraction=0.0009765625, trajectory_val_loss=0.0041071828454732895) (from W&B history)
  run=ees17qgj: DiagnosticMetrics(one_step_mase=0.5866382122039795, loop_closure_loss=1.1077107191085815, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004578075837343931) (from W&B history)

Ranking method:           best_traj_loss
Best run ID:              wrpnn427
Best loop_closure_weight: 1e-05
Best tangent_entropy_weight: 0.0
Best kl_dyn_weight:       0.0
Best traj loss:           0.004107
Criteria applied: ['C1', 'C2', 'C3']
Surviving: 5 / 10
Auto-selected run_id: wrpnn427

======================================================================
PARETO FRONTIER RUNS (4 runs)
======================================================================
  Run ID               LC Loss   Traj Val Loss
  ------------  --------------  --------------
  ees17qgj            1.107711        0.004578
  fsnytm0o            4.223640        0.004388
  wrpnn427            8.038137        0.004107 <-- selected
  slpqn0gt           26.886211        0.004061

======================================================================
RANKING METHOD COMPARISON (over 5 survivors)
======================================================================
  Method                  Run ID               LC Loss   Traj Val Loss
  ----------------------  ------------  --------------  --------------
  best_traj_loss          wrpnn427            8.038137        0.004107 <-- active
  pareto_knee             fsnytm0o            4.223640        0.004388
  geo_rank                wrpnn427            8.038137        0.004107
  minimax_rank            fsnytm0o            4.223640        0.004388
  geo_log_score           wrpnn427            8.038137        0.004107
  minimax_log_score       fsnytm0o            4.223640        0.004388
======================================================================

Loading run wrpnn427 from JacobianODE/WMTask_identity_encoder_verification ...
loaded wmtask RNN model checkpoint 41
Loading cached wmtask hiddens from /orcd/data/ekmiller/001/eisenaj/ControlJacobians/WMTaskModels/WMSelectionTask__cue_time_0.1__response_time_0.25__enforce_fixation_False/BiologicalRNN__cue_time_0.1__learning_rate_0.0005__max_epochs_42__N1_64__N2_64__tau_0.05__dt_0.02__eig_lower_bound_0.1__init_mode_random/_jacobianode_cache/hiddens__all__epoch41__trials4096__seed42.pt
Loading checkpoint epoch=51-step=6500.ckpt...
Train dataset shape: torch.Size([11468, 45, 128])
Validation dataset shape: torch.Size([3280, 45, 128])
Test dataset shape: torch.Size([1636, 45, 128])
Train trajectories dataset shape: torch.Size([2867, 49, 128])
Validation trajectories dataset shape: torch.Size([820, 49, 128])
Test trajectories dataset shape: torch.Size([409, 49, 128])
Loading checkpoint epoch=51-step=6500.ckpt...
Computing reconstruction ...
Computing MASE ...
Teacher-forced MASE: 0.6581
Free-running MASE:   0.7089
Computing latent utilization ...
Entropy-based utilization: 0.923
Computing Lyapunov exponents ...
  Computing full-trajectory Lyapunov (409 test trajs, T=49) ...
Predicted Lyapunov exponents (batch+burn-in, 128 windowed trajs):
  λ_1 = -0.2919 ± 0.1953
  λ_2 = -0.5957 ± 0.2851
  λ_3 = -0.8500 ± 0.2637
  λ_4 = -1.0908 ± 0.2532
  λ_5 = -1.4794 ± 0.3822
  λ_6 = -1.7354 ± 0.4481
  λ_7 = -2.8711 ± 0.4107
  λ_8 = -3.1075 ± 0.4210
  λ_9 = -4.3367 ± 0.4023
  λ_10 = -4.5240 ± 0.4686
  λ_11 = -4.9369 ± 0.4593
  λ_12 = -5.2522 ± 0.4911
  λ_13 = -5.7993 ± 0.3418
  λ_14 = -6.2156 ± 0.4879
  λ_15 = -6.5753 ± 0.4274
  λ_16 = -6.8536 ± 0.5752
  λ_17 = -7.1459 ± 0.5091
  λ_18 = -7.3337 ± 0.4712
  λ_19 = -7.4977 ± 0.4747
  λ_20 = -7.7336 ± 0.4819
  λ_21 = -7.8975 ± 0.5021
  λ_22 = -7.9836 ± 0.5237
  λ_23 = -8.0760 ± 0.5530
  λ_24 = -8.1725 ± 0.5631
  λ_25 = -8.2778 ± 0.5515
  λ_26 = -8.5449 ± 0.5790
  λ_27 = -8.7232 ± 0.5672
  λ_28 = -8.8727 ± 0.5547
  λ_29 = -8.9793 ± 0.5831
  λ_30 = -9.0870 ± 0.6018
  λ_31 = -9.1948 ± 0.6167
  λ_32 = -9.4275 ± 0.6417
  λ_33 = -9.5806 ± 0.7082
  λ_34 = -9.6897 ± 0.7035
  λ_35 = -9.9126 ± 0.7018
  λ_36 = -10.2234 ± 0.6404
  λ_37 = -10.3607 ± 0.6642
  λ_38 = -10.4651 ± 0.6771
  λ_39 = -10.5946 ± 0.7044
  λ_40 = -10.6835 ± 0.7215
  λ_41 = -10.7707 ± 0.7249
  λ_42 = -10.8927 ± 0.6929
  λ_43 = -11.0343 ± 0.6849
  λ_44 = -11.2273 ± 0.7207
  λ_45 = -11.3886 ± 0.7538
  λ_46 = -11.5021 ± 0.7571
  λ_47 = -11.6952 ± 0.7815
  λ_48 = -11.8216 ± 0.7973
  λ_49 = -11.9401 ± 0.7764
  λ_50 = -12.1496 ± 0.8515
  λ_51 = -12.2641 ± 0.8439
  λ_52 = -12.3820 ± 0.8290
  λ_53 = -12.5141 ± 0.8308
  λ_54 = -12.6870 ± 0.8583
  λ_55 = -12.8560 ± 0.8623
  λ_56 = -12.9301 ± 0.8740
  λ_57 = -13.0041 ± 0.8997
  λ_58 = -13.1030 ± 0.9062
  λ_59 = -13.1832 ± 0.8873
  λ_60 = -13.2660 ± 0.8970
  λ_61 = -13.4117 ± 0.8859
  λ_62 = -13.5067 ± 0.9118
  λ_63 = -13.6526 ± 0.9081
  λ_64 = -13.7614 ± 0.9410
  λ_65 = -13.8827 ± 0.9508
  λ_66 = -14.0767 ± 0.9907
  λ_67 = -14.3794 ± 0.9661
  λ_68 = -14.4927 ± 0.9629
  λ_69 = -14.6380 ± 0.9704
  λ_70 = -14.8529 ± 1.0421
  λ_71 = -14.9784 ± 1.0586
  λ_72 = -15.1979 ± 1.1159
  λ_73 = -15.5274 ± 1.0635
  λ_74 = -15.7083 ± 1.0663
  λ_75 = -15.8328 ± 1.0606
  λ_76 = -15.9434 ± 1.0504
  λ_77 = -16.0420 ± 1.0354
  λ_78 = -16.1183 ± 1.0425
  λ_79 = -16.2313 ± 1.0675
  λ_80 = -16.5455 ± 1.1826
  λ_81 = -16.6768 ± 1.1679
  λ_82 = -16.8938 ± 1.1171
  λ_83 = -17.2813 ± 1.1264
  λ_84 = -17.6637 ± 1.1369
  λ_85 = -18.1249 ± 1.2978
  λ_86 = -18.3085 ± 1.2776
  λ_87 = -18.4390 ± 1.2535
  λ_88 = -18.6110 ± 1.2445
  λ_89 = -18.7622 ± 1.2560
  λ_90 = -18.9071 ± 1.2646
  λ_91 = -19.0282 ± 1.3080
  λ_92 = -19.3649 ± 1.3346
  λ_93 = -19.5845 ± 1.3601
  λ_94 = -19.7530 ± 1.3645
  λ_95 = -19.9231 ± 1.3603
  λ_96 = -20.1950 ± 1.3943
  λ_97 = -20.4838 ± 1.3733
  λ_98 = -20.7975 ± 1.4246
  λ_99 = -21.1296 ± 1.4424
  λ_100 = -21.3629 ± 1.4561
  λ_101 = -21.6428 ± 1.4653
  λ_102 = -21.7722 ± 1.4870
  λ_103 = -21.8407 ± 1.4782
  λ_104 = -22.5628 ± 1.5584
  λ_105 = -22.6963 ± 1.5461
  λ_106 = -22.9475 ± 1.5759
  λ_107 = -23.1351 ± 1.5664
  λ_108 = -23.3095 ± 1.6050
  λ_109 = -23.5497 ± 1.6288
  λ_110 = -23.8408 ± 1.6255
  λ_111 = -24.1468 ± 1.6816
  λ_112 = -24.2945 ± 1.6624
  λ_113 = -24.5531 ± 1.6920
  λ_114 = -24.6980 ± 1.6744
  λ_115 = -24.8684 ± 1.6926
  λ_116 = -25.0190 ± 1.6951
  λ_117 = -25.2651 ± 1.7528
  λ_118 = -25.4775 ± 1.7879
  λ_119 = -25.6591 ± 1.7416
  λ_120 = -25.7815 ± 1.7478
  λ_121 = -25.9828 ± 1.8075
  λ_122 = -26.6421 ± 1.8279
  λ_123 = -26.8878 ± 1.8475
  λ_124 = -27.5752 ± 1.9019
  λ_125 = -27.9303 ± 1.9180
  λ_126 = -29.0782 ± 1.9984
  λ_127 = -29.1287 ± 2.0106
  λ_128 = -30.3723 ± 2.1244
Predicted Lyapunov exponents (full-length, 409 test trajs):
  λ_1 = -1.1399 ± 0.5109
  λ_2 = -1.7859 ± 0.3747
  λ_3 = -2.3811 ± 0.3407
  λ_4 = -3.4173 ± 0.5273
  λ_5 = -4.1940 ± 0.5022
  λ_6 = -4.6592 ± 0.4177
  λ_7 = -5.1301 ± 0.4067
  λ_8 = -5.6183 ± 0.5364
  λ_9 = -6.4440 ± 0.6469
  λ_10 = -7.0003 ± 0.7146
  λ_11 = -7.4564 ± 0.6467
  λ_12 = -7.8627 ± 0.5525
  λ_13 = -8.2709 ± 0.5652
  λ_14 = -9.0678 ± 0.5861
  λ_15 = -9.5400 ± 0.5886
  λ_16 = -9.8931 ± 0.5760
  λ_17 = -10.2367 ± 0.5402
  λ_18 = -10.5386 ± 0.5181
  λ_19 = -10.9159 ± 0.5409
  λ_20 = -11.2310 ± 0.5135
  λ_21 = -11.4224 ± 0.4859
  λ_22 = -11.5644 ± 0.4824
  λ_23 = -11.7321 ± 0.5107
  λ_24 = -11.8787 ± 0.5385
  λ_25 = -12.0713 ± 0.5118
  λ_26 = -12.2480 ± 0.4844
  λ_27 = -12.4398 ± 0.5043
  λ_28 = -12.6376 ± 0.5196
  λ_29 = -12.8750 ± 0.5387
  λ_30 = -13.0606 ± 0.5712
  λ_31 = -13.4257 ± 0.5535
  λ_32 = -13.6643 ± 0.5444
  λ_33 = -13.8711 ± 0.5797
  λ_34 = -14.1714 ± 0.6320
  λ_35 = -14.7666 ± 0.6188
  λ_36 = -14.9433 ± 0.6298
  λ_37 = -15.0960 ± 0.6188
  λ_38 = -15.2330 ± 0.6477
  λ_39 = -15.4058 ± 0.6463
  λ_40 = -15.5604 ± 0.6536
  λ_41 = -15.7073 ± 0.6463
  λ_42 = -15.8517 ± 0.6611
  λ_43 = -15.9978 ± 0.7149
  λ_44 = -16.1795 ± 0.6948
  λ_45 = -16.3386 ± 0.6983
  λ_46 = -16.4769 ± 0.7046
  λ_47 = -16.5854 ± 0.7031
  λ_48 = -16.7253 ± 0.7099
  λ_49 = -16.9708 ± 0.7307
  λ_50 = -17.2325 ± 0.7596
  λ_51 = -17.4745 ± 0.7844
  λ_52 = -17.6503 ± 0.7393
  λ_53 = -17.7759 ± 0.7359
  λ_54 = -17.8981 ± 0.7295
  λ_55 = -18.0285 ± 0.7344
  λ_56 = -18.1731 ± 0.7431
  λ_57 = -18.3436 ± 0.7532
  λ_58 = -18.4510 ± 0.7747
  λ_59 = -18.5608 ± 0.7900
  λ_60 = -18.6913 ± 0.8155
  λ_61 = -18.7789 ± 0.8279
  λ_62 = -18.9009 ± 0.8549
  λ_63 = -19.0124 ± 0.8293
  λ_64 = -19.1181 ± 0.8330
  λ_65 = -19.2598 ± 0.8443
  λ_66 = -19.3617 ± 0.8581
  λ_67 = -19.4374 ± 0.8720
  λ_68 = -19.5311 ± 0.8826
  λ_69 = -19.6258 ± 0.8898
  λ_70 = -19.7187 ± 0.8924
  λ_71 = -19.8350 ± 0.8914
  λ_72 = -19.9346 ± 0.9127
  λ_73 = -20.0880 ± 0.9552
  λ_74 = -20.2041 ± 0.9442
  λ_75 = -20.3295 ± 0.9378
  λ_76 = -20.5282 ± 0.9675
  λ_77 = -20.7073 ± 0.9715
  λ_78 = -20.8549 ± 0.9744
  λ_79 = -21.0886 ± 0.9603
  λ_80 = -21.2743 ± 0.9785
  λ_81 = -21.4934 ± 1.0109
  λ_82 = -21.9639 ± 1.0609
  λ_83 = -22.3425 ± 1.1518
  λ_84 = -22.6041 ± 1.1504
  λ_85 = -22.7524 ± 1.1563
  λ_86 = -22.9293 ± 1.1798
  λ_87 = -23.0696 ± 1.1665
  λ_88 = -23.2435 ± 1.1971
  λ_89 = -23.5010 ± 1.1881
  λ_90 = -23.8284 ± 1.1759
  λ_91 = -24.1177 ± 1.1203
  λ_92 = -24.3896 ± 1.1724
  λ_93 = -24.6402 ± 1.1916
  λ_94 = -24.8401 ± 1.1641
  λ_95 = -25.0903 ± 1.1358
  λ_96 = -25.4895 ± 1.2274
  λ_97 = -25.8575 ± 1.2892
  λ_98 = -26.1611 ± 1.3382
  λ_99 = -26.5009 ± 1.3684
  λ_100 = -26.8638 ± 1.3519
  λ_101 = -27.2199 ± 1.3548
  λ_102 = -27.5351 ± 1.3368
  λ_103 = -27.7822 ± 1.3578
  λ_104 = -28.0308 ± 1.3828
  λ_105 = -28.4332 ± 1.3960
  λ_106 = -28.6734 ± 1.4552
  λ_107 = -28.9030 ± 1.4973
  λ_108 = -29.0828 ± 1.4974
  λ_109 = -29.3274 ± 1.4771
  λ_110 = -29.5406 ± 1.4994
  λ_111 = -29.7645 ± 1.5208
  λ_112 = -29.9213 ± 1.5000
  λ_113 = -30.1453 ± 1.5154
  λ_114 = -30.3454 ± 1.5057
  λ_115 = -30.6203 ± 1.5343
  λ_116 = -30.7907 ± 1.5481
  λ_117 = -30.9873 ± 1.5694
  λ_118 = -31.3290 ± 1.6025
  λ_119 = -31.7141 ± 1.5959
  λ_120 = -32.1620 ± 1.5383
  λ_121 = -32.4644 ± 1.6008
  λ_122 = -32.7454 ± 1.6507
  λ_123 = -33.0591 ± 1.6519
  λ_124 = -33.3835 ± 1.7282
  λ_125 = -33.7156 ± 1.7785
  λ_126 = -35.5396 ± 1.8036
  λ_127 = -36.1090 ± 1.8137
  λ_128 = -37.0196 ± 1.9182
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
Mean KY dim (burn-in):   0.118 ± 0.447
Computing prediction windows ...
Windows: 3 — nMSE min=0.0104, median=0.0113, mean=0.0115, max=0.0127
Computing long-trajectory free-running rollouts ...
Computing encoder/decoder Jacobians ...
encoder_jacobian: (128, 128, 128)
decoder_jacobian: (128, 128, 128)
Computing amplification loss ...
Amplification loss — True state: 0.004748
Amplification loss — Latent:     0.004944
Computing tangent space spectrum ...
```

</details>
