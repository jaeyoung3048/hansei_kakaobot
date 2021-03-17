from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from utils.secrets import get_secret
import neispy, json

NEIS_API_KEY = get_secret("NEIS_API_KEY")
neis = neispy.Client(KEY=NEIS_API_KEY)
scinfo = neis.schoolInfo(SCHUL_NM="한세사이버보안고등학교")
AE = scinfo[0].ATPT_OFCDC_SC_CODE
SE = scinfo[0].SD_SCHUL_CODE


@api_view(["POST"])
def meal_info(request):

    status_code = status.HTTP_200_OK

    req = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": ""
                    }
                }
            ]
        }
    }

    try:
        user_utterance_date = request.data["action"]["detailParams"]["date"]
        YMD = json.loads(user_utterance_date["value"])["date"].replace("-","")

        scmeal = neis.mealServiceDietInfo(AE, SE, MLSV_YMD=YMD)
        meal = scmeal[0].DDISH_NM.replace("<br/>", "\n")

        req["template"]["outputs"][0]["simpleText"]["text"] = str("{}의 급식입니다!\n{}".format(user_utterance_date["origin"], meal))

    except Exception as e:
        req["template"]["outputs"][0]["simpleText"]["text"] = "해당 날짜의 급식정보가 없어요 ㅠ"
        req["error"] = str(e)

    return Response(req, status=status_code)
