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
See Notebook <strong>03, 05, 06, 07 and 08</strong> for details.

## Results

### 1. 10-Fold CV Accuracy (%) of CNN on Digits Data

| Fold 	| IDL 	| 35U 	| 35D 	| 55U 	| 55D 	| Average 	|
|:-----:|:---:	|:---:	|:---:	|:---:	|:---:	|:-------:	|
|   1  	|  85 	|    	|    	|     	|     	|         	|
|   2  	|  80  	|    	|    	|     	|     	|         	|
|   3  	|  81  	|    	|    	|     	|     	|         	|
|   4  	|  78  	|    	|    	|     	|     	|         	|
|   5  	|  84  	|    	|    	|     	|     	|         	|
|   6  	|  85  	|    	|    	|     	|     	|         	|
|   7  	|  83  	|    	|    	|     	|     	|         	|
|   8  	|  77  	|    	|    	|     	|     	|         	|
|   9  	|  80  	|    	|    	|     	|     	|         	|
|  10  	|  87  	|    	|   	|     	|     	|         	|
| Avg. 	|  82  	|       |    	|     	|     	|         	|

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

### 3. 10-Fold CV Accuracy (%) of CNN on Mixed Data

| Fold 	| IDL 	| 35U 	| 35D 	| 55U 	| 55D 	| Average 	|
|:----:	|:---:	|:---:	|:---:	|:---:	|:---:	|:-------:	|
|   1  	|  53 	|     	|    	|     	|     	|         	|
|   2  	|  53  	|     	|    	|     	|     	|         	|
|   3  	|  57  	|     	|    	|     	|     	|         	|
|   4  	|  60  	|     	|    	|     	|     	|         	|
|   5  	|  56  	|     	|    	|     	|     	|         	|
|   6  	|  56  	|     	|    	|     	|     	|         	|
|   7  	|  58  	|     	|    	|     	|     	|         	|
|   8  	|  60  	|     	|    	|     	|     	|         	|
|   9  	|  57  	|     	|    	|     	|     	|         	|
|  10  	|  54  	|     	|   	|     	|     	|         	|
| Avg. 	|  56  	|     	|    	|     	|     	|         	|
