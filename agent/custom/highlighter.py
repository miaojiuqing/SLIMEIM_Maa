import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from maa.agent.agent_server import AgentServer
from maa.custom_recognition import CustomRecognition
from maa.context import Context
from maa.custom_recognition import RecognitionResult
import cv2
import numpy as np

from utils import Prompt, Tasker, RecoHelper

# 此段为obj绿色掩码调用
green_mask_enabled = "green_mask"
run_task: green_mask = "greem_mask = trun"


@AgentServer.custom_recognition("HighlightedIconRecognizer")
class HighlightedIconRecognizer(CustomRecognition):
    def analyze(self, context: Context, argv: dict) -> RecognitionResult:
        # 初始化结果
        green_mask_enabled
        result = RecognitionResult()
        result.box = [0, 0, 0, 0]  # 默认空区域
        result.score = 0.0
        result.success = False

        # 从参数中获取配置
        template_path = argv.get("template", "")
        threshold = argv.get("threshold", 0.8)
        hsv_low = argv.get("hsv_low", [0, 100, 100])
        hsv_high = argv.get("hsv_high", [180, 255, 255])
        execute_task = argv.get("execute_task", False)
        task_name = argv.get("task_name", "")

        try:
            # 获取当前屏幕截图
            controller = context.get_controller()
            if not controller:
                Prompt.error("无法获取控制器")
                return result

            screenshot = controller.get_image()
            if screenshot is None or screenshot.size == 0:
                Prompt.error("无法获取屏幕截图")
                return result

            # 获取ROI区域
            roi = argv.get("roi", None)
            x, y = 0, 0
            if roi and len(roi) == 4:
                x, y, w, h = roi
                # 确保ROI在截图范围内
                x = max(0, min(x, screenshot.shape[1]))
                y = max(0, min(y, screenshot.shape[0]))
                w = max(0, min(w, screenshot.shape[1] - x))
                h = max(0, min(h, screenshot.shape[0] - y))
                roi_image = screenshot[y : y + h, x : x + w]
            else:
                roi_image = screenshot

            # 如果没有提供模板路径，则返回
            if not template_path:
                Prompt.error("未提供模板路径")
                return result

            # 加载模板图像
            template = cv2.imread(template_path)
            if template is None:
                Prompt.error(f"无法加载模板图像: {template_path}")
                return result

            # 确保模板和ROI图像大小兼容
            if (
                template.shape[0] > roi_image.shape[0]
                or template.shape[1] > roi_image.shape[1]
            ):
                Prompt.error("模板尺寸大于ROI区域")
                return result

            # 执行模板匹配
            result_template = cv2.matchTemplate(
                roi_image, template, cv2.TM_CCOEFF_NORMED
            )
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result_template)

            # 检查匹配阈值
            if max_val < threshold:
                Prompt.debug(f"模板匹配未通过阈值: {max_val} < {threshold}")
                return result

            # 获取匹配区域
            h, w = template.shape[:2]
            top_left = max_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)

            # 提取匹配区域图像
            matched_region = roi_image[
                top_left[1] : bottom_right[1], top_left[0] : bottom_right[0]
            ]

            # 转换到HSV颜色空间
            hsv = cv2.cvtColor(matched_region, cv2.COLOR_BGR2HSV)

            # 创建颜色掩码
            lower = np.array(hsv_low, dtype=np.uint8)
            upper = np.array(hsv_high, dtype=np.uint8)
            mask = cv2.inRange(hsv, lower, upper)

            # 检查是否有高亮颜色（非零像素存在）并且模板匹配成功
            if cv2.countNonZero(mask) > 0:
                Prompt.log(f"发现高亮图标: 匹配分数={max_val:.2f}")

                # 更新结果
                result.box = [x + top_left[0], y + top_left[1], w, h]  # 转换为全局坐标
                result.score = max_val
                result.success = True

                # 如果需要执行任务
                if execute_task and task_name:
                    if Tasker.start_task(context, task_name):
                        Prompt.log(f"执行任务成功: {task_name}")
                    else:
                        Prompt.error(f"执行任务失败: {task_name}")
        except Exception as e:
            Prompt.error(f"分析过程中发生错误", e)
            result.success = False

        return result
