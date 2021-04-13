from glob import glob

text = []
for i in range(4):
    for i, p in enumerate(glob(f'qualitative_results_{i}/n0*/*JPEG')):
        text.append(f'<div class="col col-lg "><img src="../imagenet100_qualitative_results/{p}" alt=""></div>')
        if i > 2:
            break

print('\n'.join(text))
