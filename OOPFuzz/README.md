# OOPFuzz

### Description

This is the preliminary proof-of-concept application built to verify our TSE research findings. The tool aims to automatically generate programs enhanced with OOP features for testing C++ compilers through source-2-source code mutation.

As introduced in our paper, 4 mutators have been created and verified on our seed program set, with more mutators related to different bug types underway.

### Install

The application is created based on LLVM 's Clang LibTooling library. Currently, the code has to be compiled under the whole *clang-tools-extra* project, please consult LLVM 's official instruction: [https://clang.llvm.org/docs/LibASTMatchersTutorial.html](https://clang.llvm.org/docs/LibASTMatchersTutorial.html).

A pre-built docker image is going to be provided in our future plan.

### Run the application

OOPFuzz has 2 basic running modes that allow users to choose whether to perform mutation on a single seed program file or on a set of programs.

- For a single seed program, just run the following command:

```bash
   ./mutation-instrument <target.cpp> --mutator=<mutatorID> --sourcedir=<sourcedirpath of target.cpp> -- <options> 
```
where `<target.cpp>` refers to the code under mutation, `<mutatorID>` refers to the identifier of the mutator to be applied and `<options>` refers to the necessary options for compiling `<target.cpp>`.

- For multiple seed programs, we have provided a `/setup/startup.sh` script to conduct necessary configurations:
```bash
    cd setup/
    cp * /seed/program/home/
    ./startup.sh complete
```
where `/seed/program/home` refers to the absolute file path of the directory containing the seed programs under mutation.

Please note that the script's complete workflow consists of applying selected mutators to the seed programs and performing differential testing to find bugs and generate corresponding test reports accordingly. Selectively conducting the tasks can be achieved by passing the following argument to `startup.sh`:

```python
./startup.sh mutate #only apply mutators
./startup.sh validate #only conduct differential testing*
./startup.sh complete  #both
```
The configuration options used in `startup.sh` are managed by `config.json`:

```python
{
 # path of compilers under test
"gcc_path":"/differential_tsting_compilers/gcc-13.2.0/bin/g++",
"clang_path":"/differential_tsting_compilers/llvm-17.0.1/bin/clang++",
 # mutators' total number
"mutator_number":4,
 # which mutators to apply
"active_mutators":[1,2,3],
 # decide whether to use every mutator
"use_all_mutators":false
}
```

