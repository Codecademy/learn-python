# Codecademy Curriculum Python Style Guide 


## Comments

- There should be a space between the hashtag and the text for readability.
- Use multiple `#`s for multiline comments.
- When the output is something short, e.g. one line, the output is either included immediately after the function/method call with some text like "`Output: ...`". If that output extends beyond the length of the block, the comment can be included under the function/method call.

```py
print("Hi")  # Output: Hi
```

Or:

```py
print("Hello World!")
# Output: Hello World!
```

- If the output is more than a single line, typically, we'll show the code snippet (with syntax highlighting) that we're using. Followed by plain text that reads something like, "Which prints out:". And then some unstyled code snippet (like a bash terminal).

```py
print(string1 + string2 + ".")
print(string3 + ".")
```

This will print out:

```bash
Hello goodbye.
Blah.
```

### Whitespace

<kbd>space</kbd> or <kbd>tab</kbd>? Team <kbd>spaces</kbd>!

### Names

- For functions, use `()` after the function name. For example, `say_name()`.
- For mehtods, use `.` in front of the method name. For example, `.talk()`.
- For properties, use `.` in front of the property name. For example, `.count`.

--- 

### To Be Determined...

- Do we capitalize the first word or not in a comment if it's a full sentence?
    - 👍 Yes: Sonny, Kenny, David, Sarai, Alex K, Alisha
    - 👎 No: Sophie, Jamie, Alex D, Cole, Chris, Carolyn

- Single vs Double Quotes in Python strings?
    - `"` Double: Alex K, Alex D, Sarai, Mariel, Cole, Adam
    - `'` Single: Alisha, David, Sophie, Jamie
