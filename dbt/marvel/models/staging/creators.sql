{{ config(materialized='view') }}

select 

    -- identifier
    cast(creators_id as integer) as creators_id,
    cast(character_id as integer) as character_id,

    -- creators info
    cast(creators as text) as creators_name,
    cast(creators_role as text) as creators_role

from {{ source('staging', 'events') }}
