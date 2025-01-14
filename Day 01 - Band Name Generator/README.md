# Day 1: Python Basics and My First Project  

Welcome to Day 1 of my journey through Angela Yu's *100 Days of Python* course! Today was all about laying a solid foundation with Python, starting with the essentials.

---

## What I Learned

1. **Printing Output:**
   - The `print()` function is used to display text or results.
   - Example:
     ```python
     print("Hello, World!")
     ```

2. **Debugging Basics:**
   - Identifying and fixing common syntax errors, like missing parentheses or typos.

3. **Combining Concepts in a Project:**
   - Applying new knowledge through hands-on practice.

---

## Project: Band Name Generator  
The highlight of Day 1 was creating my very first Python project: a **Band Name Generator**. This program takes user inputs and combines them to generate a unique band name. Here’s what it looks like:

### Code:
```python
print("Welcome to the Band Name Generator!")
city = input("What's the name of the city you grew up in?\n")
pet = input("What's the name of your pet?\n")
print("Your band name could be " + city + " " + pet)
```

### What I Learned from the Project:
- **Input Functions:** Collecting user input with `input()`.  
- **String Concatenation:** Combining strings to create a dynamic output.  

### Example Output:
```
Welcome to the Band Name Generator!
What's the name of the city you grew up in?
Springfield
What's the name of your pet?
Buddy
Your band name could be Springfield Buddy
```

---

## Reflections and Insights

### Additional Insights:
- I realized how powerful even the simplest code can be in creating interactive programs. It’s incredible to see how a few lines of code can produce something fun and engaging.
- The Band Name Generator also helped me see the importance of user input and how it opens up possibilities for personalization in programming.

### Challenges:
- **Formatting Issues:** Initially, I missed adding a space between the city and pet names in the output. I resolved this by double-checking string concatenation and adding a space explicitly: `city + " " + pet` and of course I wouldn't be me if I didn't miss one or two parenthesis' lol!

### Code Variations I Tried:
- Adding a greeting based on the time of day:
  ```python
  import datetime
  current_hour = datetime.datetime.now().hour
  if current_hour < 12:
      print("Good morning!")
  elif current_hour < 18:
      print("Good afternoon!")
  else:
      print("Good evening!")
  print("Welcome to the Band Name Generator!")
  ```

---

## Reflections

Starting with something so simple was a great way to build confidence. It was a reminder that even the smallest steps in programming can lead to creating something functional and fun.

I’m looking forward to building on this foundation and diving deeper into Python in the days to come. Stay tuned for more updates!

---

Thanks for following along on my journey! Feel free to share your thoughts and try the project yourself or you can [test out mine here](https://www.programiz.com/online-compiler/0EGjhGxVGkYQr)😊
