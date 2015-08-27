Sample of Data Structures
====

Goal
----
Practice of implementation of each data structure

Especially I always confuse to choose libraries in C, so I want to store my own library. (In C++, STL is good enough.)


How to build
----
0. Clone this repository
```
$ git clone hoge && cd hoge
```

1. Install gyp/ninja

```
$ sudo apt-get install gyp ninja-build
```

2. Execute ./generate_gyp.sh

```
$ ./generate_gyp.sh
```

3. Build

```
$ ninja -C ./out/Release -j5
```

4. Execute

```
$ ./out/Release/btree.bin
```
