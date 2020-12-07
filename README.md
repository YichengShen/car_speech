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
|   1  	|  85 	|   87 	|   82 	|   84 	|  61  	|    80    	|
|   2  	|  87  	|   78	|    67	|  79  	|  64  	|    75    	|
|   3  	|  88  	|   86 	|   79 	| 84   	|  67  	|    80    	|
|   4  	|  82  	|    78	|   75 	|   74 	|  64  	|    75    	|
|   5  	|  79  	|    77	|   82 	|    81	|   73 	|    78   	|
|   6  	|  82  	|    81	|   73 	|    75	|  66  	|    75    	|
|   7  	|  78  	|    86	|   65 	|     77|  71  	|   75     	|
|   8  	|  83  	|    75	|   81 	|     75|  70  	|    77    	|
|   9  	|  77  	|    79	|    75	|     80|  68  	|    76    	|
|  10  	|  76  	|    78	|   76	|     87|  69  	|    77    	|
| Avg. 	|  82  	|    80 |    76	|   80 	|  67  	|     77  	|

<span style="color:red">TODO: Turn this into box plot</span>

### 2. 10-Fold CV Accuracy (%) of CNN on Letters Data

| Fold 	| IDL 	| 35U 	| 35D 	| 55U 	| 55D 	| Average 	|
|:----:	|:---:	|:---:	|:---:	|:---:	|:---:	|:-------:	|
|   1  	|  57	|  55  	|  42  	|  49  	|  48  	|    50    	|
|   2  	|  53  	|  54  	|  49  	|  61  	|  43  	|    52    	|
|   3  	|  52  	|  55  	|  54  	|  58  	|  40  	|    52    	|
|   4  	|  62  	|  53  	|  47  	|  68  	|  43  	|    55    	|
|   5  	|  53  	|  54  	|  46  	|  59  	|  39  	|    50    	|
|   6  	|  60  	|  56  	|  48  	|  57  	|  43  	|    53    	|
|   7  	|  59  	|  57  	|  50  	|  58  	|  44  	|    54    	|
|   8  	|  57  	|  56  	|  44  	|  61  	|  45  	|    53    	|
|   9  	|  60  	|  59  	|  49  	|  56  	|  47  	|    54    	|
|  10  	|  54  	|  49  	|  44 	|  59  	|  41  	|    49    	|
| Avg. 	|  57  	|  55  	|  47  	|  59  	|  43  	|    52    	|

### 3. 10-Fold CV Accuracy (%) of CNN on Mixed Data

| Fold 	| IDL 	| 35U 	| 35D 	| 55U 	| 55D 	| Average 	|
|:----:	|:---:	|:---:	|:---:	|:---:	|:---:	|:-------:	|
|   1  	|  61 	|  58  	|  55  	|  61  	|  44  	|  56      	|
|   2  	|  63  	|  61  	|  53  	|  62  	|  47  	|  57      	|
|   3  	|  66  	|  58  	|  53  	|  59  	|  50  	|  57      	|
|   4  	|  59  	|  56  	|  54  	|  57  	|  46  	|  54      	|
|   5  	|  62  	|  57  	|  56  	|  55  	|  46  	|  55      	|
|   6  	|  56  	|  58  	|  53  	|  63  	|  48  	|  56      	|
|   7  	|  62  	|  61  	|  47  	|  61  	|  48  	|  56      	|
|   8  	|  62  	|  60  	|  56  	|  61  	|  50  	|  58      	|
|   9  	|  59  	|  63  	|  56  	|  60  	|  48  	|  57      	|
|  10  	|  56  	|  62  	|  57 	|  60  	|  43  	|  56      	|
| Avg. 	|  61  	|  59  	|  54  	|  60  	|  47  	|  56      	|
