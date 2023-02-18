# Welcome to MkDocs (README.md)

## Commands:
* `mkdocs new [dir-name]` - Create a new project
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site
* `mkdocs -h` - Print help message and exit

## Project layout:
    
    mkdocs.yml      # The configuration file.
    docs/
        index.md    # The documentation homepage.
        ...         # Other markdown pages, images and other files


## Start create MkDocs
- `mkdocs new .` - create new mkdocs.yml file
- `mkdocs serve` - run server

## Build site files
- `mkdocs build`

## GitHub Actions using:
1. Create file path:
   - .github/workflow/ci.yml
2. Write in ci.yml file:
```yaml
name: ci

on:
  push:
    branches:
      - master

permissions:
  contents: write

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: 3.9
#      - uses: actions/cache@v2
#        with:
#          key: ${{ github.ref }}
#          path: .cache
      - run: pip install mkdocs-material
      - run: mkdocs gh-deploy --force
```
