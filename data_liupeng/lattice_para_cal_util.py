"""
lattice_para_cal
    本类只计算γ相（fcc）（200）衍射晶面50.673°==>3.5975
"""
def lattice_para_calc(double_theta):
    import math
    # 将2θ转换为θ
    theta = double_theta / 2
    # math 只认弧度，不认角度，将角度转换为弧度
    arc = theta * math.pi / 180
    # Copper target 1.5406
    return 1.5406 / math.sin(arc)
def get_avg_inten(file_path):
    avg_inten_dict = {}
    with open(file_path, 'r') as file:
        for line in file.readlines():
            j, i, avg_inten = list(map(float, line.strip().split('\t')[:3]))
            avg_inten_dict[(int(j), int(i))] = avg_inten
    return avg_inten_dict
def find_peaks(row, col_list, range_tuple, folder_path, avg_inten_dict):
    import os
    file_names = os.listdir(folder_path)
    for file_name in file_names:
        if not file_name.endswith('.txt'):
            continue
        j, i = list(map(int, file_name.split('_')[:2]))
        if (j == row) and (i in col_list):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r') as file:
                x_list = []
                y_list = []
                for line in file.readlines():
                    x, y = list(map(float, line.strip().split(' ')))
                    x_list.append(x)
                    y_list.append(y)
                select_x_y_list = [(x, y) for x, y in zip(x_list, y_list) if (x > range_tuple[0]) and (x < range_tuple[1])]
                select_y_list = [y for x, y in select_x_y_list]
                y_max = max(select_y_list)
                if y_max > avg_inten_dict[(j,i)]:
                    y_max_index = select_y_list.index(y_max)
                    x = [x for x, y in select_x_y_list][y_max_index]
                    print('Row-{0}\t\tCol-{1}\t:\t{2}'.format(j, i, x))
"""
应为第一次自动处理后一些晶格常数异常的大，在下面的类中，选出异常点的（200）晶面对应的真实角度，重新计算
"""
import pandas as pd
# from cluster import cluster_main
class serialize_lattice_para:
    def __init__(self, lc_excel_path, sheet_name, com_file_path):
        self.lc_excel_path = lc_excel_path
        self.sheet_name = sheet_name
        self.com_dict = self.get_com_dict(com_file_path)
    def get_com_dict(self, com_file_path):
        com_dict = cluster_main.comMathcer(matComFile=com_file_path).getComDict()
        return com_dict
    def serialize(self):
        lc_df = pd.read_excel(self.lc_excel_path, sheet_name=self.sheet_name)
        with open('whole_lc_info.txt', 'w+') as file:
            for index, row_series in lc_df.iterrows():
                # print(index, row_series)
                key = (int(row_series[1]), int(row_series[2]))
                Fe = self.com_dict[key]['Fe']
                Cr = self.com_dict[key]['Cr']
                Ni = self.com_dict[key]['Ni']
                lc = lattice_para_calc(row_series[0])
                line = str(Fe)+'\t'+str(Cr)+'\t'+str(Ni)+'\t'+str(lc)+'\n'
                file.write(line)

if __name__ == '__main__':
    # double_theta = 52.1
    # print('2θ {0} has a = {1}'.format(double_theta, lattice_para_calc(double_theta)))

    avg_inten_dict = get_avg_inten('./20190423_9_whole_raw_vector.txt')
    # folder_path = '../../basicInfo/chi/chi2txt/afterCalibrated/bg_sm_rename_linearRM'
    folder_path = './huge'
    row = 1
    col_list = [i for i in range(37, 47+1)]
    range_tuple = (44.2, 44.9)
    find_peaks(row=row, col_list=col_list, range_tuple=range_tuple, folder_path=folder_path,avg_inten_dict=avg_inten_dict)

    # slp = serialize_lattice_para(lc_excel_path='../../../lattice_constants/lattice_constants_statistic.xlsx', sheet_name='whole_area_selected', com_file_path='../../basicInfo/composition/composition_i_j/epma_composition.txt')
    # slp.serialize()