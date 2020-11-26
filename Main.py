import time
import os
import platform

import Util
import Logic
############### start to set env ################
WORK_DIR = os.getcwd() + "/"
PROJECT_NAME = WORK_DIR.split("/")[-2]
SYSTEM_NM = platform.system()

if SYSTEM_NM == 'Linux':
    # REAL
    pass
else:
    # DEV
    WORK_DIR = "D:/000_WORK/JangHyeWon/20201126/WORK_DIR/"

INPUT = "input/"
OUTPUT = "output/"
ANALYSIS_INFO_ARR = ["FAH pegOT2_BE analyzer.xlsx", "FAH pegOT5_BE analyzer.xlsx"]
FILT_OUT_OPT_ARR = [{'28': 'T', '33': 'G'}, {'8': 'T', '18': 'T', '46': 'G'}]
############### end setting env #################


def main():
    util = Util.Utils()
    logic = Logic.Logics()

    for idx in range(len(ANALYSIS_INFO_ARR)):
        sheet_names = util.get_sheet_names(WORK_DIR + INPUT + ANALYSIS_INFO_ARR[idx])
        filt_dict = FILT_OUT_OPT_ARR[idx]

        for sheet_name in sheet_names:
            df = util.read_excel_to_df(WORK_DIR + INPUT + ANALYSIS_INFO_ARR[idx], sheet_name)
            len_df = len(df[df.columns[0]])

            result_list = []
            for i in range(len_df):
                rg_seq = df.loc[i][2]

                if logic.is_contamed_seq(filt_dict, rg_seq):
                    continue

                wt_seq = df.loc[i][0]
                align = df.loc[i][1]
                cnt = df.loc[i][3]
                length = df.loc[i][4]
                result_list.append([wt_seq, align, rg_seq, cnt, length])

            header = ['WT Sequence', '', 'RGEN Treated Sequence', 'Count', 'Length']
            util.make_excel(WORK_DIR + OUTPUT + sheet_name + "_" + ANALYSIS_INFO_ARR[idx], header, result_list)


if __name__ == '__main__':
    start_time = time.perf_counter()
    print("start [ " + PROJECT_NAME + " ]>>>>>>>>>>>>>>>>>>")
    main()
    print("::::::::::: %.2f seconds ::::::::::::::" % (time.perf_counter() - start_time))