import pandas
import matplotlib.pyplot as plt
plt.style.use('ggplot')

weather = pandas.read_csv("./data/oxforddata.txt", sep='\t')

target = 'rain'
weather['Period'] = weather['yyyy'].apply(lambda x: 'Before' if x < 1991 else 'After')
weather = weather.groupby(['mm','Period']).mean().reset_index().pivot(index='mm', columns='Period', values=target).reset_index()
print weather

weather[['After','mm','Before']].plot(kind='kde',x='mm')
plt.title('{0} comparison before and after 1991'.format(target))
plt.xlabel(target)
plt.show()
