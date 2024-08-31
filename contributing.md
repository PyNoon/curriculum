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
