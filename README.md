passwordgen
===========

Generate secure and easy to type passwords.

The passwords have no more than two consecutive characters from the same
side of the keyboard, and no capitalized characters, which makes them relatively
easy to type.

passwordgen also calculates the strength of your password. A password with 8
characters (the default) has 42 bits of entropy, which means that it will take
70 years for someone who can check a thousand passwords every second 
to find your password, given that he knows that you used passwordgen.

Passwords are created using the operating system random source (os.urandom).
