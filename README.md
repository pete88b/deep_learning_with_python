# Study notes: Deep Learning with Python

Working through [Second Edition François Chollet](https://www.manning.com/books/deep-learning-with-python-second-edition)

# Exploring `fit_residual`

The `fit_residual` idea is to build a model that has direct access to baseline results - in the hope that the model can learn to correct the errors of the baseline with a result that is;
- more accurate than without `fit_residual` and/or
- achieved with less compute / smaller models.
i.e. this is feature engineering and problem framing engineering to inject useful assumptions into the model.

- [https://github.com/pete88b/deep_learning_with_python/blob/main/10.2_temperature_forecasting.ipynb](10.2_temperature_forecasting.ipynb) 
    - creates a fully connect model that can do better than the non-machine learning baseline
- [https://github.com/pete88b/deep_learning_with_python/blob/main/10.2_temperature_forecasting_part2.ipynb](10.2_temperature_forecasting_part2.ipynb) 
    - shows how `fit_residual` can be used to get a single layer LSTM to the same test MAE as stacked GRU
    - we also use the date features to improve MAE
- [https://github.com/pete88b/deep_learning_with_python/blob/main/10.2_california_housing.ipynb](10.2_california_housing.ipynb)
    - shows that the `fit_residual` won't work on all datasets (o:

## Anaconda environment creation

I use this for trying things out on my CPU-only windows machine.

```
conda create -n tf python==3.9 -y
conda activate tf
pip install tensorflow
pip install nbdev jupyterlab pandas matplotlib
pip install --upgrade jupyter notebook
```
