{{ config(materialized='view') }}

select 

    -- identifier
    cast(creators_id as text) as creators_id,
    cast(character_id as text) as character_id,

    -- creators info
    cast(creators as text) as creators_name,
    cast(creators_role as text) as creators_role

from {{ source('staging', 'events') }}
