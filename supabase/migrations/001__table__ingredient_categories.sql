create table app.ingredient_categories (
    id uuid not null,
    name text not null,
    date_created timestamp with time zone not null,
    date_modified timestamp with time zone not null,
    constraint ingredients_categories_pkey_id primary key (id)
) TABLESPACE pg_default;


-- Enable RLS
alter table app.ingredient_categories enable row level security;


-- Create RLS policies
create policy "Allow authenticated users to read ingredients_categories"
on app.ingredient_categories
for select
to authenticated
using (true); -- Replace 'true' with your actual conditions if users should only see their own meals

create policy "Allow authenticated users to insert ingredients_categories"
on app.ingredient_categories
for insert
to authenticated
with check (true);