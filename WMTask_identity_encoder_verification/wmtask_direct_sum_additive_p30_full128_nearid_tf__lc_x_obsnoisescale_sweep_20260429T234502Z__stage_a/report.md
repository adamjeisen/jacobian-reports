# Sweep Analysis: `wmtask_direct_sum_additive_p30_full128_nearid_tf__lc_x_obsnoisescale_sweep_20260429T234502Z__stage_a`

**Project**: [WMTask_identity_encoder_verification](https://wandb.ai/JacobianODE/WMTask_identity_encoder_verification/groups/wmtask_direct_sum_additive_p30_full128_nearid_tf__lc_x_obsnoisescale_sweep_20260429T234502Z__stage_a)  
**Launched**: 2026-04-29T23:45:24Z  
**Completed**: 2026-04-30T01:35:24Z  
**Outcome**: `complete_clean`  
**Git**: `latent-JacobianODE` @ `4cd9047`  
**Expected runs**: 21

## Experiment Context

### `wmtask_direct_sum_additive_p30_full128_nearid_tf__lc_x_obsnoisescale_sweep`

**Description**

WMTask fully-observed (N1=N2=64), latent JacobianODE with
DirectSumCouplingEncoder, 128->128 (no null subspace, full target dim
per area). Additive coupling, 8 layers, hidden_dim=128.
near_identity_std=1e-3, final_perm_identity=true. 21-cell sweep over
7 LC x 3 obs_noise_scale. Split-mode loss. TF-coupled LR schedule
(k_scale=1, init 1e-4 -> min 1e-6 following TF alpha annealing).
Two-stage protocol with dual-checkpoint (primary ES patience=5,
shadow patience=2).

**Hypothesis**

Same recipe as the monolithic nearid_tf sweep; the only structural
difference is per-area block-diagonal Jacobian routing via the
DirectSum encoder. If WMTask's brain-area structure (visual/cognitive
partition) is exploitable, this should match or exceed the monolithic
sweep on val_traj_loss while preserving the cross-area Gramian
asymmetry signal that the monolithic encoder cannot represent
structurally.

**Success criteria**

- All 21 cells train without divergence
- es2-best.ckpt and es5-best.ckpt both saved per cell
- Best val traj_loss within 10% of monolithic nearid_tf sweep's best
- Cross-area Gramian asymmetry (vis -> cog > cog -> vis) at best cell
- Lyapunov spectrum NOT compressed in Stage B vs Stage A

## Results

**Swept axes** (3): `data.postprocessing.generalized_variance`, `training.lightning.loop_closure_weight`, `training.lightning.obs_noise_scale`

**Chosen run** (by `best_traj_loss`): `5j58o549` — traj_loss=0.00547, MASE=0.7147, R²=0.9937, LC loss=21.025, epoch=18.0

Swept-axis values at chosen run: `data.postprocessing.generalized_variance`=0.00954705 · `training.lightning.loop_closure_weight`=0 · `training.lightning.obs_noise_scale`=0.05

**Runs analyzed**: 21 (expected 21)

### Per-run results

| run_idx | run_id | `data.postprocessing.generalized_variance` | `training.lightning.loop_closure_weight` | `training.lightning.obs_noise_scale` | best_traj_loss | best_MASE | R² | LC loss | epoch |
|---|---|---|---|---|---|---|---|---|---|
| 2 | `5j58o549` | 0.00954705 | 0 | 0.05 | 0.00547 | 0.7147 | 0.9937 | 21.025 | 18.0 |
| 5 | `lbgfaqfr` | 0.00954705 | 1.0e-06 | 0.05 | 0.00547 | 0.7149 | 0.9937 | 14.159 | 18.0 |
| 8 | `sh3sevik` | 0.00954705 | 1.0e-05 | 0.05 | 0.00558 | 0.7212 | 0.9936 | 4.937 | 18.0 |
| 11 | `yxkhj8sm` | 0.00954705 | 1.0e-04 | 0.05 | 0.00573 | 0.7313 | 0.9934 | 1.259 | 19.0 |
| 3 | `t6hiz545` | 0.00954705 | 1.0e-06 | 0 | 0.00573 | 0.7287 | 0.9934 | 7.540 | 19.0 |
| 6 | `zg3r9p42` | 0.00954705 | 1.0e-05 | 0 | 0.00580 | 0.7320 | 0.9934 | 2.759 | 19.0 |
| 0 | `kqk288nb` | 0.00954705 | 0 | 0 | 0.00588 | 0.7359 | 0.9933 | 10.920 | 19.0 |
| 1 | `728s1wh6` | 0.00954705 | 0 | 0.01 | 0.00588 | 0.7377 | 0.9933 | 14.670 | 19.0 |
| 4 | `73xtuotf` | 0.00954705 | 1.0e-06 | 0.01 | 0.00588 | 0.7374 | 0.9933 | 9.842 | 19.0 |
| 7 | `f9qwwicv` | 0.00954705 | 1.0e-05 | 0.01 | 0.00607 | 0.7471 | 0.9930 | 3.586 | 18.0 |
| 9 | `pkoy0sd0` | 0.00954705 | 1.0e-04 | 0 | 0.00631 | 0.7586 | 0.9928 | 0.604 | 19.0 |
| 10 | `q4q6ayzb` | 0.00954705 | 1.0e-04 | 0.01 | 0.00675 | 0.7900 | 0.9922 | 0.945 | 18.0 |
| 12 | `wqvtzd3m` | 0.00954705 | 0.001 | 0 | 0.00767 | 0.8281 | 0.9912 | 0.071 | 19.0 |
| 14 | `zttsicr3` | 0.00954705 | 0.001 | 0.05 | 0.00855 | 0.8759 | 0.9902 | 0.279 | 19.0 |
| 13 | `rlpbgllk` | 0.00954705 | 0.001 | 0.01 | 0.01085 | 0.9838 | 0.9875 | 0.277 | 19.0 |
| 15 | `mf3dcgu4` | 0.00954705 | 0.01 | 0 | 0.01168 | 0.9936 | 0.9866 | 0.006 | 19.0 |
| 17 | `d60ik6yd` | 0.00954705 | 0.01 | 0.05 | 0.01667 | 1.1746 | 0.9809 | 0.036 | 19.0 |
| 18 | `wvl8xjjx` | 0.00954705 | 0.1 | 0 | 0.01886 | 1.2248 | 0.9784 | 0.000 | 19.0 |
| 16 | `fu6ejjn9` | 0.00954705 | 0.01 | 0.01 | 0.02251 | 1.3568 | 0.9742 | 0.051 | 18.0 |
| 20 | `u4a7teni` | 0.00954705 | 0.1 | 0.05 | 0.02914 | 1.5131 | 0.9666 | 0.001 | 19.0 |
| 19 | `16kpzke6` | 0.00954705 | 0.1 | 0.01 | 0.03483 | 1.6493 | 0.9601 | 0.002 | 19.0 |

### Best run per `obs_noise_scale`

| obs_noise_scale | Best LC weight | Best traj loss | MASE at best | R² | LC loss | epoch |
|---|---|---|---|---|---|---|
| 0.0 | 1.0e-06 | 0.00573 | 0.7287 | 0.9934 | 7.540 | 19.0 |
| 0.01 | 0.0e+00 | 0.00588 | 0.7377 | 0.9933 | 14.670 | 19.0 |
| 0.05 | 0.0e+00 | 0.00547 | 0.7147 | 0.9937 | 21.025 | 18.0 |

## Success-criteria verdicts (automated)

| Criterion | Verdict | Note |
|---|---|---|
| All 21 cells train without divergence | **Unknown** |  |
| es2-best.ckpt and es5-best.ckpt both saved per cell | **Unknown** |  |
| Best val traj_loss within 10% of monolithic nearid_tf sweep's best | **Unknown** |  |
| Cross-area Gramian asymmetry (vis -> cog > cog -> vis) at best cell | **Unknown** |  |
| Lyapunov spectrum NOT compressed in Stage B vs Stage A | **Unknown** |  |

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
No run_id provided — selecting best run from group 'wmtask_direct_sum_additive_p30_full128_nearid_tf__lc_x_obsnoisescale_sweep_20260429T234502Z__stage_a' ...
Found 21 total runs in JacobianODE/WMTask_identity_encoder_verification (group=wmtask_direct_sum_additive_p30_full128_nearid_tf__lc_x_obsnoisescale_sweep_20260429T234502Z__stage_a)
All runs (state, loop_closure_weight, tangent_entropy_weight, kl_dyn_weight):
  t6hiz545: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  5j58o549: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  pkoy0sd0: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  728s1wh6: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  sh3sevik: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  73xtuotf: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  f9qwwicv: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  kqk288nb: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  lbgfaqfr: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  zg3r9p42: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  q4q6ayzb: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  zttsicr3: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  d60ik6yd: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  rlpbgllk: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  yxkhj8sm: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  mf3dcgu4: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  wqvtzd3m: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  fu6ejjn9: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  wvl8xjjx: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  16kpzke6: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  u4a7teni: state=finished, lc=0.1, te=0.0, kl_dyn=0.0

slurm_timeout_min not found in any run config — falling back to 180 min
  Including t6hiz545 (lc=1e-06): use_all_runs=True (state=finished)
  Including 5j58o549 (lc=0.0): use_all_runs=True (state=finished)
  Including pkoy0sd0 (lc=0.0001): use_all_runs=True (state=finished)
  Including 728s1wh6 (lc=0.0): use_all_runs=True (state=finished)
  Including sh3sevik (lc=1e-05): use_all_runs=True (state=finished)
  Including 73xtuotf (lc=1e-06): use_all_runs=True (state=finished)
  Including f9qwwicv (lc=1e-05): use_all_runs=True (state=finished)
  Including kqk288nb (lc=0.0): use_all_runs=True (state=finished)
  Including lbgfaqfr (lc=1e-06): use_all_runs=True (state=finished)
  Including zg3r9p42 (lc=1e-05): use_all_runs=True (state=finished)
  Including q4q6ayzb (lc=0.0001): use_all_runs=True (state=finished)
  Including zttsicr3 (lc=0.001): use_all_runs=True (state=finished)
  Including d60ik6yd (lc=0.01): use_all_runs=True (state=finished)
  Including rlpbgllk (lc=0.001): use_all_runs=True (state=finished)
  Including yxkhj8sm (lc=0.0001): use_all_runs=True (state=finished)
  Including mf3dcgu4 (lc=0.01): use_all_runs=True (state=finished)
  Including wqvtzd3m (lc=0.001): use_all_runs=True (state=finished)
  Including fu6ejjn9 (lc=0.01): use_all_runs=True (state=finished)
  Including wvl8xjjx (lc=0.1): use_all_runs=True (state=finished)
  Including 16kpzke6 (lc=0.1): use_all_runs=True (state=finished)
  Including u4a7teni (lc=0.1): use_all_runs=True (state=finished)
Found 21 effectively-done sweep runs:
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=5j58o549
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=728s1wh6
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=kqk288nb
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=73xtuotf
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=lbgfaqfr
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=t6hiz545
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=f9qwwicv
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=sh3sevik
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=zg3r9p42
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=pkoy0sd0
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=q4q6ayzb
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=yxkhj8sm
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=rlpbgllk
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=wqvtzd3m
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=zttsicr3
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=d60ik6yd
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=fu6ejjn9
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=mf3dcgu4
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=16kpzke6
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=u4a7teni
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=wvl8xjjx
loaded wmtask RNN model checkpoint 41
Loading cached wmtask hiddens from /orcd/data/ekmiller/001/eisenaj/ControlJacobians/WMTaskModels/WMSelectionTask__cue_time_0.1__response_time_0.25__enforce_fixation_False/BiologicalRNN__cue_time_0.1__learning_rate_0.0005__max_epochs_42__N1_64__N2_64__tau_0.05__dt_0.02__eig_lower_bound_0.1__init_mode_random/_jacobianode_cache/hiddens__all__epoch41__trials4096__seed42.pt
n_dims=128, n_latent=128, n_dyn=128, dt=0.0200
  run=5j58o549: DiagnosticMetrics(one_step_mase=0.5727670788764954, loop_closure_loss=21.024751663208008, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005468189716339111) (from W&B history)
  run=728s1wh6: DiagnosticMetrics(one_step_mase=0.5951717495918274, loop_closure_loss=14.670292854309082, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005882310215383768) (from W&B history)
  run=kqk288nb: DiagnosticMetrics(one_step_mase=0.5898256897926331, loop_closure_loss=10.919659614562988, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005878886673599482) (from W&B history)
  run=73xtuotf: DiagnosticMetrics(one_step_mase=0.5951183438301086, loop_closure_loss=9.841719627380371, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005884873680770397) (from W&B history)
  run=lbgfaqfr: DiagnosticMetrics(one_step_mase=0.5731977224349976, loop_closure_loss=14.1589937210083, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.00546928308904171) (from W&B history)
  run=t6hiz545: DiagnosticMetrics(one_step_mase=0.5901928544044495, loop_closure_loss=7.539731979370117, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005733364727348089) (from W&B history)
  run=f9qwwicv: DiagnosticMetrics(one_step_mase=0.5967231392860413, loop_closure_loss=3.5861380100250244, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.006070139817893505) (from W&B history)
  run=sh3sevik: DiagnosticMetrics(one_step_mase=0.5749327540397644, loop_closure_loss=4.9371657371521, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005578760523349047) (from W&B history)
  run=zg3r9p42: DiagnosticMetrics(one_step_mase=0.5913226008415222, loop_closure_loss=2.758563280105591, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005796279292553663) (from W&B history)
  run=pkoy0sd0: DiagnosticMetrics(one_step_mase=0.5940946340560913, loop_closure_loss=0.6037071943283081, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0063069164752960205) (from W&B history)
  run=q4q6ayzb: DiagnosticMetrics(one_step_mase=0.6035827994346619, loop_closure_loss=0.9446823000907898, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0067540789023041725) (from W&B history)
  run=yxkhj8sm: DiagnosticMetrics(one_step_mase=0.580685555934906, loop_closure_loss=1.2594972848892212, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005731448996812105) (from W&B history)
  run=rlpbgllk: DiagnosticMetrics(one_step_mase=0.6274563074111938, loop_closure_loss=0.2769792079925537, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0108472416177392) (from W&B history)
  run=wqvtzd3m: DiagnosticMetrics(one_step_mase=0.6003233194351196, loop_closure_loss=0.07146421819925308, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.007669153623282909) (from W&B history)
  run=zttsicr3: DiagnosticMetrics(one_step_mase=0.6025753021240234, loop_closure_loss=0.2786770164966583, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.00854618288576603) (from W&B history)
  run=d60ik6yd: DiagnosticMetrics(one_step_mase=0.6293871998786926, loop_closure_loss=0.035886000841856, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.016666078940033913) (from W&B history)
  run=fu6ejjn9: DiagnosticMetrics(one_step_mase=0.643527626991272, loop_closure_loss=0.05139584466814995, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.022513141855597496) (from W&B history)
  run=mf3dcgu4: DiagnosticMetrics(one_step_mase=0.6143031716346741, loop_closure_loss=0.005748431198298931, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.01168239489197731) (from W&B history)
  run=16kpzke6: DiagnosticMetrics(one_step_mase=0.652258574962616, loop_closure_loss=0.0018083907198160887, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.03483293205499649) (from W&B history)
  run=u4a7teni: DiagnosticMetrics(one_step_mase=0.6433819532394409, loop_closure_loss=0.0013924372615292668, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.029138950631022453) (from W&B history)
  run=wvl8xjjx: DiagnosticMetrics(one_step_mase=0.6264743208885193, loop_closure_loss=0.0002865125716198236, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.018864301964640617) (from W&B history)

Ranking method:           best_traj_loss
Best run ID:              sh3sevik
Best loop_closure_weight: 1e-05
Best tangent_entropy_weight: 0.0
Best kl_dyn_weight:       0.0
Best traj loss:           0.005579
Criteria applied: ['C1', 'C2', 'C3']
Surviving: 18 / 21
Auto-selected run_id: sh3sevik

======================================================================
PARETO FRONTIER RUNS (8 runs)
======================================================================
  Run ID               LC Loss   Traj Val Loss
  ------------  --------------  --------------
  wvl8xjjx            0.000287        0.018864
  mf3dcgu4            0.005748        0.011682
  wqvtzd3m            0.071464        0.007669
  pkoy0sd0            0.603707        0.006307
  yxkhj8sm            1.259497        0.005731
  sh3sevik            4.937166        0.005579 <-- selected
  lbgfaqfr           14.158994        0.005469
  5j58o549           21.024752        0.005468

======================================================================
RANKING METHOD COMPARISON (over 18 survivors)
======================================================================
  Method                  Run ID               LC Loss   Traj Val Loss
  ----------------------  ------------  --------------  --------------
  best_traj_loss          sh3sevik            4.937166        0.005579 <-- active
  pareto_knee             yxkhj8sm            1.259497        0.005731
  geo_rank                sh3sevik            4.937166        0.005579
  minimax_rank            pkoy0sd0            0.603707        0.006307
  geo_log_score           sh3sevik            4.937166        0.005579
  minimax_log_score       mf3dcgu4            0.005748        0.011682
======================================================================

Loading run sh3sevik from JacobianODE/WMTask_identity_encoder_verification ...
loaded wmtask RNN model checkpoint 41
Loading cached wmtask hiddens from /orcd/data/ekmiller/001/eisenaj/ControlJacobians/WMTaskModels/WMSelectionTask__cue_time_0.1__response_time_0.25__enforce_fixation_False/BiologicalRNN__cue_time_0.1__learning_rate_0.0005__max_epochs_42__N1_64__N2_64__tau_0.05__dt_0.02__eig_lower_bound_0.1__init_mode_random/_jacobianode_cache/hiddens__all__epoch41__trials4096__seed42.pt
Loading checkpoint epoch=18-step=2375.ckpt...
Train dataset shape: torch.Size([11468, 45, 128])
Validation dataset shape: torch.Size([3280, 45, 128])
Test dataset shape: torch.Size([1636, 45, 128])
Train trajectories dataset shape: torch.Size([2867, 49, 128])
Validation trajectories dataset shape: torch.Size([820, 49, 128])
Test trajectories dataset shape: torch.Size([409, 49, 128])
Loading checkpoint epoch=18-step=2375.ckpt...
Computing reconstruction ...
Computing MASE ...
Teacher-forced MASE: 0.6706
Free-running MASE:   0.8111
Computing latent utilization ...
Entropy-based utilization: 0.914
Computing Lyapunov exponents ...
  Computing full-trajectory Lyapunov (409 test trajs, T=49) ...
Predicted Lyapunov exponents (batch+burn-in, 128 windowed trajs):
  λ_1 = -0.2734 ± 0.1246
  λ_2 = -0.4885 ± 0.2101
  λ_3 = -0.7218 ± 0.1504
  λ_4 = -0.9727 ± 0.1701
  λ_5 = -1.2831 ± 0.3382
  λ_6 = -1.5626 ± 0.3436
  λ_7 = -2.3837 ± 0.3677
  λ_8 = -2.5472 ± 0.4169
  λ_9 = -4.0458 ± 0.1852
  λ_10 = -4.2074 ± 0.2250
  λ_11 = -4.3540 ± 0.2935
  λ_12 = -4.6448 ± 0.3059
  λ_13 = -4.9116 ± 0.4193
  λ_14 = -5.2984 ± 0.5398
  λ_15 = -5.7616 ± 0.4111
  λ_16 = -5.8705 ± 0.3894
  λ_17 = -6.0380 ± 0.3879
  λ_18 = -6.3721 ± 0.3978
  λ_19 = -6.4965 ± 0.3963
  λ_20 = -6.6945 ± 0.4492
  λ_21 = -6.8131 ± 0.4581
  λ_22 = -6.9657 ± 0.4242
  λ_23 = -7.0740 ± 0.4270
  λ_24 = -7.1657 ± 0.4183
  λ_25 = -7.2868 ± 0.4062
  λ_26 = -7.5055 ± 0.4002
  λ_27 = -7.6924 ± 0.4578
  λ_28 = -7.8726 ± 0.4528
  λ_29 = -7.9889 ± 0.4531
  λ_30 = -8.0947 ± 0.4789
  λ_31 = -8.2753 ± 0.4959
  λ_32 = -8.4945 ± 0.4833
  λ_33 = -8.6635 ± 0.4851
  λ_34 = -8.8058 ± 0.4975
  λ_35 = -8.9800 ± 0.4678
  λ_36 = -9.1407 ± 0.4620
  λ_37 = -9.2625 ± 0.4756
  λ_38 = -9.3912 ± 0.5227
  λ_39 = -9.4650 ± 0.5327
  λ_40 = -9.5442 ± 0.5394
  λ_41 = -9.6178 ± 0.5536
  λ_42 = -9.7106 ± 0.5902
  λ_43 = -9.9163 ± 0.5729
  λ_44 = -10.1722 ± 0.5905
  λ_45 = -10.3416 ± 0.5875
  λ_46 = -10.4651 ± 0.6262
  λ_47 = -10.5227 ± 0.6340
  λ_48 = -10.5981 ± 0.6320
  λ_49 = -10.7181 ± 0.6558
  λ_50 = -11.0877 ± 0.6149
  λ_51 = -11.1720 ± 0.6153
  λ_52 = -11.2778 ± 0.6546
  λ_53 = -11.3890 ± 0.6452
  λ_54 = -11.4731 ± 0.6483
  λ_55 = -11.5608 ± 0.6540
  λ_56 = -11.7045 ± 0.6507
  λ_57 = -11.7837 ± 0.6691
  λ_58 = -11.8640 ± 0.6789
  λ_59 = -11.9327 ± 0.6862
  λ_60 = -12.0215 ± 0.7001
  λ_61 = -12.1441 ± 0.6794
  λ_62 = -12.2531 ± 0.6828
  λ_63 = -12.3671 ± 0.7129
  λ_64 = -12.4614 ± 0.7301
  λ_65 = -12.5588 ± 0.7418
  λ_66 = -12.7880 ± 0.7673
  λ_67 = -12.9323 ± 0.7479
  λ_68 = -13.0982 ± 0.7341
  λ_69 = -13.2652 ± 0.7897
  λ_70 = -13.5381 ± 0.7573
  λ_71 = -13.7059 ± 0.7934
  λ_72 = -13.9118 ± 0.7999
  λ_73 = -14.1001 ± 0.8207
  λ_74 = -14.2100 ± 0.8089
  λ_75 = -14.3454 ± 0.8327
  λ_76 = -14.5328 ± 0.8643
  λ_77 = -14.8273 ± 0.8796
  λ_78 = -14.9566 ± 0.8788
  λ_79 = -15.2410 ± 0.8700
  λ_80 = -15.3876 ± 0.8974
  λ_81 = -15.4999 ± 0.9145
  λ_82 = -15.6167 ± 0.9070
  λ_83 = -15.7881 ± 0.9285
  λ_84 = -16.1779 ± 0.9296
  λ_85 = -16.2781 ± 0.9420
  λ_86 = -16.3963 ± 0.9488
  λ_87 = -16.7524 ± 1.0132
  λ_88 = -17.0091 ± 0.9539
  λ_89 = -17.2312 ± 1.0021
  λ_90 = -17.3500 ± 1.0055
  λ_91 = -17.4729 ± 1.0273
  λ_92 = -17.6846 ± 1.0475
  λ_93 = -18.0170 ± 1.0510
  λ_94 = -18.1961 ± 1.0475
  λ_95 = -18.5036 ± 1.0731
  λ_96 = -18.7154 ± 1.0836
  λ_97 = -18.9077 ± 1.1608
  λ_98 = -19.1154 ± 1.1588
  λ_99 = -19.4343 ± 1.1569
  λ_100 = -19.7400 ± 1.1735
  λ_101 = -20.0409 ± 1.1155
  λ_102 = -20.1358 ± 1.1229
  λ_103 = -20.5022 ± 1.1626
  λ_104 = -20.6870 ± 1.2101
  λ_105 = -20.8445 ± 1.2152
  λ_106 = -21.0048 ± 1.1934
  λ_107 = -21.3623 ± 1.2612
  λ_108 = -21.5106 ± 1.2909
  λ_109 = -21.6642 ± 1.3269
  λ_110 = -21.8932 ± 1.3262
  λ_111 = -22.1239 ± 1.2798
  λ_112 = -22.2298 ± 1.3154
  λ_113 = -22.2806 ± 1.3137
  λ_114 = -22.4812 ± 1.2943
  λ_115 = -22.7699 ± 1.3552
  λ_116 = -22.9490 ± 1.3778
  λ_117 = -23.3197 ± 1.3552
  λ_118 = -23.4309 ± 1.3660
  λ_119 = -23.6245 ± 1.3720
  λ_120 = -23.7797 ± 1.3946
  λ_121 = -23.9803 ± 1.3770
  λ_122 = -24.4427 ± 1.4722
  λ_123 = -25.1819 ± 1.5156
  λ_124 = -25.3474 ± 1.5270
  λ_125 = -25.8033 ± 1.5141
  λ_126 = -26.6803 ± 1.5676
  λ_127 = -26.7340 ± 1.5874
  λ_128 = -28.0283 ± 1.6720
Predicted Lyapunov exponents (full-length, 409 test trajs):
  λ_1 = -0.7384 ± 0.5086
  λ_2 = -1.4043 ± 0.2807
  λ_3 = -1.8693 ± 0.3429
  λ_4 = -2.8121 ± 0.5137
  λ_5 = -3.5287 ± 0.3925
  λ_6 = -3.9012 ± 0.4294
  λ_7 = -4.4714 ± 0.4923
  λ_8 = -5.0047 ± 0.4845
  λ_9 = -5.8158 ± 0.5157
  λ_10 = -6.2161 ± 0.4523
  λ_11 = -6.4883 ± 0.5324
  λ_12 = -6.8377 ± 0.5017
  λ_13 = -7.2455 ± 0.5105
  λ_14 = -7.8145 ± 0.4883
  λ_15 = -8.2090 ± 0.3479
  λ_16 = -8.4042 ± 0.4019
  λ_17 = -8.6259 ± 0.4373
  λ_18 = -8.9373 ± 0.4469
  λ_19 = -9.4720 ± 0.4831
  λ_20 = -9.6752 ± 0.4511
  λ_21 = -9.8448 ± 0.4153
  λ_22 = -10.0155 ± 0.4114
  λ_23 = -10.1731 ± 0.4177
  λ_24 = -10.3097 ± 0.3997
  λ_25 = -10.5078 ± 0.3913
  λ_26 = -10.8119 ± 0.4230
  λ_27 = -11.0229 ± 0.4142
  λ_28 = -11.1646 ± 0.4302
  λ_29 = -11.3405 ± 0.4259
  λ_30 = -11.5081 ± 0.4682
  λ_31 = -11.6882 ± 0.4374
  λ_32 = -11.9488 ± 0.4533
  λ_33 = -12.2125 ± 0.4411
  λ_34 = -12.5442 ± 0.4293
  λ_35 = -12.8813 ± 0.5247
  λ_36 = -13.0493 ± 0.5477
  λ_37 = -13.1778 ± 0.5413
  λ_38 = -13.3475 ± 0.5570
  λ_39 = -13.5330 ± 0.5854
  λ_40 = -13.6764 ± 0.5799
  λ_41 = -13.8239 ± 0.5661
  λ_42 = -13.9684 ± 0.5249
  λ_43 = -14.0983 ± 0.5150
  λ_44 = -14.2403 ± 0.5215
  λ_45 = -14.3829 ± 0.5174
  λ_46 = -14.5631 ± 0.5353
  λ_47 = -14.6944 ± 0.5360
  λ_48 = -14.8034 ± 0.5589
  λ_49 = -14.9826 ± 0.6088
  λ_50 = -15.1861 ± 0.6649
  λ_51 = -15.4493 ± 0.5902
  λ_52 = -15.6002 ± 0.5932
  λ_53 = -15.7253 ± 0.5792
  λ_54 = -15.8040 ± 0.5787
  λ_55 = -15.9090 ± 0.6085
  λ_56 = -15.9969 ± 0.6206
  λ_57 = -16.0937 ± 0.6354
  λ_58 = -16.2182 ± 0.6566
  λ_59 = -16.3582 ± 0.6869
  λ_60 = -16.4514 ± 0.6920
  λ_61 = -16.5680 ± 0.6841
  λ_62 = -16.6496 ± 0.6872
  λ_63 = -16.7223 ± 0.6877
  λ_64 = -16.8393 ± 0.6832
  λ_65 = -16.9396 ± 0.7046
  λ_66 = -17.0269 ± 0.7045
  λ_67 = -17.1350 ± 0.7195
  λ_68 = -17.2332 ± 0.7205
  λ_69 = -17.3328 ± 0.7199
  λ_70 = -17.4283 ± 0.7008
  λ_71 = -17.5117 ± 0.7160
  λ_72 = -17.5875 ± 0.7240
  λ_73 = -17.6712 ± 0.7445
  λ_74 = -17.7944 ± 0.7709
  λ_75 = -17.9449 ± 0.8005
  λ_76 = -18.0611 ± 0.8194
  λ_77 = -18.2289 ± 0.8263
  λ_78 = -18.3685 ± 0.8252
  λ_79 = -18.5479 ± 0.8431
  λ_80 = -18.7323 ± 0.8387
  λ_81 = -18.9699 ± 0.7887
  λ_82 = -19.1765 ± 0.8385
  λ_83 = -19.3231 ± 0.8537
  λ_84 = -19.5462 ± 0.8549
  λ_85 = -19.7362 ± 0.9084
  λ_86 = -20.0066 ± 0.9728
  λ_87 = -20.2717 ± 1.0020
  λ_88 = -20.6205 ± 0.9116
  λ_89 = -20.8038 ± 0.9384
  λ_90 = -20.9584 ± 0.9331
  λ_91 = -21.1374 ± 0.9322
  λ_92 = -21.3157 ± 0.9549
  λ_93 = -21.5679 ± 0.9495
  λ_94 = -21.8081 ± 0.9801
  λ_95 = -22.0560 ± 0.9948
  λ_96 = -22.3646 ± 0.9864
  λ_97 = -22.8578 ± 0.9660
  λ_98 = -23.1911 ± 1.0360
  λ_99 = -23.4742 ± 1.0762
  λ_100 = -23.6776 ± 1.0604
  λ_101 = -23.9403 ± 1.0687
  λ_102 = -24.2419 ± 1.0849
  λ_103 = -24.3955 ± 1.0886
  λ_104 = -24.6389 ± 1.1495
  λ_105 = -24.8940 ± 1.1754
  λ_106 = -25.0259 ± 1.2144
  λ_107 = -25.1907 ± 1.2151
  λ_108 = -25.3345 ± 1.2014
  λ_109 = -25.5278 ± 1.1468
  λ_110 = -25.9279 ± 1.2128
  λ_111 = -26.1161 ± 1.2132
  λ_112 = -26.3049 ± 1.2318
  λ_113 = -26.4026 ± 1.2279
  λ_114 = -26.5537 ± 1.2587
  λ_115 = -26.7890 ± 1.2620
  λ_116 = -27.1403 ± 1.3513
  λ_117 = -27.4439 ± 1.2875
  λ_118 = -27.6935 ± 1.2975
  λ_119 = -27.8816 ± 1.2977
  λ_120 = -28.0384 ± 1.3239
  λ_121 = -28.2976 ± 1.3343
  λ_122 = -28.6372 ± 1.3287
  λ_123 = -29.0926 ± 1.4368
  λ_124 = -29.3985 ± 1.4495
  λ_125 = -29.7636 ± 1.4724
  λ_126 = -30.9454 ± 1.4494
  λ_127 = -31.6689 ± 1.4953
  λ_128 = -32.6094 ± 1.5435
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
Mean KY dim (predicted): 0.126 ± 0.355
Mean KY dim (empirical): 0.042 ± 0.210
Mean KY dim (burn-in):   0.000 ± 0.000
Computing prediction windows ...
Windows: 3 — nMSE min=0.0109, median=0.0154, mean=0.0140, max=0.0158
Computing long-trajectory free-running rollouts ...
Computing encoder/decoder Jacobians ...
encoder_jacobian: (128, 128, 128)
decoder_jacobian: (128, 128, 128)
Computing amplification loss ...
Amplification loss — True state: 0.004748
Amplification loss — Latent:     0.004828
Computing tangent space spectrum ...
```

</details>
