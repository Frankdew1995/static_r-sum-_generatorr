import json

from pathlib import Path

import os, shutil


def render_resume():

    resume_json = str(Path.cwd() / 'resume.json')

    with open(resume_json, "r") as f:

        data = f.read()

        resume_data = json.loads(data)

    return resume_data



def json2html(template_folder):

    data = render_resume()

    from jinja2 import Environment, FileSystemLoader

    env = Environment(loader=FileSystemLoader(template_folder))

    template = env.get_template("template.html")

    context = dict(
            name=data.get('name'),
            label=data.get('label'),
            basic=data.get('basic'),
            image=data.get('image'),
            summary=data.get('summary'),
            skills=data.get('skills'),
            socials=data.get('socials'),
            education=data.get('education'),
            languages=data.get('languages'),
            projects=data.get('projects'),
            work=data.get('work')
    )

    html = template.render(context)

    html_file = open(str(Path.cwd() / 'public' / 'index.html'), "w")

    html_file.write(html)
    html_file.close()

    try:

        shutil.rmtree(str(Path.cwd() / 'public' / 'assets'))

    except Exception as e:

        print(str(e))

    shutil.copytree(str(Path.cwd() / 'assets'), str(Path.cwd() / 'public' / 'assets'))


json2html(template_folder=str(Path.cwd()))
