#working in env called pykevin
reticulate::conda_python('pykevin')

#creat enviroment py

reticulate::repl_python()


#to install any dependency
py_install("pandas")
