rm -r -f Honey_Server
git clone https://github.com/wudijimao/Honey_Server.git Honey_Server
cd Honey_Server
nohup python -u main.py > out.log 2>&1 &