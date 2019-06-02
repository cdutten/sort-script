# Sort  script
Sorts a list of numbers with insertion sort 

### Usage

#### Without docker:
Run the script
Example:
```
$ python InsertionSort.py -v 10 9 8 7 6 5 4 3 2 1 0 33
```
#### With docker:
Create the docker
```
$ docker build -t sorting-script .
$ docker run -v /path/to/folder/of/the/project:/usr/src/app --name sort-scr sorting-script
$ python InsertionSort.py -v 10 9 8 7 6 5 4 3 2 1 0 33
```
Has a dockerfile if you don't want to install python locally but can be runned without using it.

### Trivia
I was learning with [Brilliant](https://brilliant.org/) in the course [Computer Science Fundamentals](https://www.google.com "Go, is a beatiful course.")

In the Quiz 3, of the Insertion Sort Module, I got stuck.
My only idea was make this script.
Possibly are a lot much easier ways to solve it, but this force me to think an practice coding  \O/.
