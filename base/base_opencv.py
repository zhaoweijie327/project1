import cv2

class FindOpencv:

    def find_opencv(self,target='/image/target.jpg',template='/image/template.jpg'):
        '''
        从背景图里面找到模块图片位置
        :param target: 背景图
        :param template:模块图
        :return: X像素
        '''
        # 用RGB模式去读取背景图
        target_rgb = cv2.imread(target)
        # 灰度处理
        target_gray = cv2.cvtColor(target_rgb,cv2.COLOR_RGB2GRAY)
        # 用RGB读取模块图片
        template_rgb = cv2.imread(template,0)
        # 去匹配模块在背景图里面的位置
        lo = cv2.matchTemplate(target_gray,template_rgb,cv2.TM_CCOEFF_NORMED)
        # 获取匹配后的坐标
        value = cv2.minMaxLoc(lo)
        return value[2][0]

    def find_return(self,target=None,template=None,
                    x_1=280,x_2=680,x_3=27):
        x = self.find_opencv(target,template)
        # 处理缩放
        return int(x * x_1 / x_2) - x_3