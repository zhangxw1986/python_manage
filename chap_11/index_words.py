#! /usr/bin/env python
# -*- coding:utf-8 -*-


def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, value in enumerate(text, 1):
        if value == ' ':
            result.append(index)
    return result


def g_index_words(text):
    'print the  location of every word'
    if text:
        yield 0
    for index, value in enumerate(text, 1):
        if value == ' ':
            yield index


if __name__ == "__main__":
    text = 'The Zen of Python, by Tim Peters'
    result = index_words(text)
    print(result)

    print(list(g_index_words(text)))
    print(g_index_words.__doc__)
    print(g_index_words.__name__)
