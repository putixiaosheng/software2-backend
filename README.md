# README

## 项目所属课程

| 计算器               |                                         |
| -------------------- | --------------------------------------- |
| 这个作业属于拿个课程 | https://bbs.csdn.net/forums/ssynkqtd-05 |
| 这个作业要求在哪里   | https://bbs.csdn.net/topics/617377308   |
| 这个作业的目标       | 继续完善计算器并且实现前后端分离        |
| 其他参考文献         | 无                                      |



## 项目运行

项目运行解释器为 __python3.7__，并采用__Django__框架

* 项目运行前安装__Django__框架并导入__restframework__

```python
pip install djangorestframework
```

* 导入__mysqlclient__

```python
pip install mysqlclient
```



## 功能简介

本项目设计的是一个的计算器后端实现，在实现普通计算器和科学计算器功能的基础上，提供利息计算和利率修改的功能。项目请求的发送全部基于本地实现。



## 接口设计

* user/first/

  get请求用于获取用户计算历史记录

  post请求用户用户上传算式并获取结果

* user/second/

  get请求用于获取存款利率

  post请求用于修改存款利率

* user/three/

  get请求用于获取借款利率

  post请求用于修改借款利率