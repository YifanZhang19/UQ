import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
#(a)
# Load the data
data = pd.read_excel('/Users/meviusz/UQ/sem2-23/DATA7703/ass1/Snakes.xlsx',
                     sheet_name='Adult Tiger snakes')

# Drop rows with missing values
data_cleaned = data.dropna(subset=['BODY MASS', 'SVL'])

# Split the data into features (X) and target (y)
X = data_cleaned[['SVL']]
Y = data_cleaned['BODY MASS']

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3,
                                                    random_state=42)

# Create a linear regression model
regression = LinearRegression()

# Fit the model to the training data
regression.fit(x_train, y_train)

# Get the coefficients (slope and intercept)
slope = regression.coef_[0]
intercept = regression.intercept_

# Make predictions on the test data
y_pred = regression.predict(x_test)

# Calculate the sum of squared error
sse = ((y_pred - y_test) ** 2).sum()

# Print the equation and sum of squared error
print(f"Linear Regression Equation: y = {slope:.4f} * x + {intercept:.4f}")
print(f"Sum of Squared Error: {sse:.4f}")


#(b)
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# 导入所需库
# pandas 用于数据处理
# numpy 用于数值计算
# sklearn.linear_model 中的 LinearRegression 用于线性回归分析
# sklearn.preprocessing 中的 PolynomialFeatures 用于生成多项式特征
# sklearn.model_selection 中的 train_test_split 用于划分训练集和测试集
# sklearn.metrics 中的 mean_squared_error 用于计算均方误差

# 加载数据
data = pd.read_excel('/Users/meviusz/UQ/sem2-23/DATA7703/ass1/Snakes.xlsx',
                     sheet_name='Adult Tiger snakes')
# 使用 pandas 的 read_excel 函数加载 Excel 文件中的数据

# 删除含有缺失值的行
data_cleaned = data.dropna(subset=['BODY MASS', 'SVL'])
# 使用 dropna 函数删除 'BODY MASS' 和 'SVL' 列中含有缺失值的行

# 将数据分为特征 (X) 和目标 (y)
X = data_cleaned[['SVL']]
y = data_cleaned['BODY MASS']
# 将数据分为特征 'SVL' 和目标 'BODY MASS'

# 将数据分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    random_state=42)
# 使用 train_test_split 函数将数据划分为训练集和测试集
# test_size=0.3 表示将 30% 的数据用于测试，random_state=42 保证每次运行结果一致

# 创建一个二次特征转换器
quadratic = PolynomialFeatures(degree=2)
X_train_quad = quadratic.fit_transform(X_train)
X_test_quad = quadratic.transform(X_test)
# 使用 PolynomialFeatures 类生成二次多项式特征
# degree=2 表示生成二次特征

# 创建一个二次回归模型
model_quad = LinearRegression()

# 将二次模型拟合到训练数据
model_quad.fit(X_train_quad, y_train)
# 使用 fit 方法将二次模型与二次特征训练数据拟合

# 使用二次模型对测试数据进行预测
y_pred_quad = model_quad.predict(X_test_quad)

# 计算二次模型的均方误差
mse_quad = mean_squared_error(y_test, y_pred_quad)

# 打印二次回归方程和均方误差
print(f"Quadratic Regression Equation: y = {model_quad.intercept_:.4f} + {model_quad.coef_[1]:.4f} * x + {model_quad.coef_[2]:.4f} * x^2")
print(f"Mean Squared Error (Quadratic Model): {mse_quad:.4f}")


#(c)
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# 加载数据
data = pd.read_excel('/Users/meviusz/UQ/sem2-23/DATA7703/ass1/Snakes.xlsx',
                     sheet_name='Adult Tiger snakes')

# 复制数据以进行填充操作
data_imputed = data.copy()

# 需要进行均值填充的列
columns_to_fill = ['BODY MASS', 'SVL']

# 对需要的两列进行均值填充
for column in columns_to_fill:
    mean_value = data_imputed[column][1:].astype(float).mean()  # 去除第一行并计算均值
    data_imputed[column].fillna(mean_value, inplace=True)

# 将数据分为特征 (X) 和目标 (y)
X = data_imputed[['SVL']]
y = data_imputed['BODY MASS']

# 将数据分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                    random_state=42)

# 创建一个线性回归模型
model = LinearRegression()

# 将模型拟合到训练数据
model.fit(X_train, y_train)

# 获取回归系数 (斜率和截距)
slope = model.coef_[0]
intercept = model.intercept_

# 使用模型对测试数据进行预测
y_pred = model.predict(X_test)

# 计算均方误差
mse = mean_squared_error(y_test, y_pred)

# 打印线性回归方程和均方误差
print(f"Linear Regression Equation: y = {slope:.4f} * x + {intercept:.4f}")
print(f"Mean Squared Error: {mse:.4f}")

#(d)
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load the data
data = pd.read_excel('/Users/meviusz/UQ/sem2-23/DATA7703/ass1/Snakes.xlsx', sheet_name='Adult Tiger snakes')

# Copy the data for imputation
data_imputed = data.copy()

# Columns to perform mean imputation on
columns_to_fill = ['BODY MASS', 'SVL']

# Perform mean imputation on the selected columns
for column in columns_to_fill:
    mean_value = data_imputed[column][1:].astype(float).mean()
    data_imputed[column].fillna(mean_value, inplace=True)

# Split the data into features (X) and target (y)
X = data_imputed[['SVL']]
y = data_imputed['BODY MASS']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a linear regression model for (a)
model_a = LinearRegression()
model_a.fit(X_train, y_train)

# Create a quadratic regression model for (b)
quadratic = PolynomialFeatures(degree=2)
X_train_quad = quadratic.fit_transform(X_train)
model_b = LinearRegression()
model_b.fit(X_train_quad, y_train)

# Create a linear regression model for (c)
model_c = LinearRegression()
model_c.fit(X_train, y_train)

# Generate predictions for the entire data range
X_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
y_pred_a = model_a.predict(X_range)
y_pred_b = model_b.predict(quadratic.transform(X_range))
y_pred_c = model_c.predict(X_range)

# Create a scatter plot of the imputed data
plt.scatter(X, y, label='Imputed Data', color='blue', alpha=0.5)

# Plot the regression lines for each model
plt.plot(X_range, y_pred_a, label='Linear Regression (a)', color='green')
plt.plot(X_range, y_pred_b, label='Quadratic Regression (b)', color='orange')
plt.plot(X_range, y_pred_c, label='Imputed + Linear Regression (c)', color='purple')

# Add labels and a legend
plt.xlabel('SVL')
plt.ylabel('BODY MASS')
plt.title('Regression Models for Snake Data')
plt.legend()

# Show the plot
plt.show()




