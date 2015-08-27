Sample of Data Structures
====

Goal
----
Practice of implementation of each data structure

Especially I always confuse to choose libraries in C, so I want to store my own library. (In C++, STL is good enough.)


How to build
----

1. Clone this repository

   ```
   $ git clone https://github.com/amiq11/data_structures.git && cd data_structures
   $ git submodule init && git submodule update
   ```
2. Install gyp/ninja
 
   ```
   $ sudo apt-get install gyp ninja-build
   ```
3. Execute ./generate_gyp.sh

   ```
   $ ./generate_gyp.sh
   ```
4. Build

   ```
   $ ninja -C ./out/Release -j5
   ```
5. Execute

   ```
   $ ./out/Release/btree.bin
   ```

How to use as a library
---
After the above build process, `./out/Release/obj/libdst.a` will be generated. You can use it with header files in `inc` directory.

LICENSE
---
2-Clause BSD as shown in each files.
