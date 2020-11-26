# filter_out_contaminated_seq_by_idx_char



각 excel파일의 A2 cell에 있는 것이 align할 reference 에 해당함.
FAH_pegOT2 : 28번째가 "T" & 33번째가 "G" 인 read들 제거 --> 나머지만 분석.
FAH_pegOT5 : 8번째가 "T" & 18번째가 "T" & 46번째가 "G" read들 제거 --> 나머지만 분석.

target_column : RGEN_Treated_Sequence 
1. FAH pegOT2_BE analyzer.xlsx 의 경우
    1. re_seq = reversed_comp(RGEN Treated Sequence)
    2. if re_seq[25 - 1] == 'T' and re_seq[30 - 1] == 'G': filt_out
    3. output = 
    
how to count index in RGEN_Treated_Sequence column
AG---CT
1234567