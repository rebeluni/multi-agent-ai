from tools.send_to_slack import log_to_slack

def run_logger(content):
    status = log_to_slack(content)
    return status

