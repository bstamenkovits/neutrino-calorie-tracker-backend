create table app.ingredients (
    -- columns
    id uuid not null,
    category_id uuid null,
    added_by_user_id uuid null,

    name text not null,
    calories_kcal double precision null,
    fat_g double precision null,
    carbs_g double precision null,
    protein_g double precision null,


    -- primary & foreign keys
    constraint ingredients_pkey_id primary key (id),
    constraint ingredients_fkey_category_id foreign key (category_id) references app.ingredients_categories (id) on update CASCADE on delete CASCADE,
    constraint ingredients_fkey_added_by_user_id foreign key (added_by_user_id) references auth.users (id) on update CASCADE on delete CASCADE,

    -- check valid nutritional values
    constraint ingredients_chk_calories_kcal check (calories_kcal >= 0.0),
    constraint ingredients_chk_fat_g check (fat_g >= 0.0),
    constraint ingredients_chk_carbs_g check (carbs_g >= 0.0),
    constraint ingredients_chk_protein_g check (protein_g >= 0.0)

) TABLESPACE pg_default;


-- Enable RLS
alter table app.ingredients enable row level security;


-- Create RLS policies
create policy "Allow authenticated users to read ingredients"
on app.ingredients
for select
to authenticated
using (true); -- Replace 'true' with your actual conditions if users should only see their own meals

create policy "Allow authenticated users to insert ingredients"
on app.ingredients
for insert
to authenticated
with check (true);