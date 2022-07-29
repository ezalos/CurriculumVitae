# Curriculum Vitae

Automatic Curriculum Vitae generation

- [Curriculum Vitae](#curriculum-vitae)
	- [My Resume](#my-resume)
	- [Project goals](#project-goals)
	- [Dependencies](#dependencies)
	- [Installation](#installation)
	- [Build](#build)

## My Resume

![CV Louis DEVELLE](CV_Louis_DEVELLE.png)

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
 - `conda`


## Installation


Optional step for conda + direnv combo:
```sh
echo "eval \"\$(conda shell.bash hook)\"" > .envrc
echo "conda activate resume" > .envrc
direnv allow
```

Env creation:
```sh
conda env create --file environment.yml
conda activate resume
```


## Build

```sh
./build_it.sh CV_name
```
