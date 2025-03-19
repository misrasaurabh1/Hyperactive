class Checks:
    _fit_successful = False

    def verify_fit(function):
        def wrapper(self, X, y):
            self._fit_successful = True
            return function(self, X, y)

        return wrapper
