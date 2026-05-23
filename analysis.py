def dataset_info(customers):
    print("\nDataset Info:")
    print(customers.info())


def dataset_shape(customers):
    print("\nDataset Shape:")
    print(customers.shape)


def missing_values(customers):
    print("\nMissing Values:")
    print(customers.isnull().sum())


def top_states(customers):
    print("\nTop 10 States:")

    print(
        customers["customer_state"]
        .value_counts()
        .head(10)
    )


def top_cities(customers):
    print("\nTop 10 Cities:")

    print(
        customers["customer_city"]
        .value_counts()
        .head(10)
    )