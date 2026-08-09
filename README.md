<!-- markdownlint-disable MD033 MD041 -->

<p align="center">
  <img alt="LOGO" src="assets/resource/image/logo.png" width="256" height="256" />
</p>

<div align="center">

# 中文名：辛西娅小助手

## SLIMEIM_Maa

基于MAA框架制作的魔王与龙的建国谭小助手。图像技术 + 模拟控制，解放双手！由 [MaaFramework](https://github.com/MaaXYZ/MaaFramework) 强力驱动！

[点击申请加入小助手交流群](https://qm.qq.com/q/2I8BNwfZQA)

[国内在线文档](https://docs.qq.com/doc/p/2e3559f6b8ad6eb9c9beebe638426d8055307153?nlc=1)

关于其他语言的适配:需日服或其他语言的服的玩家与我联系，我直接远控截图

更多功能敬请期待（提issus）

</div>
<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white">
  <img alt="license" src="https://img.shields.io/github/license/miaojiuqing/SLIMEIM_Maa">
  <img alt="platform" src="https://img.shields.io/badge/platform-Windows-blueviolet">
  <img alt="commit" src="https://img.shields.io/github/commit-activity/m/miaojiuqing/SLIMEIM_Maa">
   <a href="https://mirrorchyan.com/zh/projects?source=maafw-badge&rid=SLIMEIM_Maa" target="_blank"><img alt="mirrorc" src="https://img.shields.io/badge/Mirror%E9%85%B1-%239af3f6?logo=countingworkspro&logoColor=4f46e5"></a>
</p>

  <br/>
</p>
---

## 简介

**SLIMEIM_Maa** 是由miaojiuqing（淼九清）开发的游戏自动化工具，旨在帮助玩家完成每日任务，版本活动及日常琐事。  
**注意：** 本项目仅提供支持亚服的中文的日常自动化操作，部分和其余功能仍在开发和完善中（未来有需求的话会对其他语言进行适配）
**注意：** 本项目推荐使用mumu模拟器(好用)、雷电模拟器，其他模拟器没测过
**若您是湾湾玩家注意：** 可能需要自行将 SLIMEIM\MaaSLIMEIM-win-x86_64\resource\pipeline\awa 这个文件夹删除

**对了：** Google playdate也是个模拟器，但是没adb，要用的话得用UI提供的win32开全屏食用，但是我还是建议你下mumu

[视频链接](https://www.bilibili.com/video/BV1gPjiz5EbQ/?spm_id_from=333.1387.homepage.video_card.click&vd_source=49383a2ec38e99b49eb1e3f17c256fb9)

---

## 主要功能

### 启动

- [x] 启动游戏并打开菜单
- [x] 关闭游戏

### 日常

- [x] 送礼角色好感度（可选指定角色/礼物，或自动找低好感角色）
- [x] 每日城镇角色对话（仅对话当前所在城镇的角色）
- [x] 锻造场升级任务（含当期活动装备制造）
- [x] 建筑设施申请支援任务（可地区/类别/时间排序筛选）
- [x] 捕食战（可自选捕食类型，支持自动切换上级难度）
  - [x] 心体
  - [x] 猛攻
  - [x] 坚守
  - [x] 转魂
- [x] 贸易（使用贸易票据购买心之书、武器材料等商品）
- [x] 魔王龙道（每日奖励关）
- [x] 领取日常任务奖励

### 琐事

- [x] 生产资源统一领取
- [x] 泡温泉领取体力
- [x] 进联盟签到and领取奖励
- [x] 邮箱内奖励领取
- [x] 一并支援奖励领取
- [x] 好友设施支援奖励
- [x] 果盘奖励领取

### 单独运行任务

- [x] 选章节自动过主线（支持第1章~第31章）
- [x] 自动刷关（支持主线模式、多关卡模式、连战，可自选编队）
- [x] 单副本一直刷（在战斗途中或编队界面启动，可选吃不吃体力药，支持生存战模式）
- [x] 列表关卡自动刷（在关卡列表启动，支持主线模式/多关卡模式/宽松模式/编队选择）
- [x] 盖德监工（自动建国设施升级建造，支持地区/类别/时间筛选、无限模式）
- [x] 商店清空（自动购买有购买限制的商品，请先在商店界面启动）
- [x] **复刻活动：魔国祭典** — 全自动祭典举办，包含：
  - 祭典举办策略（打折体力用完即停 / 无限开庆典）
  - 奖励上限自动停止
  - 任命策略设置（活力值 / 摊位优先级 / 角色优先级 / 角色状况）
  - 体力不足处理（回体 / 返回首页）

### 活动期间

- [x] 版本活动期间每日的20次并列演算（含月卡模式、自动编队、中断继续任务）
- [x] 版本活动期间每日的3次捕食战（结束后可选自动接续并列演算）
- [x] 自定义编队（支持十组编队切换，可配置切换方式）

### 英杰盃

- [x] **一般战** — 自动循环挑战，支持以下功能：
  - 挑战者选择（上/中/下三档，对应不同奖杯数量）
  - 编队选择（十组编队自由切换）
  - 战斗状态检测与自动处理（胜利/失败/升段/应援团）
  - 战斗方式切换（自动/手动战斗切换）
- [x] **挑战卷管理** — 挑战卷耗尽后可选：
  - 结束任务返回主菜单 + 自动领取功绩奖励
  - 使用英杰盃参加卷继续战斗
- [x] **投降速刷** — 进去直接投降，适用于已上大师积分溢出的用户快速获取魔晶，无阵容需求
- [x] **自动战斗** — 原地等战斗结束，自动开下一把，自行切换为自动战斗状态，推荐无敌命击复活队

<details>
<summary>已废弃 — 公式化战斗逻辑（旧版配队参考）</summary>

> 当前版本已使用通用战斗流程替代。以下为旧版本公式化战斗的配队思路，仅供参考：

**公式化战斗逻辑所需阵容**
![公式化战斗逻辑配队思路](<https://s21.ax1x.com/2025/06/15/pVAIVrq.png>)

- 加护位：
  - 速攻加护 如：妖狐化紫鬼·紫菀/优雅幻魔·维尔萨泽/赤焰八星魔王·金·克林姆兹等
  - 任意前三回合能每回合给30技能点的加护
- 前三位：
  - 防御位：盛装美人·夕紫叶·伊札瓦（光静）/影渡密探·苍影
  - 辅助buff位：绊之进化-辛西娅
  - 自卡转全能：魔道阴阳师·利姆露
- 后两位：
  - 5号位放自卡三转工具人：如芙莉萌，泳装日向，花嫁朱莱等
  - 6号位放任意AOE主C：如2.5光萌，封面画风露米，怪盗小黑

**关于第三回合技能自选**
![公式化战斗逻辑可选技能图标](<https://s21.ax1x.com/2025/08/23/pVrSsu8.png>)

</details>

### 梦幻镜魔境

- [x] 帮你用掉镜塔体力和刷镜塔资源，单层重复刷，性价比最高的是四十几层
- [x] 路线优先级选择（奖励 > buff > 战斗 > 传送，或自定义优先级）
- [x] 考验选择 & 战斗中开始任务支持
- [x] 体力不足处理 & 编队选择

### 作者告诫

- 本助手完全免费，没有任何收费的地方！！！！！！！！！！！！！！！！！！！！如果你是买来的请举报并拉黑商家顺便告诉我谁卖的
- 请注意!!!**以上任务的运行基本都基于菜单界面才能开始运行**，等有除了我以外的用户反馈了的话会考虑优化（希望游戏能活到那个时候）
- 其余任务（没啥活了其他都是高难本作者（英杰盃稳亚洲前百）都打不过,更多诉求请加Q群：855795905|[点击快速加群](https://qm.qq.com/q/2I8BNwfZQA)）

1. 点击链接下载最新[Release](https://github.com/miaojiuqing/SLIMEIM_Maa/releases)包

2.安装运行环境
-Windows

·对于Windows需要在运行前安装运行库。

-需要 VCRedist x64 (cli与gui都需要) 和 .NET 8 (仅使用gui时需要)。 点击 vc_redist.x64 下载安装 VCRedist x64，点击 dotnet-sdk-8.0.5-win-x64.exe 下载安装.NET 8。 也可以右键开始按钮打开终端

    winget install Microsoft.VCRedist.2017.x64 Microsoft.DotNet.DesktopRuntime.8

在终端内粘贴以上命令回车以进行安装。
3. 解压后双击`MFAAvalonia.exe`即可运行

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

- 提示"应用程序错误"，一般是缺少运行库，请尝试安装 [vc_redist](https://aka.ms/vs/17/release/vc_redist.x64.exe)
- 添加 `-d` 参数可跳过交互直接运行任务，如 `./MaaPiCli.exe -d`
- MAA framework 2.0 版本已支持 mumu 后台保活，会在 run task 时获取 mumu 最前台的 tab
- 反馈问题请附上日志文件 `debug/maa.log`以及问题界面的截图，谢谢！

## 关于新版mumu模拟器如何连接

近期 MuMu 模拟器 5.0 正在进行内测，并预计将于 6 月 20 日起陆续开放下载。此次 MuMu 新版本修改了 adb路径、模拟器程序名及安装路径。
在更新了 MuMu 5.0 后
若使用 MuMu 的默认 adb，须重新检测或手动修改 MAA 中的 ｢设置 - 连接设置 - ADB 路径｣
原路径：{安装目录}\shell\adb.exe
新路径：{安装目录}\nx_main\adb.exe

若开启自动启动模拟器，须重新设置 ｢设置 - 启动设置 - 模拟器路径｣。
原路径：{安装目录}\shell\MuMuPlayer.exe
新路径：{安装目录}\nx_device\12.0\shell\MuMuNxDevice.exe

## 免责声明

本软件开源、免费，仅供学习交流使用。若您遇到商家使用本软件进行代练并收费，可能是分发、设备或时间等费用，产生的费用、问题及后果与本项目无关。

在使用过程中，SLIMEIM_Maa 可能存在任何意想不到的 Bug，因 SLIMEIM_Maa 自身漏洞、文本理解有歧义、异常操作导致的账号问题等开发组不承担任何责任，请在确保在阅读完用户手册、自行尝试运行效果后谨慎使用！

只能说同类型项目没有被封案例，但是谁也无法保证百分之百不会被判定为外挂

游玩带有辅助检测的竞技类游戏（如CSGO，瓦罗兰特等）时，请尽量不要同时使用本助手

## 常用工具

1. 调试：[MaaDebugger](https://github.com/MaaXYZ/MaaDebugger) 进行调试json节点.
2. 截图、取色、取区域: [MFATools](https://github.com/SweetSmellFox/MFATools)

## 鸣谢

本项目由 **[MaaFramework](https://github.com/MaaXYZ/MaaFramework)** 强力驱动！

感谢以下开发者对本项目作出的贡献:

还有开发群里的各位都很感谢

<a href="https://github.com/miaojiuqing/SLIMEIM_Maa/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=miaojiuqing/SLIMEIM_Maa&max=1000" alt="Contributors to SLIMEIM_Maa"/>
</a>
