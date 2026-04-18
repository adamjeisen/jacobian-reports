# Sweep Analysis: `additive_joint_with_lpl_gennmse__lc_obsnoise_sweep`

**Project**: [WMTask_identity_encoder_verification](https://wandb.ai/JacobianODE/WMTask_identity_encoder_verification/groups/additive_joint_with_lpl_gennmse__lc_obsnoise_sweep)  
**Launched**: 2026-04-12T09:30:00Z  
**Completed**: 2026-04-12T21:00:00Z  
**Outcome**: `complete_with_failures`  
**Git**: `latent-JacobianODE` @ `retroactive`  
**Expected runs**: 27

## Experiment Context

### `wmtask_additive_joint_with_lpl_gennmse`

**Description**

Base config for the generalized_normalized_mse (gennMSE) version of the
LC × obs_noise_scale sweep. Uses a precomputed fixed denominator
det(Cov(x_recent))^(1/n_recent_dims) for all prediction losses. Compared
directly against MSE and per-batch nMSE sweeps.

**Hypothesis**

A fixed, data-scale-aware denominator gives consistent scaling across
all prediction terms while eliminating the batch-noise pathology of
per-batch nMSE. Should match or slightly beat MSE baseline with
identical-shape optimal-LC landscape.

**Success criteria**

- Best MASE matches or beats MSE baseline
- Optimal LC weight is consistent across obs_noise_scale
- No batch-noise-driven instability in the loss landscape

## Results

**Swept axes** (3): `data.postprocessing.generalized_variance`, `training.lightning.loop_closure_weight`, `training.lightning.obs_noise_scale`

**Chosen run** (by `best_traj_loss`): `—` — traj_loss=—, MASE=—, R²=—, LC loss=—, epoch=None

### Integrity checks

⚠️ **24 wandb run(s) did not match any run_idx** (excluded from the per-run table). These are most likely orphans from preempt-cycle retries or rate-limit re-launches. IDs: `ceo1z2z0`, `a9ztpmpa`, `j1gtjx02`, `j1ne5r5w`, `akh29o2g`, `mrc4x0kz`, `h0r7975j`, `6wi5e52l`, `00hdcmp9`, `znqbu94g`, `r9405hyh`, `4prl2xix`, `td1o8fm1`, `ljeooem0`, `fvlbkmpr`, `jjkfwma9`, `6wsesimk`, `msw6q774`, `4yo2u628`, `dtkrwrnt`, `hjp6f1r5`, `pcdayv3z`, `jzmoinzu`, `pc4xqu5v`.

**Runs analyzed**: 0 (expected 0)

## Success-criteria verdicts (automated)

| Criterion | Verdict | Note |
|---|---|---|
| Best MASE matches or beats MSE baseline | **Unknown** |  |
| Optimal LC weight is consistent across obs_noise_scale | **Unknown** |  |
| No batch-noise-driven instability in the loss landscape | **Unknown** |  |

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
No run_id provided — selecting best run from group 'additive_joint_with_lpl_gennmse__lc_obsnoise_sweep' ...
Found 24 total runs in JacobianODE/WMTask_identity_encoder_verification (group=additive_joint_with_lpl_gennmse__lc_obsnoise_sweep)
All runs (state, loop_closure_weight, tangent_entropy_weight, kl_dyn_weight):
  ceo1z2z0: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  a9ztpmpa: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  j1gtjx02: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  j1ne5r5w: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  akh29o2g: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  mrc4x0kz: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  h0r7975j: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  6wi5e52l: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  00hdcmp9: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  znqbu94g: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  r9405hyh: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  4prl2xix: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  td1o8fm1: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  ljeooem0: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  fvlbkmpr: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  jjkfwma9: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  6wsesimk: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  msw6q774: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  4yo2u628: state=finished, lc=1.0, te=0.0, kl_dyn=0.0
  dtkrwrnt: state=finished, lc=1.0, te=0.0, kl_dyn=0.0
  hjp6f1r5: state=finished, lc=1.0, te=0.0, kl_dyn=0.0
  pcdayv3z: state=finished, lc=10.0, te=0.0, kl_dyn=0.0
  jzmoinzu: state=finished, lc=10.0, te=0.0, kl_dyn=0.0
  pc4xqu5v: state=finished, lc=10.0, te=0.0, kl_dyn=0.0

slurm_timeout_min not found in any run config — falling back to 180 min
  Including ceo1z2z0 (lc=0.0): use_all_runs=True (state=finished)
  Including a9ztpmpa (lc=1e-06): use_all_runs=True (state=finished)
  Including j1gtjx02 (lc=0.0): use_all_runs=True (state=finished)
  Including j1ne5r5w (lc=0.0): use_all_runs=True (state=finished)
  Including akh29o2g (lc=1e-06): use_all_runs=True (state=finished)
  Including mrc4x0kz (lc=1e-05): use_all_runs=True (state=finished)
  Including h0r7975j (lc=1e-05): use_all_runs=True (state=finished)
  Including 6wi5e52l (lc=1e-05): use_all_runs=True (state=finished)
  Including 00hdcmp9 (lc=0.0001): use_all_runs=True (state=finished)
  Including znqbu94g (lc=0.0001): use_all_runs=True (state=finished)
  Including r9405hyh (lc=0.001): use_all_runs=True (state=finished)
  Including 4prl2xix (lc=0.001): use_all_runs=True (state=finished)
  Including td1o8fm1 (lc=0.01): use_all_runs=True (state=finished)
  Including ljeooem0 (lc=0.01): use_all_runs=True (state=finished)
  Including fvlbkmpr (lc=0.1): use_all_runs=True (state=finished)
  Including jjkfwma9 (lc=0.01): use_all_runs=True (state=finished)
  Including 6wsesimk (lc=0.1): use_all_runs=True (state=finished)
  Including msw6q774 (lc=0.1): use_all_runs=True (state=finished)
  Including 4yo2u628 (lc=1.0): use_all_runs=True (state=finished)
  Including dtkrwrnt (lc=1.0): use_all_runs=True (state=finished)
  Including hjp6f1r5 (lc=1.0): use_all_runs=True (state=finished)
  Including pcdayv3z (lc=10.0): use_all_runs=True (state=finished)
  Including jzmoinzu (lc=10.0): use_all_runs=True (state=finished)
  Including pc4xqu5v (lc=10.0): use_all_runs=True (state=finished)
Found 24 effectively-done sweep runs:
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=ceo1z2z0
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=j1gtjx02
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=j1ne5r5w
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=a9ztpmpa
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=akh29o2g
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=6wi5e52l
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=h0r7975j
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=mrc4x0kz
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=00hdcmp9
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=znqbu94g
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=4prl2xix
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=r9405hyh
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=jjkfwma9
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=ljeooem0
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=td1o8fm1
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=6wsesimk
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=fvlbkmpr
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=msw6q774
  loop_closure_weight=1.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=4yo2u628
  loop_closure_weight=1.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=dtkrwrnt
  loop_closure_weight=1.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=hjp6f1r5
  loop_closure_weight=10.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=jzmoinzu
  loop_closure_weight=10.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=pc4xqu5v
  loop_closure_weight=10.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=pcdayv3z
loaded wmtask RNN model checkpoint 41
Loading cached wmtask hiddens from /orcd/data/ekmiller/001/eisenaj/ControlJacobians/WMTaskModels/WMSelectionTask__cue_time_0.1__response_time_0.25__enforce_fixation_False/BiologicalRNN__cue_time_0.1__learning_rate_0.0005__max_epochs_42__N1_64__N2_64__tau_0.05__dt_0.02__eig_lower_bound_0.1__init_mode_random/_jacobianode_cache/hiddens__all__epoch41__trials4096__seed42.pt
n_dims=128, n_latent=128, n_dyn=128, dt=0.0200
  run=ceo1z2z0: DiagnosticMetrics(one_step_mase=0.5605855584144592, loop_closure_loss=44.841304779052734, fast_eigenvalue_fraction=0.13449375331401825, trajectory_val_loss=0.5318782925605774) (from cache, n_batches=100)
  run=j1gtjx02: DiagnosticMetrics(one_step_mase=0.5745500922203064, loop_closure_loss=26.198741912841797, fast_eigenvalue_fraction=0.0006398437544703484, trajectory_val_loss=0.4151560068130493) (from cache, n_batches=100)
  run=j1ne5r5w: DiagnosticMetrics(one_step_mase=0.5847537517547607, loop_closure_loss=20.77814483642578, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.44636303186416626) (from cache, n_batches=100)
  run=a9ztpmpa: DiagnosticMetrics(one_step_mase=0.5846931338310242, loop_closure_loss=20.5584716796875, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.44614851474761963) (from cache, n_batches=100)
  run=akh29o2g: DiagnosticMetrics(one_step_mase=0.5568705201148987, loop_closure_loss=46.11711120605469, fast_eigenvalue_fraction=0.033878907561302185, trajectory_val_loss=0.4035239815711975) (from cache, n_batches=100)
  run=6wi5e52l: DiagnosticMetrics(one_step_mase=0.5782102346420288, loop_closure_loss=22.084104537963867, fast_eigenvalue_fraction=0.00011210937373107299, trajectory_val_loss=0.44409817457199097) (from cache, n_batches=100)
  run=h0r7975j: DiagnosticMetrics(one_step_mase=0.5553004145622253, loop_closure_loss=40.42793655395508, fast_eigenvalue_fraction=0.069862499833107, trajectory_val_loss=0.4106222987174988) (from cache, n_batches=100)
  run=mrc4x0kz: DiagnosticMetrics(one_step_mase=0.5759663581848145, loop_closure_loss=21.80286407470703, fast_eigenvalue_fraction=1.7578124243300408e-05, trajectory_val_loss=0.3885360360145569) (from cache, n_batches=100)
  run=00hdcmp9: DiagnosticMetrics(one_step_mase=0.5737648606300354, loop_closure_loss=10.925004959106445, fast_eigenvalue_fraction=0.00015039062418509275, trajectory_val_loss=0.38790515065193176) (from cache, n_batches=100)
  run=znqbu94g: DiagnosticMetrics(one_step_mase=0.5853216052055359, loop_closure_loss=9.878469467163086, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.46720752120018005) (from cache, n_batches=100)
  run=4prl2xix: DiagnosticMetrics(one_step_mase=0.5862339735031128, loop_closure_loss=2.591629981994629, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.45144253969192505) (from cache, n_batches=100)
  run=r9405hyh: DiagnosticMetrics(one_step_mase=0.5808670520782471, loop_closure_loss=2.7957260608673096, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.4625230133533478) (from cache, n_batches=100)
  run=jjkfwma9: DiagnosticMetrics(one_step_mase=0.5641997456550598, loop_closure_loss=0.7837610840797424, fast_eigenvalue_fraction=0.049492187798023224, trajectory_val_loss=0.4985752999782562) (from cache, n_batches=100)
  run=ljeooem0: DiagnosticMetrics(one_step_mase=0.5827302932739258, loop_closure_loss=0.4745945632457733, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.4261530041694641) (from cache, n_batches=100)
  run=td1o8fm1: DiagnosticMetrics(one_step_mase=0.6069117784500122, loop_closure_loss=0.40410053730010986, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.5567625164985657) (from cache, n_batches=100)
  run=6wsesimk: DiagnosticMetrics(one_step_mase=0.5734004378318787, loop_closure_loss=0.0609065406024456, fast_eigenvalue_fraction=0.011747265234589577, trajectory_val_loss=0.6091201305389404) (from cache, n_batches=100)
  run=fvlbkmpr: DiagnosticMetrics(one_step_mase=0.5954903364181519, loop_closure_loss=0.03968322277069092, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.5353566408157349) (from cache, n_batches=100)
  run=msw6q774: DiagnosticMetrics(one_step_mase=0.590035080909729, loop_closure_loss=0.050767458975315094, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.46825236082077026) (from cache, n_batches=100)
  run=4yo2u628: DiagnosticMetrics(one_step_mase=0.6044191122055054, loop_closure_loss=0.00212790141813457, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.5803303718566895) (from cache, n_batches=100)
  run=dtkrwrnt: DiagnosticMetrics(one_step_mase=0.5772692561149597, loop_closure_loss=0.004436589777469635, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.5806950926780701) (from cache, n_batches=100)
  run=hjp6f1r5: DiagnosticMetrics(one_step_mase=0.6027210354804993, loop_closure_loss=0.002237852429971099, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.5760200619697571) (from cache, n_batches=100)
  run=jzmoinzu: DiagnosticMetrics(one_step_mase=0.6163854002952576, loop_closure_loss=7.639422983629629e-05, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.6486027240753174) (from cache, n_batches=100)
  run=pc4xqu5v: DiagnosticMetrics(one_step_mase=0.5838232040405273, loop_closure_loss=0.0002414501504972577, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.5524352788925171) (from cache, n_batches=100)
  run=pcdayv3z: DiagnosticMetrics(one_step_mase=0.6176822781562805, loop_closure_loss=6.249093712540343e-05, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.651183009147644) (from cache, n_batches=100)

Ranking method:           best_traj_loss
Best run ID:              00hdcmp9
Best loop_closure_weight: 0.0001
Best tangent_entropy_weight: 0.0
Best kl_dyn_weight:       0.0
Best traj loss:           0.387905
Criteria applied: ['C1', 'C2', 'C3']
Surviving: 14 / 24
Auto-selected run_id: 00hdcmp9

======================================================================
PARETO FRONTIER RUNS (7 runs)
======================================================================
  Run ID               LC Loss   Traj Val Loss
  ------------  --------------  --------------
  pcdayv3z            0.000062        0.651183
  jzmoinzu            0.000076        0.648603
  pc4xqu5v            0.000241        0.552435
  fvlbkmpr            0.039683        0.535357
  msw6q774            0.050767        0.468252
  ljeooem0            0.474595        0.426153
  00hdcmp9           10.925005        0.387905 <-- selected

======================================================================
RANKING METHOD COMPARISON (over 14 survivors)
======================================================================
  Method                  Run ID               LC Loss   Traj Val Loss
  ----------------------  ------------  --------------  --------------
  best_traj_loss          00hdcmp9           10.925005        0.387905 <-- active
  pareto_knee             fvlbkmpr            0.039683        0.535357
  geo_rank                00hdcmp9           10.925005        0.387905
  minimax_rank            fvlbkmpr            0.039683        0.535357
  geo_log_score           00hdcmp9           10.925005        0.387905
  minimax_log_score       msw6q774            0.050767        0.468252
======================================================================

Loading run 00hdcmp9 from JacobianODE/WMTask_identity_encoder_verification ...
loaded wmtask RNN model checkpoint 41
Loading cached wmtask hiddens from /orcd/data/ekmiller/001/eisenaj/ControlJacobians/WMTaskModels/WMSelectionTask__cue_time_0.1__response_time_0.25__enforce_fixation_False/BiologicalRNN__cue_time_0.1__learning_rate_0.0005__max_epochs_42__N1_64__N2_64__tau_0.05__dt_0.02__eig_lower_bound_0.1__init_mode_random/_jacobianode_cache/hiddens__all__epoch41__trials4096__seed42.pt
Train dataset shape: torch.Size([68808, 25, 128])
Validation dataset shape: torch.Size([19680, 25, 128])
Test dataset shape: torch.Size([9816, 25, 128])
Train trajectories dataset shape: torch.Size([2867, 49, 128])
Validation trajectories dataset shape: torch.Size([820, 49, 128])
Test trajectories dataset shape: torch.Size([409, 49, 128])
Loading checkpoint epoch=32-step=1650.ckpt...
Computing reconstruction ...
Computing MASE ...
Teacher-forced MASE: 0.5833
Free-running MASE:   0.6242
Computing latent utilization ...
Entropy-based utilization: 0.891
Computing Lyapunov exponents ...
  Computing full-trajectory Lyapunov (409 test trajs, T=49) ...
Predicted Lyapunov exponents (batch+burn-in, 128 windowed trajs):
  λ_1 = -0.5631 ± 0.2177
  λ_2 = -0.7434 ± 0.2362
  λ_3 = -1.1612 ± 0.2939
  λ_4 = -1.2859 ± 0.3373
  λ_5 = -1.7735 ± 0.4031
  λ_6 = -1.9409 ± 0.4076
  λ_7 = -2.4361 ± 0.4953
  λ_8 = -2.9332 ± 0.6710
  λ_9 = -4.2578 ± 0.4434
  λ_10 = -4.6058 ± 0.5135
  λ_11 = -5.4144 ± 0.3663
  λ_12 = -5.6190 ± 0.3922
  λ_13 = -6.3598 ± 0.4509
  λ_14 = -6.5494 ± 0.4119
  λ_15 = -6.7395 ± 0.3930
  λ_16 = -6.8712 ± 0.4218
  λ_17 = -7.0199 ± 0.4165
  λ_18 = -7.1996 ± 0.4581
  λ_19 = -7.3115 ± 0.4796
  λ_20 = -7.4098 ± 0.5022
  λ_21 = -7.5358 ± 0.5086
  λ_22 = -7.7835 ± 0.5167
  λ_23 = -8.0217 ± 0.5464
  λ_24 = -8.1892 ± 0.5560
  λ_25 = -8.3314 ± 0.5775
  λ_26 = -8.4926 ± 0.5953
  λ_27 = -8.7048 ± 0.5552
  λ_28 = -8.8658 ± 0.5527
  λ_29 = -9.1799 ± 0.6052
  λ_30 = -9.3030 ± 0.6198
  λ_31 = -9.4035 ± 0.6198
  λ_32 = -9.7344 ± 0.6948
  λ_33 = -9.8760 ± 0.7033
  λ_34 = -10.0296 ± 0.7192
  λ_35 = -10.1761 ± 0.7340
  λ_36 = -10.3599 ± 0.7243
  λ_37 = -10.6654 ± 0.7145
  λ_38 = -10.7640 ± 0.7136
  λ_39 = -10.8395 ± 0.7193
  λ_40 = -10.9142 ± 0.7359
  λ_41 = -11.0174 ± 0.7568
  λ_42 = -11.1672 ± 0.7663
  λ_43 = -11.2673 ± 0.7827
  λ_44 = -11.3570 ± 0.7931
  λ_45 = -11.4772 ± 0.8198
  λ_46 = -11.6650 ± 0.8520
  λ_47 = -11.8700 ± 0.8806
  λ_48 = -11.9530 ± 0.8996
  λ_49 = -12.0499 ± 0.9227
  λ_50 = -12.1483 ± 0.9188
  λ_51 = -12.2720 ± 0.9174
  λ_52 = -12.3805 ± 0.9147
  λ_53 = -12.4920 ± 0.8961
  λ_54 = -12.7944 ± 0.8706
  λ_55 = -12.9222 ± 0.8933
  λ_56 = -13.0094 ± 0.8805
  λ_57 = -13.1198 ± 0.8928
  λ_58 = -13.2731 ± 0.8924
  λ_59 = -13.4946 ± 0.9080
  λ_60 = -13.6695 ± 0.9868
  λ_61 = -13.7652 ± 1.0029
  λ_62 = -13.8593 ± 1.0167
  λ_63 = -13.9904 ± 1.0242
  λ_64 = -14.0863 ± 1.0155
  λ_65 = -14.1926 ± 1.0305
  λ_66 = -14.3214 ± 1.0274
  λ_67 = -14.8592 ± 1.0437
  λ_68 = -15.0220 ± 1.0440
  λ_69 = -15.1572 ± 1.0558
  λ_70 = -15.2849 ± 1.0572
  λ_71 = -15.4166 ± 1.0666
  λ_72 = -15.5473 ± 1.1007
  λ_73 = -15.7945 ± 1.0743
  λ_74 = -15.9096 ± 1.0904
  λ_75 = -16.0248 ± 1.1026
  λ_76 = -17.1252 ± 1.2323
  λ_77 = -17.2338 ± 1.2330
  λ_78 = -17.3116 ± 1.2274
  λ_79 = -17.4452 ± 1.1993
  λ_80 = -17.6445 ± 1.1655
  λ_81 = -18.3337 ± 1.1465
  λ_82 = -18.6844 ± 1.3566
  λ_83 = -19.2950 ± 1.4341
  λ_84 = -19.5522 ± 1.4066
  λ_85 = -19.8143 ± 1.3942
  λ_86 = -19.8994 ± 1.3975
  λ_87 = -19.9873 ± 1.4114
  λ_88 = -20.1979 ± 1.4937
  λ_89 = -20.5634 ± 1.4121
  λ_90 = -20.8924 ± 1.5002
  λ_91 = -21.8299 ± 1.5076
  λ_92 = -21.9743 ± 1.5340
  λ_93 = -22.2238 ± 1.5963
  λ_94 = -22.4528 ± 1.5831
  λ_95 = -22.8023 ± 1.6217
  λ_96 = -23.1029 ± 1.6075
  λ_97 = -23.5005 ± 1.6827
  λ_98 = -23.7548 ± 1.6723
  λ_99 = -23.8928 ± 1.6548
  λ_100 = -24.0227 ± 1.6661
  λ_101 = -24.1999 ± 1.6766
  λ_102 = -24.3356 ± 1.7264
  λ_103 = -24.7082 ± 1.8367
  λ_104 = -24.8761 ± 1.8292
  λ_105 = -25.0336 ± 1.8221
  λ_106 = -25.3430 ± 1.7872
  λ_107 = -25.6668 ± 1.7533
  λ_108 = -26.1345 ± 1.8968
  λ_109 = -26.3797 ± 1.8709
  λ_110 = -26.7640 ± 1.8808
  λ_111 = -26.9245 ± 1.9427
  λ_112 = -27.0915 ± 1.9020
  λ_113 = -27.2068 ± 1.9484
  λ_114 = -27.3916 ± 1.9159
  λ_115 = -27.4808 ± 1.9303
  λ_116 = -27.9663 ± 1.9686
  λ_117 = -28.6953 ± 2.0894
  λ_118 = -28.9016 ± 2.0152
  λ_119 = -29.2244 ± 2.0407
  λ_120 = -29.5009 ± 2.0663
  λ_121 = -29.6803 ± 2.1063
  λ_122 = -30.2515 ± 2.1032
  λ_123 = -30.4258 ± 2.1616
  λ_124 = -30.6122 ± 2.2037
  λ_125 = -32.2267 ± 2.3251
  λ_126 = -32.4243 ± 2.3063
  λ_127 = -33.3629 ± 2.3237
  λ_128 = -34.1030 ± 2.4557
Predicted Lyapunov exponents (full-length, 409 test trajs):
  λ_1 = -1.8845 ± 0.4303
  λ_2 = -2.2462 ± 0.4266
  λ_3 = -2.5697 ± 0.4026
  λ_4 = -2.9097 ± 0.4826
  λ_5 = -3.2138 ± 0.4630
  λ_6 = -3.7359 ± 0.6005
  λ_7 = -4.3113 ± 0.5707
  λ_8 = -5.0572 ± 0.5553
  λ_9 = -5.9379 ± 0.3133
  λ_10 = -6.5742 ± 0.4593
  λ_11 = -6.9434 ± 0.4310
  λ_12 = -7.2369 ± 0.4399
  λ_13 = -7.5647 ± 0.3667
  λ_14 = -7.8415 ± 0.4643
  λ_15 = -8.2581 ± 0.4827
  λ_16 = -8.5497 ± 0.5000
  λ_17 = -8.8833 ± 0.5139
  λ_18 = -9.0481 ± 0.5322
  λ_19 = -9.3047 ± 0.5570
  λ_20 = -9.4766 ± 0.5449
  λ_21 = -9.6733 ± 0.5478
  λ_22 = -9.9962 ± 0.5029
  λ_23 = -10.2588 ± 0.4962
  λ_24 = -10.4388 ± 0.4859
  λ_25 = -10.5746 ± 0.5076
  λ_26 = -10.7115 ± 0.5486
  λ_27 = -10.8121 ± 0.5546
  λ_28 = -10.9437 ± 0.5528
  λ_29 = -11.0546 ± 0.5634
  λ_30 = -11.1578 ± 0.5849
  λ_31 = -11.2839 ± 0.5915
  λ_32 = -11.4355 ± 0.6356
  λ_33 = -11.5756 ± 0.6421
  λ_34 = -11.7775 ± 0.6487
  λ_35 = -11.9759 ± 0.6427
  λ_36 = -12.5310 ± 0.7143
  λ_37 = -12.9584 ± 0.6654
  λ_38 = -13.1221 ± 0.6615
  λ_39 = -13.2645 ± 0.7064
  λ_40 = -13.5367 ± 0.7287
  λ_41 = -13.7049 ± 0.7795
  λ_42 = -13.8580 ± 0.8211
  λ_43 = -14.0019 ± 0.8149
  λ_44 = -14.1134 ± 0.8290
  λ_45 = -14.2344 ± 0.8714
  λ_46 = -14.3744 ± 0.8766
  λ_47 = -14.6202 ± 0.8766
  λ_48 = -14.8086 ± 0.8564
  λ_49 = -14.9839 ± 0.8799
  λ_50 = -15.1507 ± 0.8769
  λ_51 = -15.3075 ± 0.8994
  λ_52 = -15.4553 ± 0.8940
  λ_53 = -15.6353 ± 0.9062
  λ_54 = -15.7758 ± 0.9490
  λ_55 = -15.8898 ± 0.9602
  λ_56 = -16.0144 ± 0.9550
  λ_57 = -16.1188 ± 0.9532
  λ_58 = -16.2668 ± 0.9371
  λ_59 = -16.4311 ± 0.9582
  λ_60 = -16.5667 ± 0.9427
  λ_61 = -16.7446 ± 0.9588
  λ_62 = -16.9334 ± 0.9893
  λ_63 = -17.2163 ± 1.0133
  λ_64 = -17.5263 ± 1.0798
  λ_65 = -17.7489 ± 1.1200
  λ_66 = -17.9373 ± 1.1539
  λ_67 = -18.1872 ± 1.1241
  λ_68 = -18.5153 ± 1.1529
  λ_69 = -18.7381 ± 1.1272
  λ_70 = -18.9047 ± 1.0909
  λ_71 = -19.0773 ± 1.0994
  λ_72 = -19.2268 ± 1.1016
  λ_73 = -19.3637 ± 1.0926
  λ_74 = -19.5143 ± 1.0765
  λ_75 = -19.6871 ± 1.0773
  λ_76 = -19.9229 ± 1.0881
  λ_77 = -20.1603 ± 1.1074
  λ_78 = -20.4171 ± 1.1091
  λ_79 = -20.6616 ± 1.0953
  λ_80 = -20.9325 ± 1.1403
  λ_81 = -21.6812 ± 1.3806
  λ_82 = -22.1840 ± 1.3046
  λ_83 = -22.3870 ± 1.3196
  λ_84 = -22.6261 ± 1.3346
  λ_85 = -22.7810 ± 1.3708
  λ_86 = -23.0027 ± 1.4169
  λ_87 = -23.1765 ± 1.4280
  λ_88 = -23.4124 ± 1.4438
  λ_89 = -23.7302 ± 1.5088
  λ_90 = -24.2417 ± 1.5074
  λ_91 = -24.7733 ± 1.5058
  λ_92 = -25.1706 ± 1.5238
  λ_93 = -25.5026 ± 1.5760
  λ_94 = -25.7800 ± 1.5580
  λ_95 = -25.9937 ± 1.5685
  λ_96 = -26.2770 ± 1.7442
  λ_97 = -26.5356 ± 1.7189
  λ_98 = -26.9300 ± 1.7293
  λ_99 = -27.3242 ± 1.6354
  λ_100 = -27.6195 ± 1.7022
  λ_101 = -27.8446 ± 1.7511
  λ_102 = -28.0418 ± 1.7617
  λ_103 = -28.1664 ± 1.7767
  λ_104 = -28.2874 ± 1.7996
  λ_105 = -28.4377 ± 1.8143
  λ_106 = -28.5828 ± 1.8001
  λ_107 = -28.7671 ± 1.8052
  λ_108 = -29.0398 ± 1.8678
  λ_109 = -29.4635 ± 1.9337
  λ_110 = -29.8236 ± 1.9509
  λ_111 = -30.1807 ± 1.9516
  λ_112 = -30.6284 ± 1.9231
  λ_113 = -30.9017 ± 1.9235
  λ_114 = -31.4151 ± 2.0103
  λ_115 = -31.9798 ± 1.8639
  λ_116 = -32.2127 ± 1.9452
  λ_117 = -32.4187 ± 1.9755
  λ_118 = -32.6145 ± 2.0382
  λ_119 = -32.9726 ± 1.9998
  λ_120 = -33.2839 ± 2.0635
  λ_121 = -33.5509 ± 2.0756
  λ_122 = -33.7887 ± 2.0318
  λ_123 = -34.1633 ± 1.9574
  λ_124 = -34.9360 ± 2.0426
  λ_125 = -35.6370 ± 2.2987
  λ_126 = -36.0449 ± 2.3888
  λ_127 = -38.4216 ± 2.2557
  λ_128 = -39.1965 ± 2.4620
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
Windows: 9 — nMSE min=0.0102, median=0.0115, mean=0.0122, max=0.0153
Computing long trajectory prediction ...
Computing encoder/decoder Jacobians ...
encoder_jacobian: (128, 128, 128)
decoder_jacobian: (128, 128, 128)
Computing amplification loss ...
Amplification loss — True state: 0.004748
Amplification loss — Latent:     0.005116
```

</details>
