# Fake Alignment: Are LLMs Really Aligned Well?
The source code for our paper "[Fake Alignment: Are LLMs Really Aligned Well?](https://arxiv.org/abs/2311.05915)". We verify the existence of the fake alignment problem and propose the Fake alIgNment Evaluation (FINE) framework.

## Installation

Environment can be set up as:

```bash
$ pip install -r requirements.txt
```

## Datasets
We provide a test dataset in `safety.jsonl` of five safety-relevant subcategories that can be used to evaluate the alignment of LLMs. Each question contains a question stem and corresponding positive and negative options:
<p align="center"> <img src="images/img_examples.png" style="width: 85%;" id="title-icon"></p>



## Citation

If you think this project is helpful, please cite the paper.

```bibtex
@misc{wang2023fake,
      title={Fake Alignment: Are LLMs Really Aligned Well?}, 
      author={Yixu Wang and Yan Teng and Kexin Huang and Chengqi Lyu and Songyang Zhang and Wenwei Zhang and Xingjun Ma and Yu-Gang Jiang and Yu Qiao and Yingchun Wang},
      year={2023},
      eprint={2311.05915},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```