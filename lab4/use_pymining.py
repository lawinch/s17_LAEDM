import pandas as pd
# See: https://github.com/bartdag/pymining
from pymining import itemmining, assocrules, seqmining

enrollment = pd.read_csv('course-enrollment.csv')
grouped = (enrollment.groupby('user_id')['course_id']
           .agg({'course_id': lambda x: x.tolist()})
           .reset_index()[-40000:])

events = grouped.course_id.values.tolist()

relim_input = itemmining.get_relim_input(events)
report = itemmining.relim(relim_input, min_support=2)

print('Associative rules:')
rules = assocrules.mine_assoc_rules(report, min_support=5, min_confidence=0.6)
rules_df = pd.DataFrame.from_records(rules, columns=['from', 'to', 'support', 'confidence'])
print(rules_df.sort_values('support', ascending=False).head(10))

print('Frequent sequences: ')
freq_seqs = seqmining.freq_seq_enum(events, 5)
freq_seqs_df = pd.DataFrame.from_records(list(freq_seqs), columns=['sequence', 'support'])
freq_seqs_df['sequence_len'] = freq_seqs_df.sequence.apply(len)
print(freq_seqs_df[freq_seqs_df.sequence_len > 1]
      .sort_values(['sequence_len', 'support'], ascending=False).head(10))
