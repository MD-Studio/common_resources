FROM mdstudio/mdstudio_docker3:0.0.3

COPY . /home/mdstudio/common_resources/

RUN chown mdstudio:mdstudio /home/mdstudio/common_resources

WORKDIR /home/mdstudio/common_resources

RUN pip install -e . 

CMD ["bash", "entry_point_common_resources.sh"]
