# Sweep Analysis: `lorenz_partial_additive_splitmode_p30_obsnoise001_nd75_init15_pcainit_autodim__lc_sweep`

**Project**: [Lorenz_INDpartial_NDInitSweep_autodim_D1_NormTrue__JacobianODE](https://wandb.ai/JacobianODE/Lorenz_INDpartial_NDInitSweep_autodim_D1_NormTrue__JacobianODE/groups/lorenz_partial_additive_splitmode_p30_obsnoise001_nd75_init15_pcainit_autodim__lc_sweep)  
**Launched**: 2026-04-22T04:25:10Z  
**Completed**: 2026-04-22T08:25:48Z  
**Outcome**: `complete_clean`  
**Git**: `latent-JacobianODE` @ `944fcaf`  
**Expected runs**: 5

## Experiment Context

### `lorenz_partial_additive_splitmode_p30_obsnoise001_nd75_init15_pcainit_autodim__lc_sweep`

**Description**

Lorenz partial additive coupling, obs_noise=0.01, n_delays=75,
prediction_steps=30, traj_init_steps=15. Split-mode trajectory
loss (most_recent at train and val) + uniform encoder-decoder
recon. n_target_dims auto-picked via PCA threshold=0.99. Encoder
init via PCA-basis rotation (init_pca_basis=true) — at init the
encoder is V @ x where V is the PCA basis of the noisy training
delay embeddings. 5-run LC sweep over
{0, 1e-6, 1e-5, 1e-4, 1e-3}.

**Hypothesis**

PCA-basis init places z_dyn at init exactly in the top-n_target
PCs of the (noisy) training embedding — the linear subspace that
captures most variance of the signal. The dynamics MLP starts
with a near-optimal linear chart and only has to learn nonlinear
corrections, vs identity init where it starts on the lag-axis
basis (also sensible but linearly misaligned with the principal
directions). Expect comparable or modestly better val trajectory
loss compared to the identity-init companion sweep at the same
n_delays. If PCA wins consistently across noise levels, switch
the convention; if equal, identity init wins on interpretability.

**Success criteria**

- All 5 runs train without divergence
- Best val traj loss is comparable or better than identity-init companion sweep at the same LC
- Convergence (epochs to best val loss) is faster than identity-init companion (PCA gives a head start)
- λ-spectrum at best LC matches identity-init companion within tolerance — same dynamics, just different starting basis

## Results

**Swept axes** (2): `model.n_target_dims_pca_cum_var`, `training.lightning.loop_closure_weight`

**Chosen run** (by `best_traj_loss`): `34et2hk9` — traj_loss=0.00036, MASE=0.5082, R²=0.9990, LC loss=8.032, epoch=97.0

Swept-axis values at chosen run: `model.n_target_dims_pca_cum_var`=0.993244 · `training.lightning.loop_closure_weight`=0

**Runs analyzed**: 5 (expected 5)

### Per-run results

| run_idx | run_id | `model.n_target_dims_pca_cum_var` | `training.lightning.loop_closure_weight` | best_traj_loss | best_MASE | R² | LC loss | epoch |
|---|---|---|---|---|---|---|---|---|
| 0 | `34et2hk9` | 0.993244 | 0 | 0.00036 | 0.5082 | 0.9990 | 8.032 | 97.0 |
| 2 | `bqr94eu5` | 0.993244 | 1.0e-05 | 0.00037 | 0.4916 | 0.9990 | 0.915 | 154.0 |
| 3 | `sp745jkz` | 0.993244 | 1.0e-04 | 0.00038 | 0.4939 | 0.9990 | 0.186 | 154.0 |
| 1 | `1rjo2r7a` | 0.993244 | 1.0e-06 | 0.00040 | 0.5253 | 0.9989 | 4.304 | 83.0 |
| 4 | `i3ebq21q` | 0.993244 | 0.001 | 0.00049 | 0.5318 | 0.9987 | 0.042 | 101.0 |

## Success-criteria verdicts (automated)

| Criterion | Verdict | Note |
|---|---|---|
| All 5 runs train without divergence | **Unknown** |  |
| Best val traj loss is comparable or better than identity-init companion sweep at the same LC | **Unknown** |  |
| Convergence (epochs to best val loss) is faster than identity-init companion (PCA gives a head start) | **Unknown** |  |
| λ-spectrum at best LC matches identity-init companion within tolerance — same dynamics, just different starting basis | **Unknown** |  |

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
