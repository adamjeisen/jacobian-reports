# Sweep Analysis: `lorenz_partial_additive_encoderonly_nd75_init15_pcainit_autodim__kl_sweep_obsnoise005`

**Project**: [Lorenz_INDpartial_NDInitSweep_autodim_D1_NormTrue__JacobianODE](https://wandb.ai/JacobianODE/Lorenz_INDpartial_NDInitSweep_autodim_D1_NormTrue__JacobianODE/groups/lorenz_partial_additive_encoderonly_nd75_init15_pcainit_autodim__kl_sweep_obsnoise005)  
**Launched**: 2026-04-22T05:55:45Z  
**Completed**: 2026-04-22T09:45:17Z  
**Outcome**: `complete_clean`  
**Git**: `latent-JacobianODE` @ `290cc47`  
**Expected runs**: 12

## Experiment Context

### `lorenz_partial_additive_encoderonly_nd75_init15_pcainit_autodim__kl_sweep_obsnoise005`

**Description**

Lorenz partial additive coupling, obs_noise=0.05, n_delays=75.
encoder_only_mode=true, init_pca_basis=true, use_vae=true.
12-run sweep: 6 kl_dyn_weight × 2 kl_null_weight. Best by
val/recon_loss. Tangent-spectrum diagnostic post-training.

**Hypothesis**

At obs_noise=0.05 the encoder has to learn to denoise as well as
reconstruct. KL shaping may matter more here than at noise=0.01:
a mild kl_dyn should smooth the latent while kl_null suppresses the
noise-dominated off-manifold variance. Expect best val/recon_loss at
kl_dyn slightly higher than the obsnoise001 companion. Tangent spectrum
should still concentrate on top 3 components — Lorenz intrinsic dim
doesn't depend on noise level, only on the attractor.

**Success criteria**

- All 12 runs train without divergence
- Best val/recon_loss at some kl_dyn > 0 with clear margin over kl_dyn=0
- Top 3 components of tangent spectrum at best run carry >= 90% of energy
- Best kl_dyn at noise=0.05 is >= best kl_dyn at noise=0.01 (more regularization helps at higher noise)

## Results

**Swept axes** (3): `model.kl_dyn_weight`, `model.kl_null_weight`, `model.n_target_dims_pca_cum_var`

**Chosen run** (by `best_traj_loss`): `a0o5cslr` — traj_loss=0.00314, MASE=—, R²=—, LC loss=—, epoch=24.0

Swept-axis values at chosen run: `model.kl_dyn_weight`=0 · `model.kl_null_weight`=None · `model.n_target_dims_pca_cum_var`=0.990036

**Runs analyzed**: 12 (expected 12)

### Per-run results

| run_idx | run_id | `model.kl_dyn_weight` | `model.kl_null_weight` | `model.n_target_dims_pca_cum_var` | best_traj_loss | best_MASE | R² | LC loss | epoch |
|---|---|---|---|---|---|---|---|---|---|
| 0 | `a0o5cslr` | 0 | None | 0.990036 | 0.00314 | — | — | — | 24.0 |
| 1 | `palbdcgi` | 0 | 0 | 0.990036 | 0.00314 | — | — | — | 24.0 |
| 2 | `yofig4zo` | 1.0e-04 | None | 0.990036 | 0.00314 | — | — | — | 24.0 |
| 3 | `tbrwzoco` | 1.0e-04 | 0 | 0.990036 | 0.00314 | — | — | — | 24.0 |
| 4 | `2ahnvord` | 0.001 | None | 0.990036 | 0.00314 | — | — | — | 24.0 |
| 6 | `hoagpu5a` | 0.01 | None | 0.990036 | 0.00314 | — | — | — | 24.0 |
| 7 | `kdzzgd4k` | 0.01 | 0 | 0.990036 | 0.00314 | — | — | — | 24.0 |
| 8 | `ziyd9p3i` | 0.1 | None | 0.990036 | 0.00314 | — | — | — | 24.0 |
| 10 | `gxorl40v` | 1 | None | 0.990036 | 0.00314 | — | — | — | 24.0 |
| 11 | `ygdijtfm` | 1 | 0 | 0.990036 | 0.00314 | — | — | — | 24.0 |
| 5 | `armg82o9` | 0.001 | 0 | 0.990036 | 0.00315 | — | — | — | 25.0 |
| 9 | `60fu5rs0` | 0.1 | 0 | 0.990036 | 0.00315 | — | — | — | 24.0 |

## Success-criteria verdicts (automated)

| Criterion | Verdict | Note |
|---|---|---|
| All 12 runs train without divergence | **Unknown** |  |
| Best val/recon_loss at some kl_dyn > 0 with clear margin over kl_dyn=0 | **Unknown** |  |
| Top 3 components of tangent spectrum at best run carry >= 90% of energy | **Unknown** |  |
| Best kl_dyn at noise=0.05 is >= best kl_dyn at noise=0.01 (more regularization helps at higher noise) | **Unknown** |  |

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
