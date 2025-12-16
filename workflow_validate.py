from prefect import flow

@flow
def validate_data():
    print("Data validated")
