import matplotlib.pyplot as plt


def plot_top_states(customers):

    top_states = (
        customers["customer_state"]
        .value_counts()
        .head(10)
    )

    top_states.plot(kind="bar")

    plt.title("Top 10 Customer States")
    plt.xlabel("State")
    plt.ylabel("Customer Count")

    plt.savefig(
        "charts/customer_states.png"
    )

    plt.show()