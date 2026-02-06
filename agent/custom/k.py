# from maa.agent.agent_server import AgentServer
# from maa.custom_action import CustomAction
# from maa.custom_recognition import RecognitionResult
# from maa.context import Context

# import time
# import random

# from .utils import Prompt, Tasker, RecoHelper  # type: ignore

# # 自动挖掘
# colors = ["yellow", "blue", "green"]


# def cnColor(color: str):
#     if color == "yellow":
#         return "黄"
#     if color == "blue":
#         return "蓝"
#     if color == "green":
#         return "绿"


# @AgentServer.custom_action("auto_search")
# class AutoSearch(CustomAction):
#     def run(
#         self, context: Context, argv: CustomAction.RunArg
#     ) -> CustomAction.RunResult | bool:
#         global colors
#         last_deploy = "-1"
#         same_counter = 0
#         try:
#             while True:
#                 # 结束
#                 if Tasker.is_stopping(context):
#                     return False
#                 if check_end(context):
#                     return True
#                 # 检测剩余槽位
#                 groove_num = check_groove(context)
#                 if groove_num == 0:
#                     time.sleep(1)
#                     continue

#                 # 勘探
#                 pairs = exploration(context)

#                 # 挖掘
#                 color = ""
#                 for pair in pairs:
#                     if (
#                         pair["bottom_block"] > 0
#                         and pair["first_faucet"] > 0
#                         and pair["cur_faucet"] < 1
#                     ):
#                         color = pair["color"]
#                         excavation(context, pair["color"])
#                         Prompt.log(f"勘探到 {cnColor(color)}色 可开采岩层")
#                         break

#                 # 二位部署
#                 if color == "" and same_counter > 1:
#                     random.shuffle(pairs)
#                     for pair in pairs:
#                         if (
#                             pair["bottom_block"] > 0
#                             and pair["first_faucet"] > 0
#                             and pair["cur_faucet"] == 1
#                         ):
#                             color = pair["color"]
#                             Prompt.log(f"勘探到 {cnColor(color)}色 可开采岩层")
#                             excavation(context, pair["color"])
#                             same_counter = 0
#                             break

#                 # 临时喷口
#                 if color == "" and same_counter > 1:
#                     random.shuffle(pairs)
#                     for pair in pairs:
#                         if pair["first_faucet"] > 0:
#                             color = pair["color"]
#                             Prompt.log(f"部署临时喷口({cnColor(color)})")
#                             excavation(context, pair["color"])
#                             break

#                 if color == last_deploy:
#                     same_counter += 1
#                 else:
#                     same_counter = 0
#                 last_deploy = color
#                 time.sleep(1)
#         except Exception as e:
#             return Prompt.error("自动挖掘", e)


# # 识别数量
# def exploration(context: Context):
#     reco_helper = RecoHelper(context)
#     pairs = []

#     # 识别数量
#     for color in colors:
#         pair = {"color": color}
#         # 底部砖块数量
#         reco_helper.recognize(
#             "遗迹寻获_底部识别",
#             {"template": f"activity/block/{color}.png", "threshold": 0.82},
#         )
#         pair["bottom_block"] = (
#             len(reco_helper.reco_detail.filterd_results) if reco_helper.hit() else 0
#         )
#         reco_helper.recognize(
#             "遗迹寻获_底部识别",
#             {
#                 "template": [
#                     f"activity/block/{color}-l.png",
#                     f"activity/block/{color}-l2.png",
#                 ],
#                 "threshold": [0.95, 0.96],
#             },
#         )
#         pair["bottom_block"] += (
#             len(reco_helper.reco_detail.filterd_results) * 20
#             if reco_helper.hit()
#             else 0
#         )
#         # 顶部水龙头数量
#         reco_helper.recognize(
#             "遗迹寻获_第一排水龙头识别",
#             {"template": get_faucet_path_list(color)},
#         )
#         pair["first_faucet"] = (
#             len(reco_helper.reco_detail.filterd_results) if reco_helper.hit() else 0
#         )
#         # 现有数量
#         reco_helper.recognize(
#             "遗迹寻获_检测空位",
#             {"template": get_faucet_path_list(color)},
#         )
#         pair["cur_faucet"] = (
#             len(reco_helper.reco_detail.filterd_results) if reco_helper.hit() else 0
#         )

#         pairs.append(pair)

#     # 排序
#     random.shuffle(pairs)
#     pairs.sort(key=lambda x: x["bottom_block"], reverse=True)
#     return pairs


# def get_faucet_path_list(color: str):
#     return [
#         # f"activity/faucet/{color}.png",
#         f"activity/faucet/{color}-l2.png",
#     ]


# # 点击
# def excavation(context: Context, color: str):
#     reco_helper = RecoHelper(context).recognize(
#         "遗迹寻获_第一排水龙头识别", {"template": get_faucet_path_list(color)}
#     )
#     if not reco_helper.hit():
#         return
#     results = reco_helper.reco_detail.filterd_results
#     res = random.choice(results)
#     Tasker.click(context, res.box[0] + 2, res.box[1] + 2)


# # 检测是否还有空位
# def check_groove(context: Context):
#     reco_helper = RecoHelper(context).recognize(
#         "遗迹寻获_检测空位", {"template": "activity/groove.png"}
#     )
#     return len(reco_helper.reco_detail.filterd_results) if reco_helper.hit() else 0


# # 检测是否在输出
# def check_left(context: Context) -> str:
#     reco_helper = RecoHelper(context).recognize("遗迹寻获_检测当前剩余水量")
#     return reco_helper.concat() if reco_helper.hit() else "0"


# # 考察完毕
# def check_end(context: Context):
#     return RecoHelper(context).recognize("遗迹寻获_考察结束").hit()
