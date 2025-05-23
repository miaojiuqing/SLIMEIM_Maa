<!-- markdownlint-disable MD033 MD041 -->

<p align="center">
  <img alt="LOGO" src="logo.png" width="256" height="256" />
</p>

<div align="center">

## SLIMEIM_Maa

基于MAA框架制作的魔王与龙的建国谭小助手。图像技术 + 模拟控制，解放双手！
由 [MaaFramework](https://github.com/MaaXYZ/MaaFramework) 强力驱动！
目前已能在大部分情况下稳定运行三四个日常任务
</div>
<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white">
  我不会填我先写个python后面补上（
</p>
---

## 简介

**SLIMEIM_Maa** 是由miaojiuqing开发的游戏自动化工具，旨在帮助玩家完成每日任务，和以后会添加的一些小活动。  
**注意：** 本项目仅提供每日任务自动化操作，部分和其余功能仍在开发和完善中。  
**注意：** 本项目推荐使用mumu模拟器，其他模拟器没测过

---

## 主要功能

- [x] 启动游戏并打开菜单
- [x] 喂食(bushi)送礼角色
- [x] 每日城镇角色对话（仅对话当前所在城镇的角色）
- [x] 锻造场升级任务
- [x] 建筑设施申请支援任务
- [x] 捕食战（不稳定）
  - [x] 心体
  - [x] 猛攻
  - [x] 坚守
  - [x] 转魂
- [x] 领取日常奖励
- 其余任务（如镜塔和英桀杯战斗正在开发中）

1. 点击链接下载最新[Release](https://github.com/miaojiuqing/SLIMEIM_Maa/releases)包

2. 解压后双击`MFAAvalonia.exe`即可运行
    可以通过创建快捷方式之后，右键该快捷方式,点击属性自行更改图标

### Windows

- 对于绝大部分用户，请下载 MaaSLIMEIM-win-x86_64.zip
- 若确定自己的电脑是 arm 架构，请下载 MaaSLIMEIM-win-x86_64.zip
- 请注意！Windows 的电脑几乎全都是 x86_64 的，可能占 99.999%，除非你非常确定自己是 arm，否则别下这个！_
- 解压后运行 MFAAvalonia.exe（图形化界面，推荐使用，老版本UI为MFAWPF.exe）或 MaaPiCli.exe（命令行）即可

### macOS

没接触过

### Linux

都用Linux了一定是大佬，大佬会自己改的（确信

## 图形化界面

- <span style="font-size:25px;">[MFAAvalonia](https://github.com/SweetSmellFox/MFAAvalonia/)</span>  
- 由社区大佬[SweetSmellFox](https://github.com/SweetSmellFox)编写的基于Avalonia的GUI,通过内置的MAAframework来直接控制任务流程  
- 打开本程序和模拟器后，先在右上方选择要控制的模拟器  
- 勾选想要执行的任务后**开始任务**，任务会顺序执行，所有任务都需要游戏为开启状态  
- 点击部分任务右方的设置，可以配置任务属性

## 注意事项

- 提示“应用程序错误”，一般是缺少运行库，请尝试安装 [vc_redist](https://aka.ms/vs/17/release/vc_redist.x64.exe)
- 添加 `-d` 参数可跳过交互直接运行任务，如 `./MaaPiCli.exe -d`（这段话啥意思不是很清楚我这个网页用别人的改的
- MAA framework 2.0 版本已支持 mumu 后台保活，会在 run task 时获取 mumu 最前台的 tab
- 反馈问题请附上日志文件 `debug/maa.log`以及问题界面的截图，谢谢！

## 鸣谢

本项目由 **[MaaFramework](https://github.com/MaaXYZ/MaaFramework)** 强力驱动！

感谢以下开发者对本项目作出的贡献:
怎么把ERR_OverFlow佬加进去（
[![Contributors]](https://github.com/miaojiuqing/SLIMEIM_Maa/graphs/contributors)
