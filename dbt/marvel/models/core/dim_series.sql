{{ config(materialized='table') }}

select *

from {{ ref('series')}}

