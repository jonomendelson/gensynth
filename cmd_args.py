import argparse
import os

cmd_opt = argparse.ArgumentParser(description='Argparser')
cmd_opt.add_argument("benchmark_dir", help="the parent directory of the benchmark you want to run gensynth on")
cmd_opt.add_argument("benchmark_name", help="the name of the benchmark you want to run gensynth on")
cmd_opt.add_argument("-l", "--log_number", default=0, help="the folder number to store your logs in", type=int)
cmd_opt.add_argument("-n", "--num_pops", default=1, help="the number of populations to process parallelly", type=int)
cmd_opt.add_argument("-t", "--target_score", default=1.0, help="the minimum f1 score for the generated solution", type=float)
cmd_opt.add_argument("--use_neg", action="store_true", help="to be used if a specific undesired file is provided")
cmd_opt.add_argument("--souffle_path", help="path to souffle", default="souffle")

cmd_args, _ = cmd_opt.parse_known_args()