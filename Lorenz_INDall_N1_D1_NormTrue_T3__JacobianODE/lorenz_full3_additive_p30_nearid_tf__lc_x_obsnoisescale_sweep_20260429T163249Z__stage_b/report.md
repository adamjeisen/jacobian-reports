# Sweep Analysis: `lorenz_full3_additive_p30_nearid_tf__lc_x_obsnoisescale_sweep_20260429T163249Z__stage_b`

**Project**: [Lorenz_INDall_N1_D1_NormTrue_T3__JacobianODE](https://wandb.ai/JacobianODE/Lorenz_INDall_N1_D1_NormTrue_T3__JacobianODE/groups/lorenz_full3_additive_p30_nearid_tf__lc_x_obsnoisescale_sweep_20260429T163249Z__stage_b)  
**Launched**: 2026-04-29T19:30:18Z  
**Completed**: 2026-04-29T20:10:32Z  
**Outcome**: `complete_with_failures`  
**Git**: `latent-JacobianODE` @ `3195286`  
**Expected runs**: 10

## Experiment Context

### `lorenz_full3_additive_p30_nearid_tf__lc_x_obsnoisescale_sweep`

**Description**

Fully-observed Lorenz (3 dims, no delay embedding). Monolithic
CouplingEncoder (additive coupling, 8 layers, hidden_dim=128),
near_identity_std=1e-3, final_perm_identity=true. 21-cell sweep
over 7 LC x 3 obs_noise_scale. TF-coupled LR schedule (k_scale=1).
Two-stage protocol with dual-checkpoint (primary ES patience=5,
shadow-freeze patience=2). Same recipe as the matched WMTask
128->128 sweep.

**Hypothesis**

If the orig recipe (TF-coupled LR, mean ~5e-5 effective in the
high-LR phase) is portable, Lorenz 3->3 should hit good Lyapunov
spectrum recovery across the LC x obs_noise grid without
spectrum compression in Stage B. Recovery of all three Lyapunov
exponents (positive, zero, negative) within ~30% of empirical
is the success bar — same standard the existing
lorenz_full_additive_mse_p30 sweep was held to. This sweep is
the matched-recipe Lorenz control for the WMTask sweep.

**Success criteria**

- All 21 cells train without divergence
- es2-best.ckpt and es5-best.ckpt both saved per cell
- Best run's predicted Lyapunov spectrum within ~30% of empirical
- Lyapunov spectrum NOT compressed in Stage B vs Stage A
- Result shape is consistent with the matched WMTask sweep (LC dependence, init effect)

## Results

**Swept axes** (4): `data.postprocessing.generalized_variance`, `training.ckpt_path`, `training.lightning.loop_closure_weight`, `training.lightning.obs_noise_scale`

**Chosen run** (by `best_traj_loss`): `—` — traj_loss=—, MASE=—, R²=—, LC loss=—, epoch=None

### Integrity checks

⚠️ **Matched-run count mismatch**: expected 10 run_idx slots per the sentinel, matched 0 in wandb. The sweep may still be in progress, or some slots failed without producing wandb evidence.

**Runs analyzed**: 0 (expected 10)

## Success-criteria verdicts (automated)

| Criterion | Verdict | Note |
|---|---|---|
| All 21 cells train without divergence | **Unknown** |  |
| es2-best.ckpt and es5-best.ckpt both saved per cell | **Unknown** |  |
| Best run's predicted Lyapunov spectrum within ~30% of empirical | **Unknown** |  |
| Lyapunov spectrum NOT compressed in Stage B vs Stage A | **Unknown** |  |
| Result shape is consistent with the matched WMTask sweep (LC dependence, init effect) | **Unknown** |  |

_Automated verdicts use simple numeric-threshold parsing and may mis-classify qualitative criteria. The Discussion section below takes precedence._

## Figures

_(no figures produced — analytics may have failed)_

```
FileNotFoundError: [Errno 2] No such file or directory: '/orcd/data/ekmiller/001/eisenaj/JacobianODE/lightning/latent_jac_runs/Lorenz_INDall_N1_D1_NormTrue_T3__JacobianODE/cn2wglxg/checkpoints'
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
