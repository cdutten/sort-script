 Sort  script
Sorts a list of numbers with insertion sort algorithm

### Usage

#### Without docker:
Run the script
Example:
```
$ python InsertionSort.py 10 9 8 7 6 5 4 3 2 1 0 33

// Expected return: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 33]

```
#### With docker:
Create the docker
```
$ docker build -t sorting-script .
$ docker run -v /path/to/folder/of/the/project:/usr/src/app --name sort-scr sorting-script
```

Get inside the container with
```
$ docker exec -ti sort-scr bash
```

### Trivia
I was learning with [Brilliant](https://brilliant.org/) in the course [Computer Science Fundamentals](https://www.google.com "Go, is a beautiful course.")

In the Quiz 3, of the Insertion Sort Module, I got stuck.
My only idea was make this script.
Possibly are a lot much easier ways to solve it, but why not practice coding? ¯\\\_\(ツ\)\_\/¯. 
