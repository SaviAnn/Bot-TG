FROM python:slim
ENV TOKEN='6045276061:AAFq_6NjQfmu198X2DBu96MWZYszDKjSe5A'
COPY . . 
RUN pip install -r requirements.txt
CMD python bot.py