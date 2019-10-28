# Time Series

**Time series** problems are problems that involve forecasting (extrapolating) the future based on the information of the past. Typically we have to make a chain of non-independent predictions rather than predict discrete, indepdenent events.

Most machine learning problems assume that the order of rows don't matter and that each row is independent of each other. Since time series problems involve time-ordered rows where past events influence future events, the rows are not independent and this independence assumption is violated.

Another key assumption of ML is that the training data is similar to the data being predicted (in this case, future data). This assumption must be true for time series as well.


# Decomposition

You can **decompose** a time series into four key parts:

- The **trend** (T), where the mean is changing over time (e.g., sales generally keep increasing over time)
- **Seasonality** (S) (e.g., sales are higher in the holiday season)
- A non-seasonal **cyclical** (C) component (e.g., stock market follows "business cycles"). This is distinct from seasonality as seasonality has a fixed period (e.g., every November), whereas cycle does not.
- A **random** component (e)

## Types of decomposition

There are two types of decomposition -- **addititive**, where `y = T + S + C + e` and **multiplicative**, where `y = T * S * C * e`.

# Stationary vs. non-stationarity

**Stationary** time series (a) do not have a trend and also (b) do not have variance that changes over time. **Non-stationary** trends do have (a) and/or (b). Typically (a) and (b) create problems for modeling, as models have trouble extrapolating these and they tend to violate the assumption that the training data is similar to the data being predicted.

## Converting to stationary

We can resolve these issues by converting a non-stationary series to a stationary series. This is done by **differencing**, where we look at the differences in the target over time rather than the actual target (y[t]-> y[t] - y[t-1]).

We can also handle exponential trends using techniques like log transformations.


# Handling Features

## Lags

Lagging is pretty key to time series. A **lag** is when you use the value from the previous series to forecast the next series. You can lag the target variable (e.g., use last month's sales to predict next month's sales) and/or you can lag independent variables. Lagging works because the real world has delays (e.g., it takes a few weeks for marketing to transition to sales so marketing spend from three weeks ago may be more predictive than marketing spend of the same week) and causations over time (e.g., sales from last year show that the store is more popular so there is more word of mouth and it is even more popular the next year).

Lagging risks losing some data, as if you are using data from the previous month you won't be able to use the first month in your training data (because there's no previous month data for month -1). If you are using data from the three previous months, you won't be able to train on the first three months. This may not be an issue though, because unlike with non-time series problems, more data in time series isn't always better (since you might prefer to only be modeling the most recent trend).

We can mix lags of different lengths.

## Rolling Statistics

Lags aren't the only thing we can do - we can also calculate **rolling statistics**, like the mean of a variable over the past 14 days. You can also do rolling stats on differences.

## Which Lags / Rolling Stats to Use?

- Assess with **cross correlation function**, which tests correlation of many different lags.

- Assess with **partial autocorrelation function** (PACF), which gives the partial correlation of a stationary time series with its own lagged values, regressed the values of the time series at all shorter lags. Also can assess with the **autocorrelation function** (ACF), which does not control for other lags. 

- changing lag lengths based on data type, domain knowledge, and how quickly you think the series reacts to change (e.g., use shorter lags for stocks)

- compare by backtesting

## Known in Advance vs. Not

When we are trying to predict in the future, we run into an issue that the features we are using for prediction might also be unknown at prediction time. For example, our historical data might contain information about rainfall and how that connects to sales, but we can't reliably know the rainfall three months in the future to predict future sales.

However, some features are known in advance - like Christmas time may also have a big impact on sales and we always know exactly when Christmas will be.

For features that are not known in advance, we can still use them by either explicitly forecasting them, extrapolating them out using lags / rolling stats of sufficient size, or extrapolating from current values using differing forecast differences.


# Validation

Normally for ML problems we use cross validation, where we randomly partition the data and then predict one partition using data from all the other partitions. The problem with this for time series is that this will involve using future data to predict the past, which will make for unrealistically good predictions.

Instead, we ca use **backtesting** where we predict a future time using a window of past times (e.g., predict Year 6 using Years 3-5, predict Year 5 using Years 2-4, predict Year 4 using Years 1-3).

For metrics, it's good to compare the evaluation metric to a **naive baseline model**, or an intentionally minimal extrapolation.


# Types of Models

- **Integrated model** - move model one step at a time, e.g., ARIMA, exponential smoothing - univariate
- **Forecast distance model** - predict fixed distances, e.g., XGB
- **Trend and decomposition model** - predict a different model for each distance, e.g., FB Prophet

## ARIMA

**Autoregressive process**: AR(p): fit coefficients to p lags

**Moving average process**: MA(q): fit coefficients to q previous errors

**ARMA model**: X = f(AR, MA)

**I(d)** = Differencing d times

**ARIMA(p, d, q)** = AR(p) + I(d) + MA(q)


# Multiseries

Predict a different time series for each unit (e.g., sales by store). Can use features across series (**cross series features**).
