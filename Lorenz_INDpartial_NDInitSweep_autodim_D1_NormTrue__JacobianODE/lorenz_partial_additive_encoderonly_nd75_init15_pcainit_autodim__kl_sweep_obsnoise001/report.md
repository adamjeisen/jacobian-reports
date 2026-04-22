# Sweep Analysis: `lorenz_partial_additive_encoderonly_nd75_init15_pcainit_autodim__kl_sweep_obsnoise001`

**Project**: [Lorenz_INDpartial_NDInitSweep_autodim_D1_NormTrue__JacobianODE](https://wandb.ai/JacobianODE/Lorenz_INDpartial_NDInitSweep_autodim_D1_NormTrue__JacobianODE/groups/lorenz_partial_additive_encoderonly_nd75_init15_pcainit_autodim__kl_sweep_obsnoise001)  
**Launched**: 2026-04-22T05:55:15Z  
**Completed**: 2026-04-22T09:40:18Z  
**Outcome**: `complete_clean`  
**Git**: `latent-JacobianODE` @ `290cc47`  
**Expected runs**: 12

## Experiment Context

### `lorenz_partial_additive_encoderonly_nd75_init15_pcainit_autodim__kl_sweep_obsnoise001`

**Description**

Lorenz partial additive coupling, obs_noise=0.01, n_delays=75,
traj_init_steps=15 (only governs dataloader seq_length, not training).
encoder_only_mode=true → training + validation skip all dynamics work
and use only recon + KL losses. init_pca_basis=true → encoder starts
as the PCA rotation V. use_vae=true so kl_dyn_weight has teeth.
12-run sweep: 6 kl_dyn_weight × 2 kl_null_weight.
Analytics includes the new tangent_spectrum section: per-point latent
tangents (z_{t+1} - z_t) projected onto encoder Jacobian columns,
ranked by magnitude, averaged over val set. For the true 3-dim Lorenz
attractor, we expect the top 3 components to carry most of the energy.

**Hypothesis**

With PCA-basis init the encoder already reconstructs cleanly. The KL
regularizers shape the latent geometry: kl_null pushes z_null → 0,
concentrating representation on z_dyn; kl_dyn (VAE Gaussian KL on
z_dyn) encourages smooth/Gaussian latent codes. Too much kl_dyn will
collapse the latent entirely; too little gives no shaping benefit.
Prior: best val/recon_loss at small-to-mid kl_dyn (~1e-4 to 1e-2),
kl_null=0 (let z_null stay untouched since PCA already picked the
right subspace). The tangent_spectrum should concentrate on the top
3 directions at every KL weight, since Lorenz is intrinsically 3-dim
— this is a check on the encoder, not on the KL choice.

**Success criteria**

- All 12 runs train without divergence (val/recon_loss finite throughout)
- Best val/recon_loss achieved at some kl_dyn in {1e-4, 1e-3, 1e-2}
- Top 3 components of the tangent spectrum at the best run carry >= 95% of energy
- Cumulative tangent energy at dim 3 is higher than at the worst run

## Results

**Swept axes** (3): `model.kl_dyn_weight`, `model.kl_null_weight`, `model.n_target_dims_pca_cum_var`

**Chosen run** (by `best_traj_loss`): `8zj4cex3` — traj_loss=0.00015, MASE=—, R²=—, LC loss=—, epoch=27.0

Swept-axis values at chosen run: `model.kl_dyn_weight`=1 · `model.kl_null_weight`=0 · `model.n_target_dims_pca_cum_var`=0.993244

**Runs analyzed**: 12 (expected 12)

### Per-run results

| run_idx | run_id | `model.kl_dyn_weight` | `model.kl_null_weight` | `model.n_target_dims_pca_cum_var` | best_traj_loss | best_MASE | R² | LC loss | epoch |
|---|---|---|---|---|---|---|---|---|---|
| 11 | `8zj4cex3` | 1 | 0 | 0.993244 | 0.00015 | — | — | — | 27.0 |
| 0 | `27186ol7` | 0 | None | 0.993244 | 0.00015 | — | — | — | 27.0 |
| 1 | `hgy3ujb9` | 0 | 0 | 0.993244 | 0.00015 | — | — | — | 27.0 |
| 2 | `4ap9r1kz` | 1.0e-04 | None | 0.993244 | 0.00015 | — | — | — | 27.0 |
| 3 | `qznhfxfy` | 1.0e-04 | 0 | 0.993244 | 0.00015 | — | — | — | 27.0 |
| 4 | `r8vva785` | 0.001 | None | 0.993244 | 0.00015 | — | — | — | 27.0 |
| 5 | `cjfiyh0f` | 0.001 | 0 | 0.993244 | 0.00015 | — | — | — | 27.0 |
| 6 | `z8glgmy1` | 0.01 | None | 0.993244 | 0.00015 | — | — | — | 27.0 |
| 7 | `atja9o1s` | 0.01 | 0 | 0.993244 | 0.00015 | — | — | — | 27.0 |
| 8 | `gl4zjkyi` | 0.1 | None | 0.993244 | 0.00015 | — | — | — | 27.0 |
| 9 | `e31w0cua` | 0.1 | 0 | 0.993244 | 0.00015 | — | — | — | 27.0 |
| 10 | `gf33rdwr` | 1 | None | 0.993244 | 0.00015 | — | — | — | 27.0 |

## Success-criteria verdicts (automated)

| Criterion | Verdict | Note |
|---|---|---|
| All 12 runs train without divergence (val/recon_loss finite throughout) | **Unknown** |  |
| Best val/recon_loss achieved at some kl_dyn in {1e-4, 1e-3, 1e-2} | **Unknown** |  |
| Top 3 components of the tangent spectrum at the best run carry >= 95% of energy | **Unknown** |  |
| Cumulative tangent energy at dim 3 is higher than at the worst run | **Unknown** |  |

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
