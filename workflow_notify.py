from prefect import flow

@flow
def send_notification():
    print("Notification sent")
