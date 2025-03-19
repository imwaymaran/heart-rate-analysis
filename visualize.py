import matplotlib.pyplot as plt


def heart_rate_plot(data: list, filename: str):
    """
    Generates and saves a heart rate line plot based on the provided data.

    Args:
        data (list[int]): list of integers representing heart rate samples.
        filename (str): the file path from which the heart rate data was extracted.

    Returns:
        None: The function saves the plot as an image and does not return any value.

    Example:
        >>> heart_rate_plot([72, 75, 78, 80, 76], "data/phase0.txt")
        # Saves the plot as 'images/phase0.png'
    """
    time_intervals = [i * 5 for i in range(len(data))]

    plt.figure(figsize=(12, 5))
    plt.plot(
        time_intervals,
        data,
        marker=".",
        color="r",
        markeredgecolor="black",
        markersize=8,
        label="Heart Rate",
    )
    plt.xlabel("Time (minutes)")
    plt.ylabel("Heart Rate (BPM)")

    # extract and format the filename to use as the plot title for clarity
    plot_title = filename.split("/")[-1]
    plot_title = plot_title.split(".")[0]

    plt.title(f"{plot_title.title()}: Heart Rate Over Time")

    plt.legend()
    plt.grid(True)

    plt.savefig(f"images/{plot_title}.png")
    plt.close()
