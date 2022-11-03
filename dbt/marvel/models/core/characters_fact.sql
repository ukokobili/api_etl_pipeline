{{ config(materialized='table') }}

with characters as (
    select
        *
    from {{ ref('character') }}
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

events as (
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
    

from characters c
left join comics m 
on c.character_id = m.character_id
left join creators r 
on c.character_id = r.character_id
left join events e 
on c.character_id = e.character_id
left join series s 
on c.character_id = s.character_id
left join stories t 
on c.character_id = t.character_id



