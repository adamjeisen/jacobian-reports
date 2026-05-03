# Sweep Analysis: `lorenz_partial_additive_splitmode_p30_obsnoise005_cayley_autodim_top3nd_v2__lc_obsnoisescale_sweep_20260503T045452Z__stage_a`

**Project**: [Lorenz_INDpartial_NDsweep_cayley_autodim_D1_NormTrue__JacobianODE](https://wandb.ai/JacobianODE/Lorenz_INDpartial_NDsweep_cayley_autodim_D1_NormTrue__JacobianODE/groups/lorenz_partial_additive_splitmode_p30_obsnoise005_cayley_autodim_top3nd_v2__lc_obsnoisescale_sweep_20260503T045452Z__stage_a)  
**Launched**: 2026-05-03T04:55:20Z  
**Completed**: 2026-05-03T08:50:38Z  
**Outcome**: `complete_clean`  
**Git**: `latent-JacobianODE` @ `3032f43`  
**Expected runs**: 108

## Experiment Context

### `lorenz_partial_additive_splitmode_p30_obsnoise005_cayley_autodim_top3nd_v2__lc_obsnoisescale_sweep`

**Description**

Lorenz partial additive coupling, Cayley + autodim + split-mode +
TF-coupled LR. Single observed channel (idx 0), obs_noise=0.05,
prediction_steps=30, traj_init_steps=15. 108-run grid: 3 n_delays
(chain-pinned) × 9 LC weights × 4 obs_noise_scale values.

**Hypothesis**

Same noise-injection / LC ramp hypothesis as the prior splitmode
obsnoise005 grid, now run under the standard Cayley + autodim recipe
end-to-end so the n_delays choice from the scout transfers cleanly.

**Success criteria**

- All 108 Stage A runs train without divergence
- Per-cell autodim n_target_dims logged
- two_stage_cull keeps top ~54 (cull_fraction=0.5)
- Best obs_noise_scale > 0 cell strictly improves vs obs_noise_scale=0 baseline at the same (n_delays, LC) cell on val/trajectory_loss

## Results

**Swept axes** (9): `data.train_test_params.delay_embedding_params.n_delays`, `model.encoder.n_input`, `model.n_target_dims`, `model.n_target_dims_pca_auto`, `model.n_target_dims_pca_cum_var`, `model.params.input_dim`, `model.params.output_dim`, `training.lightning.loop_closure_weight`, `training.lightning.obs_noise_scale`

**Chosen run** (by `best_traj_loss`): `id6d0nan` — traj_loss=0.01006, MASE=0.9201, R²=0.9732, LC loss=18.979, epoch=15.0

Swept-axis values at chosen run: `data.train_test_params.delay_embedding_params.n_delays`=65 · `model.encoder.n_input`=65 · `model.n_target_dims`=11 · `model.n_target_dims_pca_auto`=11 · `model.n_target_dims_pca_cum_var`=0.990219 · `model.params.input_dim`=11 · `model.params.output_dim`=121 · `training.lightning.loop_closure_weight`=0 · `training.lightning.obs_noise_scale`=0

**Runs analyzed**: 108 (expected 108)

### Per-run results

| run_idx | run_id | `data.train_test_params.delay_embedding_params.n_delays` | `model.encoder.n_input` | `model.n_target_dims` | `model.n_target_dims_pca_auto` | `model.n_target_dims_pca_cum_var` | `model.params.input_dim` | `model.params.output_dim` | `training.lightning.loop_closure_weight` | `training.lightning.obs_noise_scale` | best_traj_loss | best_MASE | R² | LC loss | epoch |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `id6d0nan` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 0 | 0 | 0.01006 | 0.9201 | 0.9732 | 18.979 | 15.0 |
| 13 | `xpqhs9r5` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 1.0e-06 | 0 | 0.01024 | 0.9310 | 0.9728 | 8.552 | 15.0 |
| 41 | `365xxmpk` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 1.0e-04 | 0.003 | 0.01028 | 0.9417 | 0.9722 | 0.977 | 18.0 |
| 2 | `3cexp570` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 0 | 0 | 0.01069 | 0.9607 | 0.9714 | 18.976 | 17.0 |
| 25 | `3nplzrjw` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 1.0e-05 | 0 | 0.01076 | 0.9253 | 0.9713 | 2.516 | 13.0 |
| 3 | `jgms7rny` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 0 | 0.003 | 0.01087 | 0.9557 | 0.9715 | 86.920 | 17.0 |
| 14 | `o032u4j4` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 1.0e-06 | 0 | 0.01100 | 0.9747 | 0.9705 | 8.814 | 17.0 |
| 0 | `3nstn66s` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 0 | 0 | 0.01101 | 0.9373 | 0.9710 | 42.097 | 17.0 |
| 15 | `b2q4dvxe` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 1.0e-06 | 0.003 | 0.01142 | 0.9667 | 0.9700 | 52.719 | 17.0 |
| 26 | `eyo7kbrd` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 1.0e-05 | 0 | 0.01156 | 0.9773 | 0.9689 | 2.702 | 18.0 |
| 17 | `klj5tn5w` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 1.0e-06 | 0.003 | 0.01174 | 1.0206 | 0.9684 | 51.114 | 12.0 |
| 29 | `r5y3m8kt` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 1.0e-05 | 0.003 | 0.01178 | 0.9921 | 0.9683 | 15.208 | 16.0 |
| 12 | `wizbsqsw` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 1.0e-06 | 0 | 0.01182 | 0.9626 | 0.9689 | 14.054 | 17.0 |
| 27 | `6v59mul9` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 1.0e-05 | 0.003 | 0.01200 | 0.9557 | 0.9684 | 6.129 | 17.0 |
| 37 | `0enol8sg` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 1.0e-04 | 0 | 0.01212 | 0.9597 | 0.9676 | 0.486 | 13.0 |
| 39 | `60bbpe0s` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 1.0e-04 | 0.003 | 0.01255 | 0.9694 | 0.9671 | 0.722 | 19.0 |
| 24 | `322zwhto` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 1.0e-05 | 0 | 0.01265 | 0.9535 | 0.9666 | 4.460 | 12.0 |
| 5 | `egrstbam` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 0 | 0.003 | 0.01341 | 1.0278 | 0.9639 | 121.262 | 12.0 |
| 28 | `4o129gpe` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 1.0e-05 | 0.003 | 0.01365 | 0.9809 | 0.9636 | 3.756 | 18.0 |
| 36 | `r838tfeu` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 1.0e-04 | 0 | 0.01381 | 0.9985 | 0.9634 | 0.462 | 17.0 |
| 48 | `a8rjy7kg` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 0.001 | 0 | 0.01434 | 0.9849 | 0.9622 | 0.054 | 17.0 |
| 51 | `anrfk2i7` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 0.001 | 0.003 | 0.01441 | 1.0298 | 0.9621 | 0.099 | 17.0 |
| 38 | `pxft8ayf` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 1.0e-04 | 0 | 0.01449 | 1.0308 | 0.9610 | 0.355 | 18.0 |
| 52 | `qj02b8u0` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 0.001 | 0.003 | 0.01511 | 0.9931 | 0.9597 | 0.061 | 19.0 |
| 60 | `lu9mdd3t` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 0.01 | 0 | 0.01531 | 1.0093 | 0.9596 | 0.007 | 19.0 |
| 50 | `fgorh2u6` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 0.001 | 0 | 0.01582 | 1.0770 | 0.9577 | 0.066 | 10.0 |
| 53 | `0dn67ryj` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 0.001 | 0.003 | 0.01588 | 1.0509 | 0.9575 | 0.233 | 17.0 |
| 49 | `qk5kwnu4` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 0.001 | 0 | 0.01591 | 1.0322 | 0.9575 | 0.073 | 11.0 |
| 40 | `w4yawenf` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 1.0e-04 | 0.003 | 0.01750 | 1.0480 | 0.9531 | 0.629 | 13.0 |
| 63 | `onfwfz1d` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 0.01 | 0.003 | 0.01868 | 1.1177 | 0.9506 | 0.013 | 17.0 |
| 62 | `35v0e7ov` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 0.01 | 0 | 0.02127 | 1.1073 | 0.9425 | 0.005 | 19.0 |
| 61 | `g8e71vju` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 0.01 | 0 | 0.02132 | 1.1701 | 0.9429 | 0.018 | 11.0 |
| 65 | `fuixohqa` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 0.01 | 0.003 | 0.02173 | 1.1904 | 0.9418 | 0.004 | 18.0 |
| 64 | `45cyq4v1` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 0.01 | 0.003 | 0.02200 | 1.1615 | 0.9411 | 0.005 | 19.0 |
| 56 | `c2fxqa3c` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 0.001 | 0.01 | 0.02259 | 1.1993 | 0.9390 | 0.190 | 8.0 |
| 55 | `9xwwuzd1` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 0.001 | 0.01 | 0.02374 | 1.1906 | 0.9365 | 0.075 | 8.0 |
| 16 | `1r0paozx` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 1.0e-06 | 0.003 | 0.02576 | 1.3056 | 0.9313 | 61.036 | 7.0 |
| 54 | `jbd5yb6z` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 0.001 | 0.01 | 0.02577 | 1.2107 | 0.9317 | 0.269 | 9.0 |
| 43 | `n6a0y649` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 1.0e-04 | 0.01 | 0.02764 | 1.2423 | 0.9260 | 1.427 | 8.0 |
| 67 | `5nr5lua3` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 0.01 | 0.01 | 0.02822 | 1.1923 | 0.9243 | 0.005 | 8.0 |
| 4 | `0z0avj5k` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 0 | 0.003 | 0.02963 | 1.3096 | 0.9210 | 103.632 | 7.0 |
| 31 | `p5pa20fn` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 1.0e-05 | 0.01 | 0.02972 | 1.2912 | 0.9211 | 4.512 | 14.0 |
| 66 | `1pthqep1` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 0.01 | 0.01 | 0.03511 | 1.3690 | 0.9067 | 0.019 | 7.0 |
| 87 | `srme5iw0` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 1 | 0.003 | 0.03699 | 1.6170 | 0.9028 | 0.000 | 19.0 |
| 68 | `3eqixatz` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 0.01 | 0.01 | 0.03914 | 1.4123 | 0.8944 | 0.044 | 6.0 |
| 44 | `08nukj26` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 1.0e-04 | 0.01 | 0.04106 | 1.4245 | 0.8895 | 1.401 | 6.0 |
| 72 | `623olsmk` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 0.1 | 0 | 0.04106 | 1.7000 | 0.8920 | 0.000 | 17.0 |
| 75 | `q7sb3aet` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 0.1 | 0.003 | 0.04402 | 1.6776 | 0.8844 | 0.000 | 19.0 |
| 73 | `ugns9mbh` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 0.1 | 0 | 0.04442 | 1.5894 | 0.8829 | 0.000 | 17.0 |
| 79 | `zs23hgfq` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 0.1 | 0.01 | 0.04498 | 1.6737 | 0.8803 | 0.001 | 9.0 |
| 76 | `31ep3aj1` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 0.1 | 0.003 | 0.04613 | 1.6566 | 0.8777 | 0.010 | 19.0 |
| 100 | `35s2gm94` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 10 | 0.003 | 0.04622 | 1.7889 | 0.8778 | 0.000 | 15.0 |
| 20 | `h1yhjzto` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 1.0e-06 | 0.01 | 0.04934 | 1.7174 | 0.8676 | 62.943 | 7.0 |
| 74 | `x65g33rr` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 0.1 | 0 | 0.04990 | 1.7051 | 0.8672 | 0.001 | 19.0 |
| 84 | `oi336ix7` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 1 | 0 | 0.05004 | 1.8605 | 0.8687 | 0.000 | 14.0 |
| 97 | `q7fvlalq` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 10 | 0 | 0.05149 | 1.9918 | 0.8633 | 0.000 | 12.0 |
| 32 | `dxi699aa` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 1.0e-05 | 0.01 | 0.05182 | 1.6848 | 0.8605 | 10.535 | 7.0 |
| 90 | `fcfnapsz` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 1 | 0.01 | 0.05186 | 1.8090 | 0.8640 | 0.000 | 14.0 |
| 78 | `75rh7ivy` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 0.1 | 0.01 | 0.05218 | 1.7162 | 0.8622 | 0.001 | 7.0 |
| 85 | `im9rzz5v` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 1 | 0 | 0.05262 | 1.9018 | 0.8607 | 0.000 | 18.0 |
| 8 | `vmewzehv` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 0 | 0.01 | 0.05262 | 1.7448 | 0.8589 | 98.683 | 7.0 |
| 88 | `q1cdbwpc` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 1 | 0.003 | 0.05320 | 1.8226 | 0.8594 | 0.000 | 7.0 |
| 77 | `8rwcbio3` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 0.1 | 0.003 | 0.05564 | 1.9178 | 0.8515 | 0.000 | 11.0 |
| 89 | `qwjfpjfp` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 1 | 0.003 | 0.05736 | 1.8840 | 0.8473 | 0.000 | 10.0 |
| 92 | `gafwihen` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 1 | 0.01 | 0.05855 | 1.8472 | 0.8435 | 0.000 | 8.0 |
| 91 | `zo2lwsax` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 1 | 0.01 | 0.05865 | 1.8224 | 0.8445 | 0.000 | 7.0 |
| 96 | `7m7sojd7` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 10 | 0 | 0.05923 | 2.1891 | 0.8445 | 0.000 | 10.0 |
| 80 | `1cirl9hq` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 0.1 | 0.01 | 0.06060 | 1.7688 | 0.8373 | 0.000 | 7.0 |
| 42 | `g5lv6psk` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 1.0e-04 | 0.01 | 0.06069 | 1.8247 | 0.8390 | 3.246 | 3.0 |
| 30 | `bopzhnhs` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 1.0e-05 | 0.01 | 0.06145 | 1.9838 | 0.8382 | 23.417 | 3.0 |
| 46 | `2vgv9d10` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 1.0e-04 | 0.03 | 0.06161 | 2.4555 | 0.8364 | 6.380 | 4.0 |
| 81 | `gnmnjxh6` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 0.1 | 0.03 | 0.06246 | 2.2037 | 0.8353 | 0.002 | 4.0 |
| 93 | `y9qw0nzw` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 1 | 0.03 | 0.06313 | 2.2874 | 0.8334 | 0.000 | 4.0 |
| 86 | `es9rkyu9` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 1 | 0 | 0.06319 | 2.0535 | 0.8311 | 0.000 | 17.0 |
| 19 | `lrjf2v59` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 1.0e-06 | 0.01 | 0.06326 | 1.8310 | 0.8313 | 42.295 | 4.0 |
| 7 | `o8sq8jwf` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 0 | 0.01 | 0.06340 | 1.8999 | 0.8308 | 50.877 | 4.0 |
| 103 | `yjaxnguc` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 10 | 0.01 | 0.06473 | 2.1584 | 0.8275 | 0.000 | 7.0 |
| 58 | `ax3i21gb` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 0.001 | 0.03 | 0.06582 | 2.3638 | 0.8252 | 0.493 | 4.0 |
| 69 | `8lzeb08m` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 0.01 | 0.03 | 0.06639 | 2.1273 | 0.8242 | 0.097 | 6.0 |
| 98 | `hb9m5cf1` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 10 | 0 | 0.06641 | 2.3487 | 0.8219 | 0.000 | 17.0 |
| 6 | `xx1o68vh` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 0 | 0.01 | 0.06758 | 1.9164 | 0.8223 | 32.562 | 2.0 |
| 70 | `djxni1pr` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 0.01 | 0.03 | 0.06814 | 2.2582 | 0.8198 | 0.907 | 5.0 |
| 104 | `vjp0e4eo` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 10 | 0.01 | 0.06827 | 1.9376 | 0.8164 | 0.000 | 8.0 |
| 18 | `bwpeva8l` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 1.0e-06 | 0.01 | 0.06833 | 1.9236 | 0.8204 | 28.169 | 2.0 |
| 57 | `kzxevesg` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 0.001 | 0.03 | 0.06856 | 2.1386 | 0.8185 | 0.445 | 6.0 |
| 105 | `i19p3en6` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 10 | 0.03 | 0.06873 | 2.3920 | 0.8187 | 0.000 | 13.0 |
| 102 | `gufk2xiq` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 10 | 0.01 | 0.07043 | 2.2564 | 0.8145 | 0.000 | 4.0 |
| 71 | `vzsmwpm8` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 0.01 | 0.03 | 0.07236 | 2.4533 | 0.8053 | 0.029 | 5.0 |
| 45 | `zn7p8iph` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 1.0e-04 | 0.03 | 0.07306 | 2.2851 | 0.8070 | 7.022 | 7.0 |
| 33 | `93th1j1d` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 1.0e-05 | 0.03 | 0.07361 | 2.1934 | 0.8064 | 18.666 | 4.0 |
| 9 | `w32a5u64` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 0 | 0.03 | 0.07460 | 2.3023 | 0.8035 | 13.012 | 1.0 |
| 21 | `1k2rt4b6` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 1.0e-06 | 0.03 | 0.07511 | 2.3128 | 0.8022 | 12.244 | 1.0 |
| 94 | `36rugyis` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 1 | 0.03 | 0.08028 | 2.7884 | 0.7866 | 0.000 | 3.0 |
| 95 | `c3hycrtu` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 1 | 0.03 | 0.08092 | 2.7129 | 0.7820 | 0.001 | 3.0 |
| 34 | `3lmyl11w` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 1.0e-05 | 0.03 | 0.08173 | 2.7292 | 0.7835 | 87.367 | 4.0 |
| 22 | `yxnynuov` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 1.0e-06 | 0.03 | 0.08278 | 2.5173 | 0.7812 | 179.406 | 4.0 |
| 83 | `d1331la8` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 0.1 | 0.03 | 0.08452 | 2.7595 | 0.7723 | 0.050 | 6.0 |
| 10 | `n3rzhgft` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 0 | 0.03 | 0.08753 | 2.7294 | 0.7673 | 68.879 | 3.0 |
| 106 | `gfab1lzv` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 10 | 0.03 | 0.08830 | 2.9786 | 0.7652 | 0.000 | 3.0 |
| 35 | `9pqw8gde` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 1.0e-05 | 0.03 | 0.08981 | 2.4959 | 0.7591 | 28.154 | 6.0 |
| 82 | `2vxqg39v` | 65 | 65 | 11 | 11 | 0.990219 | 11 | 121 | 0.1 | 0.03 | 0.09202 | 3.1109 | 0.7551 | 0.014 | — |
| 11 | `60ga05bl` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 0 | 0.03 | 0.09349 | 2.5355 | 0.7500 | 20.257 | 3.0 |
| 101 | `9c615cv1` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 10 | 0.003 | 0.09363 | 2.6015 | 0.7491 | 0.000 | 18.0 |
| 23 | `gqz7owk2` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 1.0e-06 | 0.03 | 0.09385 | 2.5412 | 0.7490 | 18.708 | 3.0 |
| 99 | `0vwtwkff` | 85 | 85 | 14 | 14 | 0.990074 | 14 | 196 | 10 | 0.003 | 0.09419 | 2.8561 | 0.7519 | 0.000 | 6.0 |
| 47 | `as98nrul` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 1.0e-04 | 0.03 | 0.10163 | 2.6064 | 0.7280 | 3.461 | 5.0 |
| 59 | `h2148c8k` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 0.001 | 0.03 | 0.10267 | 2.6626 | 0.7240 | 0.127 | 1.0 |
| 107 | `ap8tht6d` | 75 | 75 | 12 | 12 | 0.990036 | 12 | 144 | 10 | 0.03 | 0.10430 | 3.3022 | 0.7188 | 0.000 | 3.0 |

### Best run per `obs_noise_scale`

| obs_noise_scale | Best LC weight | Best traj loss | MASE at best | R² | LC loss | epoch |
|---|---|---|---|---|---|---|
| 0.0 | 0.0e+00 | 0.01006 | 0.9201 | 0.9732 | 18.979 | 15.0 |
| 0.003 | 1.0e-04 | 0.01028 | 0.9417 | 0.9722 | 0.977 | 18.0 |
| 0.01 | 1.0e-03 | 0.02259 | 1.1993 | 0.9390 | 0.190 | 8.0 |
| 0.03 | 1.0e-04 | 0.06161 | 2.4555 | 0.8364 | 6.380 | 4.0 |

## Success-criteria verdicts (automated)

| Criterion | Verdict | Note |
|---|---|---|
| All 108 Stage A runs train without divergence | **Unknown** |  |
| Per-cell autodim n_target_dims logged | **Unknown** |  |
| two_stage_cull keeps top ~54 (cull_fraction=0.5) | **Unknown** |  |
| Best obs_noise_scale > 0 cell strictly improves vs obs_noise_scale=0 baseline at the same (n_delays, LC) cell on val/trajectory_loss | **Unknown** |  |

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

### tangent_spectrum

![tangent_spectrum](figures/tangent_spectrum.png)

### per_run_tangent_spectrum

![per_run_tangent_spectrum](figures/per_run_tangent_spectrum.png)

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
No run_id provided — selecting best run from group 'lorenz_partial_additive_splitmode_p30_obsnoise005_cayley_autodim_top3nd_v2__lc_obsnoisescale_sweep_20260503T045452Z__stage_a' ...
Found 108 total runs in JacobianODE/Lorenz_INDpartial_NDsweep_cayley_autodim_D1_NormTrue__JacobianODE (group=lorenz_partial_additive_splitmode_p30_obsnoise005_cayley_autodim_top3nd_v2__lc_obsnoisescale_sweep_20260503T045452Z__stage_a)
All runs (state, loop_closure_weight, tangent_entropy_weight, kl_dyn_weight):
  egrstbam: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  xx1o68vh: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  vmewzehv: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  o8sq8jwf: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  0z0avj5k: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  60ga05bl: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  xpqhs9r5: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  wizbsqsw: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  n3rzhgft: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  w32a5u64: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  o032u4j4: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  b2q4dvxe: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  klj5tn5w: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  1r0paozx: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  bwpeva8l: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  lrjf2v59: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  3nstn66s: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  h1yhjzto: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  yxnynuov: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  1k2rt4b6: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  gqz7owk2: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  3nplzrjw: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  322zwhto: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  eyo7kbrd: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  4o129gpe: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  6v59mul9: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  bopzhnhs: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  r5y3m8kt: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  p5pa20fn: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  3lmyl11w: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  93th1j1d: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  id6d0nan: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  9pqw8gde: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  r838tfeu: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  pxft8ayf: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  0enol8sg: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  60bbpe0s: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  w4yawenf: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  365xxmpk: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  g5lv6psk: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  n6a0y649: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  08nukj26: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  3cexp570: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  2vgv9d10: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  as98nrul: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  fgorh2u6: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  qk5kwnu4: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  a8rjy7kg: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  anrfk2i7: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  0dn67ryj: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  jbd5yb6z: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  qj02b8u0: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  9xwwuzd1: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  c2fxqa3c: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  kzxevesg: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  ax3i21gb: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  g8e71vju: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  lu9mdd3t: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  jgms7rny: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  35v0e7ov: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  onfwfz1d: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  45cyq4v1: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  fuixohqa: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  1pthqep1: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  5nr5lua3: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  dxi699aa: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  zn7p8iph: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  h2148c8k: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  3eqixatz: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  8lzeb08m: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  623olsmk: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  vzsmwpm8: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  djxni1pr: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  ugns9mbh: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  x65g33rr: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  q7sb3aet: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  31ep3aj1: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  8rwcbio3: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  75rh7ivy: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  2vxqg39v: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  oi336ix7: state=finished, lc=1.0, te=0.0, kl_dyn=0.0
  d1331la8: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  srme5iw0: state=finished, lc=1.0, te=0.0, kl_dyn=0.0
  es9rkyu9: state=finished, lc=1.0, te=0.0, kl_dyn=0.0
  im9rzz5v: state=finished, lc=1.0, te=0.0, kl_dyn=0.0
  zs23hgfq: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  fcfnapsz: state=finished, lc=1.0, te=0.0, kl_dyn=0.0
  qwjfpjfp: state=finished, lc=1.0, te=0.0, kl_dyn=0.0
  q1cdbwpc: state=finished, lc=1.0, te=0.0, kl_dyn=0.0
  zo2lwsax: state=finished, lc=1.0, te=0.0, kl_dyn=0.0
  1cirl9hq: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  gafwihen: state=finished, lc=1.0, te=0.0, kl_dyn=0.0
  36rugyis: state=finished, lc=1.0, te=0.0, kl_dyn=0.0
  c3hycrtu: state=finished, lc=1.0, te=0.0, kl_dyn=0.0
  7m7sojd7: state=finished, lc=10.0, te=0.0, kl_dyn=0.0
  gnmnjxh6: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  0vwtwkff: state=finished, lc=10.0, te=0.0, kl_dyn=0.0
  hb9m5cf1: state=finished, lc=10.0, te=0.0, kl_dyn=0.0
  35s2gm94: state=finished, lc=10.0, te=0.0, kl_dyn=0.0
  9c615cv1: state=finished, lc=10.0, te=0.0, kl_dyn=0.0
  q7fvlalq: state=finished, lc=10.0, te=0.0, kl_dyn=0.0
  y9qw0nzw: state=finished, lc=1.0, te=0.0, kl_dyn=0.0
  gfab1lzv: state=finished, lc=10.0, te=0.0, kl_dyn=0.0
  i19p3en6: state=finished, lc=10.0, te=0.0, kl_dyn=0.0
  vjp0e4eo: state=finished, lc=10.0, te=0.0, kl_dyn=0.0
  yjaxnguc: state=finished, lc=10.0, te=0.0, kl_dyn=0.0
  ap8tht6d: state=finished, lc=10.0, te=0.0, kl_dyn=0.0
  gufk2xiq: state=finished, lc=10.0, te=0.0, kl_dyn=0.0

slurm_timeout_min not found in any run config — falling back to 180 min
  Including egrstbam (lc=0.0): use_all_runs=True (state=finished)
  Including xx1o68vh (lc=0.0): use_all_runs=True (state=finished)
  Including vmewzehv (lc=0.0): use_all_runs=True (state=finished)
  Including o8sq8jwf (lc=0.0): use_all_runs=True (state=finished)
  Including 0z0avj5k (lc=0.0): use_all_runs=True (state=finished)
  Including 60ga05bl (lc=0.0): use_all_runs=True (state=finished)
  Including xpqhs9r5 (lc=1e-06): use_all_runs=True (state=finished)
  Including wizbsqsw (lc=1e-06): use_all_runs=True (state=finished)
  Including n3rzhgft (lc=0.0): use_all_runs=True (state=finished)
  Including w32a5u64 (lc=0.0): use_all_runs=True (state=finished)
  Including o032u4j4 (lc=1e-06): use_all_runs=True (state=finished)
  Including b2q4dvxe (lc=1e-06): use_all_runs=True (state=finished)
  Including klj5tn5w (lc=1e-06): use_all_runs=True (state=finished)
  Including 1r0paozx (lc=1e-06): use_all_runs=True (state=finished)
  Including bwpeva8l (lc=1e-06): use_all_runs=True (state=finished)
  Including lrjf2v59 (lc=1e-06): use_all_runs=True (state=finished)
  Including 3nstn66s (lc=0.0): use_all_runs=True (state=finished)
  Including h1yhjzto (lc=1e-06): use_all_runs=True (state=finished)
  Including yxnynuov (lc=1e-06): use_all_runs=True (state=finished)
  Including 1k2rt4b6 (lc=1e-06): use_all_runs=True (state=finished)
  Including gqz7owk2 (lc=1e-06): use_all_runs=True (state=finished)
  Including 3nplzrjw (lc=1e-05): use_all_runs=True (state=finished)
  Including 322zwhto (lc=1e-05): use_all_runs=True (state=finished)
  Including eyo7kbrd (lc=1e-05): use_all_runs=True (state=finished)
  Including 4o129gpe (lc=1e-05): use_all_runs=True (state=finished)
  Including 6v59mul9 (lc=1e-05): use_all_runs=True (state=finished)
  Including bopzhnhs (lc=1e-05): use_all_runs=True (state=finished)
  Including r5y3m8kt (lc=1e-05): use_all_runs=True (state=finished)
  Including p5pa20fn (lc=1e-05): use_all_runs=True (state=finished)
  Including 3lmyl11w (lc=1e-05): use_all_runs=True (state=finished)
  Including 93th1j1d (lc=1e-05): use_all_runs=True (state=finished)
  Including id6d0nan (lc=0.0): use_all_runs=True (state=finished)
  Including 9pqw8gde (lc=1e-05): use_all_runs=True (state=finished)
  Including r838tfeu (lc=0.0001): use_all_runs=True (state=finished)
  Including pxft8ayf (lc=0.0001): use_all_runs=True (state=finished)
  Including 0enol8sg (lc=0.0001): use_all_runs=True (state=finished)
  Including 60bbpe0s (lc=0.0001): use_all_runs=True (state=finished)
  Including w4yawenf (lc=0.0001): use_all_runs=True (state=finished)
  Including 365xxmpk (lc=0.0001): use_all_runs=True (state=finished)
  Including g5lv6psk (lc=0.0001): use_all_runs=True (state=finished)
  Including n6a0y649 (lc=0.0001): use_all_runs=True (state=finished)
  Including 08nukj26 (lc=0.0001): use_all_runs=True (state=finished)
  Including 3cexp570 (lc=0.0): use_all_runs=True (state=finished)
  Including 2vgv9d10 (lc=0.0001): use_all_runs=True (state=finished)
  Including as98nrul (lc=0.0001): use_all_runs=True (state=finished)
  Including fgorh2u6 (lc=0.001): use_all_runs=True (state=finished)
  Including qk5kwnu4 (lc=0.001): use_all_runs=True (state=finished)
  Including a8rjy7kg (lc=0.001): use_all_runs=True (state=finished)
  Including anrfk2i7 (lc=0.001): use_all_runs=True (state=finished)
  Including 0dn67ryj (lc=0.001): use_all_runs=True (state=finished)
  Including jbd5yb6z (lc=0.001): use_all_runs=True (state=finished)
  Including qj02b8u0 (lc=0.001): use_all_runs=True (state=finished)
  Including 9xwwuzd1 (lc=0.001): use_all_runs=True (state=finished)
  Including c2fxqa3c (lc=0.001): use_all_runs=True (state=finished)
  Including kzxevesg (lc=0.001): use_all_runs=True (state=finished)
  Including ax3i21gb (lc=0.001): use_all_runs=True (state=finished)
  Including g8e71vju (lc=0.01): use_all_runs=True (state=finished)
  Including lu9mdd3t (lc=0.01): use_all_runs=True (state=finished)
  Including jgms7rny (lc=0.0): use_all_runs=True (state=finished)
  Including 35v0e7ov (lc=0.01): use_all_runs=True (state=finished)
  Including onfwfz1d (lc=0.01): use_all_runs=True (state=finished)
  Including 45cyq4v1 (lc=0.01): use_all_runs=True (state=finished)
  Including fuixohqa (lc=0.01): use_all_runs=True (state=finished)
  Including 1pthqep1 (lc=0.01): use_all_runs=True (state=finished)
  Including 5nr5lua3 (lc=0.01): use_all_runs=True (state=finished)
  Including dxi699aa (lc=1e-05): use_all_runs=True (state=finished)
  Including zn7p8iph (lc=0.0001): use_all_runs=True (state=finished)
  Including h2148c8k (lc=0.001): use_all_runs=True (state=finished)
  Including 3eqixatz (lc=0.01): use_all_runs=True (state=finished)
  Including 8lzeb08m (lc=0.01): use_all_runs=True (state=finished)
  Including 623olsmk (lc=0.1): use_all_runs=True (state=finished)
  Including vzsmwpm8 (lc=0.01): use_all_runs=True (state=finished)
  Including djxni1pr (lc=0.01): use_all_runs=True (state=finished)
  Including ugns9mbh (lc=0.1): use_all_runs=True (state=finished)
  Including x65g33rr (lc=0.1): use_all_runs=True (state=finished)
  Including q7sb3aet (lc=0.1): use_all_runs=True (state=finished)
  Including 31ep3aj1 (lc=0.1): use_all_runs=True (state=finished)
  Including 8rwcbio3 (lc=0.1): use_all_runs=True (state=finished)
  Including 75rh7ivy (lc=0.1): use_all_runs=True (state=finished)
  Including 2vxqg39v (lc=0.1): use_all_runs=True (state=finished)
  Including oi336ix7 (lc=1.0): use_all_runs=True (state=finished)
  Including d1331la8 (lc=0.1): use_all_runs=True (state=finished)
  Including srme5iw0 (lc=1.0): use_all_runs=True (state=finished)
  Including es9rkyu9 (lc=1.0): use_all_runs=True (state=finished)
  Including im9rzz5v (lc=1.0): use_all_runs=True (state=finished)
  Including zs23hgfq (lc=0.1): use_all_runs=True (state=finished)
  Including fcfnapsz (lc=1.0): use_all_runs=True (state=finished)
  Including qwjfpjfp (lc=1.0): use_all_runs=True (state=finished)
  Including q1cdbwpc (lc=1.0): use_all_runs=True (state=finished)
  Including zo2lwsax (lc=1.0): use_all_runs=True (state=finished)
  Including 1cirl9hq (lc=0.1): use_all_runs=True (state=finished)
  Including gafwihen (lc=1.0): use_all_runs=True (state=finished)
  Including 36rugyis (lc=1.0): use_all_runs=True (state=finished)
  Including c3hycrtu (lc=1.0): use_all_runs=True (state=finished)
  Including 7m7sojd7 (lc=10.0): use_all_runs=True (state=finished)
  Including gnmnjxh6 (lc=0.1): use_all_runs=True (state=finished)
  Including 0vwtwkff (lc=10.0): use_all_runs=True (state=finished)
  Including hb9m5cf1 (lc=10.0): use_all_runs=True (state=finished)
  Including 35s2gm94 (lc=10.0): use_all_runs=True (state=finished)
  Including 9c615cv1 (lc=10.0): use_all_runs=True (state=finished)
  Including q7fvlalq (lc=10.0): use_all_runs=True (state=finished)
  Including y9qw0nzw (lc=1.0): use_all_runs=True (state=finished)
  Including gfab1lzv (lc=10.0): use_all_runs=True (state=finished)
  Including i19p3en6 (lc=10.0): use_all_runs=True (state=finished)
  Including vjp0e4eo (lc=10.0): use_all_runs=True (state=finished)
  Including yjaxnguc (lc=10.0): use_all_runs=True (state=finished)
  Including ap8tht6d (lc=10.0): use_all_runs=True (state=finished)
  Including gufk2xiq (lc=10.0): use_all_runs=True (state=finished)
Found 108 effectively-done sweep runs:
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=0z0avj5k
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=3cexp570
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=3nstn66s
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=60ga05bl
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=egrstbam
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=id6d0nan
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=jgms7rny
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=n3rzhgft
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=o8sq8jwf
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=vmewzehv
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=w32a5u64
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=xx1o68vh
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=1k2rt4b6
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=1r0paozx
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=b2q4dvxe
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=bwpeva8l
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=gqz7owk2
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=h1yhjzto
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=klj5tn5w
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=lrjf2v59
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=o032u4j4
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=wizbsqsw
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=xpqhs9r5
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=yxnynuov
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=322zwhto
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=3lmyl11w
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=3nplzrjw
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=4o129gpe
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=6v59mul9
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=93th1j1d
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=9pqw8gde
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=bopzhnhs
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=dxi699aa
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=eyo7kbrd
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=p5pa20fn
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=r5y3m8kt
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=08nukj26
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=0enol8sg
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=2vgv9d10
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=365xxmpk
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=60bbpe0s
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=as98nrul
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=g5lv6psk
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=n6a0y649
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=pxft8ayf
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=r838tfeu
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=w4yawenf
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=zn7p8iph
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=0dn67ryj
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=9xwwuzd1
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=a8rjy7kg
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=anrfk2i7
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=ax3i21gb
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=c2fxqa3c
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=fgorh2u6
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=h2148c8k
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=jbd5yb6z
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=kzxevesg
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=qj02b8u0
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=qk5kwnu4
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=1pthqep1
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=35v0e7ov
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=3eqixatz
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=45cyq4v1
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=5nr5lua3
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=8lzeb08m
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=djxni1pr
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=fuixohqa
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=g8e71vju
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=lu9mdd3t
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=onfwfz1d
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=vzsmwpm8
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=1cirl9hq
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=2vxqg39v
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=31ep3aj1
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=623olsmk
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=75rh7ivy
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=8rwcbio3
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=d1331la8
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=gnmnjxh6
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=q7sb3aet
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=ugns9mbh
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=x65g33rr
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=zs23hgfq
  loop_closure_weight=1.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=36rugyis
  loop_closure_weight=1.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=c3hycrtu
  loop_closure_weight=1.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=es9rkyu9
  loop_closure_weight=1.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=fcfnapsz
  loop_closure_weight=1.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=gafwihen
  loop_closure_weight=1.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=im9rzz5v
  loop_closure_weight=1.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=oi336ix7
  loop_closure_weight=1.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=q1cdbwpc
  loop_closure_weight=1.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=qwjfpjfp
  loop_closure_weight=1.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=srme5iw0
  loop_closure_weight=1.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=y9qw0nzw
  loop_closure_weight=1.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=zo2lwsax
  loop_closure_weight=10.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=0vwtwkff
  loop_closure_weight=10.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=35s2gm94
  loop_closure_weight=10.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=7m7sojd7
  loop_closure_weight=10.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=9c615cv1
  loop_closure_weight=10.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=ap8tht6d
  loop_closure_weight=10.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=gfab1lzv
  loop_closure_weight=10.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=gufk2xiq
  loop_closure_weight=10.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=hb9m5cf1
  loop_closure_weight=10.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=i19p3en6
  loop_closure_weight=10.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=q7fvlalq
  loop_closure_weight=10.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=vjp0e4eo
  loop_closure_weight=10.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=yjaxnguc
n_dims=65, n_latent=65, n_dyn=11, dt=0.0150
  run=0z0avj5k: DiagnosticMetrics(one_step_mase=0.7241968512535095, loop_closure_loss=103.63204956054688, fast_eigenvalue_fraction=0.34090909361839294, trajectory_val_loss=0.029627814888954163) (from W&B history)
  run=3cexp570: DiagnosticMetrics(one_step_mase=0.6728572845458984, loop_closure_loss=18.976367950439453, fast_eigenvalue_fraction=0.5, trajectory_val_loss=0.010691762901842594) (from W&B history)
  run=3nstn66s: DiagnosticMetrics(one_step_mase=0.6879681348800659, loop_closure_loss=42.096778869628906, fast_eigenvalue_fraction=0.5, trajectory_val_loss=0.01101447269320488) (from W&B history)
  run=60ga05bl: DiagnosticMetrics(one_step_mase=1.4294403791427612, loop_closure_loss=20.257028579711914, fast_eigenvalue_fraction=0.75, trajectory_val_loss=0.09348548203706741) (from W&B history)
  run=egrstbam: DiagnosticMetrics(one_step_mase=0.7299454212188721, loop_closure_loss=121.26190185546875, fast_eigenvalue_fraction=0.375, trajectory_val_loss=0.013412844389677048) (from W&B history)
  run=id6d0nan: DiagnosticMetrics(one_step_mase=0.6610474586486816, loop_closure_loss=18.978965759277344, fast_eigenvalue_fraction=0.3636363744735718, trajectory_val_loss=0.010060817934572697) (from W&B history)
  run=jgms7rny: DiagnosticMetrics(one_step_mase=0.6975304484367371, loop_closure_loss=86.91950225830078, fast_eigenvalue_fraction=0.4285714328289032, trajectory_val_loss=0.010866080410778522) (from W&B history)
  run=n3rzhgft: DiagnosticMetrics(one_step_mase=1.2659687995910645, loop_closure_loss=68.87886810302734, fast_eigenvalue_fraction=0.6590909361839294, trajectory_val_loss=0.08753490447998047) (from W&B history)
  run=o8sq8jwf: DiagnosticMetrics(one_step_mase=0.8048585653305054, loop_closure_loss=50.877037048339844, fast_eigenvalue_fraction=0.7272727489471436, trajectory_val_loss=0.06340308487415314) (from W&B history)
  run=vmewzehv: DiagnosticMetrics(one_step_mase=0.9125231504440308, loop_closure_loss=98.68299102783203, fast_eigenvalue_fraction=0.6666666865348816, trajectory_val_loss=0.05261730030179024) (from W&B history)
  run=w32a5u64: DiagnosticMetrics(one_step_mase=1.4002432823181152, loop_closure_loss=13.012407302856445, fast_eigenvalue_fraction=0.7857142686843872, trajectory_val_loss=0.07460242509841919) (from W&B history)
  run=xx1o68vh: DiagnosticMetrics(one_step_mase=1.2272433042526245, loop_closure_loss=32.56160354614258, fast_eigenvalue_fraction=0.7857142686843872, trajectory_val_loss=0.06757896393537521) (from W&B history)
  run=1k2rt4b6: DiagnosticMetrics(one_step_mase=1.4004384279251099, loop_closure_loss=12.243999481201172, fast_eigenvalue_fraction=0.7857142686843872, trajectory_val_loss=0.0751083642244339) (from W&B history)
  run=1r0paozx: DiagnosticMetrics(one_step_mase=0.7301290035247803, loop_closure_loss=61.03571701049805, fast_eigenvalue_fraction=0.2954545319080353, trajectory_val_loss=0.02576350048184395) (from W&B history)
  run=b2q4dvxe: DiagnosticMetrics(one_step_mase=0.7090665698051453, loop_closure_loss=52.718528747558594, fast_eigenvalue_fraction=0.4285714328289032, trajectory_val_loss=0.011422554031014442) (from W&B history)
  run=bwpeva8l: DiagnosticMetrics(one_step_mase=1.2275829315185547, loop_closure_loss=28.168752670288086, fast_eigenvalue_fraction=0.7857142686843872, trajectory_val_loss=0.0683257132768631) (from W&B history)
  run=gqz7owk2: DiagnosticMetrics(one_step_mase=1.4347456693649292, loop_closure_loss=18.70840835571289, fast_eigenvalue_fraction=0.75, trajectory_val_loss=0.09385388344526291) (from W&B history)
  run=h1yhjzto: DiagnosticMetrics(one_step_mase=0.8945250511169434, loop_closure_loss=62.94300842285156, fast_eigenvalue_fraction=0.6666666865348816, trajectory_val_loss=0.049337442964315414) (from W&B history)
  run=klj5tn5w: DiagnosticMetrics(one_step_mase=0.7311393618583679, loop_closure_loss=51.11439895629883, fast_eigenvalue_fraction=0.375, trajectory_val_loss=0.011741348542273045) (from W&B history)
  run=lrjf2v59: DiagnosticMetrics(one_step_mase=0.8025417327880859, loop_closure_loss=42.29464340209961, fast_eigenvalue_fraction=0.7272727489471436, trajectory_val_loss=0.06325514614582062) (from W&B history)
  run=o032u4j4: DiagnosticMetrics(one_step_mase=0.6724947690963745, loop_closure_loss=8.813632011413574, fast_eigenvalue_fraction=0.5, trajectory_val_loss=0.010999811813235283) (from W&B history)
  run=wizbsqsw: DiagnosticMetrics(one_step_mase=0.6895160675048828, loop_closure_loss=14.053985595703125, fast_eigenvalue_fraction=0.5, trajectory_val_loss=0.011823121458292007) (from W&B history)
  run=xpqhs9r5: DiagnosticMetrics(one_step_mase=0.6622062921524048, loop_closure_loss=8.551618576049805, fast_eigenvalue_fraction=0.3636363744735718, trajectory_val_loss=0.010239110328257084) (from W&B history)
  run=yxnynuov: DiagnosticMetrics(one_step_mase=1.1202088594436646, loop_closure_loss=179.40640258789062, fast_eigenvalue_fraction=0.6704545617103577, trajectory_val_loss=0.08277576416730881) (from W&B history)
  run=322zwhto: DiagnosticMetrics(one_step_mase=0.7381312847137451, loop_closure_loss=4.4599504470825195, fast_eigenvalue_fraction=0.4285714328289032, trajectory_val_loss=0.012653304263949394) (from W&B history)
  run=3lmyl11w: DiagnosticMetrics(one_step_mase=1.123125672340393, loop_closure_loss=87.36674499511719, fast_eigenvalue_fraction=0.6704545617103577, trajectory_val_loss=0.08172541856765747) (from W&B history)
  run=3nplzrjw: DiagnosticMetrics(one_step_mase=0.6732549071311951, loop_closure_loss=2.5162665843963623, fast_eigenvalue_fraction=0.3636363744735718, trajectory_val_loss=0.010763246566057205) (from W&B history)
  run=4o129gpe: DiagnosticMetrics(one_step_mase=0.6542772650718689, loop_closure_loss=3.755850315093994, fast_eigenvalue_fraction=0.3636363744735718, trajectory_val_loss=0.013653415255248547) (from W&B history)
  run=6v59mul9: DiagnosticMetrics(one_step_mase=0.6820642948150635, loop_closure_loss=6.1289567947387695, fast_eigenvalue_fraction=0.4285714328289032, trajectory_val_loss=0.011997700668871403) (from W&B history)
  run=93th1j1d: DiagnosticMetrics(one_step_mase=1.197490930557251, loop_closure_loss=18.66613006591797, fast_eigenvalue_fraction=0.7232142686843872, trajectory_val_loss=0.07360954582691193) (from W&B history)
  run=9pqw8gde: DiagnosticMetrics(one_step_mase=1.2869155406951904, loop_closure_loss=28.154050827026367, fast_eigenvalue_fraction=0.78125, trajectory_val_loss=0.08980510383844376) (from W&B history)
  run=bopzhnhs: DiagnosticMetrics(one_step_mase=0.987337589263916, loop_closure_loss=23.41680145263672, fast_eigenvalue_fraction=0.7857142686843872, trajectory_val_loss=0.06145293638110161) (from W&B history)
  run=dxi699aa: DiagnosticMetrics(one_step_mase=0.8690254092216492, loop_closure_loss=10.535152435302734, fast_eigenvalue_fraction=0.6666666865348816, trajectory_val_loss=0.05181874334812164) (from W&B history)
  run=eyo7kbrd: DiagnosticMetrics(one_step_mase=0.6718369722366333, loop_closure_loss=2.7021450996398926, fast_eigenvalue_fraction=0.5, trajectory_val_loss=0.011564199812710285) (from W&B history)
  run=p5pa20fn: DiagnosticMetrics(one_step_mase=0.762801468372345, loop_closure_loss=4.512148857116699, fast_eigenvalue_fraction=0.7272727489471436, trajectory_val_loss=0.029722116887569427) (from W&B history)
  run=r5y3m8kt: DiagnosticMetrics(one_step_mase=0.7540072798728943, loop_closure_loss=15.207864761352539, fast_eigenvalue_fraction=0.4583333432674408, trajectory_val_loss=0.011784234084188938) (from W&B history)
  run=08nukj26: DiagnosticMetrics(one_step_mase=0.8555707335472107, loop_closure_loss=1.401369333267212, fast_eigenvalue_fraction=0.6666666865348816, trajectory_val_loss=0.0410570465028286) (from W&B history)
  run=0enol8sg: DiagnosticMetrics(one_step_mase=0.6754792332649231, loop_closure_loss=0.4858686923980713, fast_eigenvalue_fraction=0.3636363744735718, trajectory_val_loss=0.012121046893298626) (from W&B history)
  run=2vgv9d10: DiagnosticMetrics(one_step_mase=1.2262054681777954, loop_closure_loss=6.380012035369873, fast_eigenvalue_fraction=0.6477272510528564, trajectory_val_loss=0.06160847842693329) (from W&B history)
  run=365xxmpk: DiagnosticMetrics(one_step_mase=0.7194602489471436, loop_closure_loss=0.9768392443656921, fast_eigenvalue_fraction=0.5, trajectory_val_loss=0.010277488268911839) (from W&B history)
  run=60bbpe0s: DiagnosticMetrics(one_step_mase=0.6844339966773987, loop_closure_loss=0.7221170663833618, fast_eigenvalue_fraction=0.4285714328289032, trajectory_val_loss=0.012554775923490524) (from W&B history)
  run=as98nrul: DiagnosticMetrics(one_step_mase=1.5002098083496094, loop_closure_loss=3.460723876953125, fast_eigenvalue_fraction=0.7604166865348816, trajectory_val_loss=0.10162521153688431) (from W&B history)
  run=g5lv6psk: DiagnosticMetrics(one_step_mase=1.1444042921066284, loop_closure_loss=3.245896339416504, fast_eigenvalue_fraction=0.7857142686843872, trajectory_val_loss=0.06069263070821762) (from W&B history)
  run=n6a0y649: DiagnosticMetrics(one_step_mase=0.7766633629798889, loop_closure_loss=1.4267914295196533, fast_eigenvalue_fraction=0.6363636255264282, trajectory_val_loss=0.027642741799354553) (from W&B history)
  run=pxft8ayf: DiagnosticMetrics(one_step_mase=0.672496497631073, loop_closure_loss=0.35516297817230225, fast_eigenvalue_fraction=0.5, trajectory_val_loss=0.014488708227872849) (from W&B history)
  run=r838tfeu: DiagnosticMetrics(one_step_mase=0.6978986859321594, loop_closure_loss=0.4618464410305023, fast_eigenvalue_fraction=0.5, trajectory_val_loss=0.013806214556097984) (from W&B history)
  run=w4yawenf: DiagnosticMetrics(one_step_mase=0.6690781712532043, loop_closure_loss=0.6286808848381042, fast_eigenvalue_fraction=0.3636363744735718, trajectory_val_loss=0.017500177025794983) (from W&B history)
  run=zn7p8iph: DiagnosticMetrics(one_step_mase=1.3071895837783813, loop_closure_loss=7.021665096282959, fast_eigenvalue_fraction=0.7857142686843872, trajectory_val_loss=0.07306397706270218) (from W&B history)
  run=0dn67ryj: DiagnosticMetrics(one_step_mase=0.7278878688812256, loop_closure_loss=0.2334107607603073, fast_eigenvalue_fraction=0.5, trajectory_val_loss=0.015876824036240578) (from W&B history)
  run=9xwwuzd1: DiagnosticMetrics(one_step_mase=0.7613407373428345, loop_closure_loss=0.07474297285079956, fast_eigenvalue_fraction=0.5454545617103577, trajectory_val_loss=0.02374305948615074) (from W&B history)
  run=a8rjy7kg: DiagnosticMetrics(one_step_mase=0.6837940216064453, loop_closure_loss=0.0535239614546299, fast_eigenvalue_fraction=0.5, trajectory_val_loss=0.014339450746774673) (from W&B history)
  run=anrfk2i7: DiagnosticMetrics(one_step_mase=0.6890305876731873, loop_closure_loss=0.0994788333773613, fast_eigenvalue_fraction=0.4285714328289032, trajectory_val_loss=0.014408836141228676) (from W&B history)
  run=ax3i21gb: DiagnosticMetrics(one_step_mase=1.3262403011322021, loop_closure_loss=0.49275803565979004, fast_eigenvalue_fraction=0.7272727489471436, trajectory_val_loss=0.06581830233335495) (from W&B history)
  run=c2fxqa3c: DiagnosticMetrics(one_step_mase=0.8008435964584351, loop_closure_loss=0.19000989198684692, fast_eigenvalue_fraction=0.5, trajectory_val_loss=0.022591082379221916) (from W&B history)
  run=fgorh2u6: DiagnosticMetrics(one_step_mase=0.7274578809738159, loop_closure_loss=0.06564471125602722, fast_eigenvalue_fraction=0.3958333432674408, trajectory_val_loss=0.01581830345094204) (from W&B history)
  run=h2148c8k: DiagnosticMetrics(one_step_mase=1.8386024236679077, loop_closure_loss=0.127400740981102, fast_eigenvalue_fraction=0.8333333134651184, trajectory_val_loss=0.10266739130020142) (from W&B history)
  run=jbd5yb6z: DiagnosticMetrics(one_step_mase=0.7975439429283142, loop_closure_loss=0.26892897486686707, fast_eigenvalue_fraction=0.5714285969734192, trajectory_val_loss=0.025770431384444237) (from W&B history)
  run=kzxevesg: DiagnosticMetrics(one_step_mase=1.2028007507324219, loop_closure_loss=0.44490155577659607, fast_eigenvalue_fraction=0.7857142686843872, trajectory_val_loss=0.06856337189674377) (from W&B history)
  run=qj02b8u0: DiagnosticMetrics(one_step_mase=0.6468727588653564, loop_closure_loss=0.06139104813337326, fast_eigenvalue_fraction=0.3636363744735718, trajectory_val_loss=0.015108305029571056) (from W&B history)
  run=qk5kwnu4: DiagnosticMetrics(one_step_mase=0.6893457174301147, loop_closure_loss=0.07288362085819244, fast_eigenvalue_fraction=0.3636363744735718, trajectory_val_loss=0.015905121341347694) (from W&B history)
  run=1pthqep1: DiagnosticMetrics(one_step_mase=0.8109372854232788, loop_closure_loss=0.01853501796722412, fast_eigenvalue_fraction=0.5714285969734192, trajectory_val_loss=0.035107601433992386) (from W&B history)
  run=35v0e7ov: DiagnosticMetrics(one_step_mase=0.6762628555297852, loop_closure_loss=0.005392616614699364, fast_eigenvalue_fraction=0.5, trajectory_val_loss=0.021268170326948166) (from W&B history)
  run=3eqixatz: DiagnosticMetrics(one_step_mase=0.8460878133773804, loop_closure_loss=0.04432471841573715, fast_eigenvalue_fraction=0.5833333134651184, trajectory_val_loss=0.03914289548993111) (from W&B history)
  run=45cyq4v1: DiagnosticMetrics(one_step_mase=0.6513453722000122, loop_closure_loss=0.004777135327458382, fast_eigenvalue_fraction=0.3636363744735718, trajectory_val_loss=0.02199990302324295) (from W&B history)
  run=5nr5lua3: DiagnosticMetrics(one_step_mase=0.7576844096183777, loop_closure_loss=0.0046775974333286285, fast_eigenvalue_fraction=0.5454545617103577, trajectory_val_loss=0.028220312669873238) (from W&B history)
  run=8lzeb08m: DiagnosticMetrics(one_step_mase=1.1815996170043945, loop_closure_loss=0.09701453894376755, fast_eigenvalue_fraction=0.7857142686843872, trajectory_val_loss=0.06639348715543747) (from W&B history)
  run=djxni1pr: DiagnosticMetrics(one_step_mase=1.7371344566345215, loop_closure_loss=0.9066724181175232, fast_eigenvalue_fraction=0.8181818127632141, trajectory_val_loss=0.06814113259315491) (from W&B history)
  run=fuixohqa: DiagnosticMetrics(one_step_mase=0.6615667343139648, loop_closure_loss=0.0042815376073122025, fast_eigenvalue_fraction=0.3333333432674408, trajectory_val_loss=0.021729163825511932) (from W&B history)
  run=g8e71vju: DiagnosticMetrics(one_step_mase=0.667911946773529, loop_closure_loss=0.018093222752213478, fast_eigenvalue_fraction=0.4545454680919647, trajectory_val_loss=0.021315662190318108) (from W&B history)
  run=lu9mdd3t: DiagnosticMetrics(one_step_mase=0.6810129880905151, loop_closure_loss=0.006534370128065348, fast_eigenvalue_fraction=0.3571428656578064, trajectory_val_loss=0.01531012449413538) (from W&B history)
  run=onfwfz1d: DiagnosticMetrics(one_step_mase=0.689431369304657, loop_closure_loss=0.012752396054565907, fast_eigenvalue_fraction=0.4285714328289032, trajectory_val_loss=0.01867976225912571) (from W&B history)
  run=vzsmwpm8: DiagnosticMetrics(one_step_mase=1.2379919290542603, loop_closure_loss=0.029497642070055008, fast_eigenvalue_fraction=0.75, trajectory_val_loss=0.0723627433180809) (from W&B history)
  run=1cirl9hq: DiagnosticMetrics(one_step_mase=0.8179916739463806, loop_closure_loss=0.0003643915697466582, fast_eigenvalue_fraction=0.5833333134651184, trajectory_val_loss=0.06059740111231804) (from W&B history)
  run=2vxqg39v: DiagnosticMetrics(one_step_mase=1.886175513267517, loop_closure_loss=0.013650472275912762, fast_eigenvalue_fraction=0.8181818127632141, trajectory_val_loss=0.09201660007238388) (from W&B history)
  run=31ep3aj1: DiagnosticMetrics(one_step_mase=0.7003228664398193, loop_closure_loss=0.00983734242618084, fast_eigenvalue_fraction=0.3636363744735718, trajectory_val_loss=0.046130407601594925) (from W&B history)
  run=623olsmk: DiagnosticMetrics(one_step_mase=0.6918594241142273, loop_closure_loss=0.0003925988858100027, fast_eigenvalue_fraction=0.1428571492433548, trajectory_val_loss=0.04106099531054497) (from W&B history)
  run=75rh7ivy: DiagnosticMetrics(one_step_mase=0.805277943611145, loop_closure_loss=0.0007022831705398858, fast_eigenvalue_fraction=0.5714285969734192, trajectory_val_loss=0.05218138173222542) (from W&B history)
  run=8rwcbio3: DiagnosticMetrics(one_step_mase=0.6955077052116394, loop_closure_loss=0.0003795427328441292, fast_eigenvalue_fraction=0.3333333432674408, trajectory_val_loss=0.05564453452825546) (from W&B history)
  run=d1331la8: DiagnosticMetrics(one_step_mase=1.3164465427398682, loop_closure_loss=0.04951031133532524, fast_eigenvalue_fraction=0.75, trajectory_val_loss=0.08451685309410095) (from W&B history)
  run=gnmnjxh6: DiagnosticMetrics(one_step_mase=1.3115404844284058, loop_closure_loss=0.0018903347663581371, fast_eigenvalue_fraction=0.7857142686843872, trajectory_val_loss=0.06245635449886322) (from W&B history)
  run=q7sb3aet: DiagnosticMetrics(one_step_mase=0.6812309622764587, loop_closure_loss=0.0002750398125499487, fast_eigenvalue_fraction=0.2142857164144516, trajectory_val_loss=0.04401880130171776) (from W&B history)
  run=ugns9mbh: DiagnosticMetrics(one_step_mase=0.6659391522407532, loop_closure_loss=0.00040798497502692044, fast_eigenvalue_fraction=0.1818181872367859, trajectory_val_loss=0.04441814497113228) (from W&B history)
  run=x65g33rr: DiagnosticMetrics(one_step_mase=0.6846709847450256, loop_closure_loss=0.0007355820271186531, fast_eigenvalue_fraction=0.25, trajectory_val_loss=0.049903854727745056) (from W&B history)
  run=zs23hgfq: DiagnosticMetrics(one_step_mase=0.7991393804550171, loop_closure_loss=0.0008333822479471564, fast_eigenvalue_fraction=0.5454545617103577, trajectory_val_loss=0.04497918114066124) (from W&B history)
  run=36rugyis: DiagnosticMetrics(one_step_mase=1.334975242614746, loop_closure_loss=0.000483422918478027, fast_eigenvalue_fraction=0.7272727489471436, trajectory_val_loss=0.080276258289814) (from W&B history)
  run=c3hycrtu: DiagnosticMetrics(one_step_mase=1.3508409261703491, loop_closure_loss=0.0005818246281705797, fast_eigenvalue_fraction=0.6666666865348816, trajectory_val_loss=0.08092015981674194) (from W&B history)
  run=es9rkyu9: DiagnosticMetrics(one_step_mase=0.6671326160430908, loop_closure_loss=1.4060743524169084e-05, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.06318897753953934) (from W&B history)
  run=fcfnapsz: DiagnosticMetrics(one_step_mase=0.7868824005126953, loop_closure_loss=9.125625365413725e-05, fast_eigenvalue_fraction=0.5, trajectory_val_loss=0.05185893923044205) (from W&B history)
  run=gafwihen: DiagnosticMetrics(one_step_mase=0.7860724329948425, loop_closure_loss=0.00019530743884388357, fast_eigenvalue_fraction=0.5, trajectory_val_loss=0.0585535392165184) (from W&B history)
  run=im9rzz5v: DiagnosticMetrics(one_step_mase=0.6544342637062073, loop_closure_loss=2.258838685520459e-05, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.052615389227867126) (from W&B history)
  run=oi336ix7: DiagnosticMetrics(one_step_mase=0.676547646522522, loop_closure_loss=6.510676757898182e-05, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.05004074051976204) (from W&B history)
  run=q1cdbwpc: DiagnosticMetrics(one_step_mase=0.7179235219955444, loop_closure_loss=7.367211219388992e-05, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.05320004001259804) (from W&B history)
  run=qwjfpjfp: DiagnosticMetrics(one_step_mase=0.7008141279220581, loop_closure_loss=4.806132346857339e-05, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.05735868960618973) (from W&B history)
  run=srme5iw0: DiagnosticMetrics(one_step_mase=0.6892557740211487, loop_closure_loss=1.9873723431373946e-05, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.036988265812397) (from W&B history)
  run=y9qw0nzw: DiagnosticMetrics(one_step_mase=1.0245200395584106, loop_closure_loss=0.0003638988418970257, fast_eigenvalue_fraction=0.6428571343421936, trajectory_val_loss=0.0631290078163147) (from W&B history)
  run=zo2lwsax: DiagnosticMetrics(one_step_mase=0.7725304365158081, loop_closure_loss=7.059254858177155e-05, fast_eigenvalue_fraction=0.5454545617103577, trajectory_val_loss=0.05865131691098213) (from W&B history)
  run=0vwtwkff: DiagnosticMetrics(one_step_mase=0.9099114537239075, loop_closure_loss=6.392991508619161e-06, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0941852256655693) (from W&B history)
  run=35s2gm94: DiagnosticMetrics(one_step_mase=0.7041670680046082, loop_closure_loss=3.0898074783181073e-06, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.046216998249292374) (from W&B history)
  run=7m7sojd7: DiagnosticMetrics(one_step_mase=0.7175416946411133, loop_closure_loss=1.0448646207805723e-05, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.059227727353572845) (from W&B history)
  run=9c615cv1: DiagnosticMetrics(one_step_mase=0.7232962250709534, loop_closure_loss=1.8215016552858287e-06, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.09362518042325974) (from W&B history)
  run=ap8tht6d: DiagnosticMetrics(one_step_mase=1.3702729940414429, loop_closure_loss=0.0002320168714504689, fast_eigenvalue_fraction=0.6666666865348816, trajectory_val_loss=0.10429888963699341) (from W&B history)
  run=gfab1lzv: DiagnosticMetrics(one_step_mase=1.3944669961929321, loop_closure_loss=0.00027938265702687204, fast_eigenvalue_fraction=0.6363636255264282, trajectory_val_loss=0.08829818665981293) (from W&B history)
  run=gufk2xiq: DiagnosticMetrics(one_step_mase=0.8772450685501099, loop_closure_loss=3.866219776682556e-05, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.07043144106864929) (from W&B history)
  run=hb9m5cf1: DiagnosticMetrics(one_step_mase=0.6735564470291138, loop_closure_loss=7.493304110539611e-07, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.06640513986349106) (from W&B history)
  run=i19p3en6: DiagnosticMetrics(one_step_mase=1.0156329870224, loop_closure_loss=8.948043250711635e-05, fast_eigenvalue_fraction=0.6428571343421936, trajectory_val_loss=0.06873451173305511) (from W&B history)
  run=q7fvlalq: DiagnosticMetrics(one_step_mase=0.6802676916122437, loop_closure_loss=4.247644028509967e-05, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.051489826291799545) (from W&B history)
  run=vjp0e4eo: DiagnosticMetrics(one_step_mase=0.8129342794418335, loop_closure_loss=6.146420491859317e-05, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0682692676782608) (from W&B history)
  run=yjaxnguc: DiagnosticMetrics(one_step_mase=0.7712153792381287, loop_closure_loss=6.9482398430409376e-06, fast_eigenvalue_fraction=0.27272728085517883, trajectory_val_loss=0.06472831964492798) (from W&B history)

Ranking method:           best_traj_loss
Best run ID:              srme5iw0
Best loop_closure_weight: 1.0
Best tangent_entropy_weight: 0.0
Best kl_dyn_weight:       0.0
Best traj loss:           0.036988
Criteria applied: ['C1', 'C2', 'C3']
Surviving: 14 / 108
Auto-selected run_id: srme5iw0

======================================================================
PARETO FRONTIER RUNS (12 runs)
======================================================================
  Run ID               LC Loss   Traj Val Loss
  ------------  --------------  --------------
  hb9m5cf1            0.000001        0.066405
  35s2gm94            0.000003        0.046217
  srme5iw0            0.000020        0.036988 <-- selected
  fuixohqa            0.004282        0.021729
  35v0e7ov            0.005393        0.021268
  lu9mdd3t            0.006534        0.015310
  a8rjy7kg            0.053524        0.014339
  r838tfeu            0.461846        0.013806
  0enol8sg            0.485869        0.012121
  365xxmpk            0.976839        0.010277
  xpqhs9r5            8.551619        0.010239
  id6d0nan           18.978966        0.010061

======================================================================
RANKING METHOD COMPARISON (over 14 survivors)
======================================================================
  Method                  Run ID               LC Loss   Traj Val Loss
  ----------------------  ------------  --------------  --------------
  best_traj_loss          srme5iw0            0.000020        0.036988 <-- active
  pareto_knee             35s2gm94            0.000003        0.046217
  geo_rank                35s2gm94            0.000003        0.046217
  minimax_rank            35s2gm94            0.000003        0.046217
  geo_log_score           srme5iw0            0.000020        0.036988
  minimax_log_score       35s2gm94            0.000003        0.046217
======================================================================

Loading run srme5iw0 from JacobianODE/Lorenz_INDpartial_NDsweep_cayley_autodim_D1_NormTrue__JacobianODE ...
Loading checkpoint epoch=19-step=4000.ckpt...
Train dataset shape: torch.Size([23562, 45, 85])
Validation dataset shape: torch.Size([7497, 45, 85])
Test dataset shape: torch.Size([3213, 45, 85])
Train trajectories dataset shape: torch.Size([22, 1116, 85])
Validation trajectories dataset shape: torch.Size([7, 1116, 85])
Test trajectories dataset shape: torch.Size([3, 1116, 85])
Loading checkpoint epoch=19-step=4000.ckpt...
Computing reconstruction ...
Computing MASE ...
Teacher-forced MASE: 0.7339
Free-running MASE:   1.3338
Computing latent utilization ...
Entropy-based utilization: 0.833
Null subspace mean RMS: 7.882904e-02
Computing Lyapunov exponents ...
  Computing full-trajectory Lyapunov (3 test trajs, T=1116) ...
Predicted Lyapunov exponents (batch+burn-in, 128 windowed trajs):
  λ_1 = -0.2039 ± 0.0005
  λ_2 = -0.3409 ± 0.0005
  λ_3 = -0.8690 ± 0.0023
  λ_4 = -0.8829 ± 0.0010
  λ_5 = -1.2802 ± 0.0013
  λ_6 = -1.6667 ± 0.0009
  λ_7 = -1.6887 ± 0.0010
  λ_8 = -1.7169 ± 0.0009
  λ_9 = -1.8899 ± 0.0039
  λ_10 = -2.3565 ± 0.0009
  λ_11 = -27.8502 ± 0.0041
  λ_12 = -27.9852 ± 0.0034
  λ_13 = -38.7720 ± 0.0050
  λ_14 = -38.8351 ± 0.0048
Predicted Lyapunov exponents (full-length, 3 test trajs):
  λ_1 = -0.2147 ± 0.0001
  λ_2 = -0.2542 ± 0.0000
  λ_3 = -0.8785 ± 0.0000
  λ_4 = -0.8809 ± 0.0000
  λ_5 = -1.2690 ± 0.0001
  λ_6 = -1.3671 ± 0.0001
  λ_7 = -1.6674 ± 0.0001
  λ_8 = -1.7277 ± 0.0004
  λ_9 = -1.8950 ± 0.0002
  λ_10 = -2.0897 ± 0.0002
  λ_11 = -28.0713 ± 0.0002
  λ_12 = -28.1259 ± 0.0002
  λ_13 = -38.9246 ± 0.0002
  λ_14 = -38.9611 ± 0.0002
Empirical Lyapunov exponents (mean ± std):
  λ_1 = +0.4677 ± 0.0259
  λ_2 = -0.2173 ± 0.0549
  λ_3 = -13.9174 ± 0.0513
Mean KY dim (predicted): 0.000 ± 0.000
Mean KY dim (empirical): 2.018 ± 0.003
Mean KY dim (burn-in):   0.000 ± 0.000
Computing prediction windows ...
Windows: 108 — nMSE min=0.0474, median=0.0973, mean=0.1956, max=2.4416
Computing long-trajectory free-running rollouts ...
Computing encoder/decoder Jacobians ...
encoder_jacobian: (128, 85, 85)
decoder_jacobian: (128, 85, 85)
Computing amplification loss ...
Amplification loss — True state: 0.003446
Amplification loss — Latent:     0.004007
Computing tangent space spectrum ...
```

</details>
