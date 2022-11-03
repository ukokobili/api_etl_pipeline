{{ config(materialized='view') }}

select 

    -- identifier
    cast(id as text) as events_id,
    cast(character_id as text) as character_id,

    -- events info
    cast(title as text) as title,
    cast(description as text) as description,

    -- timestamps
    cast(started as timestamp) as start_date,
    cast(ended as timestamp) as end_date

from {{ source('staging', 'events') }}

