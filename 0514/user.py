def login(uid, pwd):
    # 로그인 정보 생성
    memDic = {'kim': 'k1234',
              'lee': 'l1234',
              'jung': 'j1234',
              'park': 'p1234',
              'song': 's1234'
              }

    uid = uid.lower() # 소문자로 바꾸기
    loginOK = False
    if uid in memDic.keys() and pwd == memDic[uid]: # ID와 PWD가 일치하면
        loginOK = True
    else:
        loginOK = False
    return loginOK