import glasdoor_sele as gs
import pandas as ps
path = "D:\Joseph\DS_Projects\DS_Salary\chromedriver.exe"

df = gs.get_jobs('data scientist', 15, False, path, 15)