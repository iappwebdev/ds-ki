---
myst:
  substitutions:
    key1: "I'm a **substitution**"
    key2: |
      ```{note}
      {{ key1 }}
      ```
    fishy: |
      ```{image} img/fun-fish.png
      :alt: fishy
      :width: 200px
      ```
---

# Test Definition List

Term 1
: Definition for Term 1

Term 2
: Another definition

Inline: {{ key1 }}

Block level:

{{ key2 }}