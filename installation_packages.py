import pip

def import_or_install(package):
    try:
        __import__(package)
    except:
        pip.main(['install', package]) 