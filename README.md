# GenSynth: Genetic Datalog Program Synthesis

### Demo

Please try out our (resource limited) demo at http://gensynth.cis.upenn.edu/, or run GenSynth yourself by following the instructions below.

### Prerequisites

1. Python 3
   1. Python 3 is commonly bundled with software distributions including Fedora and Homebrew.
   2. Ensure that the command `python3` works on your command line
2. Souffle, which can be installed either through a package distribution or from https://github.com/souffle-lang/souffle

### Example runs

Running the following command will print out the help message and describe all the arguments
```
./gensynth -h
```

The following command will run the scc benchmark on 1 thread and store the results in `bench/logs/trial0` (not recommended)
```
./gensynth bench scc
```

To run GenSynth on scc with more than 1 thread (let's say 32) and store the results in `bench/logs/trial0` (recommended)
```
./gensynth bench scc -n 32
```

To run the countries S1, S2 and S3 benchmarks respectively (recommended to run on 32 threads), run
```
./gensynth data countries_S1 -n 32 --use_neg
```
```
./gensynth data countries_S2 -n 32 -t 0.97 --use_neg
```
```
./gensynth data countries_S3 -n 32 -t 0.945 --use_neg
```

### Running GenSynth on Custom Benchmark Problems

```
./gensynth PROBLEM_DIR NAME -n NUM_THREADS -l LOG_NUM [-t F1_THREASHOLD] [--use_neg] [--souffle_path path/to/souffle]
```

`PROBLEM_DIR` is the directory containing all the benchmarks.
`NAME` is the name of the benchmark you want to run.

The path `PROBLEM_DIR/0/NAME` must be a directory containing:
1. `rules.t`: Specifies the signatures of the EDB and IDB relations in the following format:
    i. `*Format(Type, Type)` specifies an input relation.
    ii. `Format(Type, Type)` specifies an output relation.
2. `R.facts`, for each input relation `R` other than Rule: Specifies the EDB.
3. `R.expected`, for an output relation `R`: Specifies the positive examples.
4. (Optionally) `R.undesired`, for an output relation `R`: Specifies the negative examples. `R.undesired` will only be considered if `use_neg` is invoked.

`NUM_THREADS` is the number of threads you want to parallelize GenSynth over. This also corresponds to the number of populations which will be used by GenSynth. The default value, if not specified, is 1. It is recommended to specify this value as high as possible (our experiments use the value 32).

`LOG_NUM` is a number indicating where the logs will be stored. The logs will be stored in `PROBLEM_DIR/logs/trial${LOGNUM}`. The default value, if not specified, is 0.

`use_neg` is an option, if activated, to explicitly state negative examples in case of benchmarks where exhaustive
positive and negative labels are not available.

`F1_THRESHOLD` is the minimum tolerable F1 score for the desired solution. It will be 1.0 for the exact benchmarks, but may be lower for the noisy benchmarks. The default value, if not specified, is 1.0.

The benchmarks are all present under bench/0/
