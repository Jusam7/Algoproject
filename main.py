import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance .csv')
print(df)
df.info()

# Подтверждение первой гипотезы: "Ученики, которые хорошо поели перед тестом, написали его лучше
norm = df[df['lunch']=='standard']['math score'].mean()
malo = df[df['lunch']=='free/reduced']['math score'].mean()
s = pd.Series(data = [norm, malo], index = ['Стандартный обед', "Бесплатный обед"])
s.plot(kind = 'barh', figsize = (8, 5), grid = True,)
plt.show()

# Подтверждение второй гипотезы: "Если ученик прошёл курс подготовки к тестированию, то он написа тест лучше"
curs = df[df['test preparation course']=='completed']['math score'].mean()
necurs = df[df['test preparation course']=='none']['math score'].mean()
s = pd.Series(data = [norm, malo], index = ['Пройденный курс', "Без курса"])
s.plot(kind = 'barh', figsize = (8, 5), grid = True,)
plt.show()


