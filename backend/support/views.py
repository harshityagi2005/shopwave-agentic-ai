from rest_framework.decorators import api_view
from rest_framework.response import Response
from .agent import process_ticket

@api_view(["POST"])
def process_ticket_view(request):
    ticket = request.data
    result = process_ticket(ticket)
    return Response(result)