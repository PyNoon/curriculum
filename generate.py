from pathlib import Path
import re
import subprocess

base_url = 'https://pynoon.github.io/curriculum'
raw_repo_url = 'https://raw.githubusercontent.com/pynoon/curriculum/main'
colab_url = 'https://colab.research.google.com/github/pynoon/curriculum/blob/main'
curriculum_dir = Path(__file__).parent

def main():
    index_markdown = f'''
# PyNoon Curriculum

Slides and tutorials for PyNoon.

## Lesson Guide for instructors

### Before the Lesson

1. Print out the **Tutorial Speaker Notes** for the lesson so that you can read from them as you type code in a notebook
2. Familiarise yourself with the slides and speaker notes for the lesson
   * Practising the material, even by yourself, helps build confidence in the flow of the lesson!

### Slides

1. From the start of the lesson, have the initial "Get ready" or "Warm-Up Exercise" slide in the lesson's slide deck displayed on the screen.
   * Disable auto-sleep on your machine so the slides stay up even when you're not moving the mouse
   * Turn off notifications on your machine
2. Once all attendees have arrived, continue through the administration slides in the slide deck
   * For the first lesson of any course, there is a [special set of introduction slides]({base_url}/introduction/pynoon_introduction.pdf)
3. If there is a **Lunch Talk** (or **DEMO-ONLY** portion of the tutorial), present that during the lunch time (usually during the last 15 minutes of the break)

### Tutorial

1. After the lunch time, show the **Tutorial Objectives** slide to outline the material that the tutorial will cover
2. Open up an empty Colab notebook on your screen
   * Zoom-in on Colab to ensure the font is big enough for all attendees to see
   * Bring up the bottom of your browser window if it won't be visible from all seats
3. Direct all attendees to also open an empty notebook by following the **`Colab Notebooks`** link on [pynoon.github.io](https://pynoon.github.io)
4. Work through the **Tutorial Speaker Notes** for the lesson
   * Have the speaker notes printed out ahead of time
   * Read out (or paraphrase) written material
   * Demonstrate each code example in a new cell in your notebook
   * Have attendees type along and run code with you, and regularly check if anyone needs assistance from a helper

### Exercise and self-directed learning

1. After the tutorial, present the **Independent Work/Homework** slide
2. Direct attendees to [pynoon.github.io/lessons](https://pynoon.github.io/lessons/) to find the lesson's slides, tutorial notebook, and exercise notebook
3. Also offer to help with any other course-related problems that attendees may have - such as from applying what they've learned in their job

### Assets

* [PyNoon logo](https://pynoon.github.io/_images/cooper.svg)
* [HTML Template for lanyards](https://pynoon.github.io/static_files/lanyards.html)
* [Poster to blu-tack up and direct attendees to the room](https://pynoon.github.io/static_files/pynoon_poster.svg) ([source](https://pynoon.github.io/static_files/pynoon_poster.odg))
  * Useful to put in foyers and outside lifts
  * Laminating them is optional but can be useful. Also makes it easy to write extra information on them in whiteboard pen if required.
* Find more tips for presenting from [Software Carpentry](https://carpentries.github.io/instructor-training/instructor/17-live.html#top-ten-tips-for-participatory-live-coding-in-a-workshop)

## Introduction

[Slides to present at the start of the first session of a course]({base_url}/introduction/pynoon_introduction.pdf)
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
