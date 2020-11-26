
from astroboi_bio_tools.ToolLogic import ToolLogics
class Logics(ToolLogics):
    def is_contamed_seq(self, filt_dict, trgt_seq):
        match_cnt = 0
        for idx_key, val in filt_dict.items():
            if trgt_seq[int(idx_key) - 1] == val:
                match_cnt += 1
        if match_cnt == len(filt_dict):
            return True
        return False
