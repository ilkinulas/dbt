from dataclasses import dataclass

from hologram import JsonSchemaMixin

DEFAULT_QUERY_COMMENT = '''
{%- set comment_dict = {} -%}
{%- do comment_dict.update(
    app='dbt',
    dbt_version=dbt_version,
    profile_name=target.get('profile_name'),
    target_name=target.get('target_name'),
) -%}
{%- if node is not none -%}
  {%- do comment_dict.update(
    node_id=node.unique_id,
  ) -%}
{% else %}
  {# in the node context, the connection name is the node_id #}
  {%- do comment_dict.update(connection_name=connection_name) -%}
{%- endif -%}
{{ return(tojson(comment_dict)) }}
'''


@dataclass
class QueryComment(JsonSchemaMixin):
    comment: str = DEFAULT_QUERY_COMMENT
    append: bool = False
