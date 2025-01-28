# Curriculum Vitae

Automatic Curriculum Vitae generation

- [Curriculum Vitae](#curriculum-vitae)
	- [My Resume](#my-resume)
	- [Project goals](#project-goals)
	- [Dependencies](#dependencies)
	- [Installation](#installation)
	- [Build Resume](#build-resume)
	- [Dev :](#dev-)

## My Resume

![CV Louis DEVELLE](resume/out/png/latest.png)

## Project goals

 - ✔️ A place where I can store a detailled memory of each position
 - ✔️ A tool which automatically generate an updated general resume from them
 - 🚧 A tool which helps me to tailor my resume for a given position
   - Changing the accroche
   - Selecting which positions to display
   - For a position, selecting individual elements to display from :
     - accomplishments
     - responsabilities
     - technologies


## Dependencies

For this project you need to have isntalled:

 - `docker`
 - `uv`


## Installation


```sh
uv venv
source .venv/bin/activate
uv sync
```


## Build Resume

```sh
./build_it.sh CV_name
```



## Dev :

Update requriements :

```sh
rm requirements.txt
uv pip compile pyproject.toml -o requirements.txt
```
