class ErrorService:
    def __init__(self):
        """
        main reason of this service is managing errors.
        Track errors and take actions like send email, warn systems etc.
        cache errors and occasion counts.
        """
        self.error_report_service = ErrorReportService()
        self.error_cache = dict()
        self.error_conf = dict()

    def raise_error(self, error, *args, **kwargs):
        error_parsed, error_metrics, decision = self.inspect_error(error=error)
        print(error_parsed)

    def inspect_error(self, error, *args, **kwargs):
        """
        match the error with known errors and get conf.
        Then decide what to do next.
        """
        error_parsed = self.parse_error(error)
        error_metrics = self.calculate_error_metrics(error_parsed=error_parsed)
        decision = self.make_decision(error_parsed=error_parsed, error_metrics=error_metrics)
        return error_parsed, error_metrics, decision

    def parse_error(self, error):
        """
        parse error data into dict
        """
        return error

    def calculate_error_metrics(self, error_parsed):
        error_conf = self.get_error_conf(error_parsed=error_parsed)
        # do st with error conf.
        error_metrics = dict()
        return error_metrics

    def make_decision(self, error_parsed, error_metrics):
        action = getattr(self.error_report_service, "send_email")  # get action after inspect metrics
        decision = action if callable(action) else self.do_nothing
        return decision

    def get_error_conf(self, error_parsed):
        """
        get error_parsed conf from settings
        """
        return dict(error_type="", treshold="")

    def do_nothing(self):
        pass


class ErrorReportService:
    def __init__(self):
        """
        report errors via sms or api
        """
        pass

    def send_report_mail(self):
        pass

    def send_error_data(self):
        pass

    def save_error_data(self):
        pass

