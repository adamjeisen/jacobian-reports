# Sweep Analysis: `wmtask_latent_additive_p30_nearid_tf__lc_x_obsnoisescale_sweep_20260429T163244Z__stage_b`

**Project**: [WMTask_identity_encoder_verification](https://wandb.ai/JacobianODE/WMTask_identity_encoder_verification/groups/wmtask_latent_additive_p30_nearid_tf__lc_x_obsnoisescale_sweep_20260429T163244Z__stage_b)  
**Launched**: 2026-04-29T19:40:17Z  
**Completed**: 2026-04-29T20:05:49Z  
**Outcome**: `complete_with_failures`  
**Git**: `latent-JacobianODE` @ `3195286`  
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

**Chosen run** (by `best_traj_loss`): `—` — traj_loss=—, MASE=—, R²=—, LC loss=—, epoch=None

### Integrity checks

⚠️ **Matched-run count mismatch**: expected 10 run_idx slots per the sentinel, matched 0 in wandb. The sweep may still be in progress, or some slots failed without producing wandb evidence.

**Runs analyzed**: 0 (expected 10)

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

_(no figures produced — analytics may have failed)_

```
FileNotFoundError: [Errno 2] No such file or directory: '/orcd/data/ekmiller/001/eisenaj/JacobianODE/lightning/latent_jac_runs/WMTask_identity_encoder_verification/ev3e36ug/checkpoints'
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
