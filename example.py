# Modify your own settings.json file to set source/result folders 
# and other settings.
import audio_preprocessor
import pdb

if __name__=='__main__':
	nogada = audio_preprocessor.Audio_Preprocessor(settings_path='settings.json')
	nogada.index()
	nogada.get_permutations()
	nogada.convert_all()