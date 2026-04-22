# Sweep Analysis: `lorenz_partial_additive_splitmode_p30_obsnoise005_nd75_init15_pcainit_autodim__lc_sweep`

**Project**: [Lorenz_INDpartial_NDInitSweep_autodim_D1_NormTrue__JacobianODE](https://wandb.ai/JacobianODE/Lorenz_INDpartial_NDInitSweep_autodim_D1_NormTrue__JacobianODE/groups/lorenz_partial_additive_splitmode_p30_obsnoise005_nd75_init15_pcainit_autodim__lc_sweep)  
**Launched**: 2026-04-22T04:25:38Z  
**Completed**: 2026-04-22T08:45:56Z  
**Outcome**: `complete_clean`  
**Git**: `latent-JacobianODE` @ `944fcaf`  
**Expected runs**: 5

## Experiment Context

### `lorenz_partial_additive_splitmode_p30_obsnoise005_nd75_init15_pcainit_autodim__lc_sweep`

**Description**

Lorenz partial additive coupling, obs_noise=0.05, n_delays=75,
prediction_steps=30, traj_init_steps=15. Split-mode trajectory
loss (most_recent at train and val) + uniform encoder-decoder
recon. n_target_dims auto-picked via PCA threshold=0.99. Encoder
init via PCA-basis rotation (init_pca_basis=true). 5-run LC sweep
over {0, 1e-6, 1e-5, 1e-4, 1e-3}.

**Hypothesis**

Same as the obsnoise001 PCA-init companion, but at higher noise.
PCA init may help MORE here than at low noise: noise inflates
variance roughly equally across all directions, so the top-PCs
chosen by PCA-auto on noisy data should still capture the
signal manifold cleanly, and starting the encoder rotated into
that basis gives the dynamics MLP a head start. Identity init
has to learn the rotation alongside the dynamics.

**Success criteria**

- All 5 runs train without divergence
- Best val traj loss is comparable or better than identity-init companion sweep at the same LC
- Convergence faster than identity-init companion
- PCA-init's advantage over identity (if any) is at least as large at noise=0.05 as at noise=0.01

## Results

**Swept axes** (1): `training.lightning.loop_closure_weight`

**Chosen run** (by `best_traj_loss`): `qx7s85sj` — traj_loss=0.00515, MASE=0.7546, R²=0.9861, LC loss=7.618, epoch=113.0

Swept-axis values at chosen run: `training.lightning.loop_closure_weight`=0

**Runs analyzed**: 5 (expected 5)

### Per-run results

| run_idx | run_id | `training.lightning.loop_closure_weight` | best_traj_loss | best_MASE | R² | LC loss | epoch |
|---|---|---|---|---|---|---|---|
| 0 | `qx7s85sj` | 0 | 0.00515 | 0.7546 | 0.9861 | 7.618 | 113.0 |
| 1 | `avtldx1b` | 1.0e-06 | 0.00517 | 0.7549 | 0.9861 | 4.042 | 113.0 |
| 2 | `2josp5ek` | 1.0e-05 | 0.00520 | 0.7557 | 0.9860 | 1.314 | 113.0 |
| 3 | `ar8w5u2w` | 1.0e-04 | 0.00525 | 0.7569 | 0.9859 | 0.322 | 113.0 |
| 4 | `ym53fkj8` | 0.001 | 0.00568 | 0.7722 | 0.9849 | 0.068 | 107.0 |

## Success-criteria verdicts (automated)

| Criterion | Verdict | Note |
|---|---|---|
| All 5 runs train without divergence | **Unknown** |  |
| Best val traj loss is comparable or better than identity-init companion sweep at the same LC | **Unknown** |  |
| Convergence faster than identity-init companion | **Unknown** |  |
| PCA-init's advantage over identity (if any) is at least as large at noise=0.05 as at noise=0.01 | **Unknown** |  |

_Automated verdicts use simple numeric-threshold parsing and may mis-classify qualitative criteria. The Discussion section below takes precedence._

## Figures

_(no figures produced — analytics may have failed)_

```
ValueError: model.encoder.init_pca_basis=True but no pca_basis tensor was passed to make_model. Compute it in run_jacobians and forward it.
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
