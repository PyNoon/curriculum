from pathlib import Path
import re
import subprocess

base_url = 'https://pynoon.github.io/curriculum'
raw_repo_url = 'https://raw.githubusercontent.com/pynoon/curriculum/main'
colab_url = 'https://colab.research.google.com/github/pynoon/curriculum/blob/main'
curriculum_dir = Path(__file__).parent

def main():
    index_markdown = '''
# PyNoon Curriculum

Slides and tutorials for PyNoon.

## Tips for instructors

* [Software Carpentry instructor tips](https://carpentries.github.io/instructor-training/instructor/17-live.html#top-ten-tips-for-participatory-live-coding-in-a-workshop)
* Ensure font is big enough
  * In JupyterLite -> View -> Presentation Mode
* Draw up bottom of browser window if it won't be visible from all seats
* Turn off notifications
* Have a print-out of the course content so that you don't have to
  bring it up on your screen
* Give sticky notes to learners
  * "Completed last task" note
  * "I'm stuck" note

## Notebook Outputs

(The instructions in this section are for course authors only, you can
ignore these instructions if you are a learner using these notebooks.)

When updating the notebooks in this repo that are shared with
learners, you should not commit the outputs of notebook cells to your
Git repository. If you have Python 3 installed, you can use
[nbstripout](https://github.com/kynan/nbstripout) to configure your
Git repository to exclude the outputs of notebook cells when running
`git add`:

1. `python3 -m pip install nbstripout nbconvert`
2. Run `nbstripout --install` in this directory (installs hooks into
   `.git`).

## Introduction

[Slides to present at the start of each course]({base_url}/introduction/pynoon_introduction.pdf)
'''

    for course in ['starter', 'data', 'plus']:
        index_markdown += f'''
## PyNoon {course.capitalize()}
'''
        lesson_dirs = sorted([
            child for child in curriculum_dir.iterdir()
            if (
                    child.is_dir()
                    and child.name.startswith(f'lesson_{course}_')
                    and not child.name.startswith('.')
            )
        ])

        for lesson_dir in lesson_dirs:
            lesson_links = []
            notebook_paths = []

            if (lesson_dir / 'slides.md').exists():
                subprocess.run([
                    'pandoc',
                    '-s', '-t', 'revealjs',
                    '--template', str(curriculum_dir / 'revealjs' / 'pandoc.html'),
                    '-o', str(lesson_dir / 'slides.html'),
                    str(lesson_dir / 'slides.md'),
                    '-V', 'revealjs-url=../revealjs',
                ], check=True)
                lesson_links.append(f'[Slides]({base_url}/{lesson_dir.name}/slides.html)')

            if (lesson_dir / 'tutorial.md').exists():
                subprocess.run([
                    'pandoc',
                    '-s', '--embed-resources',
                    '--css', str(curriculum_dir / 'revealjs' / 'tutorial.css'),
                    '-o', str(lesson_dir / 'tutorial_speaker_notes.html'),
                    str(lesson_dir / 'tutorial.md'),
                ], check=True)
                lesson_links.append(f'[Tutorial Speaker Notes]({base_url}/{lesson_dir.name}/tutorial_speaker_notes.html)')

                tutorial_notebook_path = str(lesson_dir / f'{lesson_dir.name}_tutorial.ipynb')
                subprocess.run([
                    'pandoc', '-s',
                    '-o', tutorial_notebook_path,
                    str(lesson_dir / 'tutorial.md'),
                ], check=True)
                lesson_links.append(f'[Tutorial Notebook]({colab_url}/{lesson_dir.name}/{lesson_dir.name}_tutorial.ipynb)')
                notebook_paths.append(tutorial_notebook_path)

            if (lesson_dir / 'exercise.md').exists():
                exercise_notebook_path = str(lesson_dir / f'{lesson_dir.name}_exercise.ipynb')
                subprocess.run([
                    'pandoc', '-s',
                    '-o', exercise_notebook_path,
                    str(lesson_dir / 'exercise.md'),
                ], check=True)
                lesson_links.append(f'[Exercise Notebook]({colab_url}/{lesson_dir.name}/{lesson_dir.name}_exercise.ipynb)')
                notebook_paths.append(exercise_notebook_path)

            # Quick fix for `"execution_count": null` that JupyterLite doesn't like.
            for notebook_path in notebook_paths:
                subprocess.run([
                    f'''jq '.cells[] |= if has("execution_count") then .execution_count = 0 else . end' {notebook_path} > {notebook_path}.tmp && mv {notebook_path}.tmp {notebook_path}''',
                ], check=True, shell=True)

            lesson_link_bullets = '\n'.join([f'* {lesson_link}' for lesson_link in lesson_links])
            index_markdown += f'''
### {lesson_dir.name.replace('_', ' ').title()}

{lesson_link_bullets}
'''

    with Path(curriculum_dir / 'README.md').open('w') as readme_file:
        readme_file.write(index_markdown.strip())


if __name__ == '__main__':
    main()
