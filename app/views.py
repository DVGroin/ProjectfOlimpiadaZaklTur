from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import os
from django.conf import settings
from django.core.files.storage import default_storage
# Create your views here.
def test_view(request):
    return render(request, "123.html")

def upload_audio(request):
    if request.method == 'POST' and request.FILES.get('audio_file'):
        audio_file = request.FILES['audio_file']
        
        # Проверка расширения (по желанию)
        ext = os.path.splitext(audio_file.name)[1].lower()
        allowed = ['.mp3', '.wav', '.ogg', '.m4a', '.flac']
        if ext not in allowed:
            return HttpResponse('Неподдерживаемый формат файла', status=400)

        # Сохраняем файл в папку media/uploads/
        file_path = default_storage.save(f'uploads/{audio_file.name}', audio_file)
        
        # Здесь можно добавить логику обработки файла, сохранить ссылку в БД и т.д.
        # Например: AudioFile.objects.create(file=file_path, ...)

        return HttpResponse(f'Файл успешно загружен: {file_path}')
    
    # GET-запрос — показываем форму
    return render(request, 'upload_audio.html')