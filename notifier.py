import requests, re, subprocess, time, sys

oq = ""
while True:
    t = requests.get("https://stackoverflow.com/questions/tagged/python?sort=newest&pageSize=1").text
    nq = re.findall('question-hyperlink">(.*?)<', t)[0]
    if nq != oq:
        tgs = re.findall('tag">(.*?)<', t)
        tgs = tgs[:next(i for i, e in enumerate(tgs) if tgs.index(e) != i)]
        subprocess.call(["notify-send", nq, "[" + "] [".join(tgs) + "]"])
        if len(sys.argv) > 1:
            for i in range(20):
                sys.stdout.write('\a')
                sys.stdout.flush()
                time.sleep(0.05)
        oq = nq
    time.sleep(20)
