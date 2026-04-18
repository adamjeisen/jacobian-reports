# Sweep Analysis: `lorenz_partial_25d_additive_mse_uniform_p30_obsnoise001__vae_kl_lc_sweep`

**Project**: [Lorenz_INDpartial_N25_D1_NormTrue_T3__JacobianODE](https://wandb.ai/JacobianODE/Lorenz_INDpartial_N25_D1_NormTrue_T3__JacobianODE/groups/lorenz_partial_25d_additive_mse_uniform_p30_obsnoise001__vae_kl_lc_sweep)  
**Launched**: 2026-04-17T21:06:15Z  
**Completed**: 2026-04-18T18:30:25Z  
**Outcome**: `complete_clean`  
**Git**: `latent-JacobianODE` @ `5051646`  
**Expected runs**: 64

## Experiment Context

### `lorenz_partial_25d_additive_mse_uniform_p30_obsnoise001__vae_kl_lc_sweep`

**Description**

Same base as lorenz_partial_25d_additive_mse_uniform_p30 with
obs_noise=0.01 and model.use_vae=true. Sweeps kl_dyn_weight over
{1e-4, 1e-3, 1e-2, 1e-1} × kl_null_weight over {null (= coupled to
dyn), 0} × the standard 9-value loop_closure_weight grid (3-D
sweep, 72 runs).

**Hypothesis**

Open question whether adding VAE-style stochasticity to the dyn
latent (regularized by kl_dyn_weight) improves Lyapunov-spectrum
estimation — in particular, whether posterior noise on z_dyn acts
as a helpful implicit ensemble average that stabilizes stable-
direction contraction rate estimates, or instead destabilizes
training through interaction with LPL (known LPL × LC sensitivity
from prior runs) and loop closure.
The null toggle (kl_null=coupled vs 0) separately tests whether
pulling z_null toward zero adds signal on top of dyn regularization
or is redundant once the dyn posterior is constrained.

**Success criteria**

- At some kl_dyn setting, λ_min accuracy improves vs the kl_dyn → 0 limit (or equivalently the existing obsnoise001 baseline)
- Trajectory loss and loop closure don't catastrophically diverge at any kl_dyn × LC cell (beyond the already-known LC=1,10 explosion)
- Detectable, interpretable difference between kl_null=coupled and kl_null=0 (e.g., in null-space RMS or in λ accuracy)

## Results

**Swept axes** (3): `model.kl_dyn_weight`, `model.kl_null_weight`, `training.lightning.loop_closure_weight`

**Chosen run** (by `best_traj_loss`): `woyar9p7` — traj_loss=0.00092, MASE=0.6699, R²=0.9975, LC loss=1.290, epoch=136.0

Swept-axis values at chosen run: `model.kl_dyn_weight`=0.1 · `model.kl_null_weight`=0 · `training.lightning.loop_closure_weight`=0

### Integrity checks

⚠️ **Matched-run count mismatch**: expected 64 run_idx slots per the sentinel, matched 63 in wandb. The sweep may still be in progress, or some slots failed without producing wandb evidence.

**Runs analyzed**: 63 (expected 64)

### Per-run results

| run_idx | run_id | `model.kl_dyn_weight` | `model.kl_null_weight` | `training.lightning.loop_closure_weight` | best_traj_loss | best_MASE | R² | LC loss | epoch |
|---|---|---|---|---|---|---|---|---|---|
| 7 | `woyar9p7` | 0.1 | 0 | 0 | 0.00092 | 0.6699 | 0.9975 | 1.290 | 136.0 |
| 16 | `p38fmyvc` | 1.0e-04 | None | 1.0e-05 | 0.00097 | 0.6715 | 0.9974 | 0.658 | 136.0 |
| 26 | `484c0z3q` | 0.001 | None | 1.0e-04 | 0.00105 | 0.6802 | 0.9972 | 0.135 | 157.0 |
| 29 | `pbwuap66` | 0.01 | 0 | 1.0e-04 | 0.00105 | 0.6790 | 0.9972 | 0.135 | 157.0 |
| 25 | `k2fep9bj` | 1.0e-04 | 0 | 1.0e-04 | 0.00111 | 0.6872 | 0.9970 | 0.166 | 136.0 |
| 9 | `vp290wvr` | 1.0e-04 | 0 | 1.0e-06 | 0.00133 | 0.7237 | 0.9965 | 1.086 | 111.0 |
| 10 | `9zlv6c8f` | 0.001 | None | 1.0e-06 | 0.00133 | 0.7237 | 0.9965 | 1.086 | 111.0 |
| 14 | `3va9k281` | 0.1 | None | 1.0e-06 | 0.00133 | 0.7237 | 0.9965 | 1.086 | 111.0 |
| 4 | `eva1dhi2` | 0.01 | None | 0 | 0.00134 | 0.7218 | 0.9964 | 1.217 | 111.0 |
| 13 | `oekgahlb` | 0.01 | 0 | 1.0e-06 | 0.00138 | 0.7227 | 0.9963 | 1.056 | 112.0 |
| 8 | `yqpugnso` | 1.0e-04 | None | 1.0e-06 | 0.00140 | 0.7237 | 0.9962 | 1.082 | 109.0 |
| 22 | `aoip40y6` | 0.1 | None | 1.0e-05 | 0.00141 | 0.7264 | 0.9962 | 0.695 | 114.0 |
| 0 | `7fbysy29` | 1.0e-04 | None | 0 | 0.00144 | 0.7381 | 0.9961 | 1.048 | 104.0 |
| 1 | `g8o7na1y` | 1.0e-04 | 0 | 0 | 0.00144 | 0.7381 | 0.9961 | 1.048 | 104.0 |
| 2 | `rdj1b28f` | 0.001 | None | 0 | 0.00146 | 0.7449 | 0.9961 | 1.227 | 101.0 |
| 12 | `yxtj4hcl` | 0.01 | None | 1.0e-06 | 0.00147 | 0.7445 | 0.9961 | 1.058 | 93.0 |
| 11 | `3arrmkzt` | 0.001 | 0 | 1.0e-06 | 0.00147 | 0.7460 | 0.9961 | 1.064 | 92.0 |
| 17 | `exgytghz` | 1.0e-04 | 0 | 1.0e-05 | 0.00150 | 0.7511 | 0.9960 | 0.623 | 92.0 |
| 23 | `uj209cig` | 0.1 | 0 | 1.0e-05 | 0.00150 | 0.7511 | 0.9960 | 0.623 | 92.0 |
| 37 | `0vkz7g4e` | 0.01 | 0 | 0.001 | 0.00196 | 0.8182 | 0.9947 | 0.024 | 109.0 |
| 38 | `tojbiomf` | 0.1 | None | 0.001 | 0.00196 | 0.8182 | 0.9947 | 0.024 | 109.0 |
| 40 | `uatzu31i` | 1.0e-04 | None | 0.01 | 0.00198 | 0.8396 | 0.9947 | 0.003 | 162.0 |
| 42 | `r621iqtc` | 0.001 | None | 0.01 | 0.00198 | 0.8396 | 0.9947 | 0.003 | 162.0 |
| 32 | `7e3r2zyx` | 1.0e-04 | None | 0.001 | 0.00205 | 0.8317 | 0.9945 | 0.020 | 104.0 |
| 33 | `cu0sl2nd` | 1.0e-04 | 0 | 0.001 | 0.00205 | 0.8317 | 0.9945 | 0.020 | 104.0 |
| 35 | `97ivioxy` | 0.001 | 0 | 0.001 | 0.00205 | 0.8317 | 0.9945 | 0.020 | 104.0 |
| 36 | `8ivnt3l7` | 0.01 | None | 0.001 | 0.00205 | 0.8317 | 0.9945 | 0.020 | 104.0 |
| 34 | `6wzv3u23` | 0.001 | None | 0.001 | 0.00206 | 0.8401 | 0.9944 | 0.022 | 96.0 |
| 41 | `0kvw66hh` | 1.0e-04 | 0 | 0.01 | 0.00264 | 0.9388 | 0.9929 | 0.003 | 114.0 |
| 45 | `gxdxg4k6` | 0.01 | 0 | 0.01 | 0.00264 | 0.9388 | 0.9929 | 0.003 | 114.0 |
| 44 | `pkxb1ppj` | 0.01 | None | 0.01 | 0.00268 | 0.9388 | 0.9928 | 0.003 | 108.0 |
| 46 | `sahk6vlc` | 0.1 | None | 0.01 | 0.00268 | 0.9388 | 0.9928 | 0.003 | 108.0 |
| 43 | `w4a489s1` | 0.001 | 0 | 0.01 | 0.00268 | 0.9583 | 0.9928 | 0.003 | 101.0 |
| 47 | `271p1dpn` | 0.1 | 0 | 0.01 | 0.00268 | 0.9583 | 0.9928 | 0.003 | 101.0 |
| 6 | `rgf08xme` | 0.1 | None | 0 | 0.00278 | 0.9736 | 0.9925 | 0.822 | 42.0 |
| 39 | `i9qkmp7i` | 0.1 | 0 | 0.001 | 0.00280 | 0.9394 | 0.9925 | 0.018 | 66.0 |
| 27 | `ersc8ygg` | 0.001 | 0 | 1.0e-04 | 0.00314 | 0.9646 | 0.9916 | 0.085 | 48.0 |
| 28 | `2x7ekkqi` | 0.01 | None | 1.0e-04 | 0.00314 | 0.9646 | 0.9916 | 0.085 | 48.0 |
| 31 | `cmwt2hyw` | 0.1 | 0 | 1.0e-04 | 0.00314 | 0.9646 | 0.9916 | 0.085 | 48.0 |
| 50 | `6qm1u6g4` | 0.001 | None | 0.1 | 0.00329 | 1.0512 | 0.9912 | 0.000 | 166.0 |
| 49 | `9pl0onpl` | 1.0e-04 | 0 | 0.1 | 0.00388 | 1.1493 | 0.9896 | 0.001 | 124.0 |
| 53 | `z15ffzqn` | 0.01 | 0 | 0.1 | 0.00396 | 1.1534 | 0.9894 | 0.000 | 130.0 |
| 51 | `yhgos07q` | 0.001 | 0 | 0.1 | 0.00406 | 1.1742 | 0.9891 | 0.001 | 106.0 |
| 18 | `msjbff6m` | 0.001 | None | 1.0e-05 | 0.00412 | 1.1911 | 0.9889 | 0.351 | 23.0 |
| 19 | `vks3fqi1` | 0.001 | 0 | 1.0e-05 | 0.00412 | 1.2027 | 0.9889 | 0.351 | 23.0 |
| 20 | `ttfix0ds` | 0.01 | None | 1.0e-05 | 0.00412 | 1.2027 | 0.9889 | 0.351 | 23.0 |
| 21 | `brw8gnww` | 0.01 | 0 | 1.0e-05 | 0.00412 | 1.2027 | 0.9889 | 0.351 | 23.0 |
| 5 | `u9ycjqgr` | 0.01 | 0 | 0 | 0.00427 | 1.2419 | 0.9885 | 1.015 | 23.0 |
| 60 | `jm2usilb` | 0.01 | None | 1 | 0.00442 | 1.2667 | 0.9881 | 0.000 | 157.0 |
| 61 | `6mn0rfx4` | 0.01 | 0 | 1 | 0.00442 | 1.2667 | 0.9881 | 0.000 | 157.0 |
| 48 | `4d9c1nnz` | 1.0e-04 | None | 0.1 | 0.00454 | 1.2369 | 0.9878 | 0.000 | 102.0 |
| 55 | `59yp2sbp` | 0.1 | 0 | 0.1 | 0.00470 | 1.2386 | 0.9874 | 0.000 | 96.0 |
| 58 | `8o59e2de` | 0.001 | None | 1 | 0.00502 | 1.3605 | 0.9865 | 0.000 | 119.0 |
| 24 | `zshabt0n` | 1.0e-04 | None | 1.0e-04 | 0.00506 | 1.3188 | 0.9864 | 0.076 | 23.0 |
| 52 | `1bnoisgr` | 0.01 | None | 0.1 | 0.00539 | 1.3810 | 0.9856 | 0.001 | 70.0 |
| 62 | `nye1x9uz` | 0.1 | None | 1 | 0.00652 | 1.5714 | 0.9825 | 0.000 | 80.0 |
| 56 | `17c3f7rc` | 1.0e-04 | None | 1 | 0.00864 | 1.8520 | 0.9769 | 0.000 | 62.0 |
| 3 | `hc4garym` | 0.001 | 0 | 0 | 0.01080 | 1.8858 | 0.9712 | 2.381 | 12.0 |
| 63 | `464l19pi` | 0.1 | 0 | 1 | 0.01341 | 2.1859 | 0.9642 | 0.000 | 41.0 |
| 30 | `ttg3nq3e` | 0.1 | None | 1.0e-04 | 0.02243 | 2.5872 | 0.9400 | 0.256 | 7.0 |
| 59 | `f9192hgz` | 0.001 | 0 | 1 | 0.08500 | 5.5989 | 0.7739 | 0.000 | 14.0 |
| 57 | `1sz19nh6` | 1.0e-04 | 0 | 1 | 0.08887 | 5.8889 | 0.7635 | 0.000 | 10.0 |
| 54 | `qxievp33` | 0.1 | None | 0.1 | 0.15758 | 10.7542 | 0.5803 | 0.000 | — |

## Success-criteria verdicts (automated)

| Criterion | Verdict | Note |
|---|---|---|
| At some kl_dyn setting, λ_min accuracy improves vs the kl_dyn → 0 limit (or equivalently the existing obsnoise001 baseline) | **Unknown** |  |
| Trajectory loss and loop closure don't catastrophically diverge at any kl_dyn × LC cell (beyond the already-known LC=1,10 explosion) | **Pass** | Worst LC loss at best_tl = 2.381 |
| Detectable, interpretable difference between kl_null=coupled and kl_null=0 (e.g., in null-space RMS or in λ accuracy) | **Unknown** |  |

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
No run_id provided — selecting best run from group 'lorenz_partial_25d_additive_mse_uniform_p30_obsnoise001__vae_kl_lc_sweep' ...
Found 64 total runs in JacobianODE/Lorenz_INDpartial_N25_D1_NormTrue_T3__JacobianODE (group=lorenz_partial_25d_additive_mse_uniform_p30_obsnoise001__vae_kl_lc_sweep)
All runs (state, loop_closure_weight, tangent_entropy_weight, kl_dyn_weight):
  7fbysy29: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  g8o7na1y: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  rdj1b28f: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  hc4garym: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  eva1dhi2: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  u9ycjqgr: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  rgf08xme: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  woyar9p7: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  9zlv6c8f: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  vp290wvr: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  3arrmkzt: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  yqpugnso: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  oekgahlb: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  yxtj4hcl: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  3va9k281: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  25ngyuvz: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  p38fmyvc: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  exgytghz: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  msjbff6m: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  vks3fqi1: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  brw8gnww: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  ttfix0ds: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  zshabt0n: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  uj209cig: state=crashed, lc=1e-05, te=0.0, kl_dyn=0.0
  484c0z3q: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  k2fep9bj: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  ersc8ygg: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  2x7ekkqi: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  pbwuap66: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  ttg3nq3e: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  cmwt2hyw: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  7e3r2zyx: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  cu0sl2nd: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  6wzv3u23: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  8ivnt3l7: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  97ivioxy: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  0vkz7g4e: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  tojbiomf: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  i9qkmp7i: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  uatzu31i: state=crashed, lc=0.01, te=0.0, kl_dyn=0.0
  0kvw66hh: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  r621iqtc: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  w4a489s1: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  gxdxg4k6: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  pkxb1ppj: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  271p1dpn: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  sahk6vlc: state=crashed, lc=0.01, te=0.0, kl_dyn=0.0
  4d9c1nnz: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  9pl0onpl: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  6qm1u6g4: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  yhgos07q: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  1bnoisgr: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  qxievp33: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  z15ffzqn: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  59yp2sbp: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  1sz19nh6: state=finished, lc=1.0, te=0.0, kl_dyn=0.0
  8o59e2de: state=finished, lc=1.0, te=0.0, kl_dyn=0.0
  17c3f7rc: state=finished, lc=1.0, te=0.0, kl_dyn=0.0
  f9192hgz: state=finished, lc=1.0, te=0.0, kl_dyn=0.0
  nye1x9uz: state=finished, lc=1.0, te=0.0, kl_dyn=0.0
  jm2usilb: state=finished, lc=1.0, te=0.0, kl_dyn=0.0
  6mn0rfx4: state=finished, lc=1.0, te=0.0, kl_dyn=0.0
  464l19pi: state=finished, lc=1.0, te=0.0, kl_dyn=0.0
  aoip40y6: state=crashed, lc=1e-05, te=0.0, kl_dyn=0.0

slurm_timeout_min not found in any run config — falling back to 180 min
  Including 7fbysy29 (lc=0.0): use_all_runs=True (state=finished)
  Including g8o7na1y (lc=0.0): use_all_runs=True (state=finished)
  Including rdj1b28f (lc=0.0): use_all_runs=True (state=finished)
  Including hc4garym (lc=0.0): use_all_runs=True (state=finished)
  Including eva1dhi2 (lc=0.0): use_all_runs=True (state=finished)
  Including u9ycjqgr (lc=0.0): use_all_runs=True (state=finished)
  Including rgf08xme (lc=0.0): use_all_runs=True (state=finished)
  Including woyar9p7 (lc=0.0): use_all_runs=True (state=finished)
  Including 9zlv6c8f (lc=1e-06): use_all_runs=True (state=finished)
  Including vp290wvr (lc=1e-06): use_all_runs=True (state=finished)
  Including 3arrmkzt (lc=1e-06): use_all_runs=True (state=finished)
  Including yqpugnso (lc=1e-06): use_all_runs=True (state=finished)
  Including oekgahlb (lc=1e-06): use_all_runs=True (state=finished)
  Including yxtj4hcl (lc=1e-06): use_all_runs=True (state=finished)
  Including 3va9k281 (lc=1e-06): use_all_runs=True (state=finished)
  Including 25ngyuvz (lc=1e-06): use_all_runs=True (state=finished)
  Including p38fmyvc (lc=1e-05): use_all_runs=True (state=finished)
  Including exgytghz (lc=1e-05): use_all_runs=True (state=finished)
  Including msjbff6m (lc=1e-05): use_all_runs=True (state=finished)
  Including vks3fqi1 (lc=1e-05): use_all_runs=True (state=finished)
  Including brw8gnww (lc=1e-05): use_all_runs=True (state=finished)
  Including ttfix0ds (lc=1e-05): use_all_runs=True (state=finished)
  Including zshabt0n (lc=0.0001): use_all_runs=True (state=finished)
  Including uj209cig (lc=1e-05): use_all_runs=True (state=crashed)
  Including 484c0z3q (lc=0.0001): use_all_runs=True (state=finished)
  Including k2fep9bj (lc=0.0001): use_all_runs=True (state=finished)
  Including ersc8ygg (lc=0.0001): use_all_runs=True (state=finished)
  Including 2x7ekkqi (lc=0.0001): use_all_runs=True (state=finished)
  Including pbwuap66 (lc=0.0001): use_all_runs=True (state=finished)
  Including ttg3nq3e (lc=0.0001): use_all_runs=True (state=finished)
  Including cmwt2hyw (lc=0.0001): use_all_runs=True (state=finished)
  Including 7e3r2zyx (lc=0.001): use_all_runs=True (state=finished)
  Including cu0sl2nd (lc=0.001): use_all_runs=True (state=finished)
  Including 6wzv3u23 (lc=0.001): use_all_runs=True (state=finished)
  Including 8ivnt3l7 (lc=0.001): use_all_runs=True (state=finished)
  Including 97ivioxy (lc=0.001): use_all_runs=True (state=finished)
  Including 0vkz7g4e (lc=0.001): use_all_runs=True (state=finished)
  Including tojbiomf (lc=0.001): use_all_runs=True (state=finished)
  Including i9qkmp7i (lc=0.001): use_all_runs=True (state=finished)
  Including uatzu31i (lc=0.01): use_all_runs=True (state=crashed)
  Including 0kvw66hh (lc=0.01): use_all_runs=True (state=finished)
  Including r621iqtc (lc=0.01): use_all_runs=True (state=finished)
  Including w4a489s1 (lc=0.01): use_all_runs=True (state=finished)
  Including gxdxg4k6 (lc=0.01): use_all_runs=True (state=finished)
  Including pkxb1ppj (lc=0.01): use_all_runs=True (state=finished)
  Including 271p1dpn (lc=0.01): use_all_runs=True (state=finished)
  Including sahk6vlc (lc=0.01): use_all_runs=True (state=crashed)
  Including 4d9c1nnz (lc=0.1): use_all_runs=True (state=finished)
  Including 9pl0onpl (lc=0.1): use_all_runs=True (state=finished)
  Including 6qm1u6g4 (lc=0.1): use_all_runs=True (state=finished)
  Including yhgos07q (lc=0.1): use_all_runs=True (state=finished)
  Including 1bnoisgr (lc=0.1): use_all_runs=True (state=finished)
  Including qxievp33 (lc=0.1): use_all_runs=True (state=finished)
  Including z15ffzqn (lc=0.1): use_all_runs=True (state=finished)
  Including 59yp2sbp (lc=0.1): use_all_runs=True (state=finished)
  Including 1sz19nh6 (lc=1.0): use_all_runs=True (state=finished)
  Including 8o59e2de (lc=1.0): use_all_runs=True (state=finished)
  Including 17c3f7rc (lc=1.0): use_all_runs=True (state=finished)
  Including f9192hgz (lc=1.0): use_all_runs=True (state=finished)
  Including nye1x9uz (lc=1.0): use_all_runs=True (state=finished)
  Including jm2usilb (lc=1.0): use_all_runs=True (state=finished)
  Including 6mn0rfx4 (lc=1.0): use_all_runs=True (state=finished)
  Including 464l19pi (lc=1.0): use_all_runs=True (state=finished)
  Including aoip40y6 (lc=1e-05): use_all_runs=True (state=crashed)
Found 64 effectively-done sweep runs:
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=7fbysy29
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=eva1dhi2
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=g8o7na1y
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=hc4garym
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=rdj1b28f
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=rgf08xme
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=u9ycjqgr
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=woyar9p7
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=25ngyuvz
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=3arrmkzt
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=3va9k281
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=9zlv6c8f
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=oekgahlb
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=vp290wvr
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=yqpugnso
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=yxtj4hcl
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=aoip40y6
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=brw8gnww
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=exgytghz
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=msjbff6m
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=p38fmyvc
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=ttfix0ds
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=uj209cig
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=vks3fqi1
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=2x7ekkqi
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=484c0z3q
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=cmwt2hyw
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=ersc8ygg
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=k2fep9bj
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=pbwuap66
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=ttg3nq3e
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=zshabt0n
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=0vkz7g4e
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=6wzv3u23
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=7e3r2zyx
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=8ivnt3l7
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=97ivioxy
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=cu0sl2nd
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=i9qkmp7i
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=tojbiomf
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=0kvw66hh
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=271p1dpn
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=gxdxg4k6
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=pkxb1ppj
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=r621iqtc
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=sahk6vlc
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=uatzu31i
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=w4a489s1
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=1bnoisgr
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=4d9c1nnz
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=59yp2sbp
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=6qm1u6g4
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=9pl0onpl
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=qxievp33
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=yhgos07q
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=z15ffzqn
  loop_closure_weight=1.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=17c3f7rc
  loop_closure_weight=1.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=1sz19nh6
  loop_closure_weight=1.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=464l19pi
  loop_closure_weight=1.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=6mn0rfx4
  loop_closure_weight=1.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=8o59e2de
  loop_closure_weight=1.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=f9192hgz
  loop_closure_weight=1.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=jm2usilb
  loop_closure_weight=1.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=nye1x9uz
  Dropping 1 run(s) with no checkpoint dir: ['25ngyuvz']
n_dims=25, n_latent=25, n_dyn=3, dt=0.0150
  run=7fbysy29: DiagnosticMetrics(one_step_mase=0.3869808316230774, loop_closure_loss=1.048264503479004, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0014373239828273654) (from cache, n_batches=100)
  run=eva1dhi2: DiagnosticMetrics(one_step_mase=0.4039267301559448, loop_closure_loss=1.2166098356246948, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.001338681555353105) (from cache, n_batches=100)
  run=g8o7na1y: DiagnosticMetrics(one_step_mase=0.3869808316230774, loop_closure_loss=1.048264503479004, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0014373239828273654) (from cache, n_batches=100)
  run=hc4garym: DiagnosticMetrics(one_step_mase=0.6619769334793091, loop_closure_loss=2.3806772232055664, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.010799749754369259) (from cache, n_batches=100)
  run=rdj1b28f: DiagnosticMetrics(one_step_mase=0.39119601249694824, loop_closure_loss=1.227062702178955, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0014568982878699899) (from cache, n_batches=100)
  run=rgf08xme: DiagnosticMetrics(one_step_mase=0.4025774598121643, loop_closure_loss=0.822045087814331, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0027783019468188286) (from cache, n_batches=100)
  run=u9ycjqgr: DiagnosticMetrics(one_step_mase=0.47561559081077576, loop_closure_loss=1.015472412109375, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0042665861546993256) (from cache, n_batches=100)
  run=woyar9p7: DiagnosticMetrics(one_step_mase=0.38817936182022095, loop_closure_loss=1.2898691892623901, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0009220679639838636) (from cache, n_batches=100)
  run=3arrmkzt: DiagnosticMetrics(one_step_mase=0.3903183341026306, loop_closure_loss=1.0639581680297852, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0014690797543153167) (from cache, n_batches=100)
  run=3va9k281: DiagnosticMetrics(one_step_mase=0.4051494002342224, loop_closure_loss=1.0861575603485107, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0013331950176507235) (from cache, n_batches=100)
  run=9zlv6c8f: DiagnosticMetrics(one_step_mase=0.4051494002342224, loop_closure_loss=1.0861575603485107, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0013331950176507235) (from cache, n_batches=100)
  run=oekgahlb: DiagnosticMetrics(one_step_mase=0.40156251192092896, loop_closure_loss=1.0557167530059814, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0013816597638651729) (from cache, n_batches=100)
  run=vp290wvr: DiagnosticMetrics(one_step_mase=0.4051494002342224, loop_closure_loss=1.0861575603485107, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0013331950176507235) (from cache, n_batches=100)
  run=yqpugnso: DiagnosticMetrics(one_step_mase=0.39890238642692566, loop_closure_loss=1.0820763111114502, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0014020070666447282) (from cache, n_batches=100)
  run=yxtj4hcl: DiagnosticMetrics(one_step_mase=0.3901089131832123, loop_closure_loss=1.0575110912322998, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0014653484104201198) (from cache, n_batches=100)
  run=aoip40y6: DiagnosticMetrics(one_step_mase=0.388451486825943, loop_closure_loss=0.6953887939453125, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.001407712115906179) (from cache, n_batches=100)
  run=brw8gnww: DiagnosticMetrics(one_step_mase=0.4685956537723541, loop_closure_loss=0.35088062286376953, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004123499151319265) (from cache, n_batches=100)
  run=exgytghz: DiagnosticMetrics(one_step_mase=0.39065977931022644, loop_closure_loss=0.6232660412788391, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.001500411075539887) (from cache, n_batches=100)
  run=msjbff6m: DiagnosticMetrics(one_step_mase=0.4685956537723541, loop_closure_loss=0.35088062286376953, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004123499151319265) (from cache, n_batches=100)
  run=p38fmyvc: DiagnosticMetrics(one_step_mase=0.38911598920822144, loop_closure_loss=0.658134937286377, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0009650313877500594) (from cache, n_batches=100)
  run=ttfix0ds: DiagnosticMetrics(one_step_mase=0.4685956537723541, loop_closure_loss=0.35088062286376953, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004123499151319265) (from cache, n_batches=100)
  run=uj209cig: DiagnosticMetrics(one_step_mase=0.39065977931022644, loop_closure_loss=0.6232660412788391, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.001500411075539887) (from cache, n_batches=100)
  run=vks3fqi1: DiagnosticMetrics(one_step_mase=0.4685956537723541, loop_closure_loss=0.35088062286376953, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004123499151319265) (from cache, n_batches=100)
  run=2x7ekkqi: DiagnosticMetrics(one_step_mase=0.41675394773483276, loop_closure_loss=0.08489125967025757, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0031365836039185524) (from cache, n_batches=100)
  run=484c0z3q: DiagnosticMetrics(one_step_mase=0.38378655910491943, loop_closure_loss=0.13548998534679413, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0010451687267050147) (from cache, n_batches=100)
  run=cmwt2hyw: DiagnosticMetrics(one_step_mase=0.41675394773483276, loop_closure_loss=0.08489125967025757, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0031365836039185524) (from cache, n_batches=100)
  run=ersc8ygg: DiagnosticMetrics(one_step_mase=0.41675394773483276, loop_closure_loss=0.08489125967025757, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0031365836039185524) (from cache, n_batches=100)
  run=k2fep9bj: DiagnosticMetrics(one_step_mase=0.3904956579208374, loop_closure_loss=0.16606086492538452, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0011060986435040832) (from cache, n_batches=100)
  run=pbwuap66: DiagnosticMetrics(one_step_mase=0.38378655910491943, loop_closure_loss=0.13548998534679413, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0010451687267050147) (from cache, n_batches=100)
  run=ttg3nq3e: DiagnosticMetrics(one_step_mase=0.999679684638977, loop_closure_loss=0.255731999874115, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.022427380084991455) (from cache, n_batches=100)
  run=zshabt0n: DiagnosticMetrics(one_step_mase=0.46656540036201477, loop_closure_loss=0.07624845206737518, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005060472525656223) (from cache, n_batches=100)
  run=0vkz7g4e: DiagnosticMetrics(one_step_mase=0.3970675468444824, loop_closure_loss=0.02352321147918701, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0019610796589404345) (from cache, n_batches=100)
  run=6wzv3u23: DiagnosticMetrics(one_step_mase=0.4034833610057831, loop_closure_loss=0.022446054965257645, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0020628052297979593) (from cache, n_batches=100)
  run=7e3r2zyx: DiagnosticMetrics(one_step_mase=0.3971720337867737, loop_closure_loss=0.02042379416525364, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0020534340292215347) (from cache, n_batches=100)
  run=8ivnt3l7: DiagnosticMetrics(one_step_mase=0.3971720337867737, loop_closure_loss=0.02042379416525364, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0020534340292215347) (from cache, n_batches=100)
  run=97ivioxy: DiagnosticMetrics(one_step_mase=0.3971720337867737, loop_closure_loss=0.02042379416525364, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0020534340292215347) (from cache, n_batches=100)
  run=cu0sl2nd: DiagnosticMetrics(one_step_mase=0.3971720337867737, loop_closure_loss=0.02042379416525364, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0020534340292215347) (from cache, n_batches=100)
  run=i9qkmp7i: DiagnosticMetrics(one_step_mase=0.399803102016449, loop_closure_loss=0.01845659874379635, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.002796090906485915) (from cache, n_batches=100)
  run=tojbiomf: DiagnosticMetrics(one_step_mase=0.3970675468444824, loop_closure_loss=0.02352321147918701, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0019610796589404345) (from cache, n_batches=100)
  run=0kvw66hh: DiagnosticMetrics(one_step_mase=0.41049808263778687, loop_closure_loss=0.003413381287828088, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0026409064885228872) (from cache, n_batches=100)
  run=271p1dpn: DiagnosticMetrics(one_step_mase=0.42168691754341125, loop_closure_loss=0.0032091005705296993, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0026790655683726072) (from cache, n_batches=100)
  run=gxdxg4k6: DiagnosticMetrics(one_step_mase=0.41049808263778687, loop_closure_loss=0.003413381287828088, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0026409064885228872) (from cache, n_batches=100)
  run=pkxb1ppj: DiagnosticMetrics(one_step_mase=0.40122172236442566, loop_closure_loss=0.0028395431581884623, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.002677427139133215) (from cache, n_batches=100)
  run=r621iqtc: DiagnosticMetrics(one_step_mase=0.39307647943496704, loop_closure_loss=0.0025188936851918697, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.001982414862141013) (from cache, n_batches=100)
  run=sahk6vlc: DiagnosticMetrics(one_step_mase=0.40122172236442566, loop_closure_loss=0.0028395431581884623, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.002677427139133215) (from cache, n_batches=100)
  run=uatzu31i: DiagnosticMetrics(one_step_mase=0.39307647943496704, loop_closure_loss=0.0025188936851918697, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.001982414862141013) (from cache, n_batches=100)
  run=w4a489s1: DiagnosticMetrics(one_step_mase=0.42168691754341125, loop_closure_loss=0.0032091005705296993, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0026790655683726072) (from cache, n_batches=100)
  run=1bnoisgr: DiagnosticMetrics(one_step_mase=0.4300001561641693, loop_closure_loss=0.0006902347668074071, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0053939963690936565) (from cache, n_batches=100)
  run=4d9c1nnz: DiagnosticMetrics(one_step_mase=0.47221583127975464, loop_closure_loss=0.0003819532284978777, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0045369272120296955) (from cache, n_batches=100)
  run=59yp2sbp: DiagnosticMetrics(one_step_mase=0.4172241985797882, loop_closure_loss=0.0002944920852314681, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004700945224612951) (from cache, n_batches=100)
  run=6qm1u6g4: DiagnosticMetrics(one_step_mase=0.4083031713962555, loop_closure_loss=0.00032821594504639506, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0032906504347920418) (from cache, n_batches=100)
  run=9pl0onpl: DiagnosticMetrics(one_step_mase=0.42354482412338257, loop_closure_loss=0.0005852364702150226, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.003881216747686267) (from cache, n_batches=100)
  run=qxievp33: DiagnosticMetrics(one_step_mase=4.602756023406982, loop_closure_loss=0.0001914576132548973, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.15758392214775085) (from cache, n_batches=100)
  run=yhgos07q: DiagnosticMetrics(one_step_mase=0.43008196353912354, loop_closure_loss=0.000507631222717464, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004056598991155624) (from cache, n_batches=100)
  run=z15ffzqn: DiagnosticMetrics(one_step_mase=0.40854960680007935, loop_closure_loss=0.00028863464831374586, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.003957892768085003) (from cache, n_batches=100)
  run=17c3f7rc: DiagnosticMetrics(one_step_mase=0.47996047139167786, loop_closure_loss=0.00026949585299007595, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.008635932579636574) (from cache, n_batches=100)
  run=1sz19nh6: DiagnosticMetrics(one_step_mase=0.7231795191764832, loop_closure_loss=2.150908130715834e-06, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.08887294679880142) (from cache, n_batches=100)
  run=464l19pi: DiagnosticMetrics(one_step_mase=0.49543794989585876, loop_closure_loss=3.500767343211919e-05, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.013408510945737362) (from cache, n_batches=100)
  run=6mn0rfx4: DiagnosticMetrics(one_step_mase=0.4279318153858185, loop_closure_loss=6.48333880235441e-05, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004423497244715691) (from cache, n_batches=100)
  run=8o59e2de: DiagnosticMetrics(one_step_mase=0.4330974817276001, loop_closure_loss=5.992245496599935e-05, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005015549249947071) (from cache, n_batches=100)
  run=f9192hgz: DiagnosticMetrics(one_step_mase=0.6519649028778076, loop_closure_loss=1.7884171938931104e-06, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.08500079065561295) (from cache, n_batches=100)
  run=jm2usilb: DiagnosticMetrics(one_step_mase=0.4279318153858185, loop_closure_loss=6.48333880235441e-05, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004423497244715691) (from cache, n_batches=100)
  run=nye1x9uz: DiagnosticMetrics(one_step_mase=0.47074559330940247, loop_closure_loss=9.489760850556195e-05, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.006516226101666689) (from cache, n_batches=100)

Ranking method:           best_traj_loss
Best run ID:              woyar9p7
Best loop_closure_weight: 0.0
Best tangent_entropy_weight: 0.0
Best kl_dyn_weight:       0.0
Best traj loss:           0.000922
Criteria applied: ['C1', 'C2', 'C3']
Surviving: 62 / 63
Auto-selected run_id: woyar9p7

======================================================================
PARETO FRONTIER RUNS (15 runs)
======================================================================
  Run ID               LC Loss   Traj Val Loss
  ------------  --------------  --------------
  f9192hgz            0.000002        0.085001
  464l19pi            0.000035        0.013409
  8o59e2de            0.000060        0.005016
  6mn0rfx4            0.000065        0.004423
  jm2usilb            0.000065        0.004423
  z15ffzqn            0.000289        0.003958
  6qm1u6g4            0.000328        0.003291
  r621iqtc            0.002519        0.001982
  uatzu31i            0.002519        0.001982
  0vkz7g4e            0.023523        0.001961
  tojbiomf            0.023523        0.001961
  484c0z3q            0.135490        0.001045
  pbwuap66            0.135490        0.001045
  p38fmyvc            0.658135        0.000965
  woyar9p7            1.289869        0.000922 <-- selected

======================================================================
RANKING METHOD COMPARISON (over 62 survivors)
======================================================================
  Method                  Run ID               LC Loss   Traj Val Loss
  ----------------------  ------------  --------------  --------------
  best_traj_loss          woyar9p7            1.289869        0.000922 <-- active
  pareto_knee             z15ffzqn            0.000289        0.003958
  geo_rank                woyar9p7            1.289869        0.000922
  minimax_rank            r621iqtc            0.002519        0.001982
  geo_log_score           woyar9p7            1.289869        0.000922
  minimax_log_score       6mn0rfx4            0.000065        0.004423
======================================================================

Loading run woyar9p7 from JacobianODE/Lorenz_INDpartial_N25_D1_NormTrue_T3__JacobianODE ...
Train dataset shape: torch.Size([24882, 45, 25])
Validation dataset shape: torch.Size([7917, 45, 25])
Test dataset shape: torch.Size([3393, 45, 25])
Train trajectories dataset shape: torch.Size([22, 1176, 25])
Validation trajectories dataset shape: torch.Size([7, 1176, 25])
Test trajectories dataset shape: torch.Size([3, 1176, 25])
Loading checkpoint epoch=136-step=27400.ckpt...
Computing reconstruction ...
Computing MASE ...
Teacher-forced MASE: 0.3930
Free-running MASE:   0.5291
Computing latent utilization ...
Entropy-based utilization: 0.955
Null subspace mean RMS: 1.560927e-02
Computing Lyapunov exponents ...
  Computing full-trajectory Lyapunov (3 test trajs, T=1176) ...
Predicted Lyapunov exponents (batch+burn-in, 128 windowed trajs):
  λ_1 = +0.3180 ± 0.4503
  λ_2 = -0.4482 ± 0.6187
  λ_3 = -12.3565 ± 1.5677
Predicted Lyapunov exponents (full-length, 3 test trajs):
  λ_1 = +0.2363 ± 0.0747
  λ_2 = -0.2168 ± 0.1113
  λ_3 = -12.7030 ± 0.0421
Empirical Lyapunov exponents (mean ± std):
  λ_1 = +0.3846 ± 0.0251
  λ_2 = -0.1716 ± 0.0444
  λ_3 = -13.8799 ± 0.0398
Mean KY dim (predicted): 1.979 ± 0.031
Mean KY dim (empirical): 2.015 ± 0.002
Mean KY dim (burn-in):   1.594 ± 0.459
Computing prediction windows ...
Windows: 114 — nMSE min=0.0008, median=0.0017, mean=0.0029, max=0.0818
Computing long trajectory prediction ...
Computing encoder/decoder Jacobians ...
encoder_jacobian: (128, 25, 25)
decoder_jacobian: (128, 25, 25)
Computing amplification loss ...
Amplification loss — True state: 0.000221
Amplification loss — Latent:     0.000321
```

</details>
