import pandas as pd
import matplotlib.pyplot as plt

def generate():
    graph_data = pd.read_csv('data.csv')

    # Generate each plot
    difficulty(graph_data)
    time(graph_data)
    input(graph_data)
    error(graph_data)
    failure(graph_data)

    # Display all plots together
    plt.show()

def difficulty(data):
    data.plot(x='Name', y='Difficulty', kind='bar', color='red')
    plt.title('Difficulty')
    plt.xlabel('Name')
    plt.ylabel('Count')
    plt.tight_layout()  # Ensures labels and titles fit well

def time(data):
    data.plot(x='Name', y='Time', kind='bar', color='green')
    plt.title('Time')
    plt.xlabel('Name')
    plt.ylabel('Time in Seconds')
    plt.tight_layout()

def input(data):
    data.plot(x='Name', y='Inputs', kind='bar', color='blue')
    plt.title('Clicks')
    plt.xlabel('Name')
    plt.ylabel('Number of Clicks')
    plt.tight_layout()

def error(data):
    data.plot(x='Name', y='Errors', kind='bar', color='purple')
    plt.title('Errors')
    plt.xlabel('Name')
    plt.ylabel('Number of Errors')
    plt.tight_layout()

def failure(data):
    data['Failures'] = data['Failures'].apply(lambda x: 1 if x == 'TRUE' else 0)
    data.plot(x='Name', y='Failures', kind='bar', color='orange')
    plt.title('Failed Pages')
    plt.xlabel('Name')
    plt.ylabel('Failures (0 = FALSE, 1 = TRUE)')

if __name__ == "__main__":
    generate()