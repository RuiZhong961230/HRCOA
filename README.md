# HRCOA
Hybrid remora crayfish optimization for engineering and wireless sensor network coverage optimization

## Abstract
This paper proposes a novel hybrid metaheuristic algorithm called the remora crayfish optimization algorithm (HRCOA) designed for solving continuous optimization problems. The crayfish optimization algorithm (COA), recently proposed as a meta-heuristic algorithm (MA), exhibits certain limitations such as imbalanced exploration and exploitation capacities, susceptibility to premature optimization, and a propensity for stagnation. To address these shortcomings, we incorporate the exploitation operators from the remora optimization algorithm (ROA) to enhance the exploitative behaviors of COA. In addition, we simplify the summer resort operator in the original COA to streamline the search operator design, thus avoiding unnecessary complexity. Furthermore, numerical experiments on 10-dimensional (D) and 20-D CEC2022 benchmark functions, 50-D and 100-D CEC2020 benchmark functions, engineering optimization problems, and wireless sensor networks (WSNs) coverage optimization problems are conducted to investigate the performance of our proposed HRCOA comprehensively. We compare the proposed HRCOA against eight well-known state-of-the-art MAs, including CMAES and the original COA, as competitor algorithms. The experimental and statistical results confirm the effectiveness, competitiveness, and scalability of our proposal. Finally, we conclude that the proposed HRCOA possesses significant potential for addressing diverse optimization challenges in real-world scenarios.

## Citation
@article{Zhong:24,  
  title={Hybrid remora crayfish optimization for engineering and wireless sensor network coverage optimization},  
  author={Rui Zhong and Qinqin Fan and Chao Zhang and Jun Yu},  
  journal={Cluster Computing},  
  volume={27}, 
  pages={10141–10168},  
  year={2024},  
  publisher={Springer},  
  doi = {https://doi.org/10.1007/s10586-024-04508-1 },  
}

## Datasets and Libraries
CEC benchmarks are provided by the opfunu library and engineering problems are provided by the enoppy library.
