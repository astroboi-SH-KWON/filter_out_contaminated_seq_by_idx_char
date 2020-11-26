# filter_out_contaminated_seq_by_idx_char



각 excel파일의 A2 cell에 있는 것이 align할 reference 에 해당함.
FAH_pegOT2 : 28번째가 "T" & 33번째가 "G" 인 read들 제거 --> 나머지만 분석.
FAH_pegOT5 : 8번째가 "T" & 18번째가 "T" & 46번째가 "G" read들 제거 --> 나머지만 분석.

target_column : RGEN_Treated_Sequence 

how to count index in RGEN_Treated_Sequence column
AG---CT
1234567