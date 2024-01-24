export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

cd ~/repos/weather_scraper
pyenv shell 3.12
python gsheet.py