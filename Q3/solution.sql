select owner_id, owner_name, count(category_article_mapping.category_id) as different_category_count
from owner o, article a, category_article_mapping c
where a.owner_id = o.owner_id and a.category_id = c.category_id
group by o.owner_id
order by count(c.category_id) desc;
