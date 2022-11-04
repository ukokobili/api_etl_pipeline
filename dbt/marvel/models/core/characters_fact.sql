{{ config(materialized='table') }}

with characters as (
    select
        *
    from {{ ref('characters') }}
),

comics as (
    select
        * 
    from {{ ref('comics') }}
)

select 
    c.character_id,
    m.comics_id,
    c.name as character_name,
    m.title as comics_title,
    m.print_price as comics_print_price,
    m.digital_purchase_price as comics_digital_purchase_price,
    m.number_of_pages as number_of_pages_per_comics
from characters as c
inner join comics as m 
on c.character_id = m.character_id




