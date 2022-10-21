import time
import numpy as np
from imgui_bundle import implot, ImVec2, imgui_knobs, imgui, run


t = np.arange(0, np.pi * 2, 0.01)
x = np.power(np.sin(t), 3) * 16
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
t0 = time.time() + 0.2
heart_pulse_rate = 80


def gui():
    global heart_pulse_rate
    k = 0.8 + 0.1 * np.cos((time.time() - t0) * heart_pulse_rate / (np.pi * 2))
    imgui.text("Bloat free code")
    implot.begin_plot("Heart")
    implot.plot_line("", x * k, y * k)
    implot.end_plot()
    _, heart_pulse_rate = imgui_knobs.knob("Pulse", heart_pulse_rate, 30, 180)


run(gui, window_size=ImVec2(300, 450), window_title="Hello!", with_implot=True)