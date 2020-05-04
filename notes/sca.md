#Timing Side-Channels
##Author: Edward Krawczyk

### Side-Channels

We are now going to explore a different class of exploits, called side-channel attacks.
Like before, we try to leverage a flaw in the implementation of a program. Unlike the previous
attacks that have been covered, we often do not seek to redirect program execution. Now, we usually have
a different goal: we only
aim to recover information that we are not supposed to have access to. While this sounds
pretty useless (what's the point of an attack if you can't pop a shell or get root access?)
it can lead to catastrophic data breaches. For example, your web traffic (when using HTTPS)
is encrypted with a secret key. This prevents any third party from snooping on you. If this
secret key is leaked, though, anybody can decrypt your web traffic.

Side-channel attacks do not use any form of binary exploitation to accomplish this.
These attacks do not directly try and read
out information from a program (like we might do with a format string vulnerability). Instead they try and obtain information
\textit{related} to the data they want. This is an odd concept, so we
begin with an example.

The classic analogy is a poker face. When you play poker, you do not know the
cards your competitor has in their hand. You want to know what cards they have,
though, so you can determine if your hand is better than theirs. You obviously
cannot look at their hand, so what can you do? Well, perhaps you can examine
their facial expression, or body language. If they have a good hand, they might
appear confident, while a bad hand might cause them to look a little nervous.
Of course, they might also have a good poker face, but we're going to ignore
that.

Reading an opponent's face is a side-channel attack. Instead of directly
determining what cards they have, you determine information *about* those
cards: whether they form a good or bad hand. We call the medium used
to obtain this information a \textit{side-channel}. Here, the face is a
side-channel. Formally, a side-channel leakage is an unintended source of information *about* some
secret. This secret may be a password, encryption key, or PIN. The medium that
the information is leaked through is the side-channel

Now, we will examine side-channel attacks on software, in the case where
the side-channel is time. There are other side-channels that can be exploited
to attack software, notably caches. We will not discuss these here. 

### An example attack

An *timing* side-channel attack assumes that the time that is consumed to perform a task
leaks information about the data that task is being performed on. Consider a simple bit of code that
checks if a password is correct:

```
int password_checker (char* input_pass, char* saved_pass) {
	for (int i = 0; i < PASS_LEN; i++) {
		if (input_pass[i] != saved_pass[i])
			return BAD_PASS; // short circuit for efficiency!
	}
	return GOOD_PASS;
}
```

Here, we compare the two passwords character by character. If two characters do not match, we
return early and don't bother comparing the rest of the
passwords. Note that this is very similar to how the standard `strcmp()` function works
in C. While this saves time and is efficient, doesn't it leak information about the password?
If we enter a password where only the first few characters are correct, `password_checker` will
take a little bit longer to return a value than if we enter a password where the first character
is incorrect. So, the time this code takes to return gives us information about how many leading
characters in an incorrect password are correct. 

With this timing difference, we can put together an attack that can correctly guess the password in
a relatively small number of tries. To start, we try entering all passwords with all possible leading
characters. If the passwords are alphanumeric, we would try all passwords from 'Abcd...', 'Bbcd...',
... '0bcd...', 9bcd...'. We keep the remainder of the password constant to isolate the effect of just
this first character. Timing how long it takes to evaluate each password, we will notice that one of these
takes slightly longer than the others. That password guess is the one with the correct first character.
To understand why, notice that if the first character is correct, the function moves on and compares the
second characters. Since an incorrect guess will terminate the function after just examining the first
character, a password with the correct first character (but an incorrect second character) will take
roughly twice as long to evaluate.

Now that the first password character is determined, we target the second character. Like before, we try
all passwords with all possible characters in the second position. However, for all of these guesses, we
fix the first character to be what we previously determined to be the correct first character. Again, we
will notice that one guess takes a little longer to be processed, indicating that it has the correct second
character. We then repeat this process for the remaining characters in the password.

**Wait a minute, isn't this just brute forcing the password?** Yes, and no. It is intelligently brute forcing
the password over a much much smaller search space than a simple brute force attack. For a basic brute force
search, we would evaluate every possible password. For a 16 character alphanumeric password, this would mean testing
up to 36^16 = 7.96 * 10^24 possible passwords. With our approach, we brute force each character individually, cutting
down the maximum number of tries to 36 * 16 = 576. That is a lot smaller, and we will take seconds, not years, to run.

###Constant-time code

The password checker example given above may seem a little contrived, but actually isn't uncommon. To provide
another real-world example of a vulnerability, we look at code from ..


flush and reload.

was actually exploited using cache...

Constant-time code.

The implementations of the RSA crypto algorithm, modular exponentiation
data-dependent timing. secret key determines time it takes
 (anyone taken ECE/CS 4802?)


If you tried to look at them, you
likely would be kicked out of the game, or beat up. But, what if you didnt

What about other side-channels?

Another commonly exploited side-channel on general purpose computing systems (servers,
laptops, etc.) is the processor's hardware cache.

How do we prevent them?

Are there other side-channels?

Yes, many. Device power usage, a program's cache access patterns, behavior of
speculative execution engines, and even your PC's cooling fan can be
exploited by a side channel attack. Of course, as side-channels become more
esoteric, the attacks become much more complex (and eventually more of a
novelty than a threat). BUT that does not mean they should be ignored. Side-
channel attacks, while difficult to find and exploit, are some of the most
severe and dangerous. Why? Because when they exploit hardware (not software)
the vulnerability cannot be patched.

## References
