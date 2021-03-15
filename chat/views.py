from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from utils.secrets import get_secret
import neispy

NEIS_API_KEY = get_secret("NEIS_API_KEY")
neis = neispy.Client(KEY=NEIS_API_KEY)
scinfo = neis.schoolInfo(SCHUL_NM="한세사이버보안고등학교")
AE = scinfo[0].ATPT_OFCDC_SC_CODE
SE = scinfo[0].SD_SCHUL_CODE


@api_view(["POST"])
def meal_info(request):
    return Response(request.data, status=status.HTTP_200_OK)