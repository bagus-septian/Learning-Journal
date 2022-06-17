def bmi_index(w,h):
  bmi = w/(h**2)
  if bmi <= 18.5:
    return(print("BMI underweight"))
  elif 18.5 <= bmi <= 24.9:
    return(print("BMI Normal"))
  elif 25 <= bmi <= 29.9:
    return(print("BMI Overweight"))
  else:
    return(print("BMI Very Overweight"))