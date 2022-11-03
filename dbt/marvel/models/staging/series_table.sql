{{ config(materialized='view') }}

select 
-- identifier
cast(id as text) as series_id,
cast(character_id as text) as character_id,
cast(comics_id as text) as comics_id,

-- series info
cast(title as text) as title,
cast(description as text) as description,

-- timestamps
modified_date,

-- series info
cast(start_year as integer) as start_year,
cast(end_year as integer) as end_year,
cast(rating as text) as rating,
cast(type as text) as type

from {{ ref('series')}}

