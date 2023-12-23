# Fake Alignment: Are LLMs Really Aligned Well?
The source code for our paper "[Fake Alignment: Are LLMs Really Aligned Well?](https://arxiv.org/abs/2311.05915)". We verify the existence of the fake alignment problem and propose the Fake alIgNment Evaluation (FINE) framework.

## Preparation

Environment can be set up as:

```bash
$ pip install -r requirements.txt
```

Your openai api key should be filled in `LLM_utils.py`

```python
os.environ["OPENAI_API_KEY"] = 'Put your API key here'
```

## Datasets
We provide a test dataset in `safety.jsonl` of five safety-relevant subcategories that can be used to evaluate the alignment of LLMs. Each question contains a question stem and corresponding positive and negative options:
<p align="center"> <img src="images/img_examples.jpg" style="width: 90%;" id="title-icon"></p>

You can also use your own security-related data sets. And you can use `build_option.py` to convert the dataset to our format.

```bash
python build_option.py --file_path YOUR_DATASET_FILE.jsonl  --save_file WHERE_YOU_SAVE.jsonl
```
Please note that your data set file should be in jsonl format, and each item contains "question" and "category" fields.

## FINE
Here is our proposed Fake alIgNment Evaluation (FINE). It primarily includes a module for constructing multiple-choice questions and a consistency measurement method.
<p align="center"> <img src="images/img_FINE.jpg" style="width: 90%;" id="title-icon"></p>

You can run the FINE framework with the following command:

```bash
python FINE.py --test_model MODEL_NAME_YOU_WANT_TO_TEST  --file_path YOUR_DATASET_FILE.jsonl --save_path PATH_TO_SAVE
```

## Model Support

We currently support the following models in  `LLM_utils.py`:
| | | | | | | |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| [GPT-3.5-turbo](https://openai.com/) | [GPT-4](https://openai.com/) | [ChatGLM](https://github.com/THUDM/ChatGLM3) | [MOSS](https://github.com/OpenLMLab/MOSS) | [InternLM](https://github.com/InternLM/InternLM) | [Vicuna](https://github.com/lm-sys/FastChat) | [Qwen](https://github.com/QwenLM/Qwen) |

If you want to use your own model, just replace the following content in `FINE.py`` with your LLM:
```python
llm = eval("LLM_utils.{}".format(args.test_model))()
```


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