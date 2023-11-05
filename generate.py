from pathlib import Path
import re
import subprocess

base_url = 'https://pynoon.github.io/curriculum'
curriculum_dir = Path(__file__).parent

def main():
    week_dirs = [
        child for child in curriculum_dir.iterdir()
        if (
                child.is_dir()
                and child.name not in ['template', 'revealjs']
                and not child.name.startswith('.')
        )
    ]

    index_markdown = '''
# PyNoon Curriculum

Weekly slides and tutorials for PyNoon.

## Tips for instructors

* [Software Carpentry instructor tips](https://carpentries.github.io/instructor-training/instructor/17-live.html#top-ten-tips-for-participatory-live-coding-in-a-workshop)
* Ensure font is big enough
  * In Jupyterlite -> View -> Presentation Mode
* Draw up bottom of browser window if it won't be visible from all seats
* Turn off notifications
* Have a print-out of the course content so that you don't have to
  bring it up on your screen
* Give sticky notes to learners
  * "Completed last task" note
  * "I'm stuck" note
    '''

    for week_dir in week_dirs:
        subprocess.run([
            'pandoc',
            '-s', '-t', 'revealjs',
            '--template', str(curriculum_dir / 'revealjs' / 'pandoc.html'),
            '-o', str(week_dir / 'slides.html'),
            str(week_dir / 'slides.md'),
            '-V', 'revealjs-url=../revealjs',
        ])
        subprocess.run([
            'pandoc',
            '-o', str(week_dir / 'tutorial.html'),
            str(week_dir / 'tutorial.md'),
        ])
        index_markdown += f'''
## {week_dir.name.capitalize().replace('_', ' ')}

* [Tutorial]({base_url}/{week_dir.name}/tutorial.html)
* [Slides]({base_url}/{week_dir.name}/slides.html)
        '''

    with Path(curriculum_dir / 'README.md').open('w') as readme_file:
        readme_file.write(index_markdown.strip())


if __name__ == '__main__':
    main()
