create view app.food_summary with (security_invoker = on) as (
    select
        fl.consumed_on as date,
        m.name as meal_name,
        i.name as name,
        fl.quantity as quantity,
        s.name as serving_name,
        s.size_g * fl.quantity as total_weight_g,
        (s.size_g * fl.quantity) * i.calories_kcal/100 as total_calories_kcal,
        (s.size_g * fl.quantity) * i.protein_g/100 as total_protein_g,
        (s.size_g * fl.quantity) * i.carbs_g/100 as total_carbs_g,
        (s.size_g * fl.quantity) * i.fat_g/100 as total_fat_g
    from app.food_logs as fl

    left join app.meals as m
        on fl.meal_id = m.id

    left join app.ingredients as i
        on fl.ingredient_id = i.id

    left join app.servings as s
        on fl.serving_id = s.id
)
