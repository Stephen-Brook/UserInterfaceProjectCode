import pandas as pd
import matplotlib.pyplot as plt

def calculateStatistics(graph):
    means = graph[['Difficulty', 'Time', 'Inputs', 'Errors']].mean()
    standardDiv = graph[['Difficulty', 'Time', 'Inputs', 'Errors']].std()  # Calculate std for each column
    return means, standardDiv

def plotStatistics(means, standardDiv):
    print("Data Statistics: ")
    print("Means: ")
    print(means)
    print("Standard Deviations: ")
    print(standardDiv)

    plt.figure()

    # Plot for difficulty
    plt.subplot(2, 2, 1)
    plt.bar(['Difficulty'], means['Difficulty'], yerr=standardDiv['Difficulty'], color='red', capsize=5, width=0.5)
    plt.title('Difficulty Mean with Standard Deviation')
    plt.ylabel('Mean Difficulty')

    # Plot for time
    plt.subplot(2, 2, 2)
    plt.bar(['Time'], means['Time'], yerr=standardDiv['Time'], color='green', capsize=5, width=0.5)
    plt.title('Time Mean with Standard Deviation')
    plt.ylabel('Mean Time in Seconds')

    # Plot for inputs
    plt.subplot(2, 2, 3)
    plt.bar(['Inputs'], means['Inputs'], yerr=standardDiv['Inputs'], color='blue', capsize=5, width=0.5)
    plt.title('Inputs Mean with Standard Deviation')
    plt.ylabel('Mean Inputs')

    # Plot for Errors
    plt.subplot(2, 2, 4)
    plt.bar(['Errors'], means['Errors'], yerr=standardDiv['Errors'], color='purple', capsize=5, width=0.5)
    plt.title('Errors Mean with Standard Deviation')
    plt.ylabel('Mean Errors')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    graph = pd.read_csv('data.csv')

    means, standardDiv = calculateStatistics(graph)
    plotStatistics(means, standardDiv)