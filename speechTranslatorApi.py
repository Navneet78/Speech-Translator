from flask import Flask, send_file
from flask_restplus import Resource, Api
from Main_App import speech_convert
import os
from werkzeug import secure_filename
from time import time
import languages
import werkzeug
import settings
app= Flask(__name__)
api=Api(app = app,
		  version = "1.0",
		  title = "Speech to speech converter",
		  description = "Convert your speech into another different language")
name_space = api.namespace('names', description='')


class get_audio(Resource):
    speech_converter_parser = api.parser()
    speech_converter_parser.add_argument('input_language',
                                         type=str,
                                         required=True,
                                         choices=list(languages.languages.keys()),
                                         help="This field is required",
                                         location='form'),

    speech_converter_parser.add_argument('output_language',
                                         type=str,
                                         required=True,
                                         choices=list(languages.languages.keys()),
                                         help="This field is required",
                                         location='form')

    speech_converter_parser.add_argument('audio_file',
                                         type=werkzeug.datastructures.FileStorage,
                                         required=True,
                                         help="This field is required",
                                         location='files')
    @api.expect(speech_converter_parser)
    def post(self):
        data= get_audio.speech_converter_parser.parse_args()
        file = data['audio_file']
        if file:
            filename = secure_filename(file.filename)
            current_time = time()
            filename = str(current_time) + "_" + filename
            file.save(os.path.join(filename))
        translator=speech_convert()
        translator.speech_to_speech(filename,data['input_language'], data['output_language'])
        filepath = os.path.join(settings.output_path,  translator.FileName)
        return send_file(filepath, mimetype="audio/wav")

api.add_resource(get_audio, '/get_audio')
app.run(port=5000, debug=True)












# if file:
#         filename = secure_filename(file.filename)
#         current_time = time()
#         filename = str(current_time) + "_" + filename
#         file.save(os.path.join(filename))
#         # move(os.path.join(filename), os.path.join("input_audio.wav"))
#         stt_result = do_work(filename)
#         return Response(response=stt_result, status=200, mimetype="application/json", )