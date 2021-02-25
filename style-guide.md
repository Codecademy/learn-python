# Codecademy Curriculum Python Style Guide 


## Comments

- There should be a space between the hashtag and the text for readability.
- Use multiple `#`s for multiline comments.
- To write a comment that , use `Output: `.

```py
print("Hello World!")
# Output: Hello World!
```

1. When the output is something short, e.g. one line, the output is either included immediately after the function/method call with some text like "Output: ..."
2. If that output extends beyond the length of the block, the comment can be included under the function/method call.

```py
console.log('hi'); // Prints: hi
```

```py
console.log('well now this is way longer...');
// Output: well now this is way longer...
```

2. If the output is more than a single line, typically, we'll show the code snippet (with syntax highlighting) that we're using. Followed by plain text that reads something like, "Which prints out:". And then some unstyled code snippet (like a bash terminal).

```py
console.log("
asd
```

This will print out:

```bash
This is like:
asdf
```

### Whitespace

<kbd>space</kbd> or <kbd>tab</kbd>? <kbd>spaces</kbd> ftw!

### Functions

Funcation names in the narrative use `()`, for example `say_name()`.

Mehtods use `.` in front of it. `.talk()`
Properties use `.` in front of it. `.count`

--- 

### To Be Determined...

- Do we capitalize the first word or not in a comment if it's a full sentence?
    - 👍 Yes: Sonny, Kenny, David, Sarai, Alex K, Alisha
    - 👎 No: Sophie, Jamie, Alex D, Cole, Chris, Carolyn

- Single vs Double Quotes in Python strings?
    - `"` Double: Alex K, Alex D, Sarai, Mariel, Cole, Adam
    - `'` Single: Alisha, David, Sophie, Jamie
