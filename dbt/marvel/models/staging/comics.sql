{{ config(materialized='view') }}

select 

    -- identifier
    cast(id as text) as comics_id,
    cast(character_id as text) as character_id,

    -- comics info
    cast(title as text) as title,
    cast(description as text) as description,

    -- timestamps
    cast(modified_date as timestamp) as modified_date,

    -- comics info
    cast(number_of_pages as integer) as number_of_pages,
    cast(print_price as integer) as print_price,
    cast(digital_purchase_price as integer) as digital_purchase_price

from {{ source('staging', 'comics') }}
