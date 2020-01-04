### About
We have often seen a lot of time is wasted in taking attendance in class . So , to tackle this problem we have designed a ML project that will automatically mark present of the student present in the class based upon their interaction in the class.



### Usage

Speaker Recognition Command Line Tool
  -h, --help            show this help message and exit
  -t TASK, --task TASK  Task to do. Either "enroll" or "predict"
  -i INPUT, --input INPUT
                        Input Files(to predict) or Directories(to enroll)
  -m MODEL, --model MODEL
                        Model file to save(in enroll) or use(in predict)

Wav files in each input directory will be labeled as the basename of the directory.
Note that wildcard inputs should be *quoted*.

Examples:
    Train:
    ./speaker-recognition.py -t enroll -i "training_data\*" -m model.out

    Predict:
    ./speaker-recognition.py -t predict -i test.wav -m model.out
```
