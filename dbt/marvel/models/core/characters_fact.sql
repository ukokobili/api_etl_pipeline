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
),

creators as (
    select
        * 
    from {{ ref('creators') }}
),

events as (
    select
        *
    from {{ ref('events') }}
),

series as (
    select
        * 
    from {{ ref('series_table') }}
),

stories as (
    select
        * 
    from {{ ref('stories') }}
)

select 
    c.character_id,
    m.comics_id,
    r.creators_id,
    c.name as character_name,
    e.events_id,
    s.series_id,
    t.stories_id,
    c.description as character_description,
    c.modified_date as character_modified_date,
    m.print_price as comics_print_price,  
    m.digital_purchase_price as comics_digital_purchase_price,
    m.number_of_pages
from characters as c
left join comics as m 
on c.character_id = m.character_id
left join creators as r 
on c.character_id = r.character_id
left join events as e 
on c.character_id = e.character_id
left join series as s 
on c.character_id = s.character_id
left join stories as t 
on c.character_id = t.character_id



