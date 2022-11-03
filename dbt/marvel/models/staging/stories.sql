{{ config(materialized='view') }}

select 

    -- identifier
    cast(id as text) as stories_id,
    cast(character_id as text) as character_id,
    cast(comics_id as text) as comics_id,

    -- stories info
    cast(title as text) as title,
    cast(description as text) as description,

    -- timestamps
    cast(modified_date as timestamp) as modified_date,

    -- stories info
    cast(type as text) as type

from {{ source('staging', 'stories') }}
