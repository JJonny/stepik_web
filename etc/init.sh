sudo rm -r /etc/nginx/sites-enabled/default
sudo ln -s /home/jonny/web/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/jonny/web/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -s /home/jonny/web/box/web/etc/guni-dj.py /etc/gunicorn.d/guni-dj.py
sudo /etc/init.d/gunicorn restart
#sudo gunicorn -b 0.0.0.0:8080 etc.hello:app
#sudo gunicorn -b 0.0.0.0:8000 wsgi:application
