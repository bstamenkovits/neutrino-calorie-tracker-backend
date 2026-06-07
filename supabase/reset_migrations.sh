#!/bin/zsh

echo "Resetting Migrations..."

supabase migration repair --status reverted 000
supabase migration repair --status reverted 001
supabase migration repair --status reverted 002
supabase migration repair --status reverted 003
supabase migration repair --status reverted 004
supabase migration repair --status reverted 005

echo "All done!"