import pandas as pd

from mia.synthesizers.base import BaseSynthesizer


class IdentitySynthesizer(BaseSynthesizer):
    """Trivial synthesizer.

    Returns the same exact data that is used to fit it.
    """
    def fit(self, train_data, *args):
        self.data = pd.DataFrame(train_data)

    def sample(self, samples):
        return self.data.sample(samples, replace=False).to_numpy().copy()
