

response = supabase.schema("app").table('meals').select("*").execute()
print(response)

