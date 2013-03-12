import editor
import clipboard
import console
import urllib

editor.reload_files()
filePath = editor.get_path()

rawName = filePath[filePath.rfind('/Documents/') + 11:-3]

pythonistaUrl = 'pythonista://' + urllib.quote(rawName) + '?action=run&argv='
clipboard.set(pythonistaUrl)
console.alert('Path copied to clipboard:',pythonistaUrl)

