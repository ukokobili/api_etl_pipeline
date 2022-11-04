{{ config(materialized='table') }}

with dim as (
    select 
        * 
    from {{ ref('characters_fact') }}
)

select 
    -- Comics Revenue Calculations
    character_id,
    character_name,
    avg(comics_print_price)  as avg_comics_print_price,
    avg(comics_digital_purchase_price) as avg_comics_digital_purchase_price,
    (comics_digital_purchase_price - comics_print_price) as comics_profit_loss,
    count(comics_id) as number_of_comics,
    avg(number_of_pages) as avg_number_of_pages_per_comics
from dim
group by 1, 2, 5