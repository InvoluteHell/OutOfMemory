import sys
import typing
import pathlib


filter_ext = [".md", ".txt", ".png", ".jpg", ".gif", ".bmp"]


def file_score(path: pathlib.Path) -> typing.Optional[typing.Tuple[int, int, int]]:
    """Return the score of a file based on its length and number of used characters."""
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        print(f'File: {path} is not UTF-8.')
        return None
    except Exception as e:
        print(f'File: {path} cannot be read. Error: {e}')
        return None
    
    # if not content.isascii():
    #     print(f'File: {path} is not ASCII.')
    #     return None
    
    # for char in 'HELLOWORLDhelloworld':
    #     if char in content:
    #         print(f'File: {path} contains {char}.')
    #         return None

    # Score based on length
    score_len = len(content)

    # Score based on number of used characters
    score_cate = len(set(content))

    return score_len, score_cate, score_len * score_cate


def best_file_score(path_list: typing.List[pathlib.Path]) -> typing.Optional[typing.Tuple[int, int, int]]:
    """Return the best score of a list of files."""
    
    str_list = [str(p) for p in path_list]
    print(f'Scoring files: {str_list}\n')

    min_scores = (0, 0, 0)
    min_path = pathlib.Path()
    for path in path_list:
        if not path.exists():
            print(f'File: {path} does not exist.')
            continue
        scores = file_score(path)
        if not scores:
            continue
        print(f'File: {path}, Length: {scores[0]}, Category: {scores[1]}, Score: {scores[2]}')
        if scores[2] < min_scores[2] or min_scores[2] == 0:
            min_scores = scores
            min_path = path
            
    if min_scores[2] == 0:
        print(f'\nNo valid file in {str_list}.\n\n')
        return None
    else:
        print(f'\nBest file: {min_path}, Length: {min_scores[0]}, Category: {min_scores[1]}, Score: {min_scores[2]}\n\n')
        return min_path, min_scores


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('Usage: python scoring.py <files>')
        exit()

    paths = [pathlib.Path(arg) for arg in sys.argv[1:] if not pathlib.Path(arg).suffix in filter_ext]
    best_file_score(paths)
