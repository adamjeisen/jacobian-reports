# Sweep submission instructions

Endeavour-side workflow: write a YAML file under `instructions/pending/`,
commit + push, and the engaging cron `engaging-controller` picks it up
within ~5 min, runs `jsweep` locally on engaging, and moves the file to
`instructions/claimed/` (annotated with the SLURM array id) on success
or `instructions/failed/` with an error message on failure.

Reports land under `<wandb_project>/<wandb_group>/` after the controller
completes the analysis sbatch downstream.

## File format

```yaml
experiment: lorenz_full_additive_mse_p30
overrides:
  - hydra.launcher.partition=ou_bcs_normal
  - data.postprocessing.obs_noise=0.05   # any other Hydra-style overrides
submitted_at: 20260415T204500Z           # UTC ISO-8601 (controller fills this if absent)
submitted_from: endeavour                # informational
```

`experiment` is required and must reference an experiment YAML under
`JacobianODE/jacobians/conf/experiment/<name>.yaml`. `overrides` is a
list of dotted-path Hydra overrides forwarded verbatim to `jsweep`.
Everything else is informational.

The filename convention is `<UTC-timestamp>-<experiment>.yaml`, e.g.
`20260415T204500Z-lorenz_full_additive_mse_p30.yaml`. The controller
ignores `.gitkeep` and any non-`.yaml` files.

## Lifecycle

```
pending/  -> claimed/     (controller submitted; annotated with slurm_array_id)
pending/  -> failed/      (controller's prepare_sweep / jsweep returned an error)
```

The annotated file in `claimed/` looks like:

```yaml
experiment: lorenz_full_additive_mse_p30
overrides: [...]
submitted_at: 20260415T204500Z
submitted_from: endeavour
slurm_array_id: 11924964
slurm_submitted_at: 20260415T204732Z
wandb_group: lorenz_full_additive_mse_p30__lc_sweep
expected_run_count: 9
```

## Helper script

On endeavour, `~/bin/j-submit` writes one of these files for you and pushes:

```bash
j-submit lorenz_full_additive_mse_p30 hydra.launcher.partition=ou_bcs_normal
```
