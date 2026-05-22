import matplotlib.pyplot as plt

def plot_phase(
    phase,
    flux
):

    plt.figure(
        figsize=(8,6)
    )

    plt.scatter(
        phase,
        flux,
        s=3
    )

    plt.xlabel(
        "Phase"
    )

    plt.ylabel(
        "Flux"
    )

    plt.title(
        "Phase Folded Light Curve"
    )

    plt.tight_layout()

    plt.savefig(
        "phase_curve.png",
        dpi=300
    )

    plt.show()
