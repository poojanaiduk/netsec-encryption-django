
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

# ASCII values of 'A' to 'Z' : 65 to 90
# ASCII values of 'a' to 'z' : 97 to 122
# If the character is uppercase or lowercase
# alphabet, we encrypt or decrypt it as per
# the rule, otherwise it is added as it is
# function for decrypting the
# ciphertext to produce plaintext
# and rendering the plaintext
# to index.html
def solve(inp1):
    out1 = ''
    for c in inp1:
        if 'A' <= c <= 'Z':
            extra = ord(c) - ord('A')
            out1 += chr(ord('A') + 25 - extra)
        elif 'a' <= c <= 'z':
            extra = ord(c) - ord('a')
            out1 += chr(ord('a') + 25 - extra)
        else:
            out1 += c
    return out1

def poo(request):
    if request.method == "GET":
        template = loader.get_template('index.html')
        return HttpResponse(template.render({'inp1': '', 'inp2': ''}, request))
    else:
        if request.POST.get('submit_type') == 'encrypt':
            inp1 = request.POST.get('inp1')
            template = loader.get_template('index.html')
            out1 = solve(inp1)
            return HttpResponse(template.render({'inp1': inp1, 'inp2': out1}, request))
        else:
            inp2 = request.POST.get('inp2')
            template = loader.get_template('index.html')
            out2 = solve(inp2)
            return HttpResponse(template.render({'inp1': out2, 'inp2': inp2}, request))