# Tuple Exercises 1
## Fork the repo!
Make sure to make a fork of this repository before starting!

## Tuple Access
**Complete the following exercises using the Python interpreter and record your answers in this file (you can edit in GitHub directly or in a local clone).**

```my_tuple = (1, 2, “kitten”,  4, “five”)```

1. How would I access the third element in the tuple? 

2. How would I access the element at the third index? 

3. What would I get if I did `my_tuple[1]`?


4. What are **three ways** I could access the last element of the tuple?<br>
(HINT: Look up the `len` method for Python tuples.)

my_tuple[4]
my_tuple[len(my_tuple)-1]
my_tuple[-1]

5. How would I find the length of the tuple?

len(my_tuple)

6. How would I update `my_tuple` to hold a new tuple that consists of the values of `my_tuple` plus the number 6 at the end? (Hint: look through the tuple lecture slides)

my_tuple = my_tuple + (6,)
print my_tuple

7. Use the tuple below to complete the following table (the first one is done for you):

```my_tuple = (1, 2, “kitten”,  4, “five”, 6, 7)```

| Access | Value |
|---------|----------|
| my_tuple[0]     | 1 |
| my_tuple[2:3]   | 'kitten',|
| my_tuple[1:5]   | 2, 'kitten', 4, 'five'|
| my_tuple[1:10]  | 2, 'kitten', 4, 'five', 6, 7|
| my_tuple[-1]    | 7|
| my_tuple[-1:-4] |()|
| my_tuple[-4:]   |4, 'five', 6, 7|
