# 2D ICON Generation with DCGAN DEMO 

This repo is a demo project so that i can learn more about building Generative Adversarial Networks (a very interesting type of nueral net that can prouduce 'fake' out puts). It is inspired by a [youtube video](https://www.youtube.com/watch?v=FlgLxSLsYWQ&t=1034s) about generating gaming assets which help shorten and reduce the time and cost for building a game.

The nueral network take input icons from world of warcraft, a game with longevity :) and the icons has distinctive art style. The nueral net was able to recreate icons with similar art style kinda.

The style and syntax of ml codes is changing rapidly year by year, as of now in  mid 2019. The trends for tf are clearer and easier to read, understand and debuging (with eager_execution). If you come across the repo when you are learning ML, i hope this can help you with your project as a general template :)


![high_level_view_gan](https://github.com/tangtai/2D_ICON_Generation_with_DCGAN_DEMO/blob/master/images/high_level_view_dcgan.png?raw=true)


#### The process the nerual net took to generate icons over 400 epochs with 1000 input icons
FYI: make sure you run dcgans on GPU, it took 3.2 hours to train on a 1070 GPU to process 128  by 128 images. or use colab provided by google, which is easy to setup and free.

![dcgan-gif](https://github.com/tangtai/2D_ICON_Generation_with_DCGAN_DEMO/blob/master/images/dcgan.gif?raw=true)

### Build with

 - python 3.6
 - tensorflow 1.13

### Todos

 - Working DCGAN (Done)
 - Better notes in Notebook
 - Convert to tf 2.0 when the offical version releases
 - demo with tf.js loading trained model


