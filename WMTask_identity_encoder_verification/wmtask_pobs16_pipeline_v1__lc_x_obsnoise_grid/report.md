# Sweep Analysis: `wmtask_pobs16_pipeline_v1__lc_x_obsnoise_grid`

**Project**: [WMTask_identity_encoder_verification](https://wandb.ai/JacobianODE/WMTask_identity_encoder_verification/groups/wmtask_pobs16_pipeline_v1__lc_x_obsnoise_grid)  
**Launched**: 2026-05-05T08:25:15Z  
**Completed**: 2026-05-05T20:05:32Z  
**Outcome**: `complete_clean`  
**Git**: `latent-JacobianODE` @ `517adfd`  
**Expected runs**: 63

## Experiment Context

### `wmtask_pobs16_pipeline_v1__lc_x_obsnoise_grid`

**Description**

Pipeline v1 GRID (Sweep 2). Chain follow-up of
`wmtask_pobs16_pipeline_v1__ndelays_scout_lc0`. n_delays pinned to
scout's top-3 by axis_select. sweep_grid covers
loop_closure_weight × obs_noise_scale =
7 × 3 = 21 cells per pinned n_delays → 63 total Stage A cells.
Two-stage cull at 20 epochs (top 50%); Stage B runs to ES or
3hr walltime.

**Hypothesis**

For the n_delays values that perform best at lc=0 (sweep 1),
sweep over loop_closure regularization × observation noise scale
to find the regime that maximizes generalization on the
partial-obs WMTask conditioned task.

**Success criteria**

- All 63 Stage A cells finish without divergence
- two_stage_cull keeps top ~32 by trajectory val_loss
- Stage B publishes report.md with at least one cell beating the scout's lc=0 winner on val traj_loss

## Results

**Swept axes** (9): `data.postprocessing.generalized_variance`, `data.train_test_params.delay_embedding_params.n_delays`, `model.n_target_dims`, `model.n_target_dims_per_block_pca_auto`, `model.n_target_dims_per_block_pca_cum_var`, `model.params.input_dim`, `model.params.output_dim`, `training.lightning.loop_closure_weight`, `training.lightning.obs_noise_scale`

**Chosen run** (by `best_traj_loss`): `3x9dcmu8` — traj_loss=0.00408, MASE=0.5996, R²=0.9958, LC loss=50.665, epoch=34.0

Swept-axis values at chosen run: `data.postprocessing.generalized_variance`=0.0244588 · `data.train_test_params.delay_embedding_params.n_delays`=9 · `model.n_target_dims`=33 · `model.n_target_dims_per_block_pca_auto`=[20, 13] · `model.n_target_dims_per_block_pca_cum_var`=[0.9901722465285276, 0.9905418872477084] · `model.params.input_dim`=33 · `model.params.output_dim`=1089 · `training.lightning.loop_closure_weight`=0 · `training.lightning.obs_noise_scale`=0

**Runs analyzed**: 63 (expected 63)

### Per-run results

| run_idx | run_id | `data.postprocessing.generalized_variance` | `data.train_test_params.delay_embedding_params.n_delays` | `model.n_target_dims` | `model.n_target_dims_per_block_pca_auto` | `model.n_target_dims_per_block_pca_cum_var` | `model.params.input_dim` | `model.params.output_dim` | `training.lightning.loop_closure_weight` | `training.lightning.obs_noise_scale` | best_traj_loss | best_MASE | R² | LC loss | epoch |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | `3x9dcmu8` | 0.0244588 | 9 | 33 | [20, 13] | [0.9901722465285276, 0.9905418872477084] | 33 | 1089 | 0 | 0 | 0.00408 | 0.5996 | 0.9958 | 50.665 | 34.0 |
| 9 | `78ox3tnj` | 0.0244588 | 9 | 33 | [20, 13] | [0.9901722465285276, 0.9905418872477084] | 33 | 1089 | 1.0e-06 | 0 | 0.00408 | 0.5999 | 0.9958 | 28.198 | 34.0 |
| 10 | `a2kmvkzo` | 0.0244588 | 15 | 41 | [25, 16] | [0.9900411020927824, 0.9907630722157732] | 41 | 1681 | 1.0e-06 | 0 | 0.00409 | 0.6003 | 0.9960 | 29.836 | 54.0 |
| 1 | `5jun6tc1` | 0.0244588 | 15 | 41 | [25, 16] | [0.9900411020927828, 0.9907630722157746] | 41 | 1681 | 0 | 0 | 0.00410 | 0.6009 | 0.9960 | 53.568 | 54.0 |
| 27 | `2luc50is` | 0.0244588 | 9 | 33 | [20, 13] | [0.9901722465285276, 0.9905418872477084] | 33 | 1089 | 1.0e-04 | 0 | 0.00410 | 0.6007 | 0.9958 | 1.955 | 40.0 |
| 19 | `uoj4xawo` | 0.0244588 | 15 | 41 | [25, 16] | [0.9900411020927828, 0.9907630722157746] | 41 | 1681 | 1.0e-05 | 0 | 0.00412 | 0.6018 | 0.9960 | 9.243 | 53.0 |
| 11 | `nyxpooea` | 0.0244588 | 6 | 29 | [17, 12] | [0.9902608766168368, 0.9919741165444216] | 29 | 841 | 1.0e-06 | 0 | 0.00412 | 0.6036 | 0.9958 | 27.630 | 37.0 |
| 2 | `48tr0xgh` | 0.0244588 | 6 | 29 | [17, 12] | [0.9902608766168368, 0.9919741165444216] | 29 | 841 | 0 | 0 | 0.00413 | 0.6037 | 0.9958 | 48.837 | 37.0 |
| 20 | `ma5q364f` | 0.0244588 | 6 | 29 | [17, 12] | [0.9902608766168368, 0.9919741165444216] | 29 | 841 | 1.0e-05 | 0 | 0.00414 | 0.6047 | 0.9958 | 9.081 | 37.0 |
| 18 | `2zu9r1v1` | 0.0244588 | 9 | 33 | [20, 13] | [0.9901722465285276, 0.9905418872477084] | 33 | 1089 | 1.0e-05 | 0 | 0.00419 | 0.6068 | 0.9957 | 8.745 | 30.0 |
| 29 | `ccpgm7cl` | 0.0244588 | 6 | 29 | [17, 12] | [0.9902608766168368, 0.9919741165444216] | 29 | 841 | 1.0e-04 | 0 | 0.00422 | 0.6100 | 0.9957 | 1.975 | 40.0 |
| 8 | `miyfq4ru` | 0.0244588 | 6 | 29 | [17, 12] | [0.9902608766168368, 0.9919741165444216] | 29 | 841 | 0 | 0.05 | 0.00424 | 0.6114 | 0.9957 | 53.168 | 38.0 |
| 17 | `ctblk4fv` | 0.0244588 | 6 | 29 | [17, 12] | [0.9902608766168368, 0.9919741165444216] | 29 | 841 | 1.0e-06 | 0.05 | 0.00425 | 0.6115 | 0.9957 | 34.647 | 38.0 |
| 26 | `cdkmy8xt` | 0.0244588 | 6 | 29 | [17, 12] | [0.9902608766168364, 0.9919741165444236] | 29 | 841 | 1.0e-05 | 0.05 | 0.00426 | 0.6125 | 0.9956 | 12.945 | 38.0 |
| 24 | `qv74v8v1` | 0.0244588 | 9 | 33 | [20, 13] | [0.9901722465285276, 0.9905418872477084] | 33 | 1089 | 1.0e-05 | 0.05 | 0.00429 | 0.6141 | 0.9956 | 16.814 | 42.0 |
| 15 | `w0xmpllx` | 0.0244588 | 9 | 33 | [20, 13] | [0.9901722465285276, 0.9905418872477084] | 33 | 1089 | 1.0e-06 | 0.05 | 0.00430 | 0.6146 | 0.9956 | 44.391 | 42.0 |
| 6 | `primfzzm` | 0.0244588 | 9 | 33 | [20, 13] | [0.9901722465285276, 0.9905418872477084] | 33 | 1089 | 0 | 0.05 | 0.00431 | 0.6150 | 0.9956 | 67.212 | 42.0 |
| 35 | `qpzk8q77` | 0.0244588 | 6 | 29 | [17, 12] | [0.9902608766168368, 0.9919741165444216] | 29 | 841 | 1.0e-04 | 0.05 | 0.00438 | 0.6203 | 0.9955 | 3.077 | 38.0 |
| 23 | `d5qrp7h9` | 0.0244588 | 6 | 29 | [17, 12] | [0.9902608766168368, 0.9919741165444216] | 29 | 841 | 1.0e-05 | 0.01 | 0.00438 | 0.6209 | 0.9955 | 12.042 | 38.0 |
| 28 | `iaj54q33` | 0.0244588 | 15 | 41 | [25, 16] | [0.9900411020927828, 0.9907630722157746] | 41 | 1681 | 1.0e-04 | 0 | 0.00441 | 0.6210 | 0.9957 | 1.815 | 44.0 |
| 5 | `udmt3lkf` | 0.0244588 | 6 | 29 | [17, 12] | [0.9902608766168364, 0.9919741165444236] | 29 | 841 | 0 | 0.01 | 0.00447 | 0.6269 | 0.9954 | 51.631 | 31.0 |
| 14 | `i542tqq9` | 0.0244588 | 6 | 29 | [17, 12] | [0.9902608766168368, 0.9919741165444216] | 29 | 841 | 1.0e-06 | 0.01 | 0.00447 | 0.6271 | 0.9954 | 32.722 | 31.0 |
| 32 | `taxfrzvi` | 0.0244588 | 6 | 29 | [17, 12] | [0.9902608766168368, 0.9919741165444216] | 29 | 841 | 1.0e-04 | 0.01 | 0.00450 | 0.6289 | 0.9954 | 2.892 | 37.0 |
| 12 | `awpb0yfy` | 0.0244588 | 9 | 33 | [20, 13] | [0.9901722465285276, 0.9905418872477084] | 33 | 1089 | 1.0e-06 | 0.01 | 0.00451 | 0.6295 | 0.9954 | 41.673 | 37.0 |
| 3 | `8c39il95` | 0.0244588 | 9 | 33 | [20, 13] | [0.9901722465285276, 0.9905418872477084] | 33 | 1089 | 0 | 0.01 | 0.00452 | 0.6297 | 0.9954 | 63.390 | 37.0 |
| 33 | `cbe7z6js` | 0.0244588 | 9 | 33 | [20, 13] | [0.9901722465285276, 0.9905418872477084] | 33 | 1089 | 1.0e-04 | 0.05 | 0.00452 | 0.6284 | 0.9954 | 3.784 | 36.0 |
| 21 | `fh7hqm2q` | 0.0244588 | 9 | 33 | [20, 13] | [0.9901722465285276, 0.9905418872477084] | 33 | 1089 | 1.0e-05 | 0.01 | 0.00460 | 0.6350 | 0.9953 | 14.638 | 33.0 |
| 30 | `y7n4fqoc` | 0.0244588 | 9 | 33 | [20, 13] | [0.9901722465285276, 0.9905418872477084] | 33 | 1089 | 1.0e-04 | 0.01 | 0.00461 | 0.6358 | 0.9953 | 3.705 | 38.0 |
| 36 | `1yhoqwg5` | 0.0244588 | 9 | 33 | [20, 13] | [0.9901722465285276, 0.9905418872477084] | 33 | 1089 | 0.001 | 0 | 0.00466 | 0.6368 | 0.9952 | 0.361 | 39.0 |
| 38 | `1184hm1z` | 0.0244588 | 6 | 29 | [17, 12] | [0.9902608766168368, 0.9919741165444216] | 29 | 841 | 0.001 | 0 | 0.00474 | 0.6425 | 0.9952 | 0.384 | 41.0 |
| 16 | `uxm7pkl1` | 0.0244588 | 15 | 41 | [25, 16] | [0.9900411020927828, 0.9907630722157746] | 41 | 1681 | 1.0e-06 | 0.05 | 0.00508 | 0.6631 | 0.9950 | 76.025 | 52.0 |
| 25 | `kybx7ydc` | 0.0244588 | 15 | 41 | [25, 16] | [0.9900411020927828, 0.9907630722157746] | 41 | 1681 | 1.0e-05 | 0.05 | 0.00509 | 0.6643 | 0.9950 | 28.726 | 49.0 |
| 37 | `wb5ogm10` | 0.0244588 | 15 | 41 | [25, 16] | [0.9900411020927824, 0.9907630722157732] | 41 | 1681 | 0.001 | 0 | 0.00509 | 0.6621 | 0.9950 | 0.316 | 42.0 |
| 44 | `yr9k1c12` | 0.0244588 | 6 | 29 | [17, 12] | [0.9902608766168368, 0.9919741165444216] | 29 | 841 | 0.001 | 0.05 | 0.00528 | 0.6749 | 0.9946 | 0.875 | 37.0 |
| 41 | `wp4net0i` | 0.0244588 | 6 | 29 | [17, 12] | [0.9902608766168368, 0.9919741165444216] | 29 | 841 | 0.001 | 0.01 | 0.00534 | 0.6793 | 0.9945 | 0.921 | 42.0 |
| 22 | `xu1eixb9` | 0.0244588 | 15 | 41 | [25, 16] | [0.9900411020927828, 0.9907630722157746] | 41 | 1681 | 1.0e-05 | 0.01 | 0.00544 | 0.6865 | 0.9947 | 25.918 | 46.0 |
| 7 | `rn8mv1jm` | 0.0244588 | 15 | 41 | [25, 16] | [0.9900411020927828, 0.9907630722157746] | 41 | 1681 | 0 | 0.05 | 0.00573 | 0.7018 | 0.9944 | 109.006 | 48.0 |
| 13 | `d4cwj81g` | 0.0244588 | 15 | 41 | [25, 16] | [0.9900411020927828, 0.9907630722157746] | 41 | 1681 | 1.0e-06 | 0.01 | 0.00610 | 0.7229 | 0.9941 | 116.670 | 49.0 |
| 46 | `fybsg3o5` | 0.0244588 | 15 | 41 | [25, 16] | [0.9900411020927828, 0.9907630722157746] | 41 | 1681 | 0.01 | 0 | 0.00630 | 0.7285 | 0.9939 | 0.040 | 51.0 |
| 45 | `9v8mih73` | 0.0244588 | 9 | 33 | [20, 13] | [0.9901722465285276, 0.9905418872477084] | 33 | 1089 | 0.01 | 0 | 0.00636 | 0.7307 | 0.9935 | 0.052 | 43.0 |
| 47 | `pjhquqis` | 0.0244588 | 6 | 29 | [17, 12] | [0.9902608766168368, 0.9919741165444216] | 29 | 841 | 0.01 | 0 | 0.00665 | 0.7463 | 0.9932 | 0.060 | 41.0 |
| 34 | `b1li01z7` | 0.0244588 | 15 | 41 | [25, 16] | [0.9900411020927828, 0.9907630722157746] | 41 | 1681 | 1.0e-04 | 0.05 | 0.00665 | 0.7496 | 0.9935 | 21.511 | 45.0 |
| 4 | `1sucuj93` | 0.0244588 | 15 | 41 | [25, 16] | [0.9900411020927828, 0.9907630722157746] | 41 | 1681 | 0 | 0.01 | 0.00671 | 0.7544 | 0.9935 | 154.249 | 42.0 |
| 31 | `6xgmlvt1` | 0.0244588 | 15 | 41 | [25, 16] | [0.9900411020927828, 0.9907630722157746] | 41 | 1681 | 1.0e-04 | 0.01 | 0.00688 | 0.7638 | 0.9933 | 21.564 | 48.0 |
| 55 | `mxcblnbv` | 0.0244588 | 15 | 41 | [25, 16] | [0.9900411020927828, 0.9907630722157746] | 41 | 1681 | 0.1 | 0 | 0.00798 | 0.8128 | 0.9922 | 0.002 | 52.0 |
| 54 | `5296bl4t` | 0.0244588 | 9 | 33 | [20, 13] | [0.9901722465285276, 0.9905418872477084] | 33 | 1089 | 0.1 | 0 | 0.00928 | 0.8658 | 0.9905 | 0.003 | 38.0 |
| 56 | `56suu9xy` | 0.0244588 | 6 | 29 | [17, 12] | [0.9902608766168368, 0.9919741165444216] | 29 | 841 | 0.1 | 0 | 0.00954 | 0.8788 | 0.9902 | 0.004 | 43.0 |
| 43 | `cjd6bfqm` | 0.0244588 | 15 | 41 | [25, 16] | [0.9900411020927824, 0.9907630722157732] | 41 | 1681 | 0.001 | 0.05 | 0.01094 | 0.9532 | 0.9893 | 6.993 | 61.0 |
| 40 | `0n5tf14x` | 0.0244588 | 15 | 41 | [25, 16] | [0.9900411020927828, 0.9907630722157746] | 41 | 1681 | 0.001 | 0.01 | 0.01126 | 0.9630 | 0.9890 | 4.169 | 50.0 |
| 61 | `l119bzlt` | 0.0244588 | 15 | 41 | [25, 16] | [0.9900411020927828, 0.9907630722157746] | 41 | 1681 | 0.1 | 0.05 | 0.01509 | 1.1044 | 0.9853 | 0.018 | 50.0 |
| 58 | `y1hvo5lg` | 0.0244588 | 15 | 41 | [25, 16] | [0.9900411020927828, 0.9907630722157746] | 41 | 1681 | 0.1 | 0.01 | 0.01527 | 1.1110 | 0.9851 | 0.019 | 49.0 |
| 60 | `mjfkpubb` | 0.0244588 | 9 | 33 | [20, 13] | [0.9901722465285276, 0.9905418872477084] | 33 | 1089 | 0.1 | 0.05 | 0.01699 | 1.1607 | 0.9826 | 0.024 | 38.0 |
| 52 | `hpi3ejsz` | 0.0244588 | 15 | 41 | [25, 16] | [0.9900411020927828, 0.9907630722157746] | 41 | 1681 | 0.01 | 0.05 | 0.02072 | 1.2822 | 0.9798 | 0.331 | 49.0 |
| 57 | `17rm3ro7` | 0.0244588 | 9 | 33 | [20, 13] | [0.9901722465285276, 0.9905418872477084] | 33 | 1089 | 0.1 | 0.01 | 0.02095 | 1.2833 | 0.9785 | 0.038 | 39.0 |
| 39 | `nw6kehrs` | 0.0244588 | 9 | 33 | [20, 13] | [0.9901722465285276, 0.9905418872477084] | 33 | 1089 | 0.001 | 0.01 | 0.03027 | 1.5042 | 0.9689 | 17.638 | 33.0 |
| 49 | `i13ej08e` | 0.0244588 | 15 | 41 | [25, 16] | [0.9900411020927828, 0.9907630722157746] | 41 | 1681 | 0.01 | 0.01 | 0.03791 | 1.6657 | 0.9632 | 0.147 | 24.0 |
| 42 | `v5oijoaq` | 0.0244588 | 9 | 33 | [20, 13] | [0.9901722465285276, 0.9905418872477084] | 33 | 1089 | 0.001 | 0.05 | 0.03952 | 1.6101 | 0.9595 | 1.434 | 3.0 |
| 62 | `jvwajp4f` | 0.0244588 | 6 | 29 | [17, 12] | [0.9902608766168368, 0.9919741165444216] | 29 | 841 | 0.1 | 0.05 | 0.04987 | 1.8511 | 0.9491 | 0.028 | 17.0 |
| 59 | `qh49bl8i` | 0.0244588 | 6 | 29 | [17, 12] | [0.9902608766168368, 0.9919741165444216] | 29 | 841 | 0.1 | 0.01 | 0.05178 | 1.8825 | 0.9472 | 0.026 | 16.0 |
| 50 | `l1bvf1hu` | 0.0244588 | 6 | 29 | [17, 12] | [0.9902608766168368, 0.9919741165444216] | 29 | 841 | 0.01 | 0.01 | 0.07281 | 2.2606 | 0.9257 | 3.235 | 39.0 |
| 53 | `139dwoa8` | 0.0244588 | 6 | 29 | [17, 12] | [0.9902608766168368, 0.9919741165444216] | 29 | 841 | 0.01 | 0.05 | 0.09812 | 2.3957 | 0.8997 | 0.146 | 3.0 |
| 48 | `9awygdxx` | 0.0244588 | 9 | 33 | [20, 13] | [0.9901722465285298, 0.9905418872477102] | 33 | 1089 | 0.01 | 0.01 | 0.14832 | 2.9600 | 0.8485 | 0.118 | 1.0 |
| 51 | `m0zb3cdy` | 0.0244588 | 9 | 33 | [20, 13] | [0.9901722465285298, 0.9905418872477102] | 33 | 1089 | 0.01 | 0.05 | 0.14856 | 2.9597 | 0.8482 | 0.157 | 1.0 |

### Best run per `obs_noise_scale`

| obs_noise_scale | Best LC weight | Best traj loss | MASE at best | R² | LC loss | epoch |
|---|---|---|---|---|---|---|
| 0.0 | 0.0e+00 | 0.00408 | 0.5996 | 0.9958 | 50.665 | 34.0 |
| 0.01 | 1.0e-05 | 0.00438 | 0.6209 | 0.9955 | 12.042 | 38.0 |
| 0.05 | 0.0e+00 | 0.00424 | 0.6114 | 0.9957 | 53.168 | 38.0 |

## Success-criteria verdicts (automated)

| Criterion | Verdict | Note |
|---|---|---|
| All 63 Stage A cells finish without divergence | **Unknown** |  |
| two_stage_cull keeps top ~32 by trajectory val_loss | **Unknown** |  |
| Stage B publishes report.md with at least one cell beating the scout's lc=0 winner on val traj_loss | **Unknown** |  |

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

### lyapunov_top10

![lyapunov_top10](figures/lyapunov_top10.png)

### kaplan_yorke

![kaplan_yorke](figures/kaplan_yorke.png)

### amplification

![amplification](figures/amplification.png)

### kaplan_yorke_pca

![kaplan_yorke_pca](figures/kaplan_yorke_pca.png)

### prediction_detail_latent

![prediction_detail_latent](figures/prediction_detail_latent.png)

### prediction_detail_obs

![prediction_detail_obs](figures/prediction_detail_obs.png)

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
No run_id provided — selecting best run from group 'wmtask_pobs16_pipeline_v1__lc_x_obsnoise_grid' ...
Found 63 total runs in JacobianODE/WMTask_identity_encoder_verification (group=wmtask_pobs16_pipeline_v1__lc_x_obsnoise_grid)
All runs (state, loop_closure_weight, tangent_entropy_weight, kl_dyn_weight):
  primfzzm: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  3x9dcmu8: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  w0xmpllx: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  awpb0yfy: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  qv74v8v1: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  2zu9r1v1: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  78ox3tnj: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  fh7hqm2q: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  y7n4fqoc: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  cbe7z6js: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  2luc50is: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  8c39il95: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  nw6kehrs: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  1yhoqwg5: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  9v8mih73: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  v5oijoaq: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  9awygdxx: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  m0zb3cdy: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  5296bl4t: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  17rm3ro7: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  mjfkpubb: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  5jun6tc1: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  1sucuj93: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  rn8mv1jm: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  a2kmvkzo: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  d4cwj81g: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  xu1eixb9: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  uoj4xawo: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  uxm7pkl1: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  kybx7ydc: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  b1li01z7: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  iaj54q33: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  6xgmlvt1: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  wb5ogm10: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  0n5tf14x: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  cjd6bfqm: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  fybsg3o5: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  i13ej08e: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  hpi3ejsz: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  mxcblnbv: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  y1hvo5lg: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  l119bzlt: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  48tr0xgh: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  udmt3lkf: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  miyfq4ru: state=finished, lc=0.0, te=0.0, kl_dyn=0.0
  nyxpooea: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  ma5q364f: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  i542tqq9: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  ctblk4fv: state=finished, lc=1e-06, te=0.0, kl_dyn=0.0
  d5qrp7h9: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  cdkmy8xt: state=finished, lc=1e-05, te=0.0, kl_dyn=0.0
  ccpgm7cl: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  taxfrzvi: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  qpzk8q77: state=finished, lc=0.0001, te=0.0, kl_dyn=0.0
  1184hm1z: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  wp4net0i: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  yr9k1c12: state=finished, lc=0.001, te=0.0, kl_dyn=0.0
  pjhquqis: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  l1bvf1hu: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  139dwoa8: state=finished, lc=0.01, te=0.0, kl_dyn=0.0
  qh49bl8i: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  56suu9xy: state=finished, lc=0.1, te=0.0, kl_dyn=0.0
  jvwajp4f: state=finished, lc=0.1, te=0.0, kl_dyn=0.0

slurm_timeout_min not found in any run config — falling back to 180 min
  Including primfzzm (lc=0.0): use_all_runs=True (state=finished)
  Including 3x9dcmu8 (lc=0.0): use_all_runs=True (state=finished)
  Including w0xmpllx (lc=1e-06): use_all_runs=True (state=finished)
  Including awpb0yfy (lc=1e-06): use_all_runs=True (state=finished)
  Including qv74v8v1 (lc=1e-05): use_all_runs=True (state=finished)
  Including 2zu9r1v1 (lc=1e-05): use_all_runs=True (state=finished)
  Including 78ox3tnj (lc=1e-06): use_all_runs=True (state=finished)
  Including fh7hqm2q (lc=1e-05): use_all_runs=True (state=finished)
  Including y7n4fqoc (lc=0.0001): use_all_runs=True (state=finished)
  Including cbe7z6js (lc=0.0001): use_all_runs=True (state=finished)
  Including 2luc50is (lc=0.0001): use_all_runs=True (state=finished)
  Including 8c39il95 (lc=0.0): use_all_runs=True (state=finished)
  Including nw6kehrs (lc=0.001): use_all_runs=True (state=finished)
  Including 1yhoqwg5 (lc=0.001): use_all_runs=True (state=finished)
  Including 9v8mih73 (lc=0.01): use_all_runs=True (state=finished)
  Including v5oijoaq (lc=0.001): use_all_runs=True (state=finished)
  Including 9awygdxx (lc=0.01): use_all_runs=True (state=finished)
  Including m0zb3cdy (lc=0.01): use_all_runs=True (state=finished)
  Including 5296bl4t (lc=0.1): use_all_runs=True (state=finished)
  Including 17rm3ro7 (lc=0.1): use_all_runs=True (state=finished)
  Including mjfkpubb (lc=0.1): use_all_runs=True (state=finished)
  Including 5jun6tc1 (lc=0.0): use_all_runs=True (state=finished)
  Including 1sucuj93 (lc=0.0): use_all_runs=True (state=finished)
  Including rn8mv1jm (lc=0.0): use_all_runs=True (state=finished)
  Including a2kmvkzo (lc=1e-06): use_all_runs=True (state=finished)
  Including d4cwj81g (lc=1e-06): use_all_runs=True (state=finished)
  Including xu1eixb9 (lc=1e-05): use_all_runs=True (state=finished)
  Including uoj4xawo (lc=1e-05): use_all_runs=True (state=finished)
  Including uxm7pkl1 (lc=1e-06): use_all_runs=True (state=finished)
  Including kybx7ydc (lc=1e-05): use_all_runs=True (state=finished)
  Including b1li01z7 (lc=0.0001): use_all_runs=True (state=finished)
  Including iaj54q33 (lc=0.0001): use_all_runs=True (state=finished)
  Including 6xgmlvt1 (lc=0.0001): use_all_runs=True (state=finished)
  Including wb5ogm10 (lc=0.001): use_all_runs=True (state=finished)
  Including 0n5tf14x (lc=0.001): use_all_runs=True (state=finished)
  Including cjd6bfqm (lc=0.001): use_all_runs=True (state=finished)
  Including fybsg3o5 (lc=0.01): use_all_runs=True (state=finished)
  Including i13ej08e (lc=0.01): use_all_runs=True (state=finished)
  Including hpi3ejsz (lc=0.01): use_all_runs=True (state=finished)
  Including mxcblnbv (lc=0.1): use_all_runs=True (state=finished)
  Including y1hvo5lg (lc=0.1): use_all_runs=True (state=finished)
  Including l119bzlt (lc=0.1): use_all_runs=True (state=finished)
  Including 48tr0xgh (lc=0.0): use_all_runs=True (state=finished)
  Including udmt3lkf (lc=0.0): use_all_runs=True (state=finished)
  Including miyfq4ru (lc=0.0): use_all_runs=True (state=finished)
  Including nyxpooea (lc=1e-06): use_all_runs=True (state=finished)
  Including ma5q364f (lc=1e-05): use_all_runs=True (state=finished)
  Including i542tqq9 (lc=1e-06): use_all_runs=True (state=finished)
  Including ctblk4fv (lc=1e-06): use_all_runs=True (state=finished)
  Including d5qrp7h9 (lc=1e-05): use_all_runs=True (state=finished)
  Including cdkmy8xt (lc=1e-05): use_all_runs=True (state=finished)
  Including ccpgm7cl (lc=0.0001): use_all_runs=True (state=finished)
  Including taxfrzvi (lc=0.0001): use_all_runs=True (state=finished)
  Including qpzk8q77 (lc=0.0001): use_all_runs=True (state=finished)
  Including 1184hm1z (lc=0.001): use_all_runs=True (state=finished)
  Including wp4net0i (lc=0.001): use_all_runs=True (state=finished)
  Including yr9k1c12 (lc=0.001): use_all_runs=True (state=finished)
  Including pjhquqis (lc=0.01): use_all_runs=True (state=finished)
  Including l1bvf1hu (lc=0.01): use_all_runs=True (state=finished)
  Including 139dwoa8 (lc=0.01): use_all_runs=True (state=finished)
  Including qh49bl8i (lc=0.1): use_all_runs=True (state=finished)
  Including 56suu9xy (lc=0.1): use_all_runs=True (state=finished)
  Including jvwajp4f (lc=0.1): use_all_runs=True (state=finished)
Found 63 effectively-done sweep runs:
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=1sucuj93
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=3x9dcmu8
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=48tr0xgh
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=5jun6tc1
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=8c39il95
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=miyfq4ru
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=primfzzm
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=rn8mv1jm
  loop_closure_weight=0.0, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=udmt3lkf
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=78ox3tnj
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=a2kmvkzo
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=awpb0yfy
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=ctblk4fv
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=d4cwj81g
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=i542tqq9
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=nyxpooea
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=uxm7pkl1
  loop_closure_weight=1e-06, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=w0xmpllx
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=2zu9r1v1
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=cdkmy8xt
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=d5qrp7h9
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=fh7hqm2q
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=kybx7ydc
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=ma5q364f
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=qv74v8v1
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=uoj4xawo
  loop_closure_weight=1e-05, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=xu1eixb9
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=2luc50is
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=6xgmlvt1
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=b1li01z7
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=cbe7z6js
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=ccpgm7cl
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=iaj54q33
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=qpzk8q77
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=taxfrzvi
  loop_closure_weight=0.0001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=y7n4fqoc
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=0n5tf14x
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=1184hm1z
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=1yhoqwg5
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=cjd6bfqm
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=nw6kehrs
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=v5oijoaq
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=wb5ogm10
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=wp4net0i
  loop_closure_weight=0.001, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=yr9k1c12
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=139dwoa8
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=9awygdxx
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=9v8mih73
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=fybsg3o5
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=hpi3ejsz
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=i13ej08e
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=l1bvf1hu
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=m0zb3cdy
  loop_closure_weight=0.01, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=pjhquqis
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=17rm3ro7
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=5296bl4t
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=56suu9xy
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=jvwajp4f
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=l119bzlt
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=mjfkpubb
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=mxcblnbv
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=qh49bl8i
  loop_closure_weight=0.1, tangent_entropy_weight=0.0, kl_dyn_weight=0.0 -> run_id=y1hvo5lg
loaded wmtask RNN model checkpoint 1
Loading cached wmtask hiddens from /orcd/data/ekmiller/001/eisenaj/ControlJacobians/WMTaskModels/WMSelectionTask__cue_time_0.1__response_time_0.25__enforce_fixation_False/BiologicalRNN__cue_time_0.1__learning_rate_0.0005__max_epochs_42__N1_64__N2_64__tau_0.05__dt_0.02__eig_lower_bound_0.1__init_mode_random/_jacobianode_cache/hiddens__all__epoch1__trials4096__seed42.pt
loaded wmtask RNN model checkpoint 41
Loading cached wmtask hiddens from /orcd/data/ekmiller/001/eisenaj/ControlJacobians/WMTaskModels/WMSelectionTask__cue_time_0.1__response_time_0.25__enforce_fixation_False/BiologicalRNN__cue_time_0.1__learning_rate_0.0005__max_epochs_42__N1_64__N2_64__tau_0.05__dt_0.02__eig_lower_bound_0.1__init_mode_random/_jacobianode_cache/hiddens__all__epoch41__trials4096__seed42.pt
n_dims=480, n_latent=480, n_dyn=41, dt=0.0200
  run=1sucuj93: DiagnosticMetrics(one_step_mase=0.6941834688186646, loop_closure_loss=154.24884033203125, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.006713333074003458) (from W&B history)
  run=3x9dcmu8: DiagnosticMetrics(one_step_mase=0.5367434024810791, loop_closure_loss=50.664642333984375, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004079318139702082) (from W&B history)
  run=48tr0xgh: DiagnosticMetrics(one_step_mase=0.5083298683166504, loop_closure_loss=48.83686065673828, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004125876352190971) (from W&B history)
  run=5jun6tc1: DiagnosticMetrics(one_step_mase=0.5831769108772278, loop_closure_loss=53.567665100097656, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004101421218365431) (from W&B history)
  run=8c39il95: DiagnosticMetrics(one_step_mase=0.5601020455360413, loop_closure_loss=63.39046859741211, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004516379442065954) (from W&B history)
  run=miyfq4ru: DiagnosticMetrics(one_step_mase=0.5203635692596436, loop_closure_loss=53.167938232421875, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004243391565978527) (from W&B history)
  run=primfzzm: DiagnosticMetrics(one_step_mase=0.5579258799552917, loop_closure_loss=67.21179962158203, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004307842347770929) (from W&B history)
  run=rn8mv1jm: DiagnosticMetrics(one_step_mase=0.6736084222793579, loop_closure_loss=109.00586700439453, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0057327705435454845) (from W&B history)
  run=udmt3lkf: DiagnosticMetrics(one_step_mase=0.522745668888092, loop_closure_loss=51.63094711303711, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004468110855668783) (from W&B history)
  run=78ox3tnj: DiagnosticMetrics(one_step_mase=0.5360577702522278, loop_closure_loss=28.198488235473633, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0040834988467395306) (from W&B history)
  run=a2kmvkzo: DiagnosticMetrics(one_step_mase=0.5822727680206299, loop_closure_loss=29.836322784423828, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004090072121471167) (from W&B history)
  run=awpb0yfy: DiagnosticMetrics(one_step_mase=0.5597743391990662, loop_closure_loss=41.673030853271484, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.00451275147497654) (from W&B history)
  run=ctblk4fv: DiagnosticMetrics(one_step_mase=0.5201564431190491, loop_closure_loss=34.64728546142578, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004246561322361231) (from W&B history)
  run=d4cwj81g: DiagnosticMetrics(one_step_mase=0.6856158971786499, loop_closure_loss=116.66996002197266, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.00610191049054265) (from W&B history)
  run=i542tqq9: DiagnosticMetrics(one_step_mase=0.5225525498390198, loop_closure_loss=32.721893310546875, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004472589120268822) (from W&B history)
  run=nyxpooea: DiagnosticMetrics(one_step_mase=0.5078095197677612, loop_closure_loss=27.629789352416992, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0041243527084589005) (from W&B history)
  run=uxm7pkl1: DiagnosticMetrics(one_step_mase=0.6394193172454834, loop_closure_loss=76.02507781982422, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005079252179712057) (from W&B history)
  run=w0xmpllx: DiagnosticMetrics(one_step_mase=0.5575961470603943, loop_closure_loss=44.39095687866211, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004301200620830059) (from W&B history)
  run=2zu9r1v1: DiagnosticMetrics(one_step_mase=0.538108766078949, loop_closure_loss=8.7445707321167, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004192638676613569) (from W&B history)
  run=cdkmy8xt: DiagnosticMetrics(one_step_mase=0.5198391079902649, loop_closure_loss=12.944990158081055, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004261708352714777) (from W&B history)
  run=d5qrp7h9: DiagnosticMetrics(one_step_mase=0.5203438997268677, loop_closure_loss=12.042349815368652, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004380335565656424) (from W&B history)
  run=fh7hqm2q: DiagnosticMetrics(one_step_mase=0.5601062178611755, loop_closure_loss=14.638494491577148, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004595106467604637) (from W&B history)
  run=kybx7ydc: DiagnosticMetrics(one_step_mase=0.645158588886261, loop_closure_loss=28.726285934448242, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005085864569991827) (from W&B history)
  run=ma5q364f: DiagnosticMetrics(one_step_mase=0.5069876313209534, loop_closure_loss=9.081457138061523, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004140170756727457) (from W&B history)
  run=qv74v8v1: DiagnosticMetrics(one_step_mase=0.5569907426834106, loop_closure_loss=16.813858032226562, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004291460383683443) (from W&B history)
  run=uoj4xawo: DiagnosticMetrics(one_step_mase=0.5811585187911987, loop_closure_loss=9.242551803588867, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004115044139325619) (from W&B history)
  run=xu1eixb9: DiagnosticMetrics(one_step_mase=0.6455537676811218, loop_closure_loss=25.918073654174805, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005441032815724611) (from W&B history)
  run=2luc50is: DiagnosticMetrics(one_step_mase=0.5336809158325195, loop_closure_loss=1.955323338508606, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004102251958101988) (from W&B history)
  run=6xgmlvt1: DiagnosticMetrics(one_step_mase=0.7317610383033752, loop_closure_loss=21.563894271850586, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.006878067273646593) (from W&B history)
  run=b1li01z7: DiagnosticMetrics(one_step_mase=0.7359299063682556, loop_closure_loss=21.511367797851562, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.006653040647506714) (from W&B history)
  run=cbe7z6js: DiagnosticMetrics(one_step_mase=0.5628478527069092, loop_closure_loss=3.783820152282715, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0045188129879534245) (from W&B history)
  run=ccpgm7cl: DiagnosticMetrics(one_step_mase=0.5066338777542114, loop_closure_loss=1.9749888181686401, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0042202165350317955) (from W&B history)
  run=iaj54q33: DiagnosticMetrics(one_step_mase=0.5880956649780273, loop_closure_loss=1.8148797750473022, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004410257562994957) (from W&B history)
  run=qpzk8q77: DiagnosticMetrics(one_step_mase=0.5224902629852295, loop_closure_loss=3.076871633529663, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004379637539386749) (from W&B history)
  run=taxfrzvi: DiagnosticMetrics(one_step_mase=0.523553192615509, loop_closure_loss=2.891845464706421, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0045012133195996284) (from W&B history)
  run=y7n4fqoc: DiagnosticMetrics(one_step_mase=0.5633376240730286, loop_closure_loss=3.705101251602173, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004614169709384441) (from W&B history)
  run=0n5tf14x: DiagnosticMetrics(one_step_mase=0.893413245677948, loop_closure_loss=4.169408798217773, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.011257043108344078) (from W&B history)
  run=1184hm1z: DiagnosticMetrics(one_step_mase=0.5129426717758179, loop_closure_loss=0.3842847943305969, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.00473680067807436) (from W&B history)
  run=1yhoqwg5: DiagnosticMetrics(one_step_mase=0.5432249903678894, loop_closure_loss=0.3609226644039154, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.004662897437810898) (from W&B history)
  run=cjd6bfqm: DiagnosticMetrics(one_step_mase=0.9097126126289368, loop_closure_loss=6.992959499359131, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.010943945497274399) (from W&B history)
  run=nw6kehrs: DiagnosticMetrics(one_step_mase=1.2501658201217651, loop_closure_loss=17.638212203979492, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.03026544116437435) (from W&B history)
  run=v5oijoaq: DiagnosticMetrics(one_step_mase=0.9429979920387268, loop_closure_loss=1.4339979887008667, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.03951830789446831) (from W&B history)
  run=wb5ogm10: DiagnosticMetrics(one_step_mase=0.5989158749580383, loop_closure_loss=0.31609421968460083, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005087880417704582) (from W&B history)
  run=wp4net0i: DiagnosticMetrics(one_step_mase=0.5527893304824829, loop_closure_loss=0.9212894439697266, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.0053449212573468685) (from W&B history)
  run=yr9k1c12: DiagnosticMetrics(one_step_mase=0.5499759912490845, loop_closure_loss=0.8748000860214233, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.005279938690364361) (from W&B history)
  run=139dwoa8: DiagnosticMetrics(one_step_mase=1.0350096225738525, loop_closure_loss=0.14634671807289124, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.09812439233064651) (from W&B history)
  run=9awygdxx: DiagnosticMetrics(one_step_mase=1.5777404308319092, loop_closure_loss=0.11762604117393494, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.14831599593162537) (from W&B history)
  run=9v8mih73: DiagnosticMetrics(one_step_mase=0.5731594562530518, loop_closure_loss=0.05244855582714081, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.006357054226100445) (from W&B history)
  run=fybsg3o5: DiagnosticMetrics(one_step_mase=0.6231552362442017, loop_closure_loss=0.040003661066293716, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.006295631639659405) (from W&B history)
  run=hpi3ejsz: DiagnosticMetrics(one_step_mase=1.378170371055603, loop_closure_loss=0.3312283456325531, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.020723305642604828) (from W&B history)
  run=i13ej08e: DiagnosticMetrics(one_step_mase=1.4314548969268799, loop_closure_loss=0.1468421220779419, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.03790925815701485) (from W&B history)
  run=l1bvf1hu: DiagnosticMetrics(one_step_mase=1.5653762817382812, loop_closure_loss=3.2347702980041504, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.07281463593244553) (from W&B history)
  run=m0zb3cdy: DiagnosticMetrics(one_step_mase=1.5764957666397095, loop_closure_loss=0.15653586387634277, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.1485595554113388) (from W&B history)
  run=pjhquqis: DiagnosticMetrics(one_step_mase=0.5420131683349609, loop_closure_loss=0.05977187305688858, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.006647801026701927) (from W&B history)
  run=17rm3ro7: DiagnosticMetrics(one_step_mase=1.1165175437927246, loop_closure_loss=0.03787314519286156, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.020945563912391663) (from W&B history)
  run=5296bl4t: DiagnosticMetrics(one_step_mase=0.6235653162002563, loop_closure_loss=0.0029698321595788, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.009283830411732197) (from W&B history)
  run=56suu9xy: DiagnosticMetrics(one_step_mase=0.5905299186706543, loop_closure_loss=0.003868252271786332, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.009539312683045864) (from W&B history)
  run=jvwajp4f: DiagnosticMetrics(one_step_mase=1.1612942218780518, loop_closure_loss=0.028461968526244164, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.04986795410513878) (from W&B history)
  run=l119bzlt: DiagnosticMetrics(one_step_mase=1.1788380146026611, loop_closure_loss=0.017762387171387672, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.015090666711330414) (from W&B history)
  run=mjfkpubb: DiagnosticMetrics(one_step_mase=1.0404412746429443, loop_closure_loss=0.02395842969417572, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.01698843576014042) (from W&B history)
  run=mxcblnbv: DiagnosticMetrics(one_step_mase=0.6633183360099792, loop_closure_loss=0.002238423563539982, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.007980351336300373) (from W&B history)
  run=qh49bl8i: DiagnosticMetrics(one_step_mase=1.1516597270965576, loop_closure_loss=0.02642839401960373, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.05178018659353256) (from W&B history)
  run=y1hvo5lg: DiagnosticMetrics(one_step_mase=1.1750528812408447, loop_closure_loss=0.018694262951612473, fast_eigenvalue_fraction=0.0, trajectory_val_loss=0.015269872732460499) (from W&B history)

Ranking method:           best_traj_loss
Best run ID:              2luc50is
Best loop_closure_weight: 0.0001
Best tangent_entropy_weight: 0.0
Best kl_dyn_weight:       0.0
Best traj loss:           0.004102
Criteria applied: ['C1', 'C2', 'C3']
Surviving: 20 / 63
Auto-selected run_id: 2luc50is

======================================================================
PARETO FRONTIER RUNS (8 runs)
======================================================================
  Run ID               LC Loss   Traj Val Loss
  ------------  --------------  --------------
  mxcblnbv            0.002238        0.007980
  fybsg3o5            0.040004        0.006296
  wb5ogm10            0.316094        0.005088
  1yhoqwg5            0.360923        0.004663
  iaj54q33            1.814880        0.004410
  2luc50is            1.955323        0.004102 <-- selected
  78ox3tnj           28.198488        0.004083
  3x9dcmu8           50.664642        0.004079

======================================================================
RANKING METHOD COMPARISON (over 20 survivors)
======================================================================
  Method                  Run ID               LC Loss   Traj Val Loss
  ----------------------  ------------  --------------  --------------
  best_traj_loss          2luc50is            1.955323        0.004102 <-- active
  pareto_knee             iaj54q33            1.814880        0.004410
  geo_rank                2luc50is            1.955323        0.004102
  minimax_rank            1yhoqwg5            0.360923        0.004663
  geo_log_score           2luc50is            1.955323        0.004102
  minimax_log_score       mxcblnbv            0.002238        0.007980
======================================================================

Loading run 2luc50is from JacobianODE/WMTask_identity_encoder_verification ...
loaded wmtask RNN model checkpoint 1
Loading cached wmtask hiddens from /orcd/data/ekmiller/001/eisenaj/ControlJacobians/WMTaskModels/WMSelectionTask__cue_time_0.1__response_time_0.25__enforce_fixation_False/BiologicalRNN__cue_time_0.1__learning_rate_0.0005__max_epochs_42__N1_64__N2_64__tau_0.05__dt_0.02__eig_lower_bound_0.1__init_mode_random/_jacobianode_cache/hiddens__all__epoch1__trials4096__seed42.pt
loaded wmtask RNN model checkpoint 41
Loading cached wmtask hiddens from /orcd/data/ekmiller/001/eisenaj/ControlJacobians/WMTaskModels/WMSelectionTask__cue_time_0.1__response_time_0.25__enforce_fixation_False/BiologicalRNN__cue_time_0.1__learning_rate_0.0005__max_epochs_42__N1_64__N2_64__tau_0.05__dt_0.02__eig_lower_bound_0.1__init_mode_random/_jacobianode_cache/hiddens__all__epoch41__trials4096__seed42.pt
Loading checkpoint epoch=40-step=5125.ckpt...
Loading checkpoint epoch=40-step=5125.ckpt...
Computing reconstruction ...
Computing MASE ...
Teacher-forced MASE: 0.6278
Free-running MASE:   1.1222
Computing latent utilization ...
Entropy-based utilization: 0.879
Null subspace mean RMS: 7.963388e-02
Computing Lyapunov exponents ...
  Computing full-trajectory Lyapunov (818 test trajs, T=41) ...
Predicted Lyapunov exponents (batch+burn-in, 128 windowed trajs):
  λ_1 = +0.0177 ± 0.5054
  λ_2 = -0.5777 ± 0.4247
  λ_3 = -1.1772 ± 0.4564
  λ_4 = -1.5194 ± 0.4411
  λ_5 = -1.8526 ± 0.4934
  λ_6 = -2.2310 ± 0.6020
  λ_7 = -2.8720 ± 0.5452
  λ_8 = -3.1829 ± 0.4385
  λ_9 = -3.3824 ± 0.4495
  λ_10 = -3.5682 ± 0.4817
  λ_11 = -3.8252 ± 0.4149
  λ_12 = -3.9909 ± 0.4916
  λ_13 = -4.2053 ± 0.5730
  λ_14 = -4.3960 ± 0.6644
  λ_15 = -4.5568 ± 0.7370
  λ_16 = -4.7436 ± 0.7805
  λ_17 = -4.8720 ± 0.8460
  λ_18 = -4.9774 ± 0.8810
  λ_19 = -5.0732 ± 0.9031
  λ_20 = -5.1880 ± 0.8734
  λ_21 = -5.2819 ± 0.8607
  λ_22 = -5.3861 ± 0.8357
  λ_23 = -5.4908 ± 0.8559
  λ_24 = -5.6147 ± 0.9070
  λ_25 = -5.7352 ± 0.9354
  λ_26 = -5.8820 ± 0.9841
  λ_27 = -6.0356 ± 1.0660
  λ_28 = -6.1920 ± 1.1386
  λ_29 = -6.4217 ± 1.1773
  λ_30 = -6.6486 ± 1.3005
  λ_31 = -6.9221 ± 1.4835
  λ_32 = -7.6068 ± 1.6369
  λ_33 = -7.9549 ± 1.7508
Predicted Lyapunov exponents (full-length, 818 test trajs):
  λ_1 = +0.0177 ± 0.5054
  λ_2 = -0.5777 ± 0.4247
  λ_3 = -1.1772 ± 0.4564
  λ_4 = -1.5194 ± 0.4411
  λ_5 = -1.8526 ± 0.4934
  λ_6 = -2.2310 ± 0.6020
  λ_7 = -2.8720 ± 0.5452
  λ_8 = -3.1829 ± 0.4385
  λ_9 = -3.3824 ± 0.4495
  λ_10 = -3.5682 ± 0.4817
  λ_11 = -3.8252 ± 0.4149
  λ_12 = -3.9909 ± 0.4916
  λ_13 = -4.2053 ± 0.5730
  λ_14 = -4.3960 ± 0.6644
  λ_15 = -4.5568 ± 0.7370
  λ_16 = -4.7436 ± 0.7805
  λ_17 = -4.8720 ± 0.8460
  λ_18 = -4.9774 ± 0.8810
  λ_19 = -5.0732 ± 0.9031
  λ_20 = -5.1880 ± 0.8734
  λ_21 = -5.2819 ± 0.8607
  λ_22 = -5.3861 ± 0.8357
  λ_23 = -5.4908 ± 0.8559
  λ_24 = -5.6147 ± 0.9070
  λ_25 = -5.7352 ± 0.9354
  λ_26 = -5.8820 ± 0.9841
  λ_27 = -6.0356 ± 1.0660
  λ_28 = -6.1920 ± 1.1386
  λ_29 = -6.4217 ± 1.1773
  λ_30 = -6.6486 ± 1.3005
  λ_31 = -6.9221 ± 1.4835
  λ_32 = -7.6068 ± 1.6369
  λ_33 = -7.9549 ± 1.7508
Empirical Lyapunov exponents (mean ± std, all trajectories):
  λ_1 = -0.6353 ± 0.3465
  λ_2 = -1.1737 ± 0.3881
  λ_3 = -1.6231 ± 0.3900
  λ_4 = -2.2124 ± 0.3684
  λ_5 = -2.6625 ± 0.3953
  λ_6 = -3.0691 ± 0.3950
  λ_7 = -3.4613 ± 0.3543
  λ_8 = -3.8197 ± 0.3905
  λ_9 = -4.1081 ± 0.4824
  λ_10 = -4.4143 ± 0.5487
  λ_11 = -4.7030 ± 0.5551
  λ_12 = -5.0074 ± 0.6444
  λ_13 = -5.4875 ± 0.6903
  λ_14 = -5.8604 ± 0.8181
  λ_15 = -6.2924 ± 0.6951
  λ_16 = -6.9284 ± 0.4605
  λ_17 = -7.2216 ± 0.4465
  λ_18 = -7.4797 ± 0.4574
  λ_19 = -7.6652 ± 0.4995
  λ_20 = -7.8578 ± 0.5279
  λ_21 = -8.0532 ± 0.5162
  λ_22 = -8.2598 ± 0.4827
  λ_23 = -8.4152 ± 0.5256
  λ_24 = -8.6150 ± 0.6191
  λ_25 = -8.7509 ± 0.6531
  λ_26 = -8.9435 ± 0.6761
  λ_27 = -9.1106 ± 0.7327
  λ_28 = -9.3066 ± 0.7789
  λ_29 = -9.5068 ± 0.8401
  λ_30 = -9.6792 ± 0.8841
  λ_31 = -9.9201 ± 0.9749
  λ_32 = -10.1668 ± 1.0064
  λ_33 = -10.5224 ± 1.1476
  λ_34 = -10.9142 ± 1.3092
  λ_35 = -11.4060 ± 1.1424
  λ_36 = -11.8052 ± 1.1426
  λ_37 = -12.2050 ± 1.1134
  λ_38 = -12.5768 ± 1.1176
  λ_39 = -12.8330 ± 1.1696
  λ_40 = -13.0615 ± 1.1851
  λ_41 = -13.3863 ± 1.2057
  λ_42 = -13.7144 ± 1.1818
  λ_43 = -14.1195 ± 1.1784
  λ_44 = -14.5715 ± 1.1662
  λ_45 = -15.0996 ± 1.2147
  λ_46 = -16.2075 ± 1.1518
  λ_47 = -17.5372 ± 0.6701
  λ_48 = -18.1930 ± 0.5876
  λ_49 = -18.7837 ± 0.4517
  λ_50 = -19.6473 ± 0.3763
  λ_51 = -20.0017 ± 0.3288
  λ_52 = -20.3280 ± 0.3108
  λ_53 = -20.6549 ± 0.3182
  λ_54 = -21.1145 ± 0.3769
  λ_55 = -22.2697 ± 0.3648
  λ_56 = -22.6857 ± 0.3070
  λ_57 = -23.0476 ± 0.3336
  λ_58 = -23.3982 ± 0.3753
  λ_59 = -23.6251 ± 0.3416
  λ_60 = -23.8476 ± 0.3017
  λ_61 = -24.0640 ± 0.3039
  λ_62 = -24.2836 ± 0.2954
  λ_63 = -24.5149 ± 0.3479
  λ_64 = -24.6883 ± 0.3695
  λ_65 = -24.8755 ± 0.3696
  λ_66 = -25.0269 ± 0.3894
  λ_67 = -25.2158 ± 0.4374
  λ_68 = -25.5075 ± 0.5625
  λ_69 = -25.6488 ± 0.5770
  λ_70 = -25.7848 ± 0.5823
  λ_71 = -25.9102 ± 0.5912
  λ_72 = -26.0255 ± 0.6052
  λ_73 = -26.1459 ± 0.6176
  λ_74 = -26.2626 ± 0.6282
  λ_75 = -26.4016 ± 0.6706
  λ_76 = -26.6179 ± 0.7431
  λ_77 = -26.7730 ± 0.7788
  λ_78 = -26.9160 ± 0.7833
  λ_79 = -27.0809 ± 0.7865
  λ_80 = -27.2758 ± 0.8021
  λ_81 = -27.4458 ± 0.8276
  λ_82 = -27.5865 ± 0.8324
  λ_83 = -27.7870 ± 0.8352
  λ_84 = -27.9605 ± 0.8251
  λ_85 = -28.1614 ± 0.8110
  λ_86 = -28.3325 ± 0.7907
  λ_87 = -28.4719 ± 0.8032
  λ_88 = -28.6079 ± 0.8138
  λ_89 = -28.7489 ± 0.8112
  λ_90 = -28.8710 ± 0.7946
  λ_91 = -28.9854 ± 0.7935
  λ_92 = -29.1186 ± 0.7767
  λ_93 = -29.2522 ± 0.7927
  λ_94 = -29.3821 ± 0.7810
  λ_95 = -29.5324 ± 0.7773
  λ_96 = -29.6540 ± 0.7694
  λ_97 = -29.8267 ± 0.8190
  λ_98 = -29.9552 ± 0.8232
  λ_99 = -30.0740 ± 0.8228
  λ_100 = -30.2080 ± 0.8069
  λ_101 = -30.3406 ± 0.7963
  λ_102 = -30.4832 ± 0.7976
  λ_103 = -30.6420 ± 0.8363
  λ_104 = -30.8079 ± 0.8398
  λ_105 = -30.9375 ± 0.8177
  λ_106 = -31.0411 ± 0.8038
  λ_107 = -31.1422 ± 0.7734
  λ_108 = -31.2421 ± 0.7336
  λ_109 = -31.3550 ± 0.6998
  λ_110 = -31.4809 ± 0.6882
  λ_111 = -31.6144 ± 0.6658
  λ_112 = -31.7371 ± 0.6622
  λ_113 = -31.8809 ± 0.6716
  λ_114 = -32.0030 ± 0.6546
  λ_115 = -32.1282 ± 0.6528
  λ_116 = -32.2557 ± 0.6494
  λ_117 = -32.4058 ± 0.6211
  λ_118 = -32.5309 ± 0.5913
  λ_119 = -32.6509 ± 0.5925
  λ_120 = -32.7307 ± 0.5701
  λ_121 = -32.8411 ± 0.5351
  λ_122 = -32.9175 ± 0.5277
  λ_123 = -33.0191 ± 0.5177
  λ_124 = -33.2099 ± 0.5575
  λ_125 = -33.4094 ± 0.5186
  λ_126 = -33.5531 ± 0.4827
  λ_127 = -33.7664 ± 0.4953
  λ_128 = -34.0341 ± 0.5345
Empirical Lyapunov per condition:
  c=[-1.0]:
    λ_1 = -0.7264 ± 0.2062
    λ_2 = -1.2654 ± 0.3226
    λ_3 = -1.5573 ± 0.2403
    λ_4 = -2.0863 ± 0.3531
    λ_5 = -2.5367 ± 0.3184
    λ_6 = -3.0274 ± 0.1980
    λ_7 = -3.3426 ± 0.1653
    λ_8 = -3.6314 ± 0.1750
    λ_9 = -3.7846 ± 0.1948
    λ_10 = -3.9868 ± 0.2175
    λ_11 = -4.2429 ± 0.1731
    λ_12 = -4.4527 ± 0.1445
    λ_13 = -4.8775 ± 0.3185
    λ_14 = -5.1479 ± 0.3151
    λ_15 = -5.6953 ± 0.2148
    λ_16 = -6.6399 ± 0.2371
    λ_17 = -6.9322 ± 0.2347
    λ_18 = -7.1369 ± 0.1550
    λ_19 = -7.2704 ± 0.1753
    λ_20 = -7.4349 ± 0.1926
    λ_21 = -7.6427 ± 0.2283
    λ_22 = -7.8503 ± 0.1553
    λ_23 = -7.9575 ± 0.1517
    λ_24 = -8.0384 ± 0.1586
    λ_25 = -8.1460 ± 0.1715
    λ_26 = -8.3200 ± 0.2010
    λ_27 = -8.4350 ± 0.2160
    λ_28 = -8.5990 ± 0.2224
    λ_29 = -8.7311 ± 0.2386
    λ_30 = -8.8670 ± 0.2619
    λ_31 = -9.0407 ± 0.3035
    λ_32 = -9.2627 ± 0.3361
    λ_33 = -9.4901 ± 0.3772
    λ_34 = -9.6855 ± 0.4066
    λ_35 = -10.3473 ± 0.3001
    λ_36 = -10.7686 ± 0.2443
    λ_37 = -11.2220 ± 0.2621
    λ_38 = -11.6036 ± 0.2220
    λ_39 = -11.8069 ± 0.2351
    λ_40 = -12.0204 ± 0.2595
    λ_41 = -12.3606 ± 0.3080
    λ_42 = -12.7107 ± 0.3902
    λ_43 = -13.1254 ± 0.3418
    λ_44 = -13.5861 ± 0.3044
    λ_45 = -14.0153 ± 0.2752
    λ_46 = -15.3154 ± 0.6518
    λ_47 = -17.1978 ± 0.4545
    λ_48 = -17.7830 ± 0.3508
    λ_49 = -18.4810 ± 0.2202
    λ_50 = -19.7867 ± 0.3377
    λ_51 = -20.1334 ± 0.1876
    λ_52 = -20.4607 ± 0.1976
    λ_53 = -20.6887 ± 0.1962
    λ_54 = -21.0423 ± 0.2688
    λ_55 = -22.4210 ± 0.2868
    λ_56 = -22.7879 ± 0.2309
    λ_57 = -23.2138 ± 0.2655
    λ_58 = -23.6314 ± 0.2396
    λ_59 = -23.8489 ± 0.1909
    λ_60 = -24.0222 ± 0.1891
    λ_61 = -24.2094 ± 0.2165
    λ_62 = -24.4002 ± 0.2494
    λ_63 = -24.6918 ± 0.3013
    λ_64 = -24.9140 ± 0.2892
    λ_65 = -25.1275 ± 0.2519
    λ_66 = -25.3093 ± 0.2336
    λ_67 = -25.5510 ± 0.2458
    λ_68 = -25.9887 ± 0.2367
    λ_69 = -26.1544 ± 0.2086
    λ_70 = -26.3032 ± 0.1657
    λ_71 = -26.4371 ± 0.1543
    λ_72 = -26.5658 ± 0.1405
    λ_73 = -26.6965 ± 0.1296
    λ_74 = -26.8203 ± 0.1375
    λ_75 = -27.0007 ± 0.1686
    λ_76 = -27.2765 ± 0.1831
    λ_77 = -27.4672 ± 0.1484
    λ_78 = -27.6048 ± 0.1759
    λ_79 = -27.7678 ± 0.2117
    λ_80 = -27.9876 ± 0.2272
    λ_81 = -28.1836 ± 0.2564
    λ_82 = -28.3277 ± 0.2590
    λ_83 = -28.5268 ± 0.2645
    λ_84 = -28.6954 ± 0.2112
    λ_85 = -28.8812 ± 0.2421
    λ_86 = -29.0294 ± 0.2607
    λ_87 = -29.1802 ± 0.2924
    λ_88 = -29.3218 ± 0.2982
    λ_89 = -29.4610 ± 0.2708
    λ_90 = -29.5741 ± 0.2550
    λ_91 = -29.6847 ± 0.2500
    λ_92 = -29.7949 ± 0.2559
    λ_93 = -29.9370 ± 0.2952
    λ_94 = -30.0633 ± 0.2881
    λ_95 = -30.2209 ± 0.2619
    λ_96 = -30.3373 ± 0.2507
    λ_97 = -30.5692 ± 0.2232
    λ_98 = -30.7046 ± 0.2081
    λ_99 = -30.8249 ± 0.1976
    λ_100 = -30.9457 ± 0.1881
    λ_101 = -31.0663 ± 0.1904
    λ_102 = -31.2034 ± 0.2055
    λ_103 = -31.3953 ± 0.2275
    λ_104 = -31.5734 ± 0.1843
    λ_105 = -31.6854 ± 0.1598
    λ_106 = -31.7745 ± 0.1514
    λ_107 = -31.8437 ± 0.1462
    λ_108 = -31.9083 ± 0.1510
    λ_109 = -31.9848 ± 0.1553
    λ_110 = -32.0977 ± 0.1758
    λ_111 = -32.2021 ± 0.1650
    λ_112 = -32.3055 ± 0.1704
    λ_113 = -32.4576 ± 0.1998
    λ_114 = -32.5686 ± 0.2206
    λ_115 = -32.6861 ± 0.2272
    λ_116 = -32.8183 ± 0.2366
    λ_117 = -32.9583 ± 0.2041
    λ_118 = -33.0708 ± 0.1866
    λ_119 = -33.1947 ± 0.1578
    λ_120 = -33.2557 ± 0.1537
    λ_121 = -33.3288 ± 0.1524
    λ_122 = -33.4019 ± 0.1463
    λ_123 = -33.4969 ± 0.1384
    λ_124 = -33.7285 ± 0.1950
    λ_125 = -33.8683 ± 0.2114
    λ_126 = -33.9820 ± 0.2101
    λ_127 = -34.2037 ± 0.2425
    λ_128 = -34.4915 ± 0.1924
  c=[1.0]:
    λ_1 = -0.5442 ± 0.4258
    λ_2 = -1.0820 ± 0.4251
    λ_3 = -1.6890 ± 0.4880
    λ_4 = -2.3384 ± 0.3395
    λ_5 = -2.7883 ± 0.4241
    λ_6 = -3.1107 ± 0.5194
    λ_7 = -3.5800 ± 0.4426
    λ_8 = -4.0079 ± 0.4513
    λ_9 = -4.4317 ± 0.4671
    λ_10 = -4.8417 ± 0.4350
    λ_11 = -5.1632 ± 0.4031
    λ_12 = -5.5621 ± 0.4401
    λ_13 = -6.0975 ± 0.3268
    λ_14 = -6.5729 ± 0.4723
    λ_15 = -6.8896 ± 0.4543
    λ_16 = -7.2168 ± 0.4491
    λ_17 = -7.5110 ± 0.4197
    λ_18 = -7.8225 ± 0.3991
    λ_19 = -8.0599 ± 0.3955
    λ_20 = -8.2807 ± 0.4031
    λ_21 = -8.4637 ± 0.3789
    λ_22 = -8.6693 ± 0.3261
    λ_23 = -8.8730 ± 0.3318
    λ_24 = -9.1916 ± 0.2755
    λ_25 = -9.3558 ± 0.3019
    λ_26 = -9.5670 ± 0.3088
    λ_27 = -9.7862 ± 0.3367
    λ_28 = -10.0143 ± 0.4015
    λ_29 = -10.2826 ± 0.3871
    λ_30 = -10.4915 ± 0.4167
    λ_31 = -10.7995 ± 0.5106
    λ_32 = -11.0708 ± 0.5261
    λ_33 = -11.5548 ± 0.5986
    λ_34 = -12.1428 ± 0.4901
    λ_35 = -12.4647 ± 0.5256
    λ_36 = -12.8417 ± 0.6327
    λ_37 = -13.1881 ± 0.6900
    λ_38 = -13.5500 ± 0.7438
    λ_39 = -13.8592 ± 0.7567
    λ_40 = -14.1026 ± 0.7561
    λ_41 = -14.4121 ± 0.8405
    λ_42 = -14.7180 ± 0.7906
    λ_43 = -15.1137 ± 0.8259
    λ_44 = -15.5569 ± 0.8270
    λ_45 = -16.1839 ± 0.7223
    λ_46 = -17.0995 ± 0.7977
    λ_47 = -17.8767 ± 0.6795
    λ_48 = -18.6031 ± 0.4807
    λ_49 = -19.0863 ± 0.4200
    λ_50 = -19.5079 ± 0.3612
    λ_51 = -19.8699 ± 0.3827
    λ_52 = -20.1953 ± 0.3452
    λ_53 = -20.6211 ± 0.4025
    λ_54 = -21.1867 ± 0.4491
    λ_55 = -22.1184 ± 0.3719
    λ_56 = -22.5835 ± 0.3383
    λ_57 = -22.8813 ± 0.3114
    λ_58 = -23.1651 ± 0.3401
    λ_59 = -23.4014 ± 0.3112
    λ_60 = -23.6730 ± 0.2922
    λ_61 = -23.9187 ± 0.3093
    λ_62 = -24.1671 ± 0.2920
    λ_63 = -24.3381 ± 0.2980
    λ_64 = -24.4625 ± 0.2961
    λ_65 = -24.6234 ± 0.2876
    λ_66 = -24.7445 ± 0.2985
    λ_67 = -24.8805 ± 0.3121
    λ_68 = -25.0262 ± 0.3364
    λ_69 = -25.1432 ± 0.3327
    λ_70 = -25.2663 ± 0.3354
    λ_71 = -25.3833 ± 0.3457
    λ_72 = -25.4851 ± 0.3580
    λ_73 = -25.5953 ± 0.3732
    λ_74 = -25.7049 ± 0.3842
    λ_75 = -25.8025 ± 0.3905
    λ_76 = -25.9593 ± 0.4502
    λ_77 = -26.0788 ± 0.4759
    λ_78 = -26.2272 ± 0.4965
    λ_79 = -26.3940 ± 0.4979
    λ_80 = -26.5639 ± 0.4700
    λ_81 = -26.7081 ± 0.4633
    λ_82 = -26.8452 ± 0.4677
    λ_83 = -27.0472 ± 0.4790
    λ_84 = -27.2257 ± 0.4858
    λ_85 = -27.4415 ± 0.4684
    λ_86 = -27.6357 ± 0.4588
    λ_87 = -27.7636 ± 0.4476
    λ_88 = -27.8940 ± 0.4641
    λ_89 = -28.0368 ± 0.4772
    λ_90 = -28.1679 ± 0.4563
    λ_91 = -28.2862 ± 0.4668
    λ_92 = -28.4423 ± 0.4748
    λ_93 = -28.5673 ± 0.4805
    λ_94 = -28.7009 ± 0.4562
    λ_95 = -28.8440 ± 0.4371
    λ_96 = -28.9707 ± 0.4320
    λ_97 = -29.0843 ± 0.4340
    λ_98 = -29.2058 ± 0.4333
    λ_99 = -29.3232 ± 0.4317
    λ_100 = -29.4704 ± 0.4210
    λ_101 = -29.6148 ± 0.4215
    λ_102 = -29.7629 ± 0.4376
    λ_103 = -29.8888 ± 0.4596
    λ_104 = -30.0424 ± 0.4510
    λ_105 = -30.1896 ± 0.4381
    λ_106 = -30.3077 ± 0.4387
    λ_107 = -30.4407 ± 0.4357
    λ_108 = -30.5759 ± 0.4065
    λ_109 = -30.7253 ± 0.4015
    λ_110 = -30.8640 ± 0.3932
    λ_111 = -31.0266 ± 0.4098
    λ_112 = -31.1687 ± 0.4488
    λ_113 = -31.3041 ± 0.4432
    λ_114 = -31.4374 ± 0.4099
    λ_115 = -31.5704 ± 0.4217
    λ_116 = -31.6930 ± 0.3921
    λ_117 = -31.8533 ± 0.3447
    λ_118 = -31.9910 ± 0.2844
    λ_119 = -32.1072 ± 0.2920
    λ_120 = -32.2057 ± 0.2734
    λ_121 = -32.3533 ± 0.2704
    λ_122 = -32.4332 ± 0.2565
    λ_123 = -32.5412 ± 0.2446
    λ_124 = -32.6914 ± 0.2128
    λ_125 = -32.9506 ± 0.2681
    λ_126 = -33.1242 ± 0.2318
    λ_127 = -33.3292 ± 0.2214
    λ_128 = -33.5768 ± 0.3401
Mean KY dim (predicted): 0.901 ± 0.957
Mean KY dim (empirical): 0.056 ± 0.249
Mean KY dim (burn-in):   0.901 ± 0.957
Computing prediction windows ...
Windows: 3 — nMSE min=0.0382, median=0.1111, mean=0.0907, max=0.1229
Computing long-trajectory free-running rollouts ...
Skipping 'encoder_decoder_jacobians' for conditioned model: vmap+jacrev OOMs on DirectSum + condition (TODO: rewrite without vmap or wait for index_copy_ batching rule).
Computing amplification loss ...
Amplification loss — True state: 0.005242
Amplification loss — Latent:     0.005311
Skipping 'tangent_spectrum' for conditioned model: compute_tangent_spectrum needs c plumbing through _encoder_jacobian_at's vmap+jacrev (TODO).
Computing gramians_overlay ...
  gramians_overlay failed: CUDA error: device-side assert triggered
Search for `cudaErrorAssert' in https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__TYPES.html for more information.
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.

Skipping 'gramians_metric_overlay': requires DirectSum 2-block encoder.
```

</details>
