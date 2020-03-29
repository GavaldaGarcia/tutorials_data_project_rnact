# tutorials_data_project_rnact
Some tutorials to teach the experimental ESRs in RNAct about python programming and data science.

The tutorials require to have **python 3.6** or newer installed on your computer. We recommend to use **anaconda** for the ease of use and the possibility to create different environments. 

To install anaconda, visit their website https://www.anaconda.com/distribution/ and download the version for your operating system. 

Once the installation is successful you'll need to create a new environment from the terminal (the anaconda shell if you're on Windows). An example code to create a new environment is: 

`conda create --name tutorials python=3.6`

Then, you'll have to activate it with:

`conda activate tutorials`

We might need to install some packages for the tutorials to work, the following command should cover most of the cases, but we will install any forgotten package on the go when necessary:

`conda install -c conda-forge jupyterlab seaborn scipy requests`

To launch the files **from the termial**, you'll need to go to the directory that contains the jupyter notebook file:
 
 * `pwd` to know your current directory.
 
 * Use `cd [directory]` to move to the correct directory.
 
 * Use `ls` to display the content of the current directory. 
 
 Then, launch the jupyter notebook with:
`jupyter lab name_of_the_tutorial_file.ipnb`

Let's have fun!
