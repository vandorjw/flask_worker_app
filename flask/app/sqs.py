from boto import sqs


def submit_to_sqs(sqs_region, sqs_queue_name, json_payload):
    """
    Submit a message into the SQS queue.
    """
    conn = sqs.connect_to_region(sqs_region)

    if conn:
        queue = conn.get_queue(sqs_queue_name)

        if queue:
            try:
                msg = conn.send_message(queue, json_payload)
                if msg.id:
                    print("msg to queue: {}".format(json_payload))
                    return True
                else:
                    log_msg = '{ident}|subject={subject}|data_title={data_title}|data={data}'.format(
                        ident='Exception sending message to queue',
                        subject='SQS Error',
                        data=json_payload,
                        data_title='SQS Payload',
                    )
                    print(log_msg)
                    return False
            except Exception as exc:
                log_msg = '{ident}|subject={subject}|data_title={data_title}|data={data}|exc={exc}'.format(
                    ident='Exception sending message to queue',
                    subject='SQS Error',
                    data=json_payload,
                    data_title='SQS Payload',
                    exc=exc,
                )
                print(log_msg)
                return False
        else:
            log_msg = 'get_queue({queue}) failed|subject={subject}|data_title={data_title}|data={data}'.format(
                queue=sqs_queue_name,
                subject='SQS Error',
                data=json_payload,
                data_title='SQS Payload'
            )
            print(log_msg)
            return False
    else:
        ident = 'boto.sqs.connect_to_region({sqs_region}) failed'.format(sqs_region=sqs_region)
        log_msg = '{ident}|subject={subject}|data_title={data_title}|data={data}'.format(
            ident=ident,
            subject='SQS Error',
            data=json_payload,
            data_title='SQS Payload',
        )
        print(log_msg)
        return False

