from math import cos, pi, floor

import requests

URL = 'https://www.profellow.com/fellowship/?page=1'


def parse_challenge(page):
    """
    Parse a challenge given by mmi and mavat's web servers, forcing us to solve
    some math stuff and send the result as a header to actually get the page.
    This logic is pretty much copied from https://github.com/R3dy/jigsaw-rails/blob/master/lib/breakbot.rb
    """
    top = page.split('<script>')[1].split('\n')
    challenge = top[1].split(';')[0].split('=')[1]
    challenge_id = top[2].split(';')[0].split('=')[1]
    return {'challenge': challenge, 'challenge_id': challenge_id, 'challenge_result': get_challenge_answer(challenge)}


def get_challenge_answer(challenge):
    """
    Solve the math part of the challenge and get the result
    """
    arr = list(challenge)
    last_digit = int(arr[-1])
    arr.sort()
    min_digit = int(arr[0])
    subvar1 = (2 * int(arr[2])) + int(arr[1])
    subvar2 = str(2 * int(arr[2])) + arr[1]
    power = ((int(arr[0]) * 1) + 2) ** int(arr[1])
    x = (int(challenge) * 3 + subvar1)
    y = cos(pi * subvar1)
    answer = x * y
    answer -= power
    answer += (min_digit - last_digit)
    answer = str(int(floor(answer))) + subvar2
    return answer


def main():
    url = 'https://www.profellow.com/fellowship/?page=1'
    s = requests.Session()
    s.headers['user-agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    r = s.get(url)
    # r.html.render(timeout=8000)
    print(r.status_code)
    print(r.content)

if __name__ == '__main__':
    main()
