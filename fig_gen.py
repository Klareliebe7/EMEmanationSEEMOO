import matplotlib.pyplot as plt

###########################start_before_input
res_dict_eve = {3: {'inferenz': 53, 'length': 60, 'accuracy': 0.8833333333333333}, 5: {'inferenz': 86, 'length': 100, 'accuracy': 0.86}, 10: {'inferenz': 174, 'length': 200, 'accuracy': 0.87}, 15: {'inferenz': 268, 'length': 300, 'accuracy': 0.8933333333333333}, 20: {'inferenz': 353, 'length': 400, 'accuracy': 0.8825}, 30: {'inferenz': 526, 'length': 600, 'accuracy': 0.8766666666666667}, 40: {'inferenz': 706, 'length': 800, 'accuracy': 0.8825}, 50: {'inferenz': 878, 'length': 1000, 'accuracy': 0.878}, 70: {'inferenz': 1213, 'length': 1400, 'accuracy': 0.8664285714285714}, 90: {'inferenz': 1564, 'length': 1800, 'accuracy': 0.8688888888888889}}
res_dict ={3: {'inferenz': 52, 'length': 60, 'accuracy': 0.8666666666666667}, 5: {'inferenz': 88, 'length': 100, 'accuracy': 0.88}, 10: {'inferenz': 176, 'length': 200, 'accuracy': 0.88}, 15: {'inferenz': 270, 'length': 300, 'accuracy': 0.9}, 20: {'inferenz': 355, 'length': 400, 'accuracy': 0.8875}, 30: {'inferenz': 528, 'length': 600, 'accuracy': 0.88}, 40: {'inferenz': 708, 'length': 800, 'accuracy': 0.885}, 50: {'inferenz': 880, 'length': 1000, 'accuracy': 0.88}, 70: {'inferenz': 1215, 'length': 1400, 'accuracy': 0.8678571428571429}, 90: {'inferenz': 1564, 'length': 1800, 'accuracy': 0.8688888888888889}}
x_eve =[]
y_eve = []
for leng in res_dict_eve:
    x_eve.append(leng)
    y_eve.append(res_dict_eve[leng]['accuracy'])

x =[]
y= []
for leng in res_dict:
    x.append(leng)
    y.append(res_dict[leng]['accuracy'])

font1 = {'color':'black','size':12}
font2 = {'color':'black','size':12}

plt.title("Antenna starts to capture signal before keyboards input", fontdict = font1)
plt.xlabel("Length of input trace sequence", fontdict = font2)
plt.ylabel("Accuracy of inference", fontdict = font2)

plt.plot(x_eve, y_eve, marker = '^', ls = '-.',color = 'g',label='Even initial probabilities')
plt.plot(x, y, marker = 'o', ls = ':',color = 'b',label='Not even initial probabilities')
plt.legend()
plt.savefig('./capture_before_input_start.jpg',dpi = 600)
plt.show()
###########################start_after_input
res_dict_eve = {3: {'inferenz': 44, 'length': 60, 'accuracy': 0.7333333333333333}, 5: {'inferenz': 77, 'length': 100, 'accuracy': 0.77}, 10: {'inferenz': 165, 'length': 200, 'accuracy': 0.825}, 15: {'inferenz': 253, 'length': 300, 'accuracy': 0.8433333333333334}, 20: {'inferenz': 347, 'length': 400, 'accuracy': 0.8675}, 30: {'inferenz': 522, 'length': 600, 'accuracy': 0.87}, 40: {'inferenz': 698, 'length': 800, 'accuracy': 0.8725}, 50: {'inferenz': 870, 'length': 1000, 'accuracy': 0.87}, 70: {'inferenz': 1229, 'length': 1400, 'accuracy': 0.8778571428571429}, 90: {'inferenz': 1585, 'length': 1800, 'accuracy': 0.8805555555555555}}
res_dict = {3: {'inferenz': 44, 'length': 60, 'accuracy': 0.7333333333333333}, 5: {'inferenz': 79, 'length': 100, 'accuracy': 0.79}, 10: {'inferenz': 164, 'length': 200, 'accuracy': 0.82}, 15: {'inferenz': 253, 'length': 300, 'accuracy': 0.8433333333333334}, 20: {'inferenz': 347, 'length': 400, 'accuracy': 0.8675}, 30: {'inferenz': 520, 'length': 600, 'accuracy': 0.8666666666666667}, 40: {'inferenz': 697, 'length': 800, 'accuracy': 0.87125}, 50: {'inferenz': 872, 'length': 1000, 'accuracy': 0.872}, 70: {'inferenz': 1229, 'length': 1400, 'accuracy': 0.8778571428571429}, 90: {'inferenz': 1584, 'length': 1800, 'accuracy': 0.88}}
x_eve =[]
y_eve = []
for leng in res_dict_eve:
    x_eve.append(leng)
    y_eve.append(res_dict_eve[leng]['accuracy'])

x =[]
y= []
for leng in res_dict:
    x.append(leng)
    y.append(res_dict[leng]['accuracy'])



plt.title("Antenna starts to capture signal during keyboards input", fontdict = font1)
plt.xlabel("Length of input trace sequence", fontdict = font2)
plt.ylabel("Accuracy of inference", fontdict = font2)

plt.plot(x_eve, y_eve, marker = '^', ls = '-.',color = 'y',label='Even initial probabilities')
plt.plot(x, y, marker = 'o', ls = ':',color = 'r',label='Not even initial probabilities')
plt.legend()
plt.savefig('./capture_after_input_start.jpg',dpi = 600)
plt.show()

###########################infuence of whether start during input
res_dict_eve = {3: {'inferenz': 52, 'length': 60, 'accuracy': 0.8666666666666667}, 5: {'inferenz': 88, 'length': 100, 'accuracy': 0.88}, 10: {'inferenz': 176, 'length': 200, 'accuracy': 0.88}, 15: {'inferenz': 270, 'length': 300, 'accuracy': 0.9}, 20: {'inferenz': 355, 'length': 400, 'accuracy': 0.8875}, 30: {'inferenz': 528, 'length': 600, 'accuracy': 0.88}, 40: {'inferenz': 708, 'length': 800, 'accuracy': 0.885}, 50: {'inferenz': 880, 'length': 1000, 'accuracy': 0.88}, 70: {'inferenz': 1215, 'length': 1400, 'accuracy': 0.8678571428571429}, 90: {'inferenz': 1564, 'length': 1800, 'accuracy': 0.8688888888888889}}
res_dict = {3: {'inferenz': 44, 'length': 60, 'accuracy': 0.7333333333333333}, 5: {'inferenz': 79, 'length': 100, 'accuracy': 0.79}, 10: {'inferenz': 164, 'length': 200, 'accuracy': 0.82}, 15: {'inferenz': 253, 'length': 300, 'accuracy': 0.8433333333333334}, 20: {'inferenz': 347, 'length': 400, 'accuracy': 0.8675}, 30: {'inferenz': 520, 'length': 600, 'accuracy': 0.8666666666666667}, 40: {'inferenz': 697, 'length': 800, 'accuracy': 0.87125}, 50: {'inferenz': 872, 'length': 1000, 'accuracy': 0.872}, 70: {'inferenz': 1229, 'length': 1400, 'accuracy': 0.8778571428571429}, 90: {'inferenz': 1584, 'length': 1800, 'accuracy': 0.88}}
x_eve =[]
y_eve = []
for leng in res_dict_eve:
    x_eve.append(leng)
    y_eve.append(res_dict_eve[leng]['accuracy'])

x =[]
y= []
for leng in res_dict:
    x.append(leng)
    y.append(res_dict[leng]['accuracy'])


# plt.title("Influence of when the antenna starts to capture signal", fontdict = font1)
plt.xlabel("Length of input trace sequence", fontdict = font2)
plt.ylabel("Accuracy of inference", fontdict = font2)

plt.plot(x_eve, y_eve, marker = '^', ls = '-.',color = 'b',label='Start before keyboard input')
plt.plot(x, y, marker = 'o', ls = ':',color = 'r',label='Start during keyboard input')
plt.legend()
plt.savefig('./when_start.jpg',dpi = 600)
plt.show()
