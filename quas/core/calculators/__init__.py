from abc import abstractmethod, ABC


class AbstractValueCalculator(ABC):
    """
    Calculators should make calculations whenever they called.
    self.result and self.errors will be created after calculation is resolved.
    """
    name = None  # str
    slug = None  # str
    config = {}
    # Following properties must be reassigned after self.calculate()
    result = None
    result_value = None
    result_unit = None

    def __init__(self, config=None, **values_kwargs):
        self._parse_config()
        self._parse_values(values_kwargs)
        self.calculate()

    @abstractmethod
    def calculate(self):
        """
        Make calculations by using class attributes which assigned by parser
        methods. Assign calculation result to self.result,
        append errors to self.errors list and raise them.
        Assign valid value to self.result or raise error.
        """
        if not (self.name and self.slug and self.config):
            raise NotImplementedError()

    @abstractmethod
    def _parse_config(self):
        """
        Create class attributes from config
        """
        if not self.config:
            raise NotImplementedError()

    @abstractmethod
    def _parse_values(self, values_kwargs):
        """
        Create class attributes from given calculation parameters/values
        """
        if not values_kwargs:
            raise NotImplementedError

    def _build_error_log(self, err, **kwargs) -> object:
        kwargs.update({'Error': err})
        return kwargs


class SimpleValueCalculator(AbstractValueCalculator):
    name = "Simple Value Calculator"
    slug = "simple_value_calculator"

    def calculate(self):
        self.result = self.result_value, self.result_unit
        return self.result

    def _parse_config(self):
        pass

    def _parse_values(self, values_kwargs):
        self.result_value = values_kwargs['default_value']
        self.result_unit = values_kwargs['default_value_unit']


class GeneralPerformanceCalculator(AbstractValueCalculator):
    """
    Pass product model as kwarg.
    """
    name = "General Performance Calculator"
    slug = "general_performance_calculator"
    product = None

    def calculate(self):
        from core.products.models import Product
        if not self.product:
            raise TypeError("calculate() missing argument: 'product'")
        if not isinstance(self.product, Product):
            raise TypeError("Argument 'product' must be "
                            "core.products.Product instance")

        self.result = 90
        return self.result

    def _parse_config(self):
        pass

    def _parse_values(self, values_kwargs):
        self.product = values_kwargs['product']


class Calculators:
    """
    ONLY the calculator variable names must end with '_calculator'
    """
    simple_value_calculator = SimpleValueCalculator
    general_performance_calculator = GeneralPerformanceCalculator

    @staticmethod
    def get_calculators():
        return (
            [getattr(Calculators, attr).slug, getattr(Calculators, attr).name]
            for attr in dir(Calculators) if attr.endswith("_calculator"))
