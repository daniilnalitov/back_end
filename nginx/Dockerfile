FROM nginx
# удаляем файл с настройками nginx по умолчанию
RUN rm /etc/nginx/conf.d/default.conf 
# добавляем файл с нашими настройками nginx
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
