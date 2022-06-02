import os
from tqdm import tqdm

code_folder = 'your code folder'
problem_folders = os.listdir(code_folder)


def preprocess_script(script):
    """
    간단한 전처리 함수
    주석 -> 삭제
    '    '-> tab 변환
    다중 개행 -> 한 번으로 변환
    """
    with open(script,'r',encoding='utf-8') as file:
        lines = file.readlines()
        preproc_lines = []
        for line in lines:
            if line.lstrip().startswith('#'):
                continue
            line = line.rstrip()
            if '#' in line:
                line = line[:line.index('#')]
            line = line.replace('\n','')
            line = line.replace('    ','\t')
            if line == '':
                continue
            preproc_lines.append(line)
        preprocessed_script = '\n'.join(preproc_lines)
    return preprocessed_script

preproc_scripts = []
problem_nums = []

for problem_folder in tqdm(problem_folders):
    scripts = os.listdir(os.path.join(code_folder,problem_folder))
    problem_num = scripts[0].split('_')[0]
    for script in scripts:
        script_file = os.path.join(code_folder,problem_folder,script)
        preprocessed_script = preprocess_script(script_file)

        preproc_scripts.append(preprocessed_script)
    problem_nums.extend([problem_num]*len(scripts))