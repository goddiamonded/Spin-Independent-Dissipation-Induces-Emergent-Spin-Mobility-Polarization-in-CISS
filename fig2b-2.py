# -*- coding: utf-8 -*-
"""
Created on Fri May 15 11:00:58 2026

@author: 83837
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.interpolate import CubicHermiteSpline
config = {
    "font.family":'Times New Roman',  # font
    "axes.unicode_minus": False 
}
from matplotlib import rcParams
rcParams.update(config)
font={"family":'Times New Roman','weight':'bold','size':20}

# ------------------------------------------------------------
# 1. define piecewise linear function in log space
#    u = log10(x), v = log10(y)
# ------------------------------------------------------------
def piecewise_linear_loglog(u, b1, b2, k1, k2, c):
    """
    u: log10(x)
    return v = log10(y)
    """
    v = np.empty_like(u, dtype=float)
    #  u <= b1
    mask1 = u <= b1
    v[mask1] = k1 * (u[mask1] - b1) + c
    #  b1 < u < b2
    mask2 = (u > b1) & (u < b2)
    v[mask2] = c
    #  u >= b2
    mask3 = u >= b2
    v[mask3] = k2 * (u[mask3] - b2) + c
    return v

# ------------------------------------------------------------
# 2. error bar conversion
# ------------------------------------------------------------
def yerr_to_logerr(y, yerr):
    with np.errstate(divide='ignore', invalid='ignore'):
        logerr = yerr / (y * np.log(10))
        logerr[~np.isfinite(logerr)] = 1e6
    return logerr

# ------------------------------------------------------------
# 3. linear fit in log space
# ------------------------------------------------------------
def fit_piecewise_loglog(x_data, y_data, yerr_data):
    # log space
    u_data = np.log10(x_data)
    v_data = np.log10(y_data)
    v_err = yerr_to_logerr(y_data, yerr_data)
    sigma = v_err

    u_min, u_max = u_data.min(), u_data.max()
    #  u space: 1/3 to 2/3
    b1_guess = u_min + (u_max - u_min) / 3.0
    b2_guess = u_min + 2 * (u_max - u_min) / 3.0

    # estimate k1
    idx_third = max(2, len(u_data) // 3)
    k1_guess = (v_data[idx_third] - v_data[0]) / (u_data[idx_third] - u_data[0])
    # estimate k2
    k2_guess = (v_data[-1] - v_data[-idx_third]) / (u_data[-1] - u_data[-idx_third])
    # platform
    c_guess = np.median(v_data[len(u_data)//3 : 2*len(u_data)//3])

    # deal useless initial value
    if not np.isfinite(k1_guess): k1_guess = 0.2
    if not np.isfinite(k2_guess): k2_guess = -0.2
    if not np.isfinite(c_guess): c_guess = v_data[len(u_data)//2]

    p0 = [b1_guess, b2_guess, k1_guess, k2_guess, c_guess]
    # b1 < b2, k1 > 0, k2 < 0
    bounds_low = [u_min, b1_guess, 1e-6, -np.inf, -np.inf]
    bounds_high = [b2_guess, u_max, np.inf, -1e-6, np.inf]

    try:
        popt, _ = curve_fit(piecewise_linear_loglog, u_data, v_data,
                            p0=p0, sigma=sigma, absolute_sigma=False,
                            bounds=(bounds_low, bounds_high), maxfev=5000)
    except Exception as e:
        print("failure:", e)
        popt = p0
    return popt

# ------------------------------------------------------------
# 4. smooth vertex
# ------------------------------------------------------------
def smooth_transition(u, v, b, left_slope, right_slope, smooth_radius):
    u_left = b - smooth_radius
    u_right = b + smooth_radius
    mask = (u >= u_left) & (u <= u_right)
    if not np.any(mask):
        return u, v
    v_left = np.interp(u_left, u, v)
    v_right = np.interp(u_right, u, v)
    if u_right - u_left < 1e-8:
        return u, v
    hermite = CubicHermiteSpline([u_left, u_right], [v_left, v_right],
                                 [left_slope, right_slope])
    v_new = v.copy()
    v_new[mask] = hermite(u[mask])
    return u, v_new

def make_curve_smooth(u_line, v_line, b1, b2, k1, k2, smooth_ratio=0.3):
    platform_len = b2 - b1
    if platform_len <= 0:
        return u_line, v_line
    smooth_radius = smooth_ratio * platform_len
    # 平滑第一个转折点 (左斜率 k1, 右斜率 0)
    u_line, v_line = smooth_transition(u_line, v_line, b1, k1, 0.0, smooth_radius)
    # 平滑第二个转折点 (左斜率 0, 右斜率 k2)
    u_line, v_line = smooth_transition(u_line, v_line, b2, 0.0, k2, smooth_radius)
    return u_line, v_line

# ------------------------------------------------------------
# 5. fit+smooth
# ------------------------------------------------------------
def fit_and_smooth_loglog(x_data, y_data, yerr_data, num_smooth=500, smooth_ratio=0.3):
    # fit parameters in log space
    b1, b2, k1, k2, c = fit_piecewise_loglog(x_data, y_data, yerr_data)

    # u = log10(x)
    u_min, u_max = np.log10(x_data.min()), np.log10(x_data.max())
    u_line = np.linspace(u_min, u_max, num_smooth)
    v_line = piecewise_linear_loglog(u_line, b1, b2, k1, k2, c)

    # smooth vertex
    u_smooth, v_smooth = make_curve_smooth(u_line, v_line, b1, b2, k1, k2, smooth_ratio)

    # conversion to original x,y
    x_smooth = 10 ** u_smooth
    y_smooth = 10 ** v_smooth
    return (b1, b2, k1, k2, c), x_smooth, y_smooth

# ------------------------------------------------------------
# 6. data
# ------------------------------------------------------------
if __name__ == "__main__":
    De=[np.float64(0.0409283006664131), #from fig2c
     np.float64(0.04142233230007517),
     np.float64(0.041760674362867276),
     np.float64(0.04179256595508956),
     np.float64(0.04180004857166041),
     np.float64(0.041760471020313855),
     np.float64(0.041647071247809496),
     np.float64(0.04137955999235258),
     np.float64(0.0411816644137627),
     np.float64(0.0407790395574613)]
    #a=[0.3,0.4,0.5,0.6,(0.7),0.8,(0.9),(1),(1.1),2,2.3]
    a=[0.3,0.4,0.5,0.6,(0.7),0.8,(0.9),(1),(1.1),1.3]
    error=[np.float64(8.776556248543763e-05),
     np.float64(8.082675638130133e-05),
     np.float64(0.00013049687135770205),
     np.float64(5.917209979332868e-05),
     np.float64(7.624926274375776e-05),
     np.float64(0.00010195813517368483),
     np.float64(0.00012104727443967758),
     np.float64(3.787612918187272e-05),
     np.float64(5.1459333738059984e-05),
     np.float64(0.00010008973789445413)]
    pv=[np.float64(0.47513834102349073),
     np.float64(0.4790586395060209),
     np.float64(0.4808947103839158),
     np.float64(0.47889036619648967),
     np.float64(0.47676547314962475),
     np.float64(0.47299148824980614),
     np.float64(0.4692024488731718),
     np.float64(0.46415267978900004),
     np.float64(0.4607306093417169),
     np.float64(0.45324506465696063)]
    error1=[np.float64(0.001572557601914354),
     np.float64(0.0018365697321693075),
     np.float64(0.00253866326650104),
     np.float64(0.001501110103388631),
     np.float64(0.001208478690149145),
     np.float64(0.0016241187015664238),
     np.float64(0.0018897171066436236),
     np.float64(0.0007604507155192786),
     np.float64(0.0008600436961426483),
     np.float64(0.0021848516993826506)]
        
    x_data=np.array(a)
    y_obs = np.array(De)
    y_obs1 = np.array(pv)
    yerr_obs = np.array(error)    # error 
    yerr_obs1 = np.array(error1)

    # fit + smooth（smooth_ratio: smooth rate）
    params, x_smooth, y_smooth = fit_and_smooth_loglog(x_data, y_obs, yerr_obs, smooth_ratio=0.2)    
    b1, b2, k1, k2, c = params
    print("result:")
    print(f"  b1 (log10(x)) = {b1:.3f}  => x = {10**b1:.3f}")
    print(f"  b2 (log10(x)) = {b2:.3f}  => x = {10**b2:.3f}")
    print(f"  k1 = {k1:.3f}, k2 = {k2:.3f}, c = {c:.3f} (log10(y) platform)")

    # plot
    plt.figure(figsize=(9, 6))
    
    #errorbar
    plt.errorbar(x_data, y_obs, yerr=yerr_obs,fmt='o', capsize=3, 
                 color='k', alpha=0.6, linewidth=4.0,markersize=10,label='$D_{\\uparrow}+D_{\\downarrow}$')
    # smooth fit curve
    plt.plot(x_smooth, y_smooth, 'r-', lw=4)
    # linear fit
    u_line = np.linspace(np.log10(x_data.min()), np.log10(x_data.max()), 500)
    v_line = piecewise_linear_loglog(u_line, b1, b2, k1, k2, c)
    x_line = 10 ** u_line
    y_line = 10 ** v_line
    plt.plot(x_line, y_line, 'b--', lw=4, alpha=0.5,label='Piecewise linear')
        
     
    plt.grid(True)
    plt.xscale('log')
    plt.xticks([0.3,0.4,0.6,0.8,1,1.2],fontsize=23.5,weight='bold')    
    
    plt.yscale('log')
    plt.xlabel('$\Gamma(eV)$',font,fontsize=23.5)
    plt.ylabel('$D_{\\uparrow}+D_{\\downarrow}(fs^{-1})$',font,fontsize=23.5)
    plt.yticks([0.0405,0.041,0.0415,0.042,0.0425],fontsize=23.5,weight='bold')
    font1={"family":'Times New Roman','weight':'bold','size':25}
    plt.legend(prop=font1,fontsize=25,frameon=False)
    
    plt.grid(True, which='both', linestyle='--', linewidth=4.0,alpha=0.5)
    plt.tight_layout()
    plt.savefig('fig2b.png',dpi=600,bbox_inches='tight')
    plt.show()
    