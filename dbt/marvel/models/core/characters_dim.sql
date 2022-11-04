{{ config(materialized='table') }}

with dim as (
    select 
        * 
    from {{ ref('characters_fact') }}
)

select 
    -- Character with highest number of comics
    character_id,
    character_name,
    number_of_pages_per_comics,
    count(comics_id) as number_of_comics,
    sum(comics_print_price) as total_print_price,
    sum(comics_digital_purchase_price) as total_purchase_price
from dim
group by 1, 2, 3
order by 4 desc
