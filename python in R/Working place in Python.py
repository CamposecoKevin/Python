#working in env called pykevin
reticulate::conda_python('pykevin')

#creat enviroment py
reticulate::repl_python()


#to install any dependency, its necesary to realiza after to inicializate py
py_install("pandas")
reticulate::py_install("matplotlib.pyplot")
