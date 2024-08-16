import json
import click
from jinja2 import Environment, FileSystemLoader

input_file = 'api_catalog.json'
output_file = 'index.html'

# @click.command()
# @click.option('-i', '--input', 'input_file', required=True, type=click.Path(exists=True), help='Input JSON file')
# @click.option('-o', '--output', 'output_file', required=True, type=click.Path(), help='Output HTML file')
def json_to_html():
    with open(input_file, 'r') as f:
        data = json.load(f)

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('./templates/catalog_template.html')
    html_content = template.render(data=data)

    with open(output_file, 'w') as f:
        f.write(html_content)

    click.echo(f'HTML file generated at {output_file}')

if __name__ == '__main__':
    json_to_html()