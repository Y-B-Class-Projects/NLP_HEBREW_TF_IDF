# HEBREW NLP TF-IDF

TF-IDF and vod2vec on 3 types of files in Hebrew.

* Type 1: Files with whole words (without punctuation).

* Type 2: Files with the roots of the words.

* Type 3: Files with words broken to their roots ("שבמצח" => "שב מצח")

Below are the results for the query
`חמאס מלחמה עזה טיל טילים פלסטיני`

The contents of the files can be viewed by clicking on them

#### Clean punctuation TF-IDF:

| file | cosine distances |
| ------------- | ------------- |
| [2763273.txt](docs/Clean_Punctuation/2763273.txt)|0.6228006344545287|
| [1705790.txt](docs/Clean_Punctuation/1705790.txt)|0.6850845805742616|
| [2767820.txt](docs/Clean_Punctuation/2767820.txt)|0.6887950367520226|
| [3224668.txt](docs/Clean_Punctuation/3224668.txt)|0.6988602770154239|
| [1863195.txt](docs/Clean_Punctuation/1863195.txt)|0.7085337541416866|
| [2578065.txt](docs/Clean_Punctuation/2578065.txt)|0.7286950287149693|
| [2765958.txt](docs/Clean_Punctuation/2765958.txt)|0.737967713244697|
| [2637035.txt](docs/Clean_Punctuation/2637035.txt)|0.7411236080169266|
| [2865996.txt](docs/Clean_Punctuation/2865996.txt)|0.7464806018495623|
| [2579104.txt](docs/Clean_Punctuation/2579104.txt)|0.7520027906747968|

#### PrefSufWords TF-IDF:

| file | cosine distances |
| ------------- | ------------- |
| [2763273prefsuf.txt](docs/Clean_Punctuation/2763273.txt)|0.8557371862932684|
| [3231307prefsuf.txt](docs/Clean_Punctuation/3231307.txt)|0.8607839814331686|
| [3191423prefsuf.txt](docs/Clean_Punctuation/3191423.txt)|0.8615751927783771|
| [2789433prefsuf.txt](docs/Clean_Punctuation/2789433.txt)|0.8673518987533998|
| [1818664prefsuf.txt](docs/Clean_Punctuation/1818664.txt)|0.869321965177581|
| [3200181prefsuf.txt](docs/Clean_Punctuation/3200181.txt)|0.8731358533354855|
| [2942877prefsuf.txt](docs/Clean_Punctuation/2942877.txt)|0.876800170732896|
| [2594594prefsuf.txt](docs/Clean_Punctuation/2594594.txt)|0.8788144348552696|
| [2578065prefsuf.txt](docs/Clean_Punctuation/2578065.txt)|0.880982998007856|
| [2777669prefsuf.txt](docs/Clean_Punctuation/2777669.txt)|0.8833262914654372|

#### RootWord TF-IDF:

| file | cosine distances |
| ------------- | ------------- |
| [3224668root.txt](docs/Clean_Punctuation/3224668.txt)|0.6067015957773455|
| [2763273root.txt](docs/Clean_Punctuation/2763273.txt)|0.6188821790762603|
| [2578065root.txt](docs/Clean_Punctuation/2578065.txt)|0.6318448601030151|
| [1818664root.txt](docs/Clean_Punctuation/1818664.txt)|0.6449171204616369|
| [3044679root.txt](docs/Clean_Punctuation/3044679.txt)|0.6585360629138286|
| [2777669root.txt](docs/Clean_Punctuation/2777669.txt)|0.6593998011996607|
| [2765958root.txt](docs/Clean_Punctuation/2765958.txt)|0.6702292160688728|
| [1592317root.txt](docs/Clean_Punctuation/1592317.txt)|0.6779143197256595|
| [2594594root.txt](docs/Clean_Punctuation/2594594.txt)|0.6780379139685844|
| [2789433root.txt](docs/Clean_Punctuation/2789433.txt)|0.6793616819070012|

#### Clean punctuation doc2vec:

| file | cosine distances |
| ------------- | ------------- |
| [1863191.txt](docs/Clean_Punctuation/1863191.txt)|0.8168900012969971|
| [2683497.txt](docs/Clean_Punctuation/2683497.txt)|0.8157790303230286|
| [2681452.txt](docs/Clean_Punctuation/2681452.txt)|0.8037642240524292|
| [1743096.txt](docs/Clean_Punctuation/1743096.txt)|0.7916077971458435|
| [2815711.txt](docs/Clean_Punctuation/2815711.txt)|0.790814995765686|

#### PrefSufWords doc2vec:

| file | cosine distances |
| ------------- | ------------- |
| [2987625prefsuf.txt](docs/Clean_Punctuation/2987625.txt)|0.8586415648460388|
| [3199629prefsuf.txt](docs/Clean_Punctuation/3199629.txt)|0.8146098256111145|
| [2770683prefsuf.txt](docs/Clean_Punctuation/2770683.txt)|0.8052554726600647|
| [3218931prefsuf.txt](docs/Clean_Punctuation/3218931.txt)|0.793726921081543|
| [3213087prefsuf.txt](docs/Clean_Punctuation/3213087.txt)|0.7875193953514099|

#### RootWord doc2vecF:

| file | cosine distances |
| ------------- | ------------- |
| [1853284root.txt](docs/Clean_Punctuation/1853284.txt)|0.8572087287902832|
| [2649467root.txt](docs/Clean_Punctuation/2649467.txt)|0.846522331237793|
| [3204941root.txt](docs/Clean_Punctuation/3204941.txt)|0.8302807807922363|
| [3164207root.txt](docs/Clean_Punctuation/3164207.txt)|0.8266716599464417|
| [1811562root.txt](docs/Clean_Punctuation/1811562.txt)|0.8077954053878784|

