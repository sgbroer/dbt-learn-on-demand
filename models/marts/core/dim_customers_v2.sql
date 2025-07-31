with customers as (
    select * from {{ ref('int_customers')}}
),

final as (

    select 
        customer_id,
        first_order_date,
        most_recent_order_date,
        number_of_orders,
        lifetime_value,
        lifetime_value / number_of_orders as average_order_amount
    from customers

)

select * from final