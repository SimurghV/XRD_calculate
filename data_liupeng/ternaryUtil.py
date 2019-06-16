import ternary
from cluster import cluster_main
from utils.plotUtils import ternaryUtil
import datetime

class ternaryPlot():
    def __init__(self, title='', left_lable='', right_lable='', bottom_lable=''):
        self.title = title
        self.left_lable = left_lable
        self.right_lable = right_lable
        self.bottom_lable = bottom_lable
    def multiPointsTernary(self, coorsList):
        """
        multiPointsTernary
            把多个点用同一种颜色画在同一张相图上，不考虑分成多种相区的事情
            coorsList的数据结构
                注意（x,y,z）分别代表的是Fe，Cr，Ni的成分
                coorsList=[
                            [x0, y0, z0],
                            [x1, y1, z1],
                            [x2, y2, z2],
                            ...
                            [xn, yn, zn]
                            ]
        """
        scale = 10
        figure, tax = ternary.figure(scale=scale)
        tax.ax.axis("off")
        figure.set_facecolor('w')
        # Draw Boundary and Gridlines
        tax.boundary(linewidth=1.0)
        tax.gridlines(color="black", multiple=1, linewidth=0.5, ls='-')
        # Set Axis labels and Title
        fontsize = 16
        tax.left_axis_label(self.left_lable, fontsize=fontsize, offset=0.13)
        tax.right_axis_label(self.right_lable, fontsize=fontsize, offset=0.12)
        tax.bottom_axis_label(self.bottom_lable, fontsize=fontsize, offset=0.06)
        tax.set_axis_limits({'b': [0, 100], 'l': [0, 100], 'r': [0, 100]})
        # get and set the custom ticks:
        tax.get_ticks_from_axis_limits()
        tax.set_custom_ticks(fontsize=10, offset=0.02)

        colorList = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'tomato', 'aquamarine', 'blueviolet', 'darkgrey', 'firebrick', 'hotpink']
        markerList = ['.', 'o', 'v', '^', '1', '3', '8', 'p', '*', 'h', 'D', '+', 's']

        points = []
        for coor in coorsList:
            # tuple(Ni, Cr, Fe)---brl
            points.append((coor[2]*100,coor[1]*100,coor[0]*100))
        points_c = tax.convert_coordinates(points, axisorder='brl')
        tax.scatter(points_c, marker=markerList[2], s=25, c=colorList[2])

        plotTitle = self.title
        tax.set_title(plotTitle)
        tax.ax.set_aspect('equal', adjustable='box')
        tax._redraw_labels()
        ternary.plt.show()
    def smallTernary(self, ternaryPointsList):
        """
        smallTernary
            画出整幅相图，将不同组别的点染上不同的颜色
            ternaryPointsList的数据结构
                注意（x,y,z）分别代表的是Fe，Cr，Ni的成分
                ternaryPointsList = [
                                      [
                                        [x0, y0, z0],
                                        [x1, y1, z1],
                                        [x2, y2, z2],
                                        ...
                                        [xn, yn, zn]
                                      ],
                                      [
                                        [x0, y0, z0],
                                        [x1, y1, z1],
                                        [x2, y2, z2],
                                        ...
                                        [xn, yn, zn]
                                      ],
                                      ...
                                      [
                                        [x0, y0, z0],
                                        [x1, y1, z1],
                                        [x2, y2, z2],
                                        ...
                                        [xn, yn, zn]
                                      ]
                                        ]
        """
        scale = 10
        figure, tax = ternary.figure(scale=scale)
        tax.ax.axis("off")
        figure.set_facecolor('w')
        # Draw Boundary and Gridlines
        tax.boundary(linewidth=1.0)
        tax.gridlines(color="black", multiple=1, linewidth=0.5, ls='-')
        # Set Axis labels and Title
        fontsize = 16
        tax.left_axis_label(self.left_lable, fontsize=fontsize, offset=0.13)
        tax.right_axis_label(self.right_lable, fontsize=fontsize, offset=0.12)
        tax.bottom_axis_label(self.bottom_lable, fontsize=fontsize, offset=0.06)
        tax.set_axis_limits({'b': [0, 25], 'l': [75, 100], 'r': [0, 25]})
        # get and set the custom ticks:
        tax.get_ticks_from_axis_limits()
        tax.set_custom_ticks(fontsize=10, offset=0.02)

        colorList = ['g', 'k', 'r']
        markerList = ['.', 'o', 'v', '^', '1', '3', '8', 'p', '*', 'h', 'D', '+', 's']

        count = 0
        ternaryPointsList.sort(key=compareLength)
        for coors in ternaryPointsList:
            points = []
            for coor in coors:
                # tuple(Ni, Cr, Fe)---brl
                points.append((coor[2] * 100, coor[1] * 100, coor[0] * 100,))
            points_c = tax.convert_coordinates(points, axisorder='brl')
            tax.scatter(points_c, marker=markerList[count], s=50, c=colorList[count])
            count += 1

        plotTitle = self.title
        tax.set_title(plotTitle)
        tax.ax.set_aspect('equal', adjustable='box')
        tax._redraw_labels()
        ternary.plt.show()
    def small_refined_ternary(self, ternaryPointsList):
        scale = 10
        figure, tax = ternary.figure(scale=scale)
        tax.ax.axis("off")
        figure.set_facecolor('w')
        # Draw Boundary and Gridlines
        tax.boundary(linewidth=1.0)
        tax.gridlines(color="black", multiple=1, linewidth=0.5, ls='-')
        # Set Axis labels and Title
        # fontsize = 16
        fontsize = 25
        tax.left_axis_label(self.left_lable, fontsize=fontsize, offset=0.13)
        tax.right_axis_label(self.right_lable, fontsize=fontsize, offset=0.12)
        tax.bottom_axis_label(self.bottom_lable, fontsize=fontsize, offset=0.06)
        tax.set_axis_limits({'b': [0, 25], 'l': [75, 100], 'r': [0, 25]})
        # get and set the custom ticks:
        tax.get_ticks_from_axis_limits()
        # tax.set_custom_ticks(fontsize=10, offset=0.02)
        tax.set_custom_ticks(fontsize=20, offset=0.02)

        # python中matplotlib的颜色及线条控制:https://www.cnblogs.com/darkknightzh/p/6117528.html
        colorList = ['r', 'b', 'g']
        # markerList = ['.', 'o', 'v', '^', '1', '3', '8', 'p', '*', 'h', 'D', '+', 's']
        markerList = ['o']

        count = 0
        ternaryPointsList.sort(key=compareLength)
        for coors in ternaryPointsList:
            points = []
            for coor in coors:
                # tuple(Ni, Cr, Fe)---brl
                points.append((coor[2] * 100, coor[1] * 100, coor[0] * 100,))
            points_c = tax.convert_coordinates(points, axisorder='brl')
            tax.scatter(points_c, marker=markerList[0], s=150, c=colorList[count])
            count += 1

        plotTitle = self.title
        tax.set_title(plotTitle)
        tax.ax.set_aspect('equal', adjustable='box')
        tax._redraw_labels()
        ternary.plt.show()
    def hugeTernary(self, ternaryPointsList):
        """
        hugeTernary
            画出右侧较大的局部相图，将不同组别的点染上不同的颜色
            ternaryPointsList的数据结构
                注意（x,y,z）分别代表的是Fe，Cr，Ni的成分
                ternaryPointsList = [
                                      [
                                        [x0, y0, z0],
                                        [x1, y1, z1],
                                        [x2, y2, z2],
                                        ...
                                        [xn, yn, zn]
                                      ],
                                      [
                                        [x0, y0, z0],
                                        [x1, y1, z1],
                                        [x2, y2, z2],
                                        ...
                                        [xn, yn, zn]
                                      ],
                                      ...
                                      [
                                        [x0, y0, z0],
                                        [x1, y1, z1],
                                        [x2, y2, z2],
                                        ...
                                        [xn, yn, zn]
                                      ]
                                        ]
        """
        scale = 10
        figure, tax = ternary.figure(scale=scale)
        tax.ax.axis("off")
        figure.set_facecolor('w')
        # Draw Boundary and Gridlines
        tax.boundary(linewidth=1.0)
        tax.gridlines(color="black", multiple=1, linewidth=0.5, ls='-')
        # Set Axis labels and Title
        fontsize = 16
        tax.left_axis_label(self.left_lable, fontsize=fontsize, offset=0.13)
        tax.right_axis_label(self.right_lable, fontsize=fontsize, offset=0.12)
        tax.bottom_axis_label(self.bottom_lable, fontsize=fontsize, offset=0.06)
        tax.set_axis_limits({'b': [30, 100], 'l': [0, 70], 'r': [0, 70]})
        # get and set the custom ticks:
        tax.get_ticks_from_axis_limits()
        tax.set_custom_ticks(fontsize=10, offset=0.02)

        colorList = ['k', 'g',]
        markerList = ['o', 'v','.',  '^', '1', '3', '8', 'p', '*', 'h', 'D', '+', 's']

        count = 0
        ternaryPointsList.sort(key=compareLength)
        for coors in ternaryPointsList:
            points = []
            for coor in coors:
                # tuple(Ni, Cr, Fe)---brl
                points.append((coor[2] * 100, coor[1] * 100, coor[0] * 100,))
            points_c = tax.convert_coordinates(points, axisorder='brl')
            tax.scatter(points_c, marker=markerList[count], s=25, c=colorList[count])
            count += 1

        plotTitle = self.title
        tax.set_title(plotTitle)
        tax.ax.set_aspect('equal', adjustable='box')
        tax._redraw_labels()
        ternary.plt.show()
    def huge_refined_ternary(self, ternaryPointsList):
        scale = 10
        figure, tax = ternary.figure(scale=scale)
        tax.ax.axis("off")
        figure.set_facecolor('w')
        # Draw Boundary and Gridlines
        tax.boundary(linewidth=1.0)
        tax.gridlines(color="black", multiple=1, linewidth=0.5, ls='-')
        # Set Axis labels and Title
        fontsize = 25
        tax.left_axis_label(self.left_lable, fontsize=fontsize, offset=0.13)
        tax.right_axis_label(self.right_lable, fontsize=fontsize, offset=0.12)
        tax.bottom_axis_label(self.bottom_lable, fontsize=fontsize, offset=0.06)
        tax.set_axis_limits({'b': [30, 100], 'l': [0, 70], 'r': [0, 70]})
        # get and set the custom ticks:
        tax.get_ticks_from_axis_limits()
        tax.set_custom_ticks(fontsize=20, offset=0.02)

        colorList = ['g', 'b',]
        # markerList = ['o', 'v','.',  '^', '1', '3', '8', 'p', '*', 'h', 'D', '+', 's']
        markerList = ['o']

        count = 0
        ternaryPointsList.sort(key=compareLength)
        for coors in ternaryPointsList:
            points = []
            for coor in coors:
                # tuple(Ni, Cr, Fe)---brl
                points.append((coor[2] * 100, coor[1] * 100, coor[0] * 100,))
            points_c = tax.convert_coordinates(points, axisorder='brl')
            tax.scatter(points_c, marker=markerList[0], s=50, c=colorList[count])
            count += 1

        plotTitle = self.title
        tax.set_title(plotTitle)
        tax.ax.set_aspect('equal', adjustable='box')
        tax._redraw_labels()
        ternary.plt.show()
    def c_refined_ternary(self, ternaryPointsList):
        scale = 10
        figure, tax = ternary.figure(scale=scale)
        tax.ax.axis("off")
        figure.set_facecolor('w')
        # Draw Boundary and Gridlines
        tax.boundary(linewidth=1.0)
        tax.gridlines(color="black", multiple=1, linewidth=0.5, ls='-')
        # Set Axis labels and Title
        fontsize = 25
        tax.left_axis_label(self.left_lable, fontsize=fontsize, offset=0.13)
        tax.right_axis_label(self.right_lable, fontsize=fontsize, offset=0.12)
        tax.bottom_axis_label(self.bottom_lable, fontsize=fontsize, offset=0.06)
        tax.set_axis_limits({'b': [0, 100], 'l': [0, 100], 'r': [0, 100]})
        # get and set the custom ticks:
        tax.get_ticks_from_axis_limits()
        tax.set_custom_ticks(fontsize=20, offset=0.02)

        colorList = ['b', 'r','g']
        # markerList = ['o', 'v','.',  '^', '1', '3', '8', 'p', '*', 'h', 'D', '+', 's']
        markerList = ['o']

        count = 0
        ternaryPointsList.sort(key=compareLength)
        for coors in ternaryPointsList:
            points = []
            for coor in coors:
                # tuple(Ni, Cr, Fe)---brl
                points.append((coor[2] * 100, coor[1] * 100, coor[0] * 100,))
            points_c = tax.convert_coordinates(points, axisorder='brl')
            tax.scatter(points_c, marker=markerList[0], s=50, c=colorList[count])
            count += 1

        plotTitle = self.title
        tax.set_title(plotTitle)
        tax.ax.set_aspect('equal', adjustable='box')
        tax._redraw_labels()
        ternary.plt.show()
    def wholeTernary(self, ternaryPointsList):
        """
        wholeTernary
            画出整幅相图，将不同组别的点染上不同的颜色
            ternaryPointsList的数据结构
                注意（x,y,z）分别代表的是Fe，Cr，Ni的成分
                ternaryPointsList = [
                                      [
                                        [x0, y0, z0],
                                        [x1, y1, z1],
                                        [x2, y2, z2],
                                        ...
                                        [xn, yn, zn]
                                      ],
                                      [
                                        [x0, y0, z0],
                                        [x1, y1, z1],
                                        [x2, y2, z2],
                                        ...
                                        [xn, yn, zn]
                                      ],
                                      ...
                                      [
                                        [x0, y0, z0],
                                        [x1, y1, z1],
                                        [x2, y2, z2],
                                        ...
                                        [xn, yn, zn]
                                      ]
                                        ]
        """
        scale = 10
        figure, tax = ternary.figure(scale=scale)
        tax.ax.axis("off")
        figure.set_facecolor('w')
        # Draw Boundary and Gridlines
        tax.boundary(linewidth=1.0)
        tax.gridlines(color="black", multiple=1, linewidth=0.5, ls='-')
        # Set Axis labels and Title
        fontsize = 16
        tax.left_axis_label(self.left_lable, fontsize=fontsize, offset=0.13)
        tax.right_axis_label(self.right_lable, fontsize=fontsize, offset=0.12)
        tax.bottom_axis_label(self.bottom_lable, fontsize=fontsize, offset=0.06)
        tax.set_axis_limits({'b': [0, 100], 'l': [0, 100], 'r': [0, 100]})
        # get and set the custom ticks:
        tax.get_ticks_from_axis_limits()
        tax.set_custom_ticks(fontsize=10, offset=0.02)

        colorList = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'tomato', 'aquamarine', 'blueviolet', 'darkgrey', 'firebrick', 'hotpink']
        markerList = ['.', 'o', 'v', '^', '1', '3', '8', 'p', '*', 'h', 'D', '+', 's']

        count = 0
        for coors in ternaryPointsList:
            points = []
            for coor in coors:
                # tuple(Ni, Cr, Fe)---brl
                points.append((coor[2]*100,coor[1]*100,coor[0]*100,))
            points_c = tax.convert_coordinates(points, axisorder='brl')
            tax.scatter(points_c, marker=markerList[count % 11], s=25, c=colorList[count % 11])
            count += 1

        plotTitle = self.title
        tax.set_title(plotTitle)
        tax.ax.set_aspect('equal', adjustable='box')
        tax._redraw_labels()
        ternary.plt.show()
    def whole_refined_ternary(self, ternaryPointsList):
        scale = 10
        figure, tax = ternary.figure(scale=scale)
        tax.ax.axis("off")
        figure.set_facecolor('w')
        # Draw Boundary and Gridlines
        tax.boundary(linewidth=1.0)
        tax.gridlines(color="black", multiple=1, linewidth=0.5, ls='-')
        # Set Axis labels and Title
        fontsize = 25
        tax.left_axis_label(self.left_lable, fontsize=fontsize, offset=0.13)
        tax.right_axis_label(self.right_lable, fontsize=fontsize, offset=0.12)
        tax.bottom_axis_label(self.bottom_lable, fontsize=fontsize, offset=0.06)
        tax.set_axis_limits({'b': [0, 100], 'l': [0, 100], 'r': [0, 100]})
        # get and set the custom ticks:
        tax.get_ticks_from_axis_limits()
        tax.set_custom_ticks(fontsize=20, offset=0.02)

        colorList = ['g','b','r']
        # markerList = ['o', 'v','.',  '^', '1', '3', '8', 'p', '*', 'h', 'D', '+', 's']
        markerList = ['o']

        count = 0
        ternaryPointsList.sort(key=compareLength)
        for coors in ternaryPointsList:
            points = []
            for coor in coors:
                # tuple(Ni, Cr, Fe)---brl
                points.append((coor[2] * 100, coor[1] * 100, coor[0] * 100,))
            points_c = tax.convert_coordinates(points, axisorder='brl')
            tax.scatter(points_c, marker=markerList[0], s=50, c=colorList[count])
            count += 1

        plotTitle = self.title
        tax.set_title(plotTitle)
        tax.ax.set_aspect('equal', adjustable='box')
        tax._redraw_labels()
        ternary.plt.show()
    """
    由于上交的方法（pattern直接转化成向量）画图的结果会与我的不同，添加两个新的画图函数
    """
    def sj_small_refined_ternary(self, ternaryPointsList):
        pass
    def sj_huge_refined_ternary(self, ternaryPointsList):
        pass
    def sj_c_refined_ternary(self, ternaryPointsList):
        pass
def compareLength(dataList):
    return -len(dataList)
# if __name__ == '__main__':
#     ternaryPlot(title='Test Ternary',left_lable='Fe', right_lable='Cr', bottom_lable='Ni').multiPointsTernary([[0,0,1]])
"""
manualTernaryPlot
    根据手动分析的数据绘制相图
    smallTer
        包含数据（对应点的实验序号）
        绘制左侧小相图
    hugeTer
        包含数据（对应点的实验序号）
        绘制右侧小相图
"""
class manualTernaryPlot():
    def __init__(self):
        # 这些点的编号是从手动识别的excel表中直接摘抄的
        # 以下是2018-12-24人工识别的结果，根据画出来的图形，两相区的区域太大，应该加强对γ相峰强度的要求，弱峰就不算了
        # self.small_alpha_phase_seqList = [[37, 19], [37, 20], [37, 21], [38, 19], [38, 20], [38, 21], [38, 22], [39, 20],
        #                                 [39, 21], [39, 22], [40, 20], [40, 21], [40, 22], [40, 23], [41, 21], [41, 22],
        #                              [41, 23], [42, 21], [42, 22], [42, 23], [43, 22], [43, 23], [43, 24], [43, 25],
        #                              [47, 24], [47, 25], [47, 26], [47, 27], [48, 25], [48, 26], [49, 25], [49, 26],
        #                              [44, 23], [44, 24], [44, 25], [45, 23], [45, 24], [45, 25], [46, 24], [46, 25],
        #                              [49, 27], [49, 28], [50, 26], [50, 27]]
        # self.small_gamma_phase_seqList = [[37, 25], [38, 25], [39, 25], [39, 26], [41, 27], [42, 28], [42, 29], [42, 30],
        #                              [43, 28], [43, 29]]
        # self.small_double_phase_seqList = [[37, 22], [37, 23], [37, 24], [38, 23], [38, 24], [39, 23], [39, 24], [40, 24],
        #                               [40, 25], [40, 26], [41, 24], [41, 25], [41, 26], [42, 24], [42, 25], [42, 26],
        #                               [42, 27], [43, 26], [43, 27], [43, 30], [44, 26], [44, 27], [44, 28], [44, 29],
        #                               [44, 30], [45, 27], [45, 28], [45, 29], [46, 26], [46, 27], [46, 28], [46, 29],
        #                               [47, 28], [47, 29], [48, 27], [48, 28]]
        # self.small_seqList = [self.small_alpha_phase_seqList, self.small_gamma_phase_seqList, self.small_double_phase_seqList]
        # 以下是2018-12-27-1人工识别的结果
        # self.small_alpha_phase_seqList = [[37, 19], [37, 20],
        #                                   [38, 19], [38, 20], [38, 21], [38, 22],
        #                                   [39, 20], [39, 21], [39, 22],
        #                                   [40, 20], [40, 21], [40, 22], [40, 23],
        #                                   [41, 21], [41, 22], [41, 23],
        #                                   [42, 21], [42, 22], [42, 23],
        #                                   [43, 22], [43, 23], [43, 24], [43, 25],
        #                                   [44, 23], [44, 24], [44, 25],
        #                                   [45, 23], [45, 24], [45, 25], [45, 26],
        #                                   [46, 24], [46, 25], [46, 26],
        #                                   [47, 24], [47, 25], [47, 26], [47, 27],
        #                                   [48, 25], [48, 26], [48, 27],
        #                                   [49, 25], [49, 26], [49, 27], [49, 28],
        #                                   [50, 26], [50, 27]]
        # self.small_gamma_phase_seqList = [[37, 24], [37, 25],
        #                                   [38, 24], [38, 25],
        #                                   [39, 25], [39, 26],
        #                                   [40, 25], [40, 26],
        #                                   [41, 27],
        #                                   [42, 27], [42, 28], [42, 30],
        #                                   [43, 28], [43, 29], [43, 30],
        #                                   [44, 28], [44, 29], [44, 30],
        #                                   [45, 29],
        #                                   [46, 28], [46, 29]]
        # self.small_double_phase_seqList = [[37, 22], [37, 23],
        #                                    [38, 23],
        #                                    [39, 23], [39, 24],
        #                                    [40, 24],
        #                                    [41, 24], [41, 25], [41, 26],
        #                                    [42, 24], [42, 25], [42, 26],
        #                                    [43, 26], [43, 27],
        #                                    [44, 26], [44, 27],
        #                                    [45, 27], [45, 28],
        #                                    [46, 26],
        #                                    [47, 28], [47, 29],
        #                                    [48, 28]]
        # 以下是2018-12-27-2人工识别的结果
        # self.small_alpha_phase_seqList = [[37, 19], [37, 20],
        #                                   [38, 19], [38, 20], [38, 21], [38, 22],
        #                                   [39, 20], [39, 21], [39, 22],
        #                                   [40, 20], [40, 21], [40, 22], [40, 23],
        #                                   [41, 21], [41, 22], [41, 23],
        #                                   [42, 21], [42, 22], [42, 23],
        #                                   [43, 22], [43, 23], [43, 24], [43, 25],
        #                                   [44, 23], [44, 24], [44, 25],
        #                                   [45, 23], [45, 24], [45, 25], [45, 26],
        #                                   [46, 24], [46, 25], [46, 26],
        #                                   [47, 24], [47, 25], [47, 26],
        #                                   [48, 25], [48, 26], [48, 27],
        #                                   [49, 25], [49, 26], [49, 27], [49, 28],
        #                                   [50, 26], [50, 27]]
        # self.small_gamma_phase_seqList = [[37, 24], [37, 25],
        #                                   [38, 24], [38, 25],
        #                                   [39, 25], [39, 26],
        #                                   [40, 25], [40, 26],
        #                                   [41, 27],
        #                                   [42, 27], [42, 28], [42, 30],
        #                                   [43, 28], [43, 29], [43, 30],
        #                                   [44, 28], [44, 29], [44, 30],
        #                                   [45, 29],
        #                                   [46, 27], [46, 28], [46, 29],
        #                                   [47, 27]]
        # self.small_double_phase_seqList = [[37, 22], [37, 23],
        #                                    [38, 23],
        #                                    [39, 23], [39, 24],
        #                                    [40, 24],
        #                                    [41, 24], [41, 25], [41, 26],
        #                                    [42, 24], [42, 25], [42, 26],
        #                                    [43, 26], [43, 27],
        #                                    [44, 26], [44, 27],
        #                                    [45, 27], [45, 28],
        #                                    [46, 26],
        #                                    [47, 28], [47, 29],
        #                                    [48, 28]]
        # 以下是2018-12-27-3人工识别的结果
        # self.small_alpha_phase_seqList = [[37, 19], [37, 20],
        #                                   [38, 19], [38, 20], [38, 21], [38, 22],
        #                                   [39, 20], [39, 21], [39, 22],
        #                                   [40, 20], [40, 21], [40, 22], [40, 23],
        #                                   [41, 21], [41, 22], [41, 23],
        #                                   [42, 21], [42, 22], [42, 23],
        #                                   [43, 22], [43, 23], [43, 24], [43, 25],
        #                                   [44, 23], [44, 24], [44, 25],
        #                                   [45, 23], [45, 24], [45, 25], [45, 26],
        #                                   [46, 24], [46, 25], [46, 26],
        #                                   [47, 24], [47, 25], [47, 26],
        #                                   [48, 25], [48, 26], [48, 27],
        #                                   [49, 25], [49, 26], [49, 27], [49, 28],
        #                                   [50, 26], [50, 27]]
        # self.small_gamma_phase_seqList = [[37, 24], [37, 25],
        #                                   [38, 24], [38, 25],
        #                                   [39, 25], [39, 26],
        #                                   [40, 25], [40, 26],
        #                                   [41, 27],
        #                                   [42, 27], [42, 28], [42, 30],
        #                                   [43, 28], [43, 29], [43, 30],
        #                                   [44, 28], [44, 29], [44, 30],
        #                                   [45, 29]]
        # self.small_double_phase_seqList = [[37, 22], [37, 23],
        #                                    [38, 23],
        #                                    [39, 23], [39, 24],
        #                                    [40, 24],
        #                                    [41, 24], [41, 25], [41, 26],
        #                                    [42, 24], [42, 25], [42, 26],
        #                                    [43, 26], [43, 27],
        #                                    [44, 26], [44, 27],
        #                                    [45, 27], [45, 28],
        #                                    [47, 28], [47, 29],
        #                                    [48, 28]]
        # 以下是2018-12-29-0人工识别的结果
        # self.small_alpha_phase_seqList = [[37, 19], [37, 20],
        #                                   [38, 19], [38, 20], [38, 21], [38, 22],
        #                                   [39, 20], [39, 21], [39, 22],
        #                                   [40, 20], [40, 21], [40, 22], [40, 23],
        #                                   [41, 21], [41, 22], [41, 23],
        #                                   [42, 21], [42, 22], [42, 23],
        #                                   [43, 22], [43, 23], [43, 24], [43, 25],
        #                                   [44, 23], [44, 24], [44, 25],
        #                                   [45, 23], [45, 24], [45, 25], [45, 26],
        #                                   [46, 24], [46, 25], [46, 26],
        #                                   [47, 24], [47, 25], [47, 26],
        #                                   [48, 25], [48, 26],
        #                                   [49, 25], [49, 26], [49, 27], [49, 28],
        #                                   [50, 26], [50, 27]]
        # self.small_gamma_phase_seqList = [[37, 24], [37, 25],
        #                                   [38, 24], [38, 25],
        #                                   [39, 25], [39, 26],
        #                                   [40, 25], [40, 26],
        #                                   [41, 27],
        #                                   [42, 27], [42, 28], [42, 30],
        #                                   [43, 28], [43, 29], [43, 30],
        #                                   [44, 28], [44, 29], [44, 30],
        #                                   [45, 29]]
        # self.small_double_phase_seqList = [[37, 22], [37, 23],
        #                                    [38, 23],
        #                                    [39, 23], [39, 24],
        #                                    [40, 24],
        #                                    [41, 24], [41, 25], [41, 26],
        #                                    [42, 24], [42, 25], [42, 26],
        #                                    [43, 26], [43, 27],
        #                                    [44, 26], [44, 27],
        #                                    [45, 27], [45, 28],
        #                                    [47, 28], [47, 29],
        #                                    [48, 27], [48, 28]]
        # 以下是2018-12-29-0人工识别的结果
        self.small_alpha_phase_seqList = [[37, 19], [37, 20],
                                          [38, 19], [38, 20], [38, 21], [38, 22],
                                          [39, 20], [39, 21], [39, 22],
                                          [40, 20], [40, 21], [40, 22], [40, 23],
                                          [41, 21], [41, 22], [41, 23], [41, 24],
                                          [42, 21], [42, 22], [42, 23],
                                          [43, 22], [43, 23], [43, 24], [43, 25],
                                          [44, 23], [44, 24], [44, 25],
                                          [45, 23], [45, 24], [45, 25], [45, 26],
                                          [46, 24], [46, 25], [46, 26],
                                          [47, 24], [47, 25], [47, 26],
                                          [48, 25], [48, 26],
                                          [49, 25], [49, 26], [49, 27], [49, 28],
                                          [50, 26], [50, 27]]
        self.small_gamma_phase_seqList = [[37, 25],
                                          [38, 25],
                                          [39, 25], [39, 26],
                                          [40, 25],
                                          [41, 27],
                                          [42, 27], [42, 28], [42, 30],
                                          [43, 28], [43, 29], [43, 30],
                                          [44, 28], [44, 29], [44, 30],
                                          [45, 29]]
        self.small_double_phase_seqList = [[37, 22], [37, 23], [37, 24],
                                           [38, 23], [38, 24],
                                           [39, 23], [39, 24],
                                           [40, 24], [40, 26],
                                           [41, 25], [41, 26],
                                           [42, 24], [42, 25], [42, 26],
                                           [43, 26], [43, 27],
                                           [44, 26], [44, 27],
                                           [45, 27], [45, 28],
                                           [47, 28], [47, 29],
                                           [48, 27], [48, 28]]
        self.small_seqList = [self.small_alpha_phase_seqList, self.small_gamma_phase_seqList, self.small_double_phase_seqList]
        # 以下是2019-01-01-0大区人工识别的结果
        self.huge_double_phase_seqList, self.huge_gamma_phase_seqList = self.huge_phases_wrapper()
        self.huge_seqList = [self.huge_gamma_phase_seqList, self.huge_double_phase_seqList]
        # C area manual results
        self.c_alpha_phase_seqList, self.c_double_phase_seqList, self.c_gamma_phase_seqList = self.c_phases_wrapper()
        self.c_seqList = [self.c_alpha_phase_seqList, self.c_double_phase_seqList, self.c_gamma_phase_seqList]
        self.whole_alpha_phase_seqList, self.whole_double_phase_seqList, self.whole_gamma_phase_seqList = self.whole_phases_wrapper()
        self.whole_seqList = [self.whole_alpha_phase_seqList, self.whole_double_phase_seqList, self.whole_gamma_phase_seqList]
    def huge_phases_wrapper(self):
        huge_double_phase_seqList = []
        huge_gamma_phase_seqList = []

        huge_gamma_phase_seqList.extend([[1,i] for i in range(37, 48)])

        huge_gamma_phase_seqList.extend([[2,i] for i in range(25, 48)])

        # 以下是2019-01-01-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[3,i] for i in range(12,27)])
        # huge_gamma_phase_seqList.extend([[3,i] for i in range(27, 46)])
        # 以下是2019-01-08-0大区人工识别的结果
        huge_double_phase_seqList.extend([[3, i] for i in range(12, 29)])
        huge_gamma_phase_seqList.extend([[3, i] for i in range(29, 46)])

        # 以下是2019-01-01-0大区人工识别的结果
        huge_double_phase_seqList.extend([[4,i] for i in range(11,31)])
        huge_gamma_phase_seqList.extend([[4,i] for i in range(31,47)])

        # 以下是2019-01-01-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[5,i] for i in range(12,23)])
        # huge_gamma_phase_seqList.extend([[5,i] for i in range(23,46)])
        # 以下是2019-01-08-0大区人工识别的结果
        huge_double_phase_seqList.extend([[5,i] for i in range(12,30)])
        huge_gamma_phase_seqList.extend([[5,i] for i in range(30,46)])

        # 以下是2019-01-01-0大区人工识别的结果
        huge_double_phase_seqList.extend([[6,i] for i in range(13,29)])
        huge_gamma_phase_seqList.extend([[6,i] for i in range(29,46)])

        # 以下是2019-01-01-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[7,i] for i in range(13,27)])
        # huge_gamma_phase_seqList.extend([[7,i] for i in range(27,46)])
        # 以下是2019-01-07-0大区人工识别的结果
        huge_double_phase_seqList.extend([[7,i] for i in range(13,30)])
        huge_gamma_phase_seqList.extend([[7,i] for i in range(30,46)])

        # 以下是2019-01-01-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[8,i] for i in range(14,20)])
        # huge_gamma_phase_seqList.extend([[8,i] for i in range(20,45)])
        # 以下是2019-01-07-0大区人工识别的结果
        huge_double_phase_seqList.extend([[8,i] for i in range(14,26)])
        huge_gamma_phase_seqList.extend([[8,i] for i in range(26,45)])

        huge_double_phase_seqList.extend([[9,i] for i in range(15,28)])
        huge_gamma_phase_seqList.extend([[9,i] for i in range(28,45)])

        # 以下是2019-01-07-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[10,i] for i in range(15,24)])
        # huge_gamma_phase_seqList.extend([[10,i] for i in range(24,44)])
        # 以下是2019-01-08-0大区人工识别的结果
        huge_double_phase_seqList.extend([[10,i] for i in range(15,28)])
        huge_gamma_phase_seqList.extend([[10,i] for i in range(28,44)])

        # 以下是2019-01-07-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[11,i] for i in range(16,25)])
        # huge_gamma_phase_seqList.extend([[11,i] for i in range(25,44)])
        # 以下是2019-01-08-0大区人工识别的结果
        huge_double_phase_seqList.extend([[11,i] for i in range(16,28)])
        huge_gamma_phase_seqList.extend([[11,i] for i in range(28,44)])

        # 以下是2019-01-07-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[12,i] for i in range(16,27)])
        # huge_gamma_phase_seqList.extend([[12,i] for i in range(27,44)])
        # 以下是2019-01-08-0大区人工识别的结果
        huge_double_phase_seqList.extend([[12,i] for i in range(16,29)])
        huge_gamma_phase_seqList.extend([[12,i] for i in range(29,44)])

        huge_double_phase_seqList.extend([[13,i] for i in range(17,28)])
        huge_gamma_phase_seqList.extend([[13,i] for i in range(28,43)])

        # 以下是2019-01-07-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[14,i] for i in range(18,27)])
        # huge_gamma_phase_seqList.extend([[14,i] for i in range(27, 43)])
        # 以下是2019-01-08-0大区人工识别的结果
        huge_double_phase_seqList.extend([[14,i] for i in range(18,29)])
        huge_gamma_phase_seqList.extend([[14,i] for i in range(29, 43)])

        # 以下是2019-01-01-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[15,i] for i in range(18,27)])
        # huge_gamma_phase_seqList.extend([[15,i] for i in range(27, 42)])
        # 以下是2019-01-03-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[15,i] for i in range(18,23)])
        # huge_gamma_phase_seqList.extend([[15,i] for i in range(23, 42)])
        # 以下是2019-01-08-0大区人工识别的结果
        huge_double_phase_seqList.extend([[15,i] for i in range(18,29)])
        huge_gamma_phase_seqList.extend([[15,i] for i in range(29, 42)])

        # 以下是2019-01-01-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[16,i] for i in range(19,23)])
        # huge_gamma_phase_seqList.extend([[16,i] for i in range(23,42)])
        # 以下是2019-01-03-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[16,i] for i in range(19,24)])
        # huge_gamma_phase_seqList.extend([[16,i] for i in range(24,42)])
        # 以下是2019-01-03-0大区人工识别的结果
        huge_double_phase_seqList.extend([[16,i] for i in range(19,26)])
        huge_gamma_phase_seqList.extend([[16,i] for i in range(26,42)])

        # 以下是2019-01-01-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[17,i] for i in range(19,26)])
        # huge_gamma_phase_seqList.extend([[17,i] for i in range(26,42)])
        # 以下是2019-01-03-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[17,i] for i in range(19,25)])
        # huge_gamma_phase_seqList.extend([[17,i] for i in range(25,42)])
        # 以下是2019-01-03-0大区人工识别的结果
        huge_double_phase_seqList.extend([[17,i] for i in range(19,27)])
        huge_gamma_phase_seqList.extend([[17,i] for i in range(27,42)])

        # 以下是2019-01-01-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[18,i] for i in range(20,26)])
        # huge_gamma_phase_seqList.extend([[18,i] for i in range(26, 41)])
        # 以下是2019-01-03-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[18,i] for i in range(20,25)])
        # huge_gamma_phase_seqList.extend([[18,i] for i in range(25, 41)])
        # 以下是2019-01-08-0大区人工识别的结果
        huge_double_phase_seqList.extend([[18,i] for i in range(20,28)])
        huge_gamma_phase_seqList.extend([[18,i] for i in range(28, 41)])

        # 以下是2019-01-01-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[19,i] for i in range(21,28)])
        # huge_gamma_phase_seqList.extend([[19,i] for i in range(28, 41)])
        # 以下是2019-01-03-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[19,i] for i in range(21, 25)])
        # huge_gamma_phase_seqList.extend([[19,i] for i in range(25, 41)])
        # 以下是2019-01-03-0大区人工识别的结果
        huge_double_phase_seqList.extend([[19,i] for i in range(21, 29)])
        huge_gamma_phase_seqList.extend([[19,i] for i in range(29, 41)])

        # 以下是2019-01-01-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[20,i] for i in range(21, 28)])
        # huge_gamma_phase_seqList.extend([[20,i] for i in range(28, 40)])
        # 以下是2019-01-03-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[20,i] for i in range(21, 26)])
        # huge_gamma_phase_seqList.extend([[20,i] for i in range(26, 40)])
        # 以下是2019-01-08-0大区人工识别的结果
        huge_double_phase_seqList.extend([[20,i] for i in range(21, 29)])
        huge_gamma_phase_seqList.extend([[20,i] for i in range(29, 40)])

        # 以下是2019-01-01-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[21,i] for i in range(22,28)])
        # huge_gamma_phase_seqList.extend([[21,i] for i in range(28,40)])
        # 以下是2019-01-03-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[21,i] for i in range(22,26)])
        # huge_gamma_phase_seqList.extend([[21,i] for i in range(26,40)])
        # 以下是2019-01-08-0大区人工识别的结果
        huge_double_phase_seqList.extend([[21,i] for i in range(22,28)])
        huge_gamma_phase_seqList.extend([[21,i] for i in range(28,40)])

        # 以下是2019-01-01-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[22,i] for i in range(23,28)])
        # huge_gamma_phase_seqList.extend([[22,i] for i in range(28, 40)])
        # 以下是2019-01-03-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[22,i] for i in range(23,27)])
        # huge_gamma_phase_seqList.extend([[22,i] for i in range(27, 40)])
        # 以下是2019-01-03-0大区人工识别的结果
        huge_double_phase_seqList.extend([[22,i] for i in range(23,28)])
        huge_gamma_phase_seqList.extend([[22,i] for i in range(28, 40)])

        # 以下是2019-01-01-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[23,i] for i in range(23,28)])
        # huge_gamma_phase_seqList.extend([[23,i] for i in range(28,39)])
        # 以下是2019-01-03-0大区人工识别的结果
        huge_double_phase_seqList.extend([[23,i] for i in range(23,26)])
        huge_gamma_phase_seqList.extend([[23,i] for i in range(26,39)])

        # 以下是2019-01-01-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[24,i] for i in range(24,28)])
        # huge_gamma_phase_seqList.extend([[24,i] for i in range(28,39)])
        # 以下是2019-01-03-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[24,i] for i in range(24,26)])
        # huge_gamma_phase_seqList.extend([[24,i] for i in range(26,39)])
        # 以下是2019-01-08-0大区人工识别的结果
        huge_double_phase_seqList.extend([[24,i] for i in range(24,27)])
        huge_gamma_phase_seqList.extend([[24,i] for i in range(27,39)])

        # 以下是2019-01-01-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[25,i] for i in range(25,28)])
        # huge_gamma_phase_seqList.extend([[25,i] for i in range(28, 38)])
        # 以下是2019-01-03-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[25,i] for i in range(25,28)])
        # huge_gamma_phase_seqList.extend([[25,i] for i in range(28, 38)])
        # 以下是2019-01-08-0大区人工识别的结果
        huge_double_phase_seqList.extend([[25,i] for i in range(25,27)])
        huge_gamma_phase_seqList.extend([[25,i] for i in range(27, 38)])

        # 以下是2019-01-01-0大区人工识别的结果
        # huge_double_phase_seqList.extend([26,i] for i in range(26,28))
        # huge_gamma_phase_seqList.extend([[26,i] for i in range(28,38)])
        # 以下是2019-01-03-0大区人工识别的结果
        huge_double_phase_seqList.extend([26,i] for i in range(26,27))
        huge_gamma_phase_seqList.extend([[26,i] for i in range(27,38)])

        # 以下是2019-01-01-0大区人工识别的结果
        # huge_double_phase_seqList.extend([[27,i] for i in range(26, 28)])
        # huge_gamma_phase_seqList.extend([[27,i] for i in range(28,38)])
        # 以下是2019-01-03-0大区人工识别的结果
        # huge_gamma_phase_seqList.extend([[27,i] for i in range(26,38)])
        # 以下是2019-01-08-0大区人工识别的结果
        huge_double_phase_seqList.extend([[27,i] for i in range(26, 27)])
        huge_gamma_phase_seqList.extend([[27,i] for i in range(27,38)])

        # 以下是2019-01-01-0大区人工识别的结果
        huge_double_phase_seqList.extend([[28,26]])
        huge_gamma_phase_seqList.extend([[28,i] for i in range(27,37)])
        # 以下是2019-01-03-0大区人工识别的结果
        # huge_gamma_phase_seqList.extend([[28,i] for i in range(26,37)])

        # 以下是2019-01-01-0大区人工识别的结果
        huge_double_phase_seqList.extend([[29,26]])
        huge_gamma_phase_seqList.extend([[29,i] for i in range(27,37)])
        # 以下是2019-01-03-0大区人工识别的结果
        # huge_gamma_phase_seqList.extend([[29,i] for i in range(26,37)])

        # 以下是2019-01-01-0大区人工识别的结果
        huge_gamma_phase_seqList.extend([[30,i] for i in range(27,36)])

        # 以下是2019-01-01-0大区人工识别的结果
        huge_gamma_phase_seqList.extend([[31,i] for i in range(27,36)])

        # 以下是2019-01-01-0大区人工识别的结果
        huge_gamma_phase_seqList.extend([[32,i] for i in range(27,36)])

        # 以下是2019-01-01-0大区人工识别的结果
        huge_gamma_phase_seqList.extend([[33,i] for i in range(28,35)])

        # 以下是2019-01-01-0大区人工识别的结果
        huge_gamma_phase_seqList.extend([[34,i] for i in range(28,35)])

        # 以下是2019-01-01-0大区人工识别的结果
        huge_gamma_phase_seqList.extend([[35,i] for i in range(29,34)])

        # 以下是2019-01-01-0大区人工识别的结果
        huge_gamma_phase_seqList.extend([[36,i] for i in range(29,34)])

        # 以下是2019-01-01-0大区人工识别的结果
        huge_gamma_phase_seqList.extend([[37,i] for i in range(30,34)])

        # 以下是2019-01-01-0大区人工识别的结果
        huge_gamma_phase_seqList.extend([[38,i] for i in range(31,33)])

        # 以下是2019-01-01-0大区人工识别的结果
        huge_gamma_phase_seqList.extend([[39,i] for i in range(31,33)])

        return huge_double_phase_seqList, huge_gamma_phase_seqList
    def c_phases_wrapper(self):
        c_alpha_phase_seqList = []
        c_double_phase_seqList = []
        c_gamma_phase_seqList = []

        # c_alpha_phase_seqList.extend([[7, i] for i in range(3, 4)])
        c_alpha_phase_seqList.extend([[7, i] for i in range(3, 6)])
        c_alpha_phase_seqList.extend([[8, i] for i in range(3, 6)])
        c_alpha_phase_seqList.extend([[9, i] for i in range(4, 7)])
        # c_alpha_phase_seqList.extend([[10, i] for i in range(5, 7)])
        c_alpha_phase_seqList.extend([[10, i] for i in range(5, 8)])
        c_alpha_phase_seqList.extend([[11, i] for i in range(5, 8)])
        c_alpha_phase_seqList.extend([[12, i] for i in range(6, 8)])
        c_alpha_phase_seqList.extend([[13, i] for i in range(6, 9)])
        c_alpha_phase_seqList.extend([[14, i] for i in range(7, 9)])
        c_alpha_phase_seqList.extend([[15, i] for i in range(7, 10)])
        c_alpha_phase_seqList.extend([[16, i] for i in range(8, 11)])
        c_alpha_phase_seqList.extend([[17, i] for i in range(8, 12)])
        c_alpha_phase_seqList.extend([[18, i] for i in range(9, 12)])
        c_alpha_phase_seqList.extend([[19, i] for i in range(9, 13)])
        c_alpha_phase_seqList.extend([[20, i] for i in range(10, 14)])
        c_alpha_phase_seqList.extend([[21, i] for i in range(10, 14)])
        c_alpha_phase_seqList.extend([[22, i] for i in range(11, 14)])
        c_alpha_phase_seqList.extend([[23, i] for i in range(11, 14)])
        # c_alpha_phase_seqList.extend([[24, i] for i in range(12, 14)])
        c_alpha_phase_seqList.extend([[24, i] for i in range(12, 15)])
        c_alpha_phase_seqList.extend([[25, i] for i in range(12, 16)])
        c_alpha_phase_seqList.extend([[26, i] for i in range(13, 15)])
        c_alpha_phase_seqList.extend([[27, i] for i in range(13, 16)])
        # c_alpha_phase_seqList.extend([[28, i] for i in range(14, 16)])
        c_alpha_phase_seqList.extend([[28, i] for i in range(14, 17)])
        c_alpha_phase_seqList.extend([[29, i] for i in range(15, 18)])
        # c_alpha_phase_seqList.extend([[30, i] for i in range(15, 17)])
        c_alpha_phase_seqList.extend([[30, i] for i in range(15, 18)])
        c_alpha_phase_seqList.extend([[31, i] for i in range(16, 18)])
        c_alpha_phase_seqList.extend([[32, i] for i in range(16, 20)])
        # c_alpha_phase_seqList.extend([[33, i] for i in range(17, 19)])
        c_alpha_phase_seqList.extend([[33, i] for i in range(17, 20)])
        c_alpha_phase_seqList.extend([[34, i] for i in range(17, 20)])
        # c_alpha_phase_seqList.extend([[35, i] for i in range(18, 20)])
        c_alpha_phase_seqList.extend([[35, i] for i in range(18, 21)])
        c_alpha_phase_seqList.extend([[36, i] for i in range(18, 21)])
        c_alpha_phase_seqList.extend([[37, i] for i in range(21, 22)])

        # c_double_phase_seqList.extend([[4,i] for i in [1,4,5,6,7,8,9]])
        c_double_phase_seqList.extend([[4,i] for i in range(4, 10)])
        c_double_phase_seqList.extend([[5,i] for i in range(5, 12)])
        c_double_phase_seqList.extend([[6,i] for i in range(5, 13)])
        # c_double_phase_seqList.extend([[7,i] for i in range(4, 13)])
        c_double_phase_seqList.extend([[7,i] for i in range(6, 13)])
        c_double_phase_seqList.extend([[8,i] for i in range(6, 14)])
        c_double_phase_seqList.extend([[9,i] for i in range(7, 15)])
        # c_double_phase_seqList.extend([[10,i] for i in range(7, 15)])
        c_double_phase_seqList.extend([[10,i] for i in range(8, 15)])
        c_double_phase_seqList.extend([[11,i] for i in range(8, 16)])
        c_double_phase_seqList.extend([[12,i] for i in range(8, 16)])
        c_double_phase_seqList.extend([[13,i] for i in range(9, 17)])
        c_double_phase_seqList.extend([[14,i] for i in range(9, 18)])
        c_double_phase_seqList.extend([[15,i] for i in range(10, 18)])
        # c_double_phase_seqList.extend([[16,i] for i in range(11, 19)])
        c_double_phase_seqList.extend([[16,i] for i in range(10, 19)])
        # c_double_phase_seqList.extend([[17,i] for i in range(12, 19)])
        c_double_phase_seqList.extend([[17,i] for i in range(11, 19)])
        # c_double_phase_seqList.extend([[18,i] for i in range(12, 20)])
        c_double_phase_seqList.extend([[18,i] for i in range(11, 20)])
        # c_double_phase_seqList.extend([[19,i] for i in range(13, 20)])
        c_double_phase_seqList.extend([[19,i] for i in range(12, 21)])
        # c_double_phase_seqList.extend([[20,i] for i in range(14, 21)])
        c_double_phase_seqList.extend([[20,i] for i in range(12, 21)])
        # c_double_phase_seqList.extend([[21,i] for i in range(14, 22)])
        c_double_phase_seqList.extend([[21,i] for i in range(13, 22)])
        # c_double_phase_seqList.extend([[22,i] for i in range(14, 23)])
        c_double_phase_seqList.extend([[22,i] for i in range(13, 23)])
        c_double_phase_seqList.extend([[23,i] for i in range(14, 23)])
        # c_double_phase_seqList.extend([[24,i] for i in range(14, 24)])
        c_double_phase_seqList.extend([[24,i] for i in range(15, 24)])
        # c_double_phase_seqList.extend([[25,i] for i in range(16, 25)])
        c_double_phase_seqList.extend([[25,i] for i in range(15, 25)])
        c_double_phase_seqList.extend([[26,i] for i in range(15, 26)])
        c_double_phase_seqList.extend([[27,i] for i in range(16, 26)])
        # c_double_phase_seqList.extend([[28,i] for i in range(16, 26)])
        c_double_phase_seqList.extend([[28,i] for i in range(17, 26)])
        c_double_phase_seqList.extend([[29,i] for i in range(18, 26)])
        c_double_phase_seqList.extend([[30,i] for i in range(18, 26)])
        # c_double_phase_seqList.extend([[31,i] for i in range(18, 27)])
        c_double_phase_seqList.extend([[31,i] for i in range(18, 26)])
        # c_double_phase_seqList.extend([[32,i] for i in range(19, 27)])
        c_double_phase_seqList.extend([[32,i] for i in range(20, 24)])
        # c_double_phase_seqList.extend([[33,i] for i in range(19, 28)])
        c_double_phase_seqList.extend([[33,i] for i in range(20, 24)])
        # c_double_phase_seqList.extend([[34,i] for i in range(20, 28)])
        c_double_phase_seqList.extend([[34,i] for i in range(20, 24)])
        # c_double_phase_seqList.extend([[35,i] for i in range(20, 22)])
        c_double_phase_seqList.extend([[35,i] for i in range(20, 23)])
        # c_double_phase_seqList.extend([[36,i] for i in range(21, 22)])
        c_double_phase_seqList.extend([[36,i] for i in range(21, 24)])

        c_gamma_phase_seqList.extend([[30, i] for i in range(26, 27)])
        c_gamma_phase_seqList.extend([[31, i] for i in range(26, 27)])
        c_gamma_phase_seqList.extend([[32, i] for i in range(24, 27)])
        c_gamma_phase_seqList.extend([[33, i] for i in range(24, 28)])
        c_gamma_phase_seqList.extend([[34, i] for i in range(24, 28)])
        c_gamma_phase_seqList.extend([[35, i] for i in range(23, 29)])
        # c_gamma_phase_seqList.extend([[36, i] for i in range(23, 29)])
        c_gamma_phase_seqList.extend([[36, i] for i in range(24, 29)])
        c_gamma_phase_seqList.extend([[37, i] for i in range(26, 30)])
        c_gamma_phase_seqList.extend([[38, i] for i in range(26, 31)])
        c_gamma_phase_seqList.extend([[39, i] for i in range(27, 31)])
        c_gamma_phase_seqList.extend([[40, i] for i in range(27, 32)])
        c_gamma_phase_seqList.extend([[41, i] for i in range(28, 32)])
        c_gamma_phase_seqList.extend([[42, i] for i in [29, 31]])
        return c_alpha_phase_seqList, c_double_phase_seqList, c_gamma_phase_seqList
    def whole_phases_wrapper(self):
        whole_alpha_phase_seqList = []
        whole_double_phase_seqList = []
        whole_gamma_phase_seqList = []

        whole_alpha_phase_seqList.extend([[7,i] for i in range(3,6)])
        whole_alpha_phase_seqList.extend([[8,i] for i in range(3,6)])
        whole_alpha_phase_seqList.extend([[9,i] for i in range(4,7)])
        whole_alpha_phase_seqList.extend([[10,i] for i in range(5,8)])
        whole_alpha_phase_seqList.extend([[11,i] for i in range(5,8)])
        whole_alpha_phase_seqList.extend([[12,i] for i in range(6,8)])
        whole_alpha_phase_seqList.extend([[13,i] for i in range(6,9)])
        whole_alpha_phase_seqList.extend([[14,i] for i in range(7,9)])
        whole_alpha_phase_seqList.extend([[15,i] for i in range(7,10)])
        whole_alpha_phase_seqList.extend([[16,i] for i in range(8,10)])
        whole_alpha_phase_seqList.extend([[17,i] for i in range(8,11)])
        whole_alpha_phase_seqList.extend([[18,i] for i in range(9,11)])
        whole_alpha_phase_seqList.extend([[19,i] for i in range(9,12)])
        whole_alpha_phase_seqList.extend([[20,i] for i in range(10,12)])
        whole_alpha_phase_seqList.extend([[21,i] for i in range(10,13)])
        whole_alpha_phase_seqList.extend([[22,i] for i in range(11,13)])
        whole_alpha_phase_seqList.extend([[23,i] for i in range(11,14)])
        whole_alpha_phase_seqList.extend([[24,i] for i in range(12,15)])
        whole_alpha_phase_seqList.extend([[25,i] for i in range(12,15)])
        whole_alpha_phase_seqList.extend([[26,i] for i in range(13,15)])
        whole_alpha_phase_seqList.extend([[27,i] for i in range(13,16)])
        whole_alpha_phase_seqList.extend([[28,i] for i in range(14,17)])
        whole_alpha_phase_seqList.extend([[29,i] for i in range(15,18)])
        whole_alpha_phase_seqList.extend([[30,i] for i in range(15,18)])
        whole_alpha_phase_seqList.extend([[31,i] for i in range(16,18)])
        whole_alpha_phase_seqList.extend([[32,i] for i in range(16,20)])
        whole_alpha_phase_seqList.extend([[33,i] for i in range(17,20)])
        whole_alpha_phase_seqList.extend([[34,i] for i in range(17,20)])
        whole_alpha_phase_seqList.extend([[35,i] for i in range(18,21)])
        whole_alpha_phase_seqList.extend([[36,i] for i in range(18,21)])
        whole_alpha_phase_seqList.extend([[37,i] for i in range(19,22)])
        whole_alpha_phase_seqList.extend([[38,i] for i in range(19,23)])
        whole_alpha_phase_seqList.extend([[39,i] for i in range(20,23)])
        whole_alpha_phase_seqList.extend([[40,i] for i in range(20,24)])
        whole_alpha_phase_seqList.extend([[41,i] for i in range(21,25)])
        whole_alpha_phase_seqList.extend([[42,i] for i in range(21,24)])
        whole_alpha_phase_seqList.extend([[43,i] for i in range(22,26)])
        whole_alpha_phase_seqList.extend([[44,i] for i in range(23,26)])
        whole_alpha_phase_seqList.extend([[45,i] for i in range(23,27)])
        whole_alpha_phase_seqList.extend([[46,i] for i in range(24,29)])
        whole_alpha_phase_seqList.extend([[47,i] for i in range(24,29)])
        whole_alpha_phase_seqList.extend([[48,i] for i in range(25,29)])
        whole_alpha_phase_seqList.extend([[49,i] for i in range(25,29)])
        whole_alpha_phase_seqList.extend([[50,i] for i in range(26,28)])

        whole_double_phase_seqList.extend([[3,i] for i in range(12,29)])
        whole_double_phase_seqList.extend([[4,i] for i in range(4,31)])
        whole_double_phase_seqList.extend([[5,i] for i in range(5,30)])
        whole_double_phase_seqList.extend([[6,i] for i in range(5,29)])
        whole_double_phase_seqList.extend([[7,i] for i in range(6,30)])
        whole_double_phase_seqList.extend([[8,i] for i in range(6,26)])
        whole_double_phase_seqList.extend([[9,i] for i in range(7,28)])
        whole_double_phase_seqList.extend([[10,i] for i in range(8,28)])
        whole_double_phase_seqList.extend([[11,i] for i in range(8,28)])
        whole_double_phase_seqList.extend([[12,i] for i in range(8,29)])
        whole_double_phase_seqList.extend([[13,i] for i in range(9,28)])
        whole_double_phase_seqList.extend([[14,i] for i in range(9,29)])
        whole_double_phase_seqList.extend([[15,i] for i in range(10,29)])
        whole_double_phase_seqList.extend([[16,i] for i in range(10,26)])
        whole_double_phase_seqList.extend([[17,i] for i in range(11,27)])
        whole_double_phase_seqList.extend([[18,i] for i in range(11,28)])
        whole_double_phase_seqList.extend([[19,i] for i in range(12,29)])
        whole_double_phase_seqList.extend([[20,i] for i in range(12,29)])
        whole_double_phase_seqList.extend([[21,i] for i in range(13,28)])
        whole_double_phase_seqList.extend([[22,i] for i in range(13,28)])
        whole_double_phase_seqList.extend([[23,i] for i in range(14,28)])
        whole_double_phase_seqList.extend([[24,i] for i in range(15,27)])
        whole_double_phase_seqList.extend([[25,i] for i in range(15,27)])
        whole_double_phase_seqList.extend([[26,i] for i in range(15,27)])
        whole_double_phase_seqList.extend([[27,i] for i in range(16,27)])
        whole_double_phase_seqList.extend([[28,i] for i in range(17,27)])
        whole_double_phase_seqList.extend([[29,i] for i in range(18,27)])
        whole_double_phase_seqList.extend([[30,i] for i in range(18,26)])
        whole_double_phase_seqList.extend([[31,i] for i in range(18,26)])
        whole_double_phase_seqList.extend([[32,i] for i in range(20,24)])
        whole_double_phase_seqList.extend([[33,i] for i in range(20,24)])
        whole_double_phase_seqList.extend([[34,i] for i in range(20,24)])
        whole_double_phase_seqList.extend([[35,i] for i in range(21,23)])
        whole_double_phase_seqList.extend([[36,i] for i in range(21,24)])
        whole_double_phase_seqList.extend([[37,i] for i in range(22,25)])
        whole_double_phase_seqList.extend([[38,i] for i in range(23,25)])
        whole_double_phase_seqList.extend([[39,i] for i in range(23,25)])
        whole_double_phase_seqList.extend([[40,i] for i in range(24,25)])
        whole_double_phase_seqList.extend([[41,i] for i in range(25,27)])
        whole_double_phase_seqList.extend([[42,i] for i in range(24,27)])
        whole_double_phase_seqList.extend([[43,i] for i in range(26,28)])
        whole_double_phase_seqList.extend([[44,i] for i in range(26,28)])
        whole_double_phase_seqList.extend([[45,i] for i in range(27,29)])
        whole_double_phase_seqList.extend([[46,i] for i in range(29,30)])
        whole_double_phase_seqList.extend([[47,i] for i in range(29,30)])

        whole_gamma_phase_seqList.extend([[1,i] for i in range(37,48)])
        whole_gamma_phase_seqList.extend([[2,i] for i in range(25,48)])
        whole_gamma_phase_seqList.extend([[3,i] for i in range(29,47)])
        whole_gamma_phase_seqList.extend([[4,i] for i in range(31,47)])
        whole_gamma_phase_seqList.extend([[5,i] for i in range(30,46)])
        whole_gamma_phase_seqList.extend([[6,i] for i in range(29,46)])
        whole_gamma_phase_seqList.extend([[7,i] for i in range(30,46)])
        whole_gamma_phase_seqList.extend([[8,i] for i in range(26,45)])
        whole_gamma_phase_seqList.extend([[9,i] for i in range(28,45)])
        whole_gamma_phase_seqList.extend([[10,i] for i in range(28,44)])
        whole_gamma_phase_seqList.extend([[11,i] for i in range(28,44)])
        whole_gamma_phase_seqList.extend([[12,i] for i in range(29,44)])
        whole_gamma_phase_seqList.extend([[13,i] for i in range(28,43)])
        whole_gamma_phase_seqList.extend([[14,i] for i in range(29,43)])
        whole_gamma_phase_seqList.extend([[15,i] for i in range(29,42)])
        whole_gamma_phase_seqList.extend([[16,i] for i in range(26,42)])
        whole_gamma_phase_seqList.extend([[17,i] for i in range(27,42)])
        whole_gamma_phase_seqList.extend([[18,i] for i in range(28,41)])
        whole_gamma_phase_seqList.extend([[19,i] for i in range(29,41)])
        whole_gamma_phase_seqList.extend([[20,i] for i in range(29,40)])
        whole_gamma_phase_seqList.extend([[21,i] for i in range(28,40)])
        whole_gamma_phase_seqList.extend([[22,i] for i in range(28,40)])
        whole_gamma_phase_seqList.extend([[23,i] for i in range(28,39)])
        whole_gamma_phase_seqList.extend([[24,i] for i in range(27,39)])
        whole_gamma_phase_seqList.extend([[25,i] for i in range(27,38)])
        whole_gamma_phase_seqList.extend([[26,i] for i in range(27,38)])
        whole_gamma_phase_seqList.extend([[27,i] for i in range(27,38)])
        whole_gamma_phase_seqList.extend([[28,i] for i in range(27,37)])
        whole_gamma_phase_seqList.extend([[29,i] for i in range(27,37)])
        whole_gamma_phase_seqList.extend([[30,i] for i in range(26,36)])
        whole_gamma_phase_seqList.extend([[31,i] for i in range(26,36)])
        whole_gamma_phase_seqList.extend([[32,i] for i in range(24,36)])
        whole_gamma_phase_seqList.extend([[33,i] for i in range(24,35)])
        whole_gamma_phase_seqList.extend([[34,i] for i in range(24,35)])
        whole_gamma_phase_seqList.extend([[35,i] for i in range(23,34)])
        whole_gamma_phase_seqList.extend([[36,i] for i in range(24,34)])
        whole_gamma_phase_seqList.extend([[37,i] for i in range(25,34)])
        whole_gamma_phase_seqList.extend([[38,i] for i in range(25,33)])
        whole_gamma_phase_seqList.extend([[39,i] for i in range(25,33)])
        whole_gamma_phase_seqList.extend([[40,i] for i in [25]+list(range(27,32))])
        whole_gamma_phase_seqList.extend([[41,i] for i in range(27,32)])
        whole_gamma_phase_seqList.extend([[42,i] for i in range(27,32)])
        whole_gamma_phase_seqList.extend([[43,i] for i in range(28,31)])
        whole_gamma_phase_seqList.extend([[44,i] for i in range(28,31)])
        whole_gamma_phase_seqList.extend([[45,i] for i in range(29,30)])
        return whole_alpha_phase_seqList, whole_double_phase_seqList, whole_gamma_phase_seqList
    def singlePointTest(self,j,i,areaType):
        ternaryPointsList = cluster_main.comMathcer(matComFile='../../basicInfo/composition/composition_i_j/epma_composition.txt',clusterList=[[[j,i]]]).matchManual()
        if areaType == 'small':
            ternaryUtil.ternaryPlot(title='Fe-Cr-Ni Ternary', left_lable='Fe (at.%)', right_lable='Cr (at.%)',bottom_lable='Ni (at.%)').smallTernary(ternaryPointsList)
        elif areaType == 'huge':
            ternaryUtil.ternaryPlot(title='Fe-Cr-Ni Ternary', left_lable='Fe (at.%)', right_lable='Cr (at.%)', bottom_lable='Ni (at.%)').hugeTernary(ternaryPointsList)
        elif areaType == 'c':
            ternaryUtil.ternaryPlot(title='Fe-Cr-Ni Ternary', left_lable='Fe (at.%)', right_lable='Cr (at.%)', bottom_lable='Ni (at.%)').c_refined_ternary(ternaryPointsList)
        elif areaType == 'whole':
            ternaryUtil.ternaryPlot(title=str(j)+'_'+str(i), left_lable='Fe (at.%)', right_lable='Cr (at.%)', bottom_lable='Ni (at.%)').whole_refined_ternary(ternaryPointsList)
    def smallTer(self,title):
        print('{0} in alpha\n{1} in gamma\n{2} in double'.format(len(self.small_alpha_phase_seqList), len(self.small_gamma_phase_seqList), len(self.small_double_phase_seqList)))
        ternaryPointsList = cluster_main.comMathcer(matComFile='../../basicInfo/composition/composition_i_j/epma_composition.txt', clusterList=self.small_seqList).matchManual()
        ternaryUtil.ternaryPlot(title, left_lable='Fe (at.%)', right_lable='Cr (at.%)', bottom_lable='Ni (at.%)').smallTernary(ternaryPointsList)
    def small_refined_ternary(self,title):
        print('{0} in alpha\n{1} in gamma\n{2} in double'.format(len(self.small_alpha_phase_seqList), len(self.small_gamma_phase_seqList), len(self.small_double_phase_seqList)))
        ternaryPointsList = cluster_main.comMathcer(matComFile='../../basicInfo/composition/composition_i_j/epma_composition.txt', clusterList=self.small_seqList).matchManual()
        ternaryUtil.ternaryPlot(title, left_lable='Fe (at.%)', right_lable='Cr (at.%)', bottom_lable='Ni (at.%)').small_refined_ternary(ternaryPointsList)
    def hugeTer(self, title):
        print('{0} in double\n{1} in gamma'.format(len(self.huge_double_phase_seqList), len(self.huge_gamma_phase_seqList)))
        ternaryPointsList = cluster_main.comMathcer(matComFile='../../basicInfo/composition/composition_i_j/epma_composition.txt', clusterList=self.huge_seqList).matchManual()
        ternaryUtil.ternaryPlot(title, left_lable='Fe (at.%)', right_lable='Cr (at.%)', bottom_lable='Ni (at.%)').hugeTernary(ternaryPointsList)
    def huge_refined_ternary(self, title):
        print('{0} in double\n{1} in gamma'.format(len(self.huge_double_phase_seqList), len(self.huge_gamma_phase_seqList)))
        ternaryPointsList = cluster_main.comMathcer(matComFile='../../basicInfo/composition/composition_i_j/epma_composition.txt', clusterList=self.huge_seqList).matchManual()
        ternaryUtil.ternaryPlot(title, left_lable='Fe (at.%)', right_lable='Cr (at.%)', bottom_lable='Ni (at.%)').huge_refined_ternary(ternaryPointsList)
    def c_refined_ternary(self, title):
        print('{0} in alpha\n{1} in double\n{2} in gamma'.format(len(self.c_alpha_phase_seqList), len(self.c_double_phase_seqList), len(self.c_gamma_phase_seqList)))
        ternaryPointsList = cluster_main.comMathcer(matComFile='../../basicInfo/composition/composition_i_j/epma_composition.txt', clusterList=self.c_seqList).matchManual()
        ternaryUtil.ternaryPlot(title, left_lable='Fe (at.%)', right_lable='Cr (at.%)', bottom_lable='Ni (at.%)').c_refined_ternary(ternaryPointsList)
    def whole_refined_ternary(self, title):
        print('{0} in alpha\n{1} in double\n{2} in gamma'.format(len(self.whole_alpha_phase_seqList),
                                                                 len(self.whole_double_phase_seqList),
                                                                 len(self.whole_gamma_phase_seqList)))
        ternaryPointsList = cluster_main.comMathcer(matComFile='../../basicInfo/composition/composition_i_j/epma_composition.txt',clusterList=self.whole_seqList).matchManual()
        ternaryUtil.ternaryPlot(title, left_lable='Fe (at.%)', right_lable='Cr (at.%)',bottom_lable='Ni (at.%)').whole_refined_ternary(ternaryPointsList)
if __name__ == '__main__':
    #------------------------------- 左侧小区的单点测试 -------------------------------
    # mtp = manualTernaryPlot()
    # small_gamma_phase_seqList = mtp.small_gamma_phase_seqList
    # small_double_phase_seqList = mtp.small_double_phase_seqList
    # for point in small_double_phase_seqList:
    #     j, i = point
    #     print(j,i)
    #     manualTernaryPlot().singlePointTest(j,i,'small')
    # ------------------------------- 单点测试 -------------------------------

    #------------------------------- C区的单点测试 -------------------------------
    # mtp = manualTernaryPlot()
    # manualTernaryPlot().singlePointTest(11,20,'whole')
    # ------------------------------- C区的单点测试 -------------------------------

    # ------------------------------- 绘制人工识别的左侧小相图 -------------------------------
    # 在图片标题中加入日期和手动/自动的标注
    # python获取当前时间的用法：https://www.cnblogs.com/general-seven/p/5893744.html
    # title = 'Manual_'+datetime.datetime.now().strftime('%Y-%m-%d')+'_Fe-Cr-Ni Ternary'
    # manualTernaryPlot().smallTer(title)

    # ------------------------------- 绘制人工识别的左侧小相图*最终结果* -------------------------------
    # title = 'Manual_' + datetime.datetime.now().strftime('%Y-%m-%d') + '_Fe-Cr-Ni Ternary'
    # title = ''
    # manualTernaryPlot().small_refined_ternary(title)

    # ------------------------------- 右侧大区的单点测试 -------------------------------
    # mtp = manualTernaryPlot()
    # huge_double_phase_seqList = mtp.huge_double_phase_seqList
    # huge_gamma_phase_seqList = mtp.huge_gamma_phase_seqList
    # mtp.singlePointTest(6,28,'huge')
    # for point in huge_double_phase_seqList:
    #     j, i = point
    #     print(j,i)
    #     mtp.singlePointTest(j,i,'huge')
    # ------------------------------- 绘制人工识别的右侧大相图 -------------------------------
    # title = 'Manual_' + datetime.datetime.now().strftime('%Y-%m-%d') + '_Fe-Cr-Ni Ternary'
    # manualTernaryPlot().hugeTer(title)

    #  ------------------------------- 绘制人工识别的右侧大相图*最终结果* -------------------------------
    # title = 'Manual_' + datetime.datetime.now().strftime('%Y-%m-%d') + '_Fe-Cr-Ni Ternary'
    # title = ""
    # manualTernaryPlot().huge_refined_ternary(title)

    #  ------------------------------- 绘制人工识别的左侧C区相图*最终结果* -------------------------------
    # title = 'Manual_' + datetime.datetime.now().strftime('%Y-%m-%d') + '_Fe-Cr-Ni Ternary'
    # title = ""
    # manualTernaryPlot().c_refined_ternary(title)

    #  ------------------------------- 绘制人工识别的整个相图*最终结果* -------------------------------
    # title = 'Manual_' + datetime.datetime.now().strftime('%Y-%m-%d') + '_Fe-Cr-Ni Ternary'
    title = ""
    manualTernaryPlot().whole_refined_ternary(title)