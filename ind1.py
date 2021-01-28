#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 5
# Написать программу, которая считывает текст из файла и выводит на
# экран только предложения, не содержащие запятых.

if __name__ == '__main__':
    with open('ind_1.txt', 'r') as f:
        text = f.read()

    sentences = text.split('.')
    del sentences[sentences.index('')]

    print([sentences for sentences in sentences if not "," in sentences])
