# HEBREW NLP TF-IDF

TF-IDF and vod2vec on 3 types of files in Hebrew.

* Type 1: Files with whole words (without punctuation).

* Type 2: Files with the roots of the words.

* Type 3: Files with words broken to their roots ("שבמצח" => "שב מצח")

Below are the results for the query
`חמאס מלחמה עזה טיל טילים פלסטינים`

The contents of the files can be viewed by clicking on them

#### TF-IDF top 10 files for each category:

|**Clean punctuation**| similarity |**PrefSufWords**| similarity |**RootWord**| similarity |
| ------------- | ------------- | ------------- | ------------- |------------- | ------------- |
| [2544137.txt](docs/Clean_Punctuation/2544137.txt)|0.6328771355794626| [2763273prefsuf.txt](docs/Clean_Punctuation/2763273.txt)|0.2369911739213888|[2516532root.txt](docs/Clean_Punctuation/2516532.txt)|0.25789237861633374|
| [1763006.txt](docs/Clean_Punctuation/1763006.txt)|0.6028766297608992| [3224668prefsuf.txt](docs/Clean_Punctuation/3224668.txt)|0.2360844896168185|[1763006root.txt](docs/Clean_Punctuation/1763006.txt)|0.25522720092802675|
| [3200525.txt](docs/Clean_Punctuation/3200525.txt)|0.5932105336176698| [1682206prefsuf.txt](docs/Clean_Punctuation/1682206.txt)|0.23207942157980932|[2763273root.txt](docs/Clean_Punctuation/2763273.txt)|0.24829179106946508|
| [3224668.txt](docs/Clean_Punctuation/3224668.txt)|0.5529987921150823| [1716814prefsuf.txt](docs/Clean_Punctuation/1716814.txt)|0.21486838009209142|[2764728root.txt](docs/Clean_Punctuation/2764728.txt)|0.24366686574589502|
| [2763273.txt](docs/Clean_Punctuation/2763273.txt)|0.5493357642260276| [3200181prefsuf.txt](docs/Clean_Punctuation/3200181.txt)|0.2141802599463245|[3224668root.txt](docs/Clean_Punctuation/3224668.txt)|0.23987286401430108|
| [3227173.txt](docs/Clean_Punctuation/3227173.txt)|0.5298776018606244| [3227173prefsuf.txt](docs/Clean_Punctuation/3227173.txt)|0.21406999200178278|[2589060root.txt](docs/Clean_Punctuation/2589060.txt)|0.23731395822517332|
| [2767441.txt](docs/Clean_Punctuation/2767441.txt)|0.5237825246168819| [2762821prefsuf.txt](docs/Clean_Punctuation/2762821.txt)|0.2089475380770338|[3044679root.txt](docs/Clean_Punctuation/3044679.txt)|0.2358677035792669|
| [1863195.txt](docs/Clean_Punctuation/1863195.txt)|0.5081887327650091| [2544137prefsuf.txt](docs/Clean_Punctuation/2544137.txt)|0.20859923531448055|[3234654root.txt](docs/Clean_Punctuation/3234654.txt)|0.23536472642344508|
| [3234654.txt](docs/Clean_Punctuation/3234654.txt)|0.5000208050141923| [2546411prefsuf.txt](docs/Clean_Punctuation/2546411.txt)|0.207481033009436|[3200181root.txt](docs/Clean_Punctuation/3200181.txt)|0.23139911815232295|
| [2767820.txt](docs/Clean_Punctuation/2767820.txt)|0.49866617638441957| [1716669prefsuf.txt](docs/Clean_Punctuation/1716669.txt)|0.20698391367803537|[1716814root.txt](docs/Clean_Punctuation/1716814.txt)|0.22784591716399072|



#### doc2vec top 10 files for each category:

|**Clean punctuation**| similarity |**PrefSufWords**| similarity |**RootWord**| similarity |
| ------------- | ------------- | ------------- | ------------- |------------- | ------------- |
| [2815711.txt](docs/Clean_Punctuation/2815711.txt)|0.8379393219947815 | [3215204prefsuf.txt](docs/Clean_Punctuation/3215204.txt)|0.8451696634292603| [2654951root.txt](docs/Clean_Punctuation/2654951.txt)|0.8426624536514282|
| [3184780.txt](docs/Clean_Punctuation/3184780.txt)|0.8259774446487427 | [1811559prefsuf.txt](docs/Clean_Punctuation/1811559.txt)|0.8209106922149658| [3204941root.txt](docs/Clean_Punctuation/3204941.txt)|0.8411526679992676|
| [1608580.txt](docs/Clean_Punctuation/1608580.txt)|0.8181542754173279 | [1811562prefsuf.txt](docs/Clean_Punctuation/1811562.txt)|0.8071666955947876| [1811562root.txt](docs/Clean_Punctuation/1811562.txt)|0.814696192741394|
| [1743096.txt](docs/Clean_Punctuation/1743096.txt)|0.8105580806732178 | [3225440prefsuf.txt](docs/Clean_Punctuation/3225440.txt)|0.7961132526397705| [1853284root.txt](docs/Clean_Punctuation/1853284.txt)|0.8077710866928101|
| [3244484.txt](docs/Clean_Punctuation/3244484.txt)|0.8082942366600037 | [3218931prefsuf.txt](docs/Clean_Punctuation/3218931.txt)|0.7953389286994934| [2649467root.txt](docs/Clean_Punctuation/2649467.txt)|0.8067579865455627|
| [3206106.txt](docs/Clean_Punctuation/3206106.txt)|0.8035317659378052 | [2759660prefsuf.txt](docs/Clean_Punctuation/2759660.txt)|0.7943722605705261| [3164207root.txt](docs/Clean_Punctuation/3164207.txt)|0.79481041431427|
| [3173668.txt](docs/Clean_Punctuation/3173668.txt)|0.8018320798873901 | [2771551prefsuf.txt](docs/Clean_Punctuation/2771551.txt)|0.7932097315788269| [3125850root.txt](docs/Clean_Punctuation/3125850.txt)|0.7935506105422974|
| [3026879.txt](docs/Clean_Punctuation/3026879.txt)|0.794529378414154|  [3215394prefsuf.txt](docs/Clean_Punctuation/3215394.txt)|0.7927966713905334| [3173668root.txt](docs/Clean_Punctuation/3173668.txt)|0.7855309844017029|
| [3036123.txt](docs/Clean_Punctuation/3036123.txt)|0.7933730483055115 | [2931445prefsuf.txt](docs/Clean_Punctuation/2931445.txt)|0.7896900773048401| [1811559root.txt](docs/Clean_Punctuation/1811559.txt)|0.7811357975006104|
| [2683497.txt](docs/Clean_Punctuation/2683497.txt)|0.7872658371925354 | [1544126prefsuf.txt](docs/Clean_Punctuation/1544126.txt)|0.7872987389564514| [3209043root.txt](docs/Clean_Punctuation/3209043.txt)|0.776106595993042|



![alt text](plots/A,%20B%20Clean_Punctuation%20TF-IDF.png)

![alt text](plots/A,%20B%20Clean_Punctuation%20TF-IDF_table.jpeg)

| A, B Clean_Punctuation TF-IDF | Kmeans | ANN | 
| ------------- | ------------- | ------------- |
Accuracy | 0.4681462328521152 | 0.818312406539917 |
F1 | 0.4316536518702584 | 0.8323577642440796 |
Precision | 0.502723391739009 | 0.8570425510406494 |
Recall | 0.5017111580640823 | 0.8178092837333679 |

![alt text](plots/A,%20B%20Clean_Punctuation%20doc2vec.png)

| A, B Clean_Punctuation doc2vec | Kmeans | ANN | 
| ------------- | ------------- | ------------- |
Accuracy | 0.49838396897220427 | 0.8222621083259583 |
F1 | 0.49814313713435476 | 0.839663565158844 |
Precision | 0.5019411349525311 | 0.8476766347885132 |
Recall | 0.501956119343891 | 0.8396168351173401 |

![alt text](plots/A,%20B%20prefSufWord%20TF-IDF.png)

| A, B prefSufWord  TF-IDF | Kmeans | ANN | 
| ------------- | ------------- | ------------- |
Accuracy | 0.470660058895353 | 0.8089766502380371  |
F1 | 0.47000092681714634 | 0.8225197196006775  |
Precision | 0.47271312807694565 | 0.8502076864242554  |
Recall | 0.47242607412926557 | 0.8059368133544922  |

![alt text](plots/A,%20B%20prefSufWord%20doc2vec.png)

| A, B prefSufWord  doc2vec | Kmeans | ANN | 
| ------------- | ------------- | ------------- |
Accuracy | 0.497737556561086 | 0.8272890448570251 |
F1 | 0.4949303112422917 | 0.8388475775718689 |
Precision | 0.4955431054355951 | 0.8655506372451782 |
Recall | 0.49549683046561954 | 0.8217422366142273 |

![alt text](plots/A,%20B%20rootWord%20TF-IDF.png)

| A, B rootWord TF-IDF| Kmeans | ANN | 
| ------------- | ------------- | ------------- |
Accuracy | 0.5383178912590677  | 0.8046678900718689  |
F1 | 0.48481053871831364  | 0.8218396902084351  |
Precision | 0.51281645345286  | 0.8355497121810913  |
Recall | 0.5092497968140103  | 0.8175587058067322  |

![alt text](plots/A,%20B%20rootWord%20doc2vec.png)

| A, B rootWord doc2vec | Kmeans | ANN | 
| ------------- | ------------- | ------------- |
Accuracy | 0.4957983193277311 | 0.814362645149231 |
F1 | 0.4940817695918667 | 0.8327144384384155 |
Precision | 0.4953872108150178 | 0.8359163403511047 |
Recall | 0.4953320576956328 | 0.8380622863769531 |

![alt text](plots/A,%20C%20Clean_Punctuation%20TF-IDF.png)

| A, C Clean_Punctuation TF-IDF | Kmeans | ANN | 
| ------------- | ------------- | ------------- |
Accuracy | 0.4014866851821598 | 0.0|
F1 | 0.19939552526420415 | 0.6625362038612366 |
Precision | 0.16014988595633758 | 0.5007400512695312 |
Recall | 0.26411951206405504 | 1.0 |

![alt text](plots/A,%20C%20Clean_Punctuation%20doc2vec.png)

| A, C Clean_Punctuation doc2vec | Kmeans | ANN | 
| ------------- | ------------- | ------------- |
Accuracy | 0.2319065512171214 | 0.19273172318935394 |
F1 | 0.1504983036471586 | 0.7553202509880066 |
Precision | 0.14849102986557874 | 0.6168949007987976 |
Recall | 0.15256058896233007 | 0.9883641600608826 |

![alt text](plots/A,%20C%20prefSufWord%20TF-IDF.png)

| A, C prefSufWord TF-IDF | Kmeans | ANN | 
| ------------- | ------------- | ------------- |
Accuracy | 0.2756085606926973 | 0.17149856686592102 |
F1 | 0.18399454669393314 | 0.743989884853363 |
Precision | 0.1867596590280084 | 0.6015133261680603 |
Recall | 0.1813101187597399 | 0.990219235420227 |

![alt text](plots/A,%20C%20prefSufWord%20doc2vec.png)

| A, C prefSufWord doc2vec | Kmeans | ANN | 
| ------------- | ------------- | ------------- |
Accuracy | 0.24113706910635518 | 0.13719885051250458 |
F1 | 0.15536433251756535 | 0.7255492210388184 |
Precision | 0.15222772277227722 | 0.5776076316833496 |
Recall | 0.158632919555054 | 0.9911186695098877 |

![alt text](plots/A,%20C%20rootWord%20TF-IDF.png)

| A, C rootWord TF-IDF | Kmeans | ANN | 
| ------------- | ------------- | ------------- |
Accuracy | 0.13388335239339977 | 0.22253981232643127 |
F1 | 0.12361881057434854 | 0.7712818384170532 |
Precision | 0.20725847243297926 | 0.6398832201957703 |
Recall | 0.08807566231393411 | 0.9839500188827515 |

![alt text](plots/A,%20C%20rootWord%20doc2vec.png)

| A, C rootWord doc2vec | Kmeans | ANN | 
| ------------- | ------------- | ------------- |
Accuracy | 0.26645972880248325 | 0.20498162508010864 |
F1 | 0.1811014878969576 | 0.7612358927726746 |
Precision | 0.1873097904105656 | 0.6265865564346313 |
Recall | 0.17529152560588965 | 0.9844071865081787 |

![alt text](plots/C,%20B%20Clean_Punctuation%20TF-IDF.png)

| C, B Clean_Punctuation TF-IDF | Kmeans | ANN | 
| ------------- | ------------- | ------------- |
Accuracy | 0.43709571916563705 | 0.5490552186965942 |
F1 | 0.21403658623389568 | 1.0 |
Precision | 0.1820438309722727 | 1.0 |
Recall | 0.25967184801381693 | 1.0 |

![alt text](plots/C,%20B%20Clean_Punctuation%20doc2vec.png)

| C, B Clean_Punctuation doc2vec | Kmeans | ANN | 
| ------------- | ------------- | ------------- |
Accuracy | 0.29798677229449816 | 0.5490552186965942 |
F1 | 0.19035680293428048 | 1.0 |
Precision | 0.20585429532560126 | 1.0 |
Recall | 0.1770293609671848 | 1.0 |

![alt text](plots/C,%20B%20prefSufWord%20TF-IDF.png)

| C, B prefSufWord TF-IDF | Kmeans | ANN | 
| ------------- | ------------- | ------------- |
Accuracy | 0.2923177556508467 | 0.5490552186965942 |
F1 | 0.17725479826359047 | 1.0 |
Precision | 0.18099995499752486 | 1.0 |
Recall | 0.17366148531951642 | 1.0 |

![alt text](plots/C,%20B%20prefSufWord%20doc2vec.png)

| C, B prefSufWord doc2vec | Kmeans | ANN | 
| ------------- | ------------- | ------------- |
Accuracy | 0.2697870484773603 | 0.5490552186965942 |
F1 | 0.16575128376869838 | 1.0 |
Precision | 0.17161349976883958 | 1.0 |
Recall | 0.16027633851468048 | 1.0 |

![alt text](plots/C,%20B%20rootWord%20TF-IDF.png)

| C, B rootWord TF-IDF | Kmeans | ANN | 
| ------------- | ------------- | ------------- |
Accuracy | 0.14179809579184532 | 0.5490552186965942 |
F1 | 0.11982189467219408 | 1.0 |
Precision | 0.20744284954811268 | 1.0 |
Recall | 0.08424006908462867 | 1.0 |

![alt text](plots/C,%20B%20rootWord%20doc2vec.png)

| C, B rootWord doc2vec | Kmeans | ANN | 
| ------------- | ------------- | ------------- |
Accuracy | 0.2681154153644887 | 0.5490552186965942 |
F1 | 0.165188966505463 | 1.0 |
Precision | 0.17154947916666666 | 1.0 |
Recall | 0.1592832469775475 | 1.0 |





