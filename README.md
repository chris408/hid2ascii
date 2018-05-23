## hid2ascii

### Background

This app was something I threw together quickly for a specific purpose: I had quietly grabbed an unattended USBC YubiKey from a friend's laptop and wanted to get a few OTP tokens to use as a prank (they of course knew about this later when I told them). However, I ran into a problem: I didn't have a USBC port on my laptop, but my headless Linux desktop did.

### Use

My Linux desktop is headless, so I only access it over SSH. This made collecting the YubiKey output an interesting challenge. A friend suggested that I collect the HID data with the following command:

```bash
root@localhost# cat /sys/kernel/debug/hid/<device_id>/events
```

Which produced a snipped output similar to the following:

```bash
report (size 8) (unnumbered) =  00 00 15 00 00 00 00 00
Keyboard.00e0 = 0
Keyboard.00e1 = 0
Keyboard.00e2 = 0
Keyboard.00e3 = 0
Keyboard.00e4 = 0
Keyboard.00e5 = 0
Keyboard.00e6 = 0
Keyboard.00e7 = 0
Keyboard.0015 = 1

report (size 8) (unnumbered) =  00 00 00 00 00 00 00 00
Keyboard.00e0 = 0
Keyboard.00e1 = 0
Keyboard.00e2 = 0
Keyboard.00e3 = 0
Keyboard.00e4 = 0
Keyboard.00e5 = 0
Keyboard.00e6 = 0
Keyboard.00e7 = 0
Keyboard.0015 = 0
```

The `15` in the first line was the character typed, in HID format. The second data block was a null value, which is seen after every character.

### Example Output

```bash
python3 hid2ascii.py hidlog.txt 
vvvvccfcirgdvbcjjhjhveriluljffukdnkullkhbrvvNewLine
```

### Notes

While this code probably won't have much use other than the specific usecase I had, it does do useful work that can be repurposed:

* Reads an ASCII file into a list.
* Does a regex search on every line, using group matching.
* Prints the group match results to screen.

Quite often in Red Teaming I will use the above items when parsing output.
