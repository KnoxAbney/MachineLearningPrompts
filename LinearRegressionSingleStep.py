def get_gradient_at_b(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
    diff += (y[i] - ((m * x[i]) + b))
  b_gradient = -(2/N) * diff  
  return b_gradient

def get_gradient_at_m(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
      diff += x[i] * (y[i] - ((m * x[i]) + b))
  m_gradient = -(2/N) * diff  
  return m_gradient

def step_gradient(x, y, b_current, m_current):
  b_gradient = get_gradient_at_b(x, y,     b_current, m_current)
  m_gradient = get_gradient_at_m(x, y, b_current, m_current)
  b = b_current - (0.01 * b_gradient)
  m = m_current - (0.01 * m_gradient)
  return (b, m)

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

# starting intercept guess:
b = 0
# starting slope guess:
m = 0


b, m = step_gradient(months, revenue, b, m)

print(b, m)
