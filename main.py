"""
The main Python mpdule that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""

from metrics import average, maximum, standard_deviation
from cleaner import filter_nondigits
from visualize import heart_rate_plot


def run(filename: str) -> None:
    """
    Process heart rate data from the specified file, clean it, calculate metrics,
    and save visualizations.

    Args:
        filename (str): the path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: the average, max, and standard deviation.
    """
    data = []

    # open file using file I/O and read it into the `data` list
    with open(filename, "r") as file:
        for line in file:
            data.append(line)

    # Use `filter_nondigits` to clean the data and remove invalid entries, save the output to a new variable
    filtered_data = filter_nondigits(data)

    # plot this data to explore changes in heart rate for this file, save this visualization to the "images" folder
    heart_rate_plot(filtered_data, filename)

    # calculate the average, maximum, and standard deviation of this file using the functions you've wrote
    avg_hr = average(filtered_data)
    max_hr = maximum(filtered_data)
    std_dev_hr = standard_deviation(filtered_data)

    # return all 3 values
    return avg_hr, max_hr, std_dev_hr


if __name__ == "__main__":
    print(run("data/phase0.txt"))
