from evaluative_plot import plot_comparison_bars

experiment_labels = ['Method', 'Method B', 'Method C']
primary = [0.62, 0.59, 0.58]  # e.g., F1 scores or CTR
secondary = [1.2e-8, 3.6e-7, 9.1e-7]  # e.g., diversity volume or entropy

annotations = {
    1: '+5.00% over A',
    2: '+7.00% over A\n+1.70% over B'
}


plot_comparison_bars(
    experiment_labels=experiment_labels,
    primary_metric_values=primary,
    secondary_metric_values=secondary,
    annotations=annotations,
    primary_label="Score 1",
    secondary_label="Score 2",
    title="Evaluation Results"
)
