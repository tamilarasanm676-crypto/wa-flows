from prefect import flow

@flow
def generate_report():
    print("Report generated")
