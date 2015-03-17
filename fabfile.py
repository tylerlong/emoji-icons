from fabric.api import local


def update():
    local('rm -rf *.png')
    local('wget https://github.com/arvida/emoji-cheat-sheet.com/archive/master.zip')
    local('unzip master.zip && rm master.zip')
    local('cp -r emoji-cheat-sheet.com-master/public/graphics/emojis/* .')
    local('rm -rf emoji-cheat-sheet.com-master')
