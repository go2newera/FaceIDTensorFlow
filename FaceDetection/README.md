负责人脸检测部分,本部分构成如下

1.PrepareData负责训练数据作成相关 -> 会最终生成一个tfrecoard文件 *

(1).WIDER 表示WIDER数据集相关

(2).以后会加入其他类型的训练数据

2.ModelFiles (保存训练好的文件ckpt)

3.Train (训练相关的代码)

4.Test (提供各种测试相关的方法)

5.Result(保存该部分的检测结果)