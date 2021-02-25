# Codecademy Curriculum Python Style Guide 


## Comments

- There should be a space between the hashtag and the text.
- Use multiple `#`s for multiline comments.
- To write a comment that , use `Output: `.

```py
print("Hello World!")
# Output: Hello World!
```

1. When the output is something short, e.g. 1 line, the output is either included immediately after the function/method call with some text like "Output: ..."
2. If that output extends beyond the length of the block, the comment can be included under the function/method call.
js
console.log('hi'); // Prints: hi
js
console.log('well now this is way longer...');
// Prints: well now this is way longer...

2. If the output is more than a single line, typically, we'll show the code snippet (with syntax highlighting) that we're using. Followed by plain text that reads something like, "Which prints out:". And then some unstyled code snippet (like a bash terminal). See 2nd pic:

### Whitespace

<kbd>space</kbd> or <kbd>tab</kbd>? <kbd>spaces</kbd> ftw!

### Functions

Funcation names in the narrative use `()`, for example `say_name()`.

Mehtods use `.` in front of it. `.talk()`
Properties use `.` in front of it. `.count`

### To Be Determined...

- Do we capitalize the first word or not?
    - 👍 Yes: Sarai, Alisha, Alex K, David, Sonny, Kenny
    - 👎 No: Jamie, Cole, Chris, Alex D, Sophie, Carolyn

- Single vs Double Quotes in Strings?
    - `"` Double: Alex K, Alex D, COle, Sarai, Adam, Mariel
    - `'` Single: Alisha, David, Sophie, Jamie
