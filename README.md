# MalBeWare Benchmark
**MalBeWare** is a malware classification benchmark designed to identify the family of a given sample (e.g., *Adialer.C*, *Agent.FYI*). It is based on the [Malimg dataset](https://paperswithcode.com/dataset/malimg), which contains 25 malware families. Each sample is represented as a grayscale image derived from an executable file. We evaluate robustness against \( L_\infty \) perturbations of magnitudes \{1/255, 2/255, 3/255\}, following the setting described in [*Case Study: Neural Network Malware Detection Verification for Feature and Image Datasets*](https://dl.acm.org/doi/abs/10.1145/3644033.3644372).  

Please see below for example images, the list of malware families included in the dataset, and the perturbations considered.


## Image Examples
![Malware Family Examples](./archive/malware_family_img.pdf)

## Classes (Families)

| Malimg Class     | Num Samples (ε=1) | Num Samples (ε=2) | Num Samples (ε=3)  |
|------------------|-----|-----|-----|
| Adialer.C        | 5   | 5   | 5   |
| Agent.FYI        | 5   | 5   | 5   |
| Allaple.A        | 5   | 5   | 5   |
| Allaple.L        | 5   | 5   | 5   |
| Alueron.gen!J    | 5   | 5   | 5   |
| Autorun.K        | 5   | 5   | 5   |
| C2LOP.P          | 5   | 5   | 5   |
| C2LOP.gen!g      | 5   | 5   | 5   |
| Dialplatform.B   | 5   | 5   | 5   |
| Dontovo.A        | 5   | 5   | 5   |
| Fakerean         | 5   | 5   | 5   |
| Instantaccess    | 5   | 5   | 5   |
| Lolyda.AA1       | 5   | 5   | 5   |
| Lolyda.AA2       | 5   | 5   | 5   |
| Lolyda.AA3       | 5   | 5   | 5   |
| Lolyda.AT        | 5   | 5   | 5   |
| Malex.gen!J      | 5   | 5   | 5   |
| Obfuscator.AD    | 5   | 5   | 5   |
| Rbot!gen         | 5   | 5   | 5   |
| Skintrim.N       | 5   | 5   | 5   |
| Swizzor.gen!E    | 5   | 5   | 5   |
| Swizzor.gen!I    | 5   | 5   | 5   |
| VB.AT            | 5   | 5   | 5   |
| Wintrim.BX       | 5   | 5   | 5   |
| Yuner.A          | 5   | 5   | 5   |


## References
```
@inproceedings{robinette2024case,
  title={Case study: Neural network malware detection verification for feature and image datasets},
  author={Robinette, Preston K and Manzanas Lopez, Diego and Serbinowska, Serena and Leach, Kevin and Johnson, Taylor T},
  booktitle={Proceedings of the 2024 IEEE/ACM 12th International Conference on Formal Methods in Software Engineering (FormaliSE)},
  pages={127--137},
  year={2024}
}
```

```
@inproceedings{nataraj2011malware,
  title={Malware images: visualization and automatic classification},
  author={Nataraj, Lakshmanan and Karthikeyan, Sreejith and Jacob, Gregoire and Manjunath, Bangalore S},
  booktitle={Proceedings of the 8th international symposium on visualization for cyber security},
  pages={1--7},
  year={2011}
}
```
