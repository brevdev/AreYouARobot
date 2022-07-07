run jupyter notebook

```
docker run --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v "/home/brev/workspace/AreYouARobot/work":/home/jovyan/work jupyter/scipy-notebook:lab-3.4.3
```

and copy the link from output into your browser

```

    To access the server, open this file in a browser:
        file:///home/jovyan/.local/share/jupyter/runtime/jpserver-72-open.html
    Or copy and paste one of these URLs:
        http://cc3497583ba8:8888/lab?token=115cb362e7f31df359a03ddc01b0e8e120d08e0375e1f97d
     or http://127.0.0.1:8888/lab?token=115cb362e7f31df359a03ddc01b0e8e120d08e0375e1f97d # <----- copy this one!
```

generate function text

```
python gentext.py
```

generate function names to copy into `all_strategies` array

```
python genfuncs.py
```

generate function names to copy into `all_strategies` array

```
python genfuncs_reduced.py
```
