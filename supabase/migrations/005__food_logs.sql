create table app.food_logs (
    -- columns
    id uuid not null,
    user_id uuid null,
    date_added timestamp with time zone not null,
    meal_id uuid null,
    ingredient_id uuid null,
    serving_id uuid null,
    quantity double precision not null,

    -- primary and foreign keys
    constraint food_logs_pkey_id primary key (id),
    constraint food_logs_fkey_ingredient_id foreign key (ingredient_id) references app.ingredients (id) on update CASCADE on delete CASCADE,
    constraint food_logs_fkey_meal_id foreign key (meal_id) references app.meals (id) on update CASCADE on delete CASCADE,
    constraint food_logs_fkey_serving_id foreign key (serving_id) references app.servings (id) on update CASCADE on delete CASCADE,
    constraint food_logs_fkey_user_id foreign key (user_id) references auth.users (id) on update CASCADE on delete CASCADE
) TABLESPACE pg_default;


-- Enable RLS
alter table app.food_logs enable row level security;


-- Create RLS policies
create policy "Allow users to read their own food_logs"
on app.food_logs
for select
to authenticated
using (auth.uid() = user_id);

create policy "Allow users to insert their own food_logs"
on app.food_logs
for insert
to authenticated
with check (auth.uid() = user_id);

create policy "Allow users to update their own food_logs"
on app.food_logs
for update
to authenticated
using (auth.uid() = user_id)
with check (auth.uid() = user_id);

create policy "Allow users to delete their own food_logs"
on app.food_logs
for delete
to authenticated
using (auth.uid() = user_id);
