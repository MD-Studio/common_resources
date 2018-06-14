FROM mdstudio/mdstudio_docker3:0.0.1

COPY . /home/mdstudio/common_resources/

COPY lie_amber /home/mdstudio/lie_amber/lie_amber

RUN chown mdstudio:mdstudio /home/mdstudio/common_resources

WORKDIR /home/mdstudio/common_resources

RUN pip -e .

USER mdstudio

CMD ["bash", "entry_point_common_resources.sh"]
