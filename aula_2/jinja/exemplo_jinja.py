import jinja2


string_template = """
Olá {{ nome }},

Sua senha expirou e teu computador vai esplodir se você não fizer nada. Clique no link abaicxo para ser hackeado:

{{ link }}
"""

template = jinja2.Template(string_template)
rendered_template = template.render({"nome": "Andre", "link": "http://caixaecnomica02.com.br"})

print(rendered_template)