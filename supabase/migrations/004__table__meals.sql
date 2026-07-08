-- Create table
create table app.meals (
    id uuid not null default gen_random_uuid(),
    name text not null,

    constraint meals_pkey_id primary key (id)
) TABLESPACE pg_default;



-- Enable RLS
alter table app.meals enable row level security;


-- Create RLS policies
create policy "Allow authenticated users to read meals"
on app.meals
for select
to authenticated
using (true); -- Replace 'true' with your actual conditions if users should only see their own meals
