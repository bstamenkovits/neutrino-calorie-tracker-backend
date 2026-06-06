create table app.servings (
    -- columns
    id uuid not null,
    name text not null,
    size_g double precision null,
    ingredient_id uuid not null,

    -- primary and foreign keys
    constraint servings_pkey_id primary key (id),
    constraint servings_fkey_ingredient_id foreign key (ingredient_id) references app.ingredients (id) on update CASCADE on delete CASCADE,

    -- data checks
    constraint servings_chk_size_g check (size_g > 0)
) TABLESPACE pg_default;



-- Enable RLS
alter table app.servings enable row level security;

-- Create RLS policies
create policy "Allow authenticated users to read servings"
on app.servings
for select
to authenticated
using (true); -- Replace 'true' with your actual conditions if users should only see their own meals

create policy "Allow authenticated users to insert servings"
on app.servings
for insert
to authenticated
with check (true);