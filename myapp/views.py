from django.shortcuts import render
import string

def homepage(request):
    return render(request, 'home.html')


def analyze(request):
    if request.method == 'POST':

        text = request.POST.get('text', '')

        remove_punc = request.POST.get('removepunc')
        capitalize = request.POST.get('capitalize')
        newlineremove = request.POST.get('newlineremove')
        spaceremove = request.POST.get('spaceremove')
        charcount = request.POST.get('charcount')

        result = text

        if remove_punc:
            new_text = ""
            for char in result:
                if char not in string.punctuation:
                    new_text += char
            result = new_text

        if capitalize:
            lines = result.split('\n')
            new_text = ""
            for line in lines:
                if len(line) > 0:
                    line = line[0].upper() + line[1:]
                    new_text += line + '\n'
            result = new_text.strip()
            
        if newlineremove:
            new_text = ""
            for char in result:
                if char != '\n' and char != '\r':
                    new_text += char
            result = new_text

        if spaceremove:
            new_text = ""
            prev_char = ""
            for char in result:
                if not (char == " " and prev_char == " "):
                    new_text += char
                prev_char = char
            result = new_text

        count = 0
        if charcount:
            count = len(result)

        return render(request, 'home.html', {
            'result': result,
            'charcount': count
        })

    return render(request, 'home.html')
