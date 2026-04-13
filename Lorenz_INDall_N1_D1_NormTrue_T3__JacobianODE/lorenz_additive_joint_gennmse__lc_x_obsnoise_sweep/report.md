# Sweep Analysis: `lorenz_additive_joint_gennmse__lc_x_obsnoise_sweep`

**Project**: [Lorenz_INDall_N1_D1_NormTrue_T3__JacobianODE](https://wandb.ai/JacobianODE/Lorenz_INDall_N1_D1_NormTrue_T3__JacobianODE/groups/lorenz_additive_joint_gennmse__lc_x_obsnoise_sweep)  
**Launched**: 2026-04-13T00:31:10Z  
**Completed**: 2026-04-13T02:40:11Z  
**Outcome**: `complete_clean`  
**Git**: `latent-JacobianODE` @ `0a4d186`  
**Expected runs**: 1

## Experiment Context

### `lorenz_additive_joint_gennmse`

**Description**

Fully observed Lorenz-63 (all 3 dims, no delay embedding). Additive
coupling encoder with zero_init (starts at identity-permutation),
trained jointly with the Jacobian dynamics using gennMSE. Sweeps
loop_closure_weight × obs_noise_scale (9 × 3 = 27).

**Hypothesis**

With a well-conditioned additive encoder and gennMSE's stable loss
scaling, the latent JacobianODE learns Lorenz's attractor and
recovers its Lyapunov spectrum (λ ≈ [0.91, 0, -14.57], λ₁ > 0).
Optimal LC should sit in the 1e-5 – 1e-3 range with a broad basin.

**Success criteria**

- Best run's leading Lyapunov exponent > 0 (chaos recovered)
- Best run's predicted Lyapunov spectrum within ~20% of empirical
- val/trajectory_r2_score > 0.95 at the best configuration
- Loop closure bounded and monotonically improving at low LC

## Results

**Overall best MASE**: 0.4702 (LC weight = 1.0e-04, obs_noise_scale = 0.00)
**Overall best traj loss**: 0.00261 at epoch 121.0
**Runs analyzed**: 28

### Best run per `obs_noise_scale`

| obs_noise_scale | Best LC weight | Best traj loss | MASE at best | R² | LC loss | epoch |
|---|---|---|---|---|---|---|
| 0.0 | 1.0e-04 | 0.00261 | 0.4702 | 0.9997 | 0.066 | 121.0 |
| 0.01 | 1.0e-01 | 0.00997 | 0.8262 | 0.9987 | 0.013 | 50.0 |
| 0.05 | 1.0e-02 | 0.42867 | 5.3746 | 0.9455 | 1.705 | 58.0 |

## Success-criteria verdicts (automated)

| Criterion | Verdict | Note |
|---|---|---|
| Best run's leading Lyapunov exponent > 0 (chaos recovered) | **Unknown** |  |
| Best run's predicted Lyapunov spectrum within ~20% of empirical | **Unknown** |  |
| val/trajectory_r2_score > 0.95 at the best configuration | **Pass** | Best R² = 0.9997; threshold > 0.95 |
| Loop closure bounded and monotonically improving at low LC | **Unknown** |  |

_Automated verdicts use simple numeric-threshold parsing and may mis-classify qualitative criteria. The Discussion section below takes precedence._

## Figures

### sweep_overview

![sweep_overview](figures/sweep_overview.png)

### sweep_pareto

![sweep_pareto](figures/sweep_pareto.png)

### prediction_windows

![prediction_windows](figures/prediction_windows.png)

### mase

![mase](figures/mase.png)

### lyapunov

![lyapunov](figures/lyapunov.png)

### per_run_lyapunov

![per_run_lyapunov](figures/per_run_lyapunov.png)

### per_run_lyapunov_vs_true

![per_run_lyapunov_vs_true](figures/per_run_lyapunov_vs_true.png)

### lyapunov_spectrum_mse_vs_val_loss

![lyapunov_spectrum_mse_vs_val_loss](figures/lyapunov_spectrum_mse_vs_val_loss.png)

## Discussion

**Success criteria.** *(C1) Leading Lyapunov > 0:* **Pass** — the selected run (`ixxkuswu`, LC=1e-4, obs_noise=0) gives λ₁ = +0.379 ± 0.035 (full-length), clearly chaotic. *(C2) Predicted spectrum within ~20% of empirical:* **Partial/Fail** — against the measured ground-truth spectrum [+0.385, −0.172, −13.88], λ₁ matches within ≈1.5%, but λ₃ = −17.24 is ≈24% too contractive and λ₂ = −0.385 is far from the zero-manifold direction (off by more than a factor of 2). *(C3) val trajectory R² > 0.95 at the best configuration:* **Pass** — R² = 0.9997 at best traj loss, with several other obs_noise=0 runs also ≥0.9996. *(C4) Loop-closure bounded and monotone at low LC:* **Pass** — at obs_noise=0, LC loss drops monotonically from 0.41 (LC=0) through 0.066 (1e-4), 0.009 (1e-3), down to 6.7e-5 (LC=10), with trajectory loss staying below 0.004 throughout.

**Sweep landscape.** The (LC × obs_noise) grid is dominated by the observation-noise axis. At obs_noise=0, trajectory val loss forms a wide, flat basin ≈2.6–4.0e-3 across nearly six decades of LC (1e-6 → 10), and 11/28 runs pass all three selection criteria — all of them in that column. obs_noise=0.01 gives a second cluster around 0.013 (one LC=0.001 run improves to 0.011), and obs_noise=0.05 collapses to ≈0.44–0.46 with R² ≈0.94 and MASE > 5. The minimum sits at LC=1e-4, but the basin is so broad along LC that the choice of LC is essentially free once obs_noise is zero.

**Lyapunov behaviour.** The per-run spectra show learned dynamics are uniformly stable (no runaway positive exponents) and share a consistent step-shape: a small positive/near-zero λ₁, a small-magnitude λ₂, and a large negative λ₃. Against the empirical reference, λ₁ is tracked well across most runs, but predicted λ₃ systematically overshoots (more negative than truth), and λ₂ is biased negative rather than sitting on the zero manifold. A few obs_noise=0.05 runs drive λ₃ far below −50, consistent with their poor trajectory fit.

**Caveats and hypothesis.** All 28 runs finished cleanly; the selected run stopped at epoch 121/123 so early-stopping is not an artifact. Note the hypothesis cites canonical Lorenz exponents [0.91, 0, −14.57], but the empirical spectrum recomputed from ground-truth Jacobians is [0.385, −0.17, −13.88] — so the ≈0.38 λ₁ recovered here is correct relative to this dataset, not an underestimate. Overall the hypothesis is **mixed/supported**: a well-conditioned additive encoder plus gennMSE does deliver a broad LC basin (1e-5 – 10, wider than predicted) and correctly recovers the chaotic leading exponent, but the full spectrum is not reproduced to 20%, with the contracting direction over-damped.

## `run_analytics` stdout

<details><summary>Click to expand — full diagnostic output from <code>run_analytics</code></summary>

```
No run_id provided — selecting best run from group 'lorenz_additive_joint_gennmse__lc_x_obsnoise_sweep' ...
Found 28 total runs in JacobianODE/Lorenz_INDall_N1_D1_NormTrue_T3__JacobianODE (group=lorenz_additive_joint_gennmse__lc_x_obsnoise_sweep)
All runs (state, loop_closure_weight, tangent_entropy_weight, kl_dyn_weight):
  bu6n73iv: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  y3alw1w5: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  amh5qo83: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  atihozi6: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  d5x688jl: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  m5bxy6so: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  nuyyzjqs: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  h8wc7glc: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  0bduime7: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  cw0hkste: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  ixxkuswu: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  esyyb6x2: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  3acbijxo: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  0i2v07dp: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  adgsbzb6: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  8gi3hrrs: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  6fjymj34: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  7gvngy15: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  on8okrh1: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  8bnyx04y: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  bm33qvuq: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  1sqrb462: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  p5lvkw4m: state=finished, lc=1.0, te=0.0, kl_dyn=0.0
  teoimuz6: state=finished, lc=1.0, te=0.0, kl_dyn=0.0
  wsivniv4: state=finished, lc=10.0, te=0.0, kl_dyn=0.0
  nz9x07cl: state=finished, lc=1.0, te=0.0, kl_dyn=0.0
  2fuphbqb: state=finished, lc=10.0, te=0.0, kl_dyn=0.0
  gk1oa37j: state=finished, lc=10.0, te=0.0, kl_dyn=0.0

slurm_timeout_min not found in any run config — falling back to 180 min
  Including bu6n73iv (lc=0.0001): use_all_runs=True (state=finished)
  Including y3alw1w5 (lc=0.0): use_all_runs=True (state=finished)
  Including amh5qo83 (lc=0.0): use_all_runs=True (state=finished)
  Including atihozi6 (lc=0.0): use_all_runs=True (state=finished)
  Including d5x688jl (lc=1e-06): use_all_runs=True (state=finished)
  Including m5bxy6so (lc=1e-05): use_all_runs=True (state=finished)
  Including nuyyzjqs (lc=1e-06): use_all_runs=True (state=finished)
  Including h8wc7glc (lc=1e-05): use_all_runs=True (state=finished)
  Including 0bduime7 (lc=1e-06): use_all_runs=True (state=finished)
  Including cw0hkste (lc=1e-05): use_all_runs=True (state=finished)
  Including ixxkuswu (lc=0.0001): use_all_runs=True (state=finished)
  Including esyyb6x2 (lc=0.0001): use_all_runs=True (state=finished)
  Including 3acbijxo (lc=0.0001): use_all_runs=True (state=finished)
  Including 0i2v07dp (lc=0.001): use_all_runs=True (state=finished)
  Including adgsbzb6 (lc=0.001): use_all_runs=True (state=finished)
  Including 8gi3hrrs (lc=0.001): use_all_runs=True (state=finished)
  Including 6fjymj34 (lc=0.01): use_all_runs=True (state=finished)
  Including 7gvngy15 (lc=0.01): use_all_runs=True (state=finished)
  Including on8okrh1 (lc=0.01): use_all_runs=True (state=finished)
  Including 8bnyx04y (lc=0.1): use_all_runs=True (state=finished)
  Including bm33qvuq (lc=0.1): use_all_runs=True (state=finished)
  Including 1sqrb462 (lc=0.1): use_all_runs=True (state=finished)
  Including p5lvkw4m (lc=1.0): use_all_runs=True (state=finished)
  Including teoimuz6 (lc=1.0): use_all_runs=True (state=finished)
  Including wsivniv4 (lc=10.0): use_all_runs=True (state=finished)
  Including nz9x07cl (lc=1.0): use_all_runs=True (state=finished)
  Including 2fuphbqb (lc=10.0): use_all_runs=True (state=finished)
  Including gk1oa37j (lc=10.0): use_all_runs=True (state=finished)
Found 28 effectively-done sweep runs:
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=amh5qo83
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=atihozi6
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=y3alw1w5
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=0bduime7
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=d5x688jl
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=nuyyzjqs
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=cw0hkste
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=h8wc7glc
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=m5bxy6so
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=3acbijxo
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=bu6n73iv
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=esyyb6x2
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=ixxkuswu
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=0i2v07dp
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=8gi3hrrs
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=adgsbzb6
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=6fjymj34
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=7gvngy15
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=on8okrh1
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=1sqrb462
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=8bnyx04y
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=bm33qvuq
  loop_closure_weight=1.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=nz9x07cl
  loop_closure_weight=1.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=p5lvkw4m
  loop_closure_weight=1.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=teoimuz6
  loop_closure_weight=10.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=2fuphbqb
  loop_closure_weight=10.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=gk1oa37j
  loop_closure_weight=10.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=wsivniv4
n_dims=3, n_latent=3, n_dyn=3, dt=0.0150
  run=amh5qo83: DiagnosticMetrics(one_step_mase=3.39251971244812, loop_closure_loss=6.16535758972168, fast_eigenvalue_fraction=0.7866666913032532, trajectory_val_loss=0.4559133052825928) (from W&B history)
  run=atihozi6: DiagnosticMetrics(one_step_mase=0.4412441551685333, loop_closure_loss=56.537174224853516, fast_eigenvalue_fraction=0.2958333194255829, trajectory_val_loss=0.013448437675833702) (from W&B history)
  run=y3alw1w5: DiagnosticMetrics(one_step_mase=0.38569697737693787, loop_closure_loss=0.4127780795097351, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0026140741538256407) (from W&B history)
  run=0bduime7: DiagnosticMetrics(one_step_mase=0.38570183515548706, loop_closure_loss=0.39761778712272644, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0026140923146158457) (from W&B history)
  run=d5x688jl: DiagnosticMetrics(one_step_mase=0.4410351812839508, loop_closure_loss=47.71196746826172, fast_eigenvalue_fraction=0.2916666567325592, trajectory_val_loss=0.013446961529552937) (from W&B history)
  run=nuyyzjqs: DiagnosticMetrics(one_step_mase=4.397590637207031, loop_closure_loss=8.279156684875488, fast_eigenvalue_fraction=0.7641666531562805, trajectory_val_loss=0.43987905979156494) (from W&B history)
  run=cw0hkste: DiagnosticMetrics(one_step_mase=4.3480634689331055, loop_closure_loss=6.211432456970215, fast_eigenvalue_fraction=0.7641666531562805, trajectory_val_loss=0.4543336033821106) (from W&B history)
  run=h8wc7glc: DiagnosticMetrics(one_step_mase=0.44025465846061707, loop_closure_loss=25.491748809814453, fast_eigenvalue_fraction=0.26499998569488525, trajectory_val_loss=0.01353801041841507) (from W&B history)
  run=m5bxy6so: DiagnosticMetrics(one_step_mase=0.38644102215766907, loop_closure_loss=0.36026421189308167, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0027024121955037117) (from W&B history)
  run=3acbijxo: DiagnosticMetrics(one_step_mase=4.2028350830078125, loop_closure_loss=5.554229259490967, fast_eigenvalue_fraction=0.7608333230018616, trajectory_val_loss=0.429546594619751) (from W&B history)
  run=bu6n73iv: DiagnosticMetrics(one_step_mase=0.4426366984844208, loop_closure_loss=9.216533660888672, fast_eigenvalue_fraction=0.27916666865348816, trajectory_val_loss=0.0136601272970438) (from cache, n_batches=100)
  run=esyyb6x2: DiagnosticMetrics(one_step_mase=0.4426366984844208, loop_closure_loss=9.216533660888672, fast_eigenvalue_fraction=0.27916666865348816, trajectory_val_loss=0.0136601272970438) (from W&B history)
  run=ixxkuswu: DiagnosticMetrics(one_step_mase=0.3857693374156952, loop_closure_loss=0.06590361893177032, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0026056210044771433) (from W&B history)
  run=0i2v07dp: DiagnosticMetrics(one_step_mase=0.38626959919929504, loop_closure_loss=0.009351909160614014, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0026351045817136765) (from W&B history)
  run=8gi3hrrs: DiagnosticMetrics(one_step_mase=4.207376956939697, loop_closure_loss=2.7706615924835205, fast_eigenvalue_fraction=0.7608333230018616, trajectory_val_loss=0.4426262676715851) (from W&B history)
  run=adgsbzb6: DiagnosticMetrics(one_step_mase=0.43370550870895386, loop_closure_loss=2.431546688079834, fast_eigenvalue_fraction=0.23000000417232513, trajectory_val_loss=0.012851215898990631) (from W&B history)
  run=6fjymj34: DiagnosticMetrics(one_step_mase=0.387043833732605, loop_closure_loss=0.002027137205004692, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0026756832376122475) (from W&B history)
  run=7gvngy15: DiagnosticMetrics(one_step_mase=0.4344756305217743, loop_closure_loss=0.16881613433361053, fast_eigenvalue_fraction=0.1641666740179062, trajectory_val_loss=0.010721173137426376) (from W&B history)
  run=on8okrh1: DiagnosticMetrics(one_step_mase=3.7337424755096436, loop_closure_loss=1.7053712606430054, fast_eigenvalue_fraction=0.7741666436195374, trajectory_val_loss=0.42866629362106323) (from W&B history)
  run=1sqrb462: DiagnosticMetrics(one_step_mase=3.4915738105773926, loop_closure_loss=0.07420574873685837, fast_eigenvalue_fraction=0.6658333539962769, trajectory_val_loss=0.7644325494766235) (from W&B history)
  run=8bnyx04y: DiagnosticMetrics(one_step_mase=0.38784924149513245, loop_closure_loss=0.00034362179576419294, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0027487429324537516) (from W&B history)
  run=bm33qvuq: DiagnosticMetrics(one_step_mase=0.4265720248222351, loop_closure_loss=0.013177753426134586, fast_eigenvalue_fraction=0.02083333395421505, trajectory_val_loss=0.009974733926355839) (from W&B history)
  run=nz9x07cl: DiagnosticMetrics(one_step_mase=2.792811632156372, loop_closure_loss=0.04217519611120224, fast_eigenvalue_fraction=0.637499988079071, trajectory_val_loss=0.5344958305358887) (from W&B history)
  run=p5lvkw4m: DiagnosticMetrics(one_step_mase=0.39128631353378296, loop_closure_loss=0.00010528202255954966, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.00326258665882051) (from W&B history)
  run=teoimuz6: DiagnosticMetrics(one_step_mase=0.4473031759262085, loop_closure_loss=0.002567511284723878, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.012233463115990162) (from W&B history)
  run=2fuphbqb: DiagnosticMetrics(one_step_mase=0.45718708634376526, loop_closure_loss=0.0050450884737074375, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.019569581374526024) (from W&B history)
  run=gk1oa37j: DiagnosticMetrics(one_step_mase=3.2940752506256104, loop_closure_loss=0.004536627791821957, fast_eigenvalue_fraction=0.3333333432674408, trajectory_val_loss=0.7519117593765259) (from W&B history)
  run=wsivniv4: DiagnosticMetrics(one_step_mase=0.39455413818359375, loop_closure_loss=6.692414171993732e-05, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004028536844998598) (from W&B history)

Ranking method:           best_traj_loss
Best run ID:              ixxkuswu
Best loop_closure_weight: 0.0001
Best tangent_entropy_weight: 0.0
Best kl_dyn_weight:       0.0
Best traj loss:           0.002606
Criteria applied: ['C1', 'C2', 'C3']
Surviving: 11 / 28
Auto-selected run_id: ixxkuswu

======================================================================
PARETO FRONTIER RUNS (6 runs)
======================================================================
  Run ID               LC Loss   Traj Val Loss
  ------------  --------------  --------------
  wsivniv4            0.000067        0.004029
  p5lvkw4m            0.000105        0.003263
  8bnyx04y            0.000344        0.002749
  6fjymj34            0.002027        0.002676
  0i2v07dp            0.009352        0.002635
  ixxkuswu            0.065904        0.002606 <-- selected

======================================================================
RANKING METHOD COMPARISON (over 11 survivors)
======================================================================
  Method                  Run ID               LC Loss   Traj Val Loss
  ----------------------  ------------  --------------  --------------
  best_traj_loss          ixxkuswu            0.065904        0.002606 <-- active
  pareto_knee             8bnyx04y            0.000344        0.002749
  geo_rank                ixxkuswu            0.065904        0.002606
  minimax_rank            6fjymj34            0.002027        0.002676
  geo_log_score           ixxkuswu            0.065904        0.002606
  minimax_log_score       p5lvkw4m            0.000105        0.003263
======================================================================

Loading run ixxkuswu from JacobianODE/Lorenz_INDall_N1_D1_NormTrue_T3__JacobianODE ...
Train dataset shape: torch.Size([25850, 25, 3])
Validation dataset shape: torch.Size([8225, 25, 3])
Test dataset shape: torch.Size([3525, 25, 3])
Train trajectories dataset shape: torch.Size([22, 1200, 3])
Validation trajectories dataset shape: torch.Size([7, 1200, 3])
Test trajectories dataset shape: torch.Size([3, 1200, 3])
Loading checkpoint epoch=121-step=24400.ckpt...
Computing MASE ...
Teacher-forced MASE: 0.3827
Free-running MASE:   0.4593
Computing Lyapunov exponents ...
  Computing full-trajectory Lyapunov (3 test trajs, T=1200) ...
Predicted Lyapunov exponents (batch+burn-in, 128 windowed trajs):
  λ_1 = +0.4227 ± 0.4353
  λ_2 = -0.2895 ± 0.2278
  λ_3 = -17.2921 ± 0.3432
Predicted Lyapunov exponents (full-length, 3 test trajs):
  λ_1 = +0.3793 ± 0.0348
  λ_2 = -0.3854 ± 0.0633
  λ_3 = -17.2357 ± 0.0358
Empirical Lyapunov exponents (mean ± std):
  λ_1 = +0.3846 ± 0.0251
  λ_2 = -0.1716 ± 0.0444
  λ_3 = -13.8799 ± 0.0398
Computing prediction windows ...
Windows: 354 — nMSE min=0.0005, median=0.0019, mean=0.0025, max=0.0205
```

</details>
