from random import shuffle

initial_file = 'data'

complete_file = open(initial_file+'.txt', 'r').readlines()
complete_gt_file = open(initial_file+'_gt.txt', 'r').readlines()

train_file = open('train.txt', 'w')
train_gt_file = open('train_gt.txt', 'w')

test_file = open('val.txt', 'w')
test_gt_file = open('val_gt.txt', 'w')

lines = []
for line in complete_file:
    lines.append(line.strip())

lines_gt = []
for line in complete_gt_file:
    lines_gt.append(line.strip())

indices = list(range(len(lines)))

shuffle(indices)

count = 0
for i in indices:
    if count<550:
        train_file.write(lines[indices[i]]+'\n')
        train_gt_file.write(lines_gt[indices[i]]+'\n')
        count+=1
    else:
        test_file.write(lines[indices[i]]+'\n')
        test_gt_file.write(lines_gt[indices[i]]+'\n')


test_file.close()
train_file.close()
train_gt_file.close()
test_gt_file.close()