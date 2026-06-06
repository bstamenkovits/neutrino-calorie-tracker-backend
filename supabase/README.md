# Supabase Migrations
For managing the supabase database (schema definition, table creation, etc.) the supabase cli is used. 

## Installation
On MacOS the Supabase CLI can be installed using homebrew (https://formulae.brew.sh/formula/supabase). Run the following command in the terminal:

```bash
brew install supabase
```

## Update Database
To run a migration, add a new .sql file to the `supabase/migrations` directory. Make sure it starts with the same numbering scheme as chosen for the other scripts, and make sure it is ascending. Then simply run

```bash
supabase db push
```

## Reset Database
To completely reset the database, first remove each individual migration first. For example:

```bash
supabase migration repair --status reverted 000                                                                          
supabase migration repair --status reverted 001
supabase migration repair --status reverted 002
supabase migration repair --status reverted 003
supabase migration repair --status reverted 004
supabase migration repair --status reverted 005
```

Then run a new migration.

```bash 
supabase db push
```

The 000 migration drops the entire schema and sets up the RLS policies a new. So no need to manually drop anything. 