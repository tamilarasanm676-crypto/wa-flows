from prefect import flow

@flow
def load_data():
    print("Data loaded")
