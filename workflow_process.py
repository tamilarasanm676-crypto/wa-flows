from prefect import flow

@flow
def process_data():
    print("Data processed")
