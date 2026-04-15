# Sweep Analysis: `wmtask_vanilla_mse_p30__lc_sweep`

**Project**: [WMTask_identity_encoder_verification](https://wandb.ai/JacobianODE/WMTask_identity_encoder_verification/groups/wmtask_vanilla_mse_p30__lc_sweep)  
**Launched**: 2026-04-15T15:11:41Z  
**Completed**: 2026-04-15T18:10:18Z  
**Outcome**: `complete_clean`  
**Git**: `latent-JacobianODE` @ `c35dd72`  
**Expected runs**: 9

## Experiment Context

### `wmtask_vanilla_mse_p30`

**Description**

Vanilla JacobianODE on WMTask: MLP predicts Jacobians directly in
observation space (no encoder). obs_noise_scale=0.05, plain MSE
loss, prediction_steps=30 (seq_length=45, traj_init 15). LC weight
swept.

**Hypothesis**

A longer rollout horizon (30 vs ~10) gives the vanilla model more
multi-step signal per batch, which should better constrain its
Jacobians across the trajectory — especially the subdominant
spectrum directions.

**Success criteria**

- val/trajectory_r2_score >= 0.99 at best LC (matches prior vanilla baseline)
- val/trajectory_mase < 1.0 at best LC
- Cleaner loop-closure plateau vs prior 10-step vanilla runs

## Results

**Overall best MASE**: 0.9038 (LC weight = 1.0e-05, obs_noise_scale = 0.05)
**Overall best traj loss**: 0.00974 at epoch 9.0
**Runs analyzed**: 9

### Best run per `obs_noise_scale`

| obs_noise_scale | Best LC weight | Best traj loss | MASE at best | R² | LC loss | epoch |
|---|---|---|---|---|---|---|
| 0.05 | 1.0e-06 | 0.00971 | 0.9148 | 0.9889 | 9.619 | 8.0 |

## Success-criteria verdicts (automated)

| Criterion | Verdict | Note |
|---|---|---|
| val/trajectory_r2_score >= 0.99 at best LC (matches prior vanilla baseline) | **Fail** | Best R² = 0.9889; threshold >= 0.99 |
| val/trajectory_mase < 1.0 at best LC | **Pass** | Best MASE = 0.9038; threshold < 1.0 |
| Cleaner loop-closure plateau vs prior 10-step vanilla runs | **Unknown** |  |

_Automated verdicts use simple numeric-threshold parsing and may mis-classify qualitative criteria. The Discussion section below takes precedence._

## Figures

_(no figures produced — analytics may have failed)_

```
RuntimeError: No finished JacobianODE sweep runs found in JacobianODE/WMTask_identity_encoder_verification group=wmtask_vanilla_mse_p30__lc_sweep
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
