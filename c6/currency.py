# 모듈을 임포트한다
import json
import urllib.request

# 환율 정보를 받는 클래스
class Currency:
    # 환율 정보를 받을 수 있는 곳
    API = "http://api.aoikujira.com/kawase/json/usd"

    # 비공개 메서드
    def __get_api(self):
        ''' API로 오늘의 환율 정보를 가져온다 '''
        res = urllib.request.urlopen(Currency.API)
        return res.read().decode('utf8')

    def __analize_result(self, json_str):
        ''' 결과를 해석한다 '''
        return json.loads(json_str)
    
    # 공개 메서드
    def get_result(self):
        ''' API로 환율 정보를 가져온다 '''
        json_str = self.__get_api()
        return self.__analize_result(json_str)

    # 정적 메서드
    @staticmethod
    def get_usd_krw():
        ''' USD/KRW 결과를 가져온다 '''
        currency = Currency()
        data = currency.get_result()
        usd = data.get("KRW", -1)
        return usd

# 오늘의 환율 정보를 표시한다
print("USD:KRW = 1:", Currency.get_usd_krw())
