import py_midicsv as pm

notes = [[196.8378, 187.87497, 176.66187], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953], [190.23453, 163.71912, 152.12268], [168.79723, 131.80833, 126.07507], [158.00676, 99.30591, 103.63717], [157.83841, 72.67649, 88.29953]]
print(len(notes))
def data_form(text):
    temp = ['0, 0, Header, 1, 3, 256\n', '1, 0, Start_track\n',  '1, 0, Title_t, "Computer Masterpiece"\n', '1, 0, Text_t, "Mr. Computer and Mason Choi"\n', '1, 0, Time_signature, 4, 4, 24, 8', '1, 0, Tempo, 1000000', '1, 0, End_track\n', '2, 0, Start_track\n', '2, 0, Title_t, "Piano"\n', '2, 0, Program_c, 0, 0\n', '2, 0, Control_c, 0, 7, 85\n', '2, 0, Control_c, 0, 10, 76\n']
    # increase tempo value for slower song
    time = 64
    time_shift = 0

    for i in range(len(text) - 1):
        if i == 0:
            temp.append('2, %d, Note_on_c, 1, %d, 20\n' % (time, int(text[i][1]))) # Why text[i + 1] not just text[i]????
            time += int(text[i][0])

        elif time_shift != 0:
            time_shift -= 1

        elif (len(text) - 4) > i > 0:
            if 57 < text[i][1] < 66:
                temp.append('2, %d, Note_off_c, 1, %d, 0\n' % (time, int(text[i][1])))
                temp.append('2, %d, Note_on_c, 1, %d, 20\n' % (time, int(text[i][1])))
                time += int(text[i][0])
                time_shift = 1
            elif 57 < text[i + 1][1] < 66:
                temp.append('2, %d, Note_off_c, 1, %d, 0\n' % (time, int(text[i][1])))
                temp.append('2, %d, Note_on_c, 1, %d, 20\n' % (time, int(text[i][1])))
                temp.append('2, %d, Note_on_c, 1, %d, 20\n' % (time, int(text[i + 1][1])))
                time += int(text[i][0])
                time_shift = 2
            elif 57 < text[i + 2][1] < 66:
                temp.append('2, %d, Note_off_c, 1, %d, 0\n' % (time, int(text[i][1])))
                temp.append('2, %d, Note_on_c, 1, %d, 20\n' % (time, int(text[i][1])))
                temp.append('2, %d, Note_on_c, 1, %d, 20\n' % (time, int(text[i + 1][1])))
                temp.append('2, %d, Note_on_c, 1, %d, 20\n' % (time, int(text[i + 2][1])))
                time += int(text[i][0])
                time_shift = 3
            elif 57 < text[i + 3][1] < 66:
                temp.append('2, %d, Note_off_c, 1, %d, 0\n' % (time, int(text[i][1])))
                temp.append('2, %d, Note_on_c, 1, %d, 20\n' % (time, int(text[i][1])))
                temp.append('2, %d, Note_on_c, 1, %d, 20\n' % (time, int(text[i + 1][1])))
                temp.append('2, %d, Note_on_c, 1, %d, 20\n' % (time, int(text[i + 2][1])))
                temp.append('2, %d, Note_on_c, 1, %d, 20\n' % (time, int(text[i + 3][1])))
                time += int(text[i][0])
                time_shift = 4

        else:
            temp.append('2, %d, Note_off_c, 1, %d, 0\n' % (time, int(text[i][1])))
            temp.append('2, %d, Note_on_c, 1, %d, 20\n' % (time, int(text[i][1])))
            time += int(text[i][0])
            time_shift = 1

    temp.append('2, %s, End_track\n' % (str(time)))
    temp.append('0, 0, End_of_file')

    return temp


midi_data = data_form(notes)
print(midi_data)
midi_object = pm.csv_to_midi(midi_data)

file_name = '456'
file_name += '.mid'
with open(file_name, "wb") as output_file:
    midi_writer = pm.FileWriter(output_file)
    midi_writer.write(midi_object)

print('Done')