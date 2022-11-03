{{ config(materialized='view') }}

select 

    -- identifier
    cast(id as integer) as character_id,

    -- character info
    cast(name as text) as name,
    cast(description as text) as description,

    -- timestamps
    cast(modified_date as timestamp) as modified_date

from {{ source('staging', 'characters') }}

