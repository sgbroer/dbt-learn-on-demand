#from bigframes.ml.linear_model import LinearRegression
import sklearn
import pandas

def model(dbt, session):

    dbt.config(
        materialized="table",
        packages=['sklearn', 'pandas']
    )

    customers_df = dbt.ref('int_customers').to_pandas()

    regression = sklearn.linear_model.LinearRegression()
    regression.fit(customers_df['customer_id'], customers_df['lifetime_value'])

    customers_df['predicted_ltv'] = customers_df['customer_id'] * regression.coef_

    final_df = customers_df.drop(['lifetime_value'])

    return final_df

