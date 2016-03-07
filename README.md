# hackbright

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)

brew install pyenv pyenv-virtualenv

if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi

vim .bash_profile

if which pyenv > /dev/null; then eval "$(pyenv init -)"; fi
if which pyenv-virtualenv-init > /dev/null; then eval "$(pyenv virtualenv-init -)"; fi

:wq

pyenv versions

pyenv install 2.7.11

pyenv global 2.7.11

pip install requests

pyenv virtualenv 2.7.11 hackbright

"navigate to directory with project"
pyenv local hackbright


