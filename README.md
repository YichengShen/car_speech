# CarSpeech
> Speech recognition for noisy environments in cars.


## How to Download Data

Download digits data

```python
download_data('digits')
```

    data_dir already exists


Download letters data

```python
download_data('letters')
```

    data_dir already exists


## Load Filenames Classified based on Noise Levels
`filenames = load_fnames("REPLACE Path Here")`

```python
filenames = load_fnames("noise_levels/digit_noise_levels/55U.data")
print('number of files:', len(filenames))
```

    number of files: 1538


## Pipeline for Feature Extraction
See Notebook <strong>04_Pipeline</strong> for details. An example is provided at the end of that notebook.

## Training and Model Selection
See Notebook <strong>03, 05, and 06</strong> for details.

## Results

### 1. 10-Fold CV Accuracy (%) of CNN on Digits Data

| Fold 	| IDL 	| 35U 	| 35D 	| 55U 	| 55D 	| Average 	|
|:-----:|:---:	|:---:	|:---:	|:---:	|:---:	|:-------:	|
|   1  	|  75 	|   75 	|   61 	|     	|     	|         	|
|   2  	|  77  	|   72 	|   72 	|     	|     	|         	|
|   3  	|  69  	|   77 	|   66 	|     	|     	|         	|
|   4  	|  70  	|   73 	|   67 	|     	|     	|         	|
|   5  	|  80  	|   74 	|   66 	|     	|     	|         	|
|   6  	|  78  	|   74 	|   62 	|     	|     	|         	|
|   7  	|  77  	|   76 	|   71 	|     	|     	|         	|
|   8  	|  77  	|   74 	|   58 	|     	|     	|         	|
|   9  	|  81  	|   74 	|   58 	|     	|     	|         	|
|  10  	|  74  	|   68 	|   71	|     	|     	|         	|
| Avg. 	|  76  	|   74  |   65 	|     	|     	|         	|

<span style="color:red">TODO: Turn this into box plot</span>

### 2. 10-Fold CV Accuracy (%) of CNN on Letters Data

| Fold 	| IDL 	| 35U 	| 35D 	| 55U 	| 55D 	| Average 	|
|:----:	|:---:	|:---:	|:---:	|:---:	|:---:	|:-------:	|
|   1  	|   	|     	|    	|     	|     	|         	|
|   2  	|    	|     	|    	|     	|     	|         	|
|   3  	|    	|     	|    	|     	|     	|         	|
|   4  	|    	|     	|    	|     	|     	|         	|
|   5  	|    	|     	|    	|     	|     	|         	|
|   6  	|    	|     	|    	|     	|     	|         	|
|   7  	|    	|     	|    	|     	|     	|         	|
|   8  	|     	|     	|    	|     	|     	|         	|
|   9  	|     	|     	|    	|     	|     	|         	|
|  10  	|     	|     	|   	|     	|     	|         	|
| Avg. 	|     	|     	|    	|     	|     	|         	|
