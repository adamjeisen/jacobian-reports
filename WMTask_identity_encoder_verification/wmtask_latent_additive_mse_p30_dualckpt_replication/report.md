# Sweep Analysis: `wmtask_latent_additive_mse_p30_dualckpt_replication`

**Project**: [WMTask_identity_encoder_verification](https://wandb.ai/JacobianODE/WMTask_identity_encoder_verification/groups/wmtask_latent_additive_mse_p30_dualckpt_replication)  
**Launched**: 2026-04-26T22:10:12Z  
**Completed**: 2026-04-26T22:20:13Z  
**Outcome**: `complete_with_failures`  
**Git**: `latent-JacobianODE` @ `6f113af`  
**Expected runs**: 1

## Experiment Context

### `wmtask_latent_additive_mse_p30_dualckpt_replication`

**Description**

Single-run replication of the monolithic CouplingEncoder best cell
(LC=1e-5, obs_noise_scale=0.05) with dual-checkpoint enabled
(early_stopping_patience=5, shadow_patience=2). Same model + data
+ loss config as wmtask_latent_additive_mse_p30__lc_sweep modulo
patience. Should reproduce that sweep's chosen-best Lyapunov
behavior at the es2-best.ckpt sidecar.

**Hypothesis**

es2-best.ckpt should match the original i73jwojr Lyapunov spectrum
(clean negative tail, Δλ_min ≈ 0). If it doesn't, code has drifted.
es5-best.ckpt may or may not match — if it ALSO degrades, then ES5
over-training contributes to the suppression we see on DirectSum
dualckpt; if it stays clean, the suppression is DirectSum-specific.

**Success criteria**

- Run trains without divergence
- Both es2-best.ckpt and (epoch-best) best.ckpt saved
- es2 Lyapunov spectrum matches empirical to within Δλ_min ≈ ±1

## Results

**Chosen run** (by `best_traj_loss`): `—` — traj_loss=—, MASE=—, R²=—, LC loss=—, epoch=None

### Integrity checks

⚠️ **Matched-run count mismatch**: expected 1 run_idx slots per the sentinel, matched 0 in wandb. The sweep may still be in progress, or some slots failed without producing wandb evidence.

**Runs analyzed**: 0 (expected 1)

## Success-criteria verdicts (automated)

| Criterion | Verdict | Note |
|---|---|---|
| Run trains without divergence | **Unknown** |  |
| Both es2-best.ckpt and (epoch-best) best.ckpt saved | **Unknown** |  |
| es2 Lyapunov spectrum matches empirical to within Δλ_min ≈ ±1 | **Unknown** |  |

_Automated verdicts use simple numeric-threshold parsing and may mis-classify qualitative criteria. The Discussion section below takes precedence._

## Figures

_(no figures produced — analytics may have failed)_

```
ValueError: attempt to get argmin of an empty sequence
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
