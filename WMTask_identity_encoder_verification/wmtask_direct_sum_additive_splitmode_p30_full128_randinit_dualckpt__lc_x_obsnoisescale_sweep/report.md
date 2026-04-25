# Sweep Analysis: `wmtask_direct_sum_additive_splitmode_p30_full128_randinit_dualckpt__lc_x_obsnoisescale_sweep`

**Project**: [WMTask_identity_encoder_verification](https://wandb.ai/JacobianODE/WMTask_identity_encoder_verification/groups/wmtask_direct_sum_additive_splitmode_p30_full128_randinit_dualckpt__lc_x_obsnoisescale_sweep)  
**Launched**: 2026-04-24T16:50:11Z  
**Completed**: 2026-04-24T23:55:17Z  
**Outcome**: `complete_clean`  
**Git**: `latent-JacobianODE` @ `d4238f4`  
**Expected runs**: 21

## Experiment Context

### `wmtask_direct_sum_additive_splitmode_p30_full128_randinit_dualckpt__lc_x_obsnoisescale_sweep`

**Description**

WMTask fully-observed (N1=N2=64), latent JacobianODE with DirectSum
coupling encoder, 128->128 (no null subspace). 21-run sweep over
7 LC × 3 obs_noise_scale. RANDOM init per area
(final_perm_identity=false). Additive coupling. Split-mode loss.
Dual checkpoint: primary ES at patience=5, shadow-freeze at patience=2.

**Hypothesis**

Isolates the two known training-config differences from the reference
monolithic wmtask_latent_additive_mse_p30__lc_sweep (patience=2,
final_perm_identity=false default). If comparing Lyapunov structure at
the es2-best.ckpt shows it matches reference better than our
patience=5 checkpoint did, the extra training was drifting the model
into a weaker-Jacobian-structure regime. If neither checkpoint
matches reference, the residual gap is attributable to the DirectSum
constraint itself.

**Success criteria**

- All 21 runs train without divergence
- es2-best.ckpt and es5-best.ckpt both saved per run
- Best val traj_loss (at either checkpoint) within 2x of reference's 0.0105
- Cross-area Gramian asymmetry (vis->cog > cog->vis) present at best cell

## Results

**Swept axes** (2): `training.lightning.loop_closure_weight`, `training.lightning.obs_noise_scale`

**Chosen run** (by `best_traj_loss`): `2j9p9bar` — traj_loss=0.00411, MASE=0.6381, R²=0.9953, LC loss=9.877, epoch=35.0

Swept-axis values at chosen run: `training.lightning.loop_closure_weight`=1.0e-05 · `training.lightning.obs_noise_scale`=0.05

**Runs analyzed**: 21 (expected 21)

### Per-run results

| run_idx | run_id | `training.lightning.loop_closure_weight` | `training.lightning.obs_noise_scale` | best_traj_loss | best_MASE | R² | LC loss | epoch |
|---|---|---|---|---|---|---|---|---|
| 8 | `2j9p9bar` | 1.0e-05 | 0.05 | 0.00411 | 0.6381 | 0.9953 | 9.877 | 35.0 |
| 2 | `om7x2lp5` | 0 | 0.05 | 0.00426 | 0.6466 | 0.9951 | 30.729 | 40.0 |
| 5 | `kpssh1t5` | 1.0e-06 | 0.05 | 0.00430 | 0.6494 | 0.9951 | 23.629 | 40.0 |
| 6 | `ruf6eimh` | 1.0e-05 | 0 | 0.00430 | 0.6487 | 0.9951 | 4.883 | 40.0 |
| 3 | `ykoqooew` | 1.0e-06 | 0 | 0.00432 | 0.6496 | 0.9950 | 9.777 | 40.0 |
| 11 | `bcqyj136` | 1.0e-04 | 0.05 | 0.00438 | 0.6564 | 0.9950 | 3.236 | 37.0 |
| 0 | `shvnbo6m` | 0 | 0 | 0.00447 | 0.6604 | 0.9949 | 11.340 | 37.0 |
| 4 | `ihruo1nh` | 1.0e-06 | 0.01 | 0.00450 | 0.6650 | 0.9948 | 17.556 | 38.0 |
| 1 | `3tsdse3q` | 0 | 0.01 | 0.00455 | 0.6680 | 0.9948 | 21.861 | 38.0 |
| 7 | `355qgefr` | 1.0e-05 | 0.01 | 0.00456 | 0.6686 | 0.9948 | 8.586 | 38.0 |
| 9 | `4b9b4zk8` | 1.0e-04 | 0 | 0.00468 | 0.6741 | 0.9946 | 1.268 | 37.0 |
| 12 | `fnxovse1` | 0.001 | 0 | 0.00491 | 0.6879 | 0.9944 | 0.205 | 39.0 |
| 10 | `pf2ebouj` | 1.0e-04 | 0.01 | 0.00527 | 0.7142 | 0.9940 | 3.594 | 38.0 |
| 14 | `jigea1r1` | 0.001 | 0.05 | 0.00538 | 0.7178 | 0.9938 | 0.499 | 38.0 |
| 13 | `ru3tfu3u` | 0.001 | 0.01 | 0.00561 | 0.7370 | 0.9936 | 0.369 | 41.0 |
| 15 | `sliyvdk6` | 0.01 | 0 | 0.00563 | 0.7326 | 0.9935 | 0.024 | 37.0 |
| 18 | `ozyq3lxf` | 0.1 | 0 | 0.00589 | 0.7513 | 0.9932 | 0.003 | 39.0 |
| 16 | `qhl82jkn` | 0.01 | 0.01 | 0.00675 | 0.8060 | 0.9923 | 0.053 | 37.0 |
| 17 | `8j99ikd7` | 0.01 | 0.05 | 0.00711 | 0.8235 | 0.9919 | 0.096 | 38.0 |
| 20 | `gfd504tk` | 0.1 | 0.05 | 0.04979 | 1.8969 | 0.9433 | 0.001 | 10.0 |
| 19 | `ot399pzt` | 0.1 | 0.01 | 0.05961 | 2.0633 | 0.9317 | 0.000 | 6.0 |

### Best run per `obs_noise_scale`

| obs_noise_scale | Best LC weight | Best traj loss | MASE at best | R² | LC loss | epoch |
|---|---|---|---|---|---|---|
| 0.0 | 1.0e-05 | 0.00430 | 0.6487 | 0.9951 | 4.883 | 40.0 |
| 0.01 | 1.0e-06 | 0.00450 | 0.6650 | 0.9948 | 17.556 | 38.0 |
| 0.05 | 1.0e-05 | 0.00411 | 0.6381 | 0.9953 | 9.877 | 35.0 |

## Success-criteria verdicts (automated)

| Criterion | Verdict | Note |
|---|---|---|
| All 21 runs train without divergence | **Unknown** |  |
| es2-best.ckpt and es5-best.ckpt both saved per run | **Unknown** |  |
| Best val traj_loss (at either checkpoint) within 2x of reference's 0.0105 | **Unknown** |  |
| Cross-area Gramian asymmetry (vis->cog > cog->vis) present at best cell | **Unknown** |  |

_Automated verdicts use simple numeric-threshold parsing and may mis-classify qualitative criteria. The Discussion section below takes precedence._

## Figures

_(no figures produced — analytics may have failed)_

```
IndexError: list index out of range
```

## Discussion

<!--
This section is intentionally left as a placeholder. A human reviewer
or Claude Code agent should fill it in based on the tables and figures
above, explicitly addressing each success criterion and comparing the
outcome to the stated hypothesis. Write the Discussion to
`discussion.md` in this directory and re-run `render_report`.
-->

_(to be written)_
