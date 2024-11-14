|   Method   |   Model   |    Training Acc  |  Test Acc |
|------------|-----------|------------------|-----------|
| Transfer   |MobileNetV2|      80.5%       |  71.66%   |(final layer: 16 neurons, 0.1 dropout)
| Learning   |96x96 0.35 |                  |           |
|------------|-----------|------------------|-----------|
| Transfer   |MobileNetV1|      46.8%       |  10.16%   |(no final dense layer, 0.1 dropout)
| Learning   |96x96 0.25 |                  |           |
|------------|-----------|------------------|-----------|
| Transfer   |EfficiNetB0|      65.6%       |  24.06%   |
| Learning   |           |                  |           |
|------------|-----------|------------------|-----------|
| Classifica | Zie beschr|      71.4%       |  56.68%   |
|------------|-----------|------------------|-----------|



MobileNetV2 96x96 0.35 TL
![alt text](image-1.png)

MobileNetV1 96x96 0.25 TL
![alt text](image.png)

EfficiNetB0 TL
![alt text](image-2.png)

Classification
![alt text](image-3.png)
