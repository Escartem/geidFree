# geidFree

bypass license in geid

tool page : https://www.allmapsoft.com/geid/

license check works by taking input, applying transformations and merging with hardcoded letters, then md5 of that and take the reversed first half of the digest and compare it against a hardcoded value. Because of the half md5 i can't find a *valid* code so only option is to patch the program hardcoded key, it's modified to be the one that's obtained when inputing `ABCDE-FGHIJ-KLMNO-PQRST-UVWXY`. You can generate your own pins with the python script. You have patched exe and .ini file if you're lazy to input the code. Made as of version `6.48`.

Have fun :)

![img](https://bin.escartem.moe/2026/03/31/2wkFNUlCW5.png)
