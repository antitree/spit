# spit
Python module specifically for Andrew Morris that I wrote on the way 
from SFO to PHL. It can be used to send SSH commands typed as a human would (poorly and with mistakes) so that it's harder to detect them with his intel tools. :P

# Example usage with a Parimiko SSH client:
 * create a SSH client (shell.py) that opens a chan and reads from stdin
 while True:
       d = sys.stdin.read(1)
       chan.send(d)
 * ./spit.py commandinput | ./shell.py
 * ...
 * profit