from typing import Any

class PID:
  def __init__(self, K_p:float, K_i:float, K_d:float) -> None:
    self.K_p = K_p
    self.K_i = K_i
    self.K_d = K_d
    
    self.current_er = 0
    self.sum_er = 0
    self.derivative_er = 0
    self.time_er = 0
    self.history_er = []
    
    
  def add_er(self, er_t):
    self.current_er = er_t
    self.derivative_er = er_t - self.history_er[-1]
    self.history_er.append(er_t)
    self.sum_er = sum(self.history_er)
    self.time_er += 1
    
  def __call__(self, *args: Any, **kwds: Any) -> float:
    return self.K_p * self.current_er + self.K_i * self.sum_er + self.K_d * self.derivative_er
  
  def reset_er(self):
    self.current_er = 0
    self.sum_er = 0
    self.derivative_er = 0
  
    self.history_er = []
    