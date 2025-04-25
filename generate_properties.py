"""
Randomly initializes the vnnlib samples from a provided seed.

Use:
python generate_properties.py 4


Output:
instances.csv file containing:
    neural network model (onnx)
    input + property (vnnlib)
    timeout (int)
"""
import random
import csv
import os
import sys

TIMEOUT=100
NUM_SAMPLES=50

def main():
    #
    # load onnx models and vnnlib files
    #
    onnx_models = list(reversed(sorted([m for m in os.listdir("onnx") if ".onnx" in m])))
    vnnlib_files = sorted([v for v in os.listdir("vnnlib") if ".vnnlib" in v])
    #
    # set the seed and randomly select files
    #
    random.seed(int(sys.argv[1]))
    selected_files = random.sample(vnnlib_files, NUM_SAMPLES)
    #
    # combine in a csv file
    #
    instances = []
    for model in onnx_models:
        for selected_file in selected_files:
            instances.append([model, selected_file, TIMEOUT])

    with open('instances.csv', mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(instances)


    print("\n", "="*50)
    print("COMPLETE... Saved to instances.csv")
    


if __name__ == "__main__":
    main()
    