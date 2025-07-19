import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

def plot_comparison_bars(
    experiment_labels,
    primary_metric_values,
    secondary_metric_values,
    annotations=None,
    primary_label="Metric A",
    secondary_label="Metric B",
    title="Evaluation Comparison",
    use_log_scale=True
):
    x = np.arange(len(experiment_labels))
    width = 0.35

    fig, ax1 = plt.subplots(figsize=(8, 5))

    bars1 = ax1.bar(x - width/2, primary_metric_values, width, color='lightcoral', label=primary_label)
    ax1.set_ylabel(primary_label, color='lightcoral')
    ax1.tick_params(axis='y', labelcolor='lightcoral')
    ax1.set_xticks(x)
    ax1.set_xticklabels(experiment_labels)
    ax1.spines['top'].set_visible(False)

    ax2 = ax1.twinx()
    bars2 = ax2.bar(x + width/2, secondary_metric_values, width, color='skyblue', label=secondary_label)
    ax2.set_ylabel(secondary_label, color='skyblue')
    ax2.tick_params(axis='y', labelcolor='skyblue')
    if use_log_scale:
        ax2.set_yscale('log')

    for bar, val in zip(bars1, primary_metric_values):
        ax1.text(bar.get_x() + bar.get_width() / 2, val + 0.01, f'{val:.3f}', ha='center', color='black')

    if annotations:
        for idx, (bar, val) in enumerate(zip(bars2, secondary_metric_values)):
            text = annotations.get(idx, "")
            if text:
                ax2.text(bar.get_x() + bar.get_width() / 2, val * 2, text,
                         ha='center', color='darkgreen', fontsize=9)

    for bar, val in zip(bars2, secondary_metric_values):
        ax2.text(bar.get_x() + bar.get_width() / 2, val * 1.2, f'{val:.2e}', ha='center', color='black')

    patch_primary = mpatches.Patch(color='lightcoral', label=primary_label)
    patch_secondary = mpatches.Patch(color='skyblue', label=secondary_label)
    patch_annot = mpatches.Patch(color='darkgreen', label='Gain Info')

    fig.legend(
        handles=[patch_primary, patch_secondary, patch_annot],
        loc='upper center',
        bbox_to_anchor=(0.5, 1.05),
        ncol=3,
        frameon=False
    )

    ax1.spines['top'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    plt.title(title)
    plt.tight_layout()
    plt.show()
