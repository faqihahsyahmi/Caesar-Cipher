# Caesar Cipher with Python

## A functional sample project fully written in Python

A simple Python-based Caesar Cipher program that allows users to encode or decode messages using a classic letter-shifting technique.

Let's get started!

## How it works
* The **Caesar Cipher** is a type of substitution cipher in which each letter in the message is **shifted a certain number of positions** down or up the alphabet.

## It has the following features:

* User can choose whether to **encode** or **decode** a message.
* User specifies the **shift number** for the cipher.
* Supports **repeated use**: the program will continue to prompt for input until the user decides to exit by typing `no` / `No` / `NO`.


## Weakness:

* Leaves numbers, spaces, and punctuation **unchanged**.


## Versioning
* 1.0: original simple program - user can only perform encode message.
* 1.1: user can only do decode message as only got decode function to call.
* 1.2: user can do both encode and decode message
* 1.3: add Caesar Cipher art logo (import form art.py)
* 1.4: combine function for encode and decode message (but decode function got issue);
        - encode: ayam -> caco
        - decode: caco -> acaq (expected "ayam")
* 1.5: user can input numbers and spaces
        - e.g. ayam kicap 123
            encoded: caco mkecr 123
            decoded: still got issue
* 1.6: both encode and decode functions working as expected. Have restart logic - `yes` to continue, `no` to exit the program...
